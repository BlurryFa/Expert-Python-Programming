# exec, eval, and compile

  * **exec(object, globals, locals)** : This allows you to dynamically execute
    the Python code.  object should be a string or code object (see
    the  compile() function) representing a single statement or sequence of multiple
    statements. The  globals and  locals arguments provide global and local
    namespaces for the executed code and are optional. If they are not provided, then
    the code is executed in the current scope. If provided,  globals must be a
    dictionary, while  locals might be any mapping object; it always returns  None
  * **eval(expression, globals, locals)** : This is used to evaluate the given
    expression by returning its value. It is similar to  exec() , but it
    expects  expression to be a single Python expression and not a sequence of
    statements. It returns the value of the evaluated expression
    
  * **compile(source, filename, mode)** : This compiles the source into the code
    object or AST object. The source code is provided as a string value in the  source
    argument. The filename should be the file from which the code was read. If it has
    no file associated (for example, because it was created dynamically),
    then  <string> is the value that is commonly used. Mode should be
    either  exec (sequence of statements),  eval (single expression), or  single (a
    single interactive statement, such as in a Python interactive session).
    
**Armin Ronacher has a good article that lists the most important of them, titled Be careful with exec and eval in Python (refer
   to  http://lucumr.pocoo.org/2011/2/1/exec-in-python/ )**

**Ned Batcheler has written a very good article in which he shows how to cause an interpreter segmentation fault
  in the  eval() call, even with erased access to all Python built-ins
  (see http://nedbatchelder.com/blog/201206/eval\_really\_is\_dangerou
  s.html )**
  
# Abstract syntax tree(AST)

Raw ASTs of Python code can be
created using the  **compile()** function with the  **ast.PyCF_ONLY_AST** flag, or by using
the  **ast.parse()** helper.

For instance, new syntax nodes can be used for additional instrumentation,
such as test coverage measurement. It is also possible to modify the existing code tree in
order to add new semantics to the existing syntax. Such a technique is used by the MacroPy
project ( https://github.com/lihaoyi/macropy ) to add syntactic macros to Python using
the already existing syntax (refer to Figure 3):


AST can also be created in a purely artificial manner, and there is no need to parse any
source at all. This gives Python programmers the ability to create Python bytecode for
custom domain-specific languages, or even completely implement other programming
languages on top of Python VMs.

# Import hooks

  * **Meta hooks**: These are called before any other  import processing has occurred.
    Using meta hooks, you can override the way in which  sys.path is processed for
    even frozen and built-in modules. To add a new meta hook, a new **meta path finder** 
    object must be added to the  _sys.meta_path_ list.
 
  * **Import path hooks**: These are called as part of  _sys.path_ processing. They are
    used if the path item associated with the given hook is encountered. The import
    path hooks are added by extending the  _sys.path_hooks_ list with a new **path finder** object.

**The details of implementing both path finders and meta path finders are extensively implemented in the official Python documentation (see  https://docs.python.org/3/reference/import.html )**

# Project that use code generation patterns

## Falcon's compiled router

Falcon ( http://falconframework.org/ ) is a minimalist Python WSGI web framework for
building fast and lightweight APIs. It strongly encourages the **REST** architectural style that
is currently very popular around the web. 

One of its features is it's very simple routing mechanism. It is not as complex as the routing
provided by Django  urlconf and does not provide as many features. 

Falcon's router
is implemented using the code generated from the list of routes, and code changes every
time a new route is registered. This is the effort that's needed to make routing fast.

Consider this very short API sample

``` Python
# sample.py
import falcon
import json


class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': 'I\'ve always been more interested in '
            'the future than in the past.',
            'author': 'Grace Hopper'
        }
        resp.body = json.dumps(quote)
        
api = falcon.API()
api.add_route('/quote', QuoteResource())

# In short, the highlighted call to the  api.add_route() method updates dynamically the
# whole generated code tree for Falcon's request router. It also compiles it using
# the  compile() function and generates the new route-finding function using  eval() . 

>>> api._router._find.__code__
<code object find at 0x00000000033C29C0, file "<string>", line 1>
>>> api.add_route('/none', None)
>>> api._router._find.__code__
<code object find at 0x00000000033C2810, file "<string>", line 1>

# This transcript shows that the code of this function was generated from the string and not
# from the real source code file (the  "<string>" file). It also shows that the actual code
# object changes with every call to the  api.add_route() method (the object's address in
# memory changes).
```

# Hy

Hy ( http://docs.hylang.org/ ) is the dialect of Lisp. 

Hy can be considered as a language that runs
fully in the Python runtime environment, just like Python does. Code written in Hy can use
the existing built-in modules and external packages and vice-versa. Code written with Hy
can be imported back into Python.

If we dig deeper and try to disassemble  hyllo.hello using the built-in  dis module, we
will notice that the byte code of the Hy function does not differ significantly from its pure
Python counterpart.
