# Iterators

  * nothing more than a container that implements the iterator protocol
  
    > **\_\_next\_\_** : This returns the next item of the container
    
    > **\_\_iter\_\_** : This returns the iterator itself
    
    ``` Python
    class CountDown:
        def __init__(self, step):
            self.step = step
            
        def __next__(self):
            """Return the next element."""
            if self.step <= 0:
                raise StopIteration
            self.step -= 1
            return self.step
            
        def __iter__(self):
            """Return the iterator itself."""
            return self
    ```
    
  * separate your iterator from its state, you will ensure that it can't be exhausted
  
    ``` Python
    class CounterState:
        def __init__(self, step):
            self.step = step
            
        def __next__(self):
            """Move the counter step towards 0 by 1."""
            if self.step <= 0:
                raise StopIteration
            self.step -= 1
            return self.step
            
    class CountDown:
        def __init__(self, steps):
            self.steps = steps
            
        def __iter__(self):
            """Return iterable state"""
            return CounterState(self.steps)
    ```
# Generators and yield statements

  > using the  next() function or for loops retrieve new values from generators
  
  > some value can be passed through it to the decorator with a new generator method, named  send()
  
  ``` Python
    def psychologist():
        print('Please tell me your problems')
        while True:
            answer = (yield)
            if answer is not None:
                if answer.endswith('?'):
                    print("Don't ask yourself too much questions")
                elif 'good' in answer:
                    print("Ahh that's good, go on")
                elif 'bad' in answer:
                    print("Don't be so negative")
                    
  ```
    
    >>> free = psychologist()
    >>> next(free)
    Please tell me your problems
    >>> free.send('I feel bad')
    Don't be so negative
    >>> free.send("Why I shouldn't ?")
    Don't ask yourself too much questions
    >>> free.send("ok then i should find what is good for me")
    Ahh that's good, go on

