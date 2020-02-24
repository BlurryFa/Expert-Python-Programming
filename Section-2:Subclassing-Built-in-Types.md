# 继承dict ,  list , and  str时, 通常用以下模块代替

  * collections.UserDict
  
  * collections.UserList
  
  * collections.UserString
  
# MRO(Method Resolution Order)

**Based on C3 algorithm**( http://www.python.org/download/releases/2.3/mro)

# Super class

``` Python
    # Instead, the  super usage would be as follows:
    class Sister(Mama):
        def says(self):
            super(Sister, self).says()
            print('and clean your bedroom')
            
    # Alternatively, you can also use the shorter form of the  super() call:
    class Sister(Mama):
        def says(self):
            super().says()
            print('and clean your bedroom')
```

**Super working with  classmethod**


``` Python
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        
    def __repr__(self):
        return "Pizza with " + " and ".join(self.toppings)
        
    @classmethod
    def recommend(cls):
        """Recommend some pizza with arbitrary toppings,"""
        return cls(['spam', 'ham', 'eggs'])
       
class VikingPizza(Pizza):
    @classmethod
    def recommend(cls):
        """Use same recommendation as super but add extra spam"""
        recommended = super(VikingPizza).recommend()
        recommended.toppings += ['spam'] * 5
        return recommended
```

# Super pitfalls

  * Mixing super and explicit class calls
  ``` Python
  class A:
    def __init__(self):
        print("A", end=" ")
         super().__init__()
         
  class B:
    def __init__(self):
        print("B", end=" ")
        super().__init__()
        
    class C(A, B):
        def __init__(self):
            print("C", end=" ")
            A.__init__(self)
            B.__init__(self)

    >>> print("MRO:", [x.__name__ for x in C.__mro__])
    MRO: ['C', 'A', 'B', 'object']
    >>> C()
    C A B B <__main__.C object at 0x0000000001217C50>
  ```
  
  * Heterogeneous arguments
  
  ``` Python
  class CommonBase:
      def __init__(self):
          print('CommonBase')
          super().__init__()
          
  class Base1(CommonBase):
      def __init__(self):
          print('Base1')
          super().__init__()
          
  class Base2(CommonBase):
      def __init__(self, arg):
          print('base2')
          super().__init__()
          
  class MyClass(Base1 , Base2):
      def __init__(self, arg):
          print('my base')
          super().__init__(arg)
          
  >>> MyClass(10)
  my base
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 4, in __init__
  TypeError: __init__() takes 1 positional argument but 2 were given
  
  ```
  
  ** One solution would be to use arguments and keyword arguments packing with  \*args and  \*\*kwargs**
  ``` Python
  class CommonBase:
      def __init__(self, *args, **kwargs):
          print('CommonBase')
          super().__init__()
          
  class Base1(CommonBase):
      def __init__(self, *args, **kwargs):
          print('Base1')
          super().__init__(*args, **kwargs)

  class Base2(CommonBase):
      def __init__(self, *args, **kwargs):
          print('base2')
          super().__init__(*args, **kwargs)

  class MyClass(Base1 , Base2):
      def __init__(self, arg):
          print('my base')
          super().__init__(arg)
  ```
