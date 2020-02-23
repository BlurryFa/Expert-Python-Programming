# name mangling

**prefixed by  \_\_**

``` Python
class MyClass:
    __secret_value = 1
    
>>> instance_of = MyClass()
>>> instance_of.__secret_value
Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
AttributeError: 'MyClass' object has no attribute '__secret_value'

>>> instance_of._MyClass__secret_value
1
```
**When an attribute is not public, the convention to use is a  \_ prefix**


