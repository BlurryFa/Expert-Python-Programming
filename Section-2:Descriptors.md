# Descriptor protocol

  > **\_\_set\_\_(self, obj, value)** : This is called whenever the attribute is set. In the following examples, I will refer to this as a setter.
  
  > **\_\_get\_\_(self, obj, owner=None)** : This is called whenever the attribute is read (referred to as a getter).
  
  > **\_\_delete\_\_(self, obj)** : This is called when  del is invoked on the attribute.
  

# Order of finding an attribute

  * It verifies whether the attribute is a data descriptor on the class object of the instance.
  
  * If not, it looks to see whether the attribute can be found in the  __dict__ lookup of the instance object.
  
  * Finally, it looks to see whether the attribute is a non-data descriptor on the class object of the instance.
  
  **data descriptors take precedence over  __dict__ lookup, and  __dict__ lookup takes precedence over non-data descriptors.**
  
  ``` Python
  class RevealAccess(object):
      """A data descriptor that sets and returns values
      normally and prints a message logging their access.
      """
      
      def __init__(self, initval=None, name='var'):
          self.val = initval
          self.name = name
          
      def __get__(self, obj, objtype):
          print('Retrieving', self.name)
          return self.val
          
      def __set__(self, obj, val):
          print('Updating', self.name)
          self.val = val
          
  class MyClass(object):
      x = RevealAccess(10, 'var "x"')
      y = 5
      
      
  >>> m = MyClass()
  >>> m.x
  Retrieving var "x"
  10
  >>> m.x = 20
  Updating var "x"
  >>> m.x
  Retrieving var "x"
  20
  >>> m.y
  5
  ```
  
# Non-data descriptors(just implements  \_\_get\_\_())
  
**function objects are non-data descriptors**

``` Python
>>> def function(): pass
>>> hasattr(function, '__get__')
True
>>> hasattr(function, '__set__')
False
```
  
# Use example - lazily evaluated attributes

``` Python
class InitOnAccess:
    def __init__(self, klass, *args, **kwargs):
        self.klass = klass
        self.args = args
        self.kwargs = kwargs
        self._initialized = None
        
    def __get__(self, instance, owner):
        if self._initialized is None:
            print('initialized!')
            self._initialized = self.klass(*self.args,
            **self.kwargs)
        else:
            print('cached!')
        return self._initialized
        
>>> class MyClass:
... lazily_initialized = InitOnAccess(list, "argument")
...
>>> m = MyClass()
>>> m.lazily_initialized
initialized!
['a', 'r', 'g', 'u', 'm', 'e', 'n', 't']
>>> m.lazily_initialized
cached!
['a', 'r', 'g', 'u', 'm', 'e', 'n', 't']
```

# Properties

**The properties provide a built-in descriptor type that knows how to link an attribute to a set of methods**

> _property_ takes 4 arguments: _fget_ , _fset_ , _fdel_ , _doc_

``` Python
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
    
    def _width_get(self):
        return self.x2 - self.x1
    
    def _width_set(self, value):
        self.x2 = self.x1 + value
    
    def _height_get(self):
        return self.y2 - self.y1
    
    def _height_set(self, value):
        self.y2 = self.y1 + value
    
    width = property(
        _width_get, _width_set,
        doc="rectangle width measured from left"
    )
    
    height = property(
        _height_get, _height_set,
        doc="rectangle height measured from top"
    )
    
    def __repr__(self):
        return "{}({}, {}, {}, {})".format(
            self.__class__.__name__,
            self.x1, self.y1, self.x2, self.y2
        )
```

**The best syntax for creating properties is to use  property as a decorator**

``` Python
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        
    @property
    def width(self):
        """rectangle width measured from left"""
        return self.x2 - self.x1
        
    @width.setter
    def width(self, value):
        self.x2 = self.x1 + value
        
    @property
    def height(self):
        """rectangle height measured from top"""
        return self.y2 - self.y1
        
    @height.setter
    def height(self, value):
        self.y2 = self.y1 + value
```

# Slots

**They allow you to set a static attribute list for a given class with the  __slots__ attribute, and skip the creation of the  __dict__ dictionary in each instance of the class**

``` Python
>>> class Frozen:
... __slots__ = ['ice', 'cream']
...
>>> '__dict__' in dir(Frozen)
False
>>> 'ice' in dir(Frozen)
True
>>> frozen = Frozen()
>>> frozen.ice = True
>>> frozen.cream = None
>>> frozen.icy = True
Traceback (most recent call last): File "<input>", line 1, in <module>
AttributeError: 'Frozen' object has no attribute 'icy'
```

**The new attributes can be added to the derived classes if they do not have their own slots defined**

``` Python
>>> class Unfrozen(Frozen):
...     pass
...
>>> unfrozen = Unfrozen()
>>> unfrozen.icy = False
>>> unfrozen.icy
False
```
  
