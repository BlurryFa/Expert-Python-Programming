# What is metaprogramming

**Metaprogramming is a technique of writing computer programs that can treat
themselves as data, so they can introspect, generate, and/or modify itself while running**

# Decorators

# Class decorators

``` Python
def short_repr(cls):
    cls.__repr__ = lambda self: super(cls, self).__repr__()[:8]
    return cls
    
@short_repr
class ClassWithRelativelyLongName:
    pass
    
>>> ClassWithRelativelyLongName()
<ClassWi
```

  * Not only instances but also class objects can be modified at runtime
  
  * Functions are descriptors too, so they can be added to the class at runtime
    because the actual method binding is performed on the attribute lookup as part
    of the descriptor protocol
  
  * The  super() call can be used outside of a class definition scope as long as proper
    arguments are provided
  
  * Finally, class decorators can be used on class definitions
  
## Parametrize class decorators

  ``` Python
  def parametrized_short_repr(max_width=8):
      """Parametrized decorator that shortens representation"""
      def parametrized(cls):
          """Inner wrapper function that is actual decorator"""
          class ShortlyRepresented(cls):
              """Subclass that provides decorated behavior"""
              def __repr__(self):
                  return super().__repr__()[:max_width]
          return ShortlyRepresented
      return parametrized
      
  
  @parametrized_short_repr(10)
  class ClassWithLittleBitLongerLongName:
     pass
     
     
  >>> ClassWithLittleBitLongerLongName().__class__
  <class 'ShortlyRepresented'>
  >>> ClassWithLittleBitLongerLongName().__doc__
  'Subclass that provides decorated behavior'
  ```

# Mixin(a class that is not meant to be instantiated)

``` Python
class SomeConcreteClass(MixinClass, SomeBaseClass):
    pass
```

# \_\_new\_\_() method

**\_\_new\_\_() is a static method, and it's called prior to the \_\_init\_\_()**

``` Python
class InstanceCountingClass:

    instances_created = 0
    
    def __new__(cls, *args, **kwargs):
        print('__new__() called with:', cls, args, kwargs)
        instance = super().__new__(cls)
        instance.number = cls.instances_created
        cls.instances_created += 1
        return instance
        
    def __init__(self, attribute):
        print('__init__() called with:', self, attribute)
        self.attribute = attribute
        
>>> instance1 = InstanceCountingClass('abc')
__new__() called with: <class '__main__.InstanceCountingClass'> ('abc',) {}
__init__() called with: <__main__.InstanceCountingClass object at 0x101259e10> abc
>>> instance2 = InstanceCountingClass('xyz')
__new__() called with: <class '__main__.InstanceCountingClass'> ('xyz',) {}
__init__() called with: <__main__.InstanceCountingClass object at 0x101259dd8> xyz
>>> instance1.number, instance1.instances_created
(0, 2)
>>> instance2.number, instance2.instances_created
(1, 2)
```

**If a different class instance is returned in \_\_new\_\_() method, the call to the \_\_init\_\_() method is skipped**

``` Python
class NonZero(int):
    def __new__(cls, value):
        return super().__new__(cls, value) if value != 0 else None
        
    def __init__(self, skipped_value):
        # implementation of __init__ could be skipped in this case
        # but it is left to present how it may be not called
        print("__init__() called")
        super().__init__()
        
>>> type(NonZero(-12))
__init__() called
<class '__main__.NonZero'>
>>> type(NonZero(0))
<class 'NoneType'>
>>> NonZero(-3.123)
__init__() called
-3

```

## When should we use  \_\_new\_\_()

  * subclassing immutable built-in
    Python types such as  int ,  str ,  float ,  frozenset , and so on.
    This is because there was no
    way to modify such an immutable object instance in the  \_\_init\_\_() method once it was
    created.
    



