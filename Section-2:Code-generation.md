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
