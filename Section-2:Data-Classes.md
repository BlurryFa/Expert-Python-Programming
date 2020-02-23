# Reducing boilerplate with data classes

``` Python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        """Add two vectors using + operator"""
        return Vector(
        self.x + other.x,
        self.y + other.y,
        )
        
    def __sub__(self, other):
        """Subtract two vectors using - operator"""
        return Vector(
        self.x - other.x,
        self.y - other.y,
        )
        
    def __repr__(self):
        """Return textual representation of vector"""
        return f"<Vector: x={self.x}, y={self.y}>"
        
    def __eq__(self, other):
        """Compare two vectors for equality"""
        return self.x == other.x and self.y == other.y
```

**With the  dataclasses module, we can make our  Vector class code a lot shorter**

``` Python
# The  dataclass class decorator reads annotations of the  Vector class attribute and
# automatically creates the  __init__() ,  __repr__() , and  __eq__() methods.
from dataclasses import dataclass


@dataclass
class Vector:
    x: int
    y: int
    
    def __add__(self, other):
        """Add two vectors using + operator"""
        return Vector(
        self.x + other.x,
        self.y + other.y,
        )
        
    def __sub__(self, other):
        """Subtract two vectors using - operator"""
        return Vector(
        self.x - other.x,
        self.y - other.y,
        )
```

**Use frozen=True to make  Vector class instances immutable**

``` Python
@dataclass(frozen=True)
class FrozenVector:
    x: int
    y: int
```

**define default values for specific attributes using the  field() constructor**

``` Python
@dataclass
class DataClassWithDefaults:
    static_default: str = field(default="this is static default value")
    factory_default: list = field(default_factory=list)
```