# Decorators

  * The decorator is generally a named callable object(any object that implements the  \_\_call\_\_ method is considered callable) 
  
  * 2 Usages
  
  ``` Python
  @some_decorator
  def decorated_function():
      pass
  ```
  ``` Python
  def decorated_function():
      pass
  decorated_function = some_decorator(decorated_function)
  ```
  
  * As a function
  
  ``` Python
  def mydecorator(function):
      def wrapped(*args, **kwargs):
          # do some stuff before the original
          # function gets called
          result = function(*args, **kwargs)
          # do some stuff after function call and
          # return the result
          return result
      # return wrapper as a decorated function
      return wrapped
  ```
  
  * As a class
  
  ``` Python
  class DecoratorAsClass:
      def __init__(self, function):
          self.function = function
          
      def __call__(self, *args, **kwargs):
          # do some stuff before the original
          # function gets called
          result = self.function(*args, **kwargs)
          # do some stuff after function call and
          # return the result
          return result
  ```
  
  * Parametrizing decorators
  
    * As a function(a second level of wrapping)
    
    ``` Python
    def repeat(number=3):
        """Cause decorated function to be repeated a number of times.
        Last value of original function call is returned as a result.
        :param number: number of repetitions, 3 if not specified
        """
        def actual_decorator(function):
            def wrapper(*args, **kwargs):
                result = None
                for _ in range(number):
                    result = function(*args, **kwargs)
                return result
            return wrapper
        return actual_decorator
    ```
    
  * use the  wraps() decorator, provided by the  functools module:
  
  ``` Python
  from functools import wraps
  
  
  def preserving_decorator(function):
      @wraps(function)
      def wrapped(*args, **kwargs):
          """Internal wrapped function documentation."""
          return function(*args, **kwargs)
      return wrapped
  ```
  
  * Usage and useful examples
  
    * Argument checking
    
    ``` Python
    rpc_info = {}
    def xmlrpc(in_=(), out=(type(None),)):
        def _xmlrpc(function):
        # registering the signature
        func_name = function.__name__
        rpc_info[func_name] = (in_, out)
        def _check_types(elements, types):
            """Subfunction that checks the types."""
            if len(elements) != len(types):
                raise TypeError('argument count is wrong')
            typed = enumerate(zip(elements, types))
            for index, couple in typed:
                arg, of_the_right_type = couple
                if isinstance(arg, of_the_right_type):
                    continue
                raise TypeError('arg #%d should be %s' % (index, of_the_right_type))
                
        # wrapped function
        def __xmlrpc(*args): # no keywords allowed
            # checking what goes in
            checkable_args = args[1:] # removing self
            _check_types(checkable_args, in_)
            # running the function
            res = function(*args)
            # checking what goes out
            if not type(res) in (tuple, list):
                checkable_res = (res,)
            else:
                checkable_res = res
            _check_types(checkable_res, out)
            # the function and the type
            # checking succeeded
            return res
        return __xmlrpc
    return _xmlrpc
    ```
    
    * Caching
    
    ``` Python
    """This module provides simple memoization arguments
    that is able to store cached return results of
    decorated function for specified period of time.
    """
    
    import time
    import hashlib
    import pickle
    
    
    cache = {}
    
    def is_obsolete(entry, duration):
        """Check if given cache entry is obsolete"""
        return time.time() - entry['time']> duration
        
    def compute_key(function, args, kw):
        """Compute caching key for given value"""
        key = pickle.dumps((function.__name__, args, kw))
        return hashlib.sha1(key).hexdigest()
        
    def memoize(duration=10):
        """Keyword-aware memoization decorator
        It allows to memoize function arguments for specified
        duration time.
        """
        def _memoize(function):
            def __memoize(*args, **kw):
                key = compute_key(function, args, kw)
                # do we have it already in cache?
                if (
                    key in cache and
                    not is_obsolete(cache[key], duration)
                ):
                    # return cached value if it exists
                    # and isn't too old
                    print('we got a winner')
                    return cache[key]['value']
                # compute result if there is no valid
                # cache available
                result = function(*args, **kw)
                # store the result for later use
                cache[key] = {
                    'value': result,
                    'time': time.time()
                }
                return result
            return __memoize
        return _memoize
    ```
    
    * Proxy
    
    ``` Python
    class User(object):
        def __init__(self, roles):
            self.roles = roles
            
    class Unauthorized(Exception):
        pass
        
    def protect(role):
        def _protect(function):
            def __protect(*args, **kw):
                user = globals().get('user')
                if user is None or role not in user.roles:
                    raise Unauthorized("I won't tell you")
                return function(*args, **kw)
            return __protect
        return _protect
    
    ```
    ```
    >>> from users import User, protect
    >>> tarek = User(('admin', 'user'))
    >>> bill = User(('user',))
    >>> class RecipeVault(object):
    ... @protect('admin')
    ... def get_waffle_recipe(self):
    ... print('use tons of butter!')
    ...
    >>> my_vault = RecipeVault()
    >>> user = tarek
    >>> my_vault.get_waffle_recipe()
    use tons of butter!
    >>> user = bill
    >>> my_vault.get_waffle_recipe()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 7, in wrap
    __main__.Unauthorized: I won't tell you
    ```
  
  * Context provider(makes sure that the function can run in the correct context)
  
   ``` Python
   from threading import RLock
   lock = RLock()
  
   def synchronized(function):
       def _synchronized(*args, **kw):
           lock.acquire()
           try:
               return function(*args, **kw)
           finally:
               lock.release()
       return _synchronized
      
   @synchronized
   def thread_safe(): # make sure it locks the resource
       pass
       
   ```
  
# Context managers - the with statement

## Use cases
  * Closing a file
  * Releasing a lock
  * Making a temporary code path
  * Running protected code in a special environment
  
* As a class

**context manager protocol consists of two special methods**

  > **\_\_enter\_\_(self)** : This allows you to define what should happen before executing the code that is wrapped with context manager and returns context variable
  
  > **\_\_exit\_\_(self, exc_type, exc_value, traceback)** : This allows you to perform additional cleanup operations after executing the code wrapped with context manager, and captures all exceptions that were raised in the process
  
  ``` Python
  class ContextIllustration:
      def __enter__(self):
          print('entering context')
          
      def __exit__(self, exc_type, exc_value, traceback):
          print('leaving context')
          if exc_type is None:
              print('with no error')
          else:
              print(f'with an error ({exc_value})')
  ```

* As a function - the contextlib module

  ``` Python
  from contextlib import contextmanager
  
  
  @contextmanager
  def context_illustration():
      print('entering context')
      try:
          yield
      except Exception as e:
          print('leaving context')
          print(f'with an error ({e})')
          # exception needs to be reraised
          raise
      else:
          print('leaving context')
          print('with no error')
  ```
  
  **four other helpers provided by contextlib module**
  
    > **closing(element)** : This returns the context manager that calls the element's close() method on exit. This is useful for classes that deal with streams and files.
    
    > **supress(\*exceptions)** : This suppresses any of the specified exceptions if they occur in the body of the  with statement.
    
    > **redirect_stdout(new_target)** and  **redirect_stderr(new_target)** : These redirect the  sys.stdout or  sys.stderr output of any code within the block to another file or file-like object.



    
