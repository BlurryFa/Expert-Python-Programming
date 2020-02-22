# dunder methods
|**Protocol name**|**Methods**|**Description**|
|-|-|-|
|Callable protocol|\_\_call\_\_()|Allows objects to be called with the parentheses syntax: <br/>instance()</br>|
|Descriptor protocols|\_\_set\_\_() ,  \_\_get\_\_() , and  \_\_del\_\_()|Allows us to manipulate the attribute access pattern of classes (see the Descriptors section)|
|Container protocol|\_\_contains\_\_()|Allows us to test whether or not an object contains some value using the  in keyword: <br/>value in instance</br>|
|Iterable protocol|\_\_iter\_\_()|Allows objects to be iterated over using the  for keyword: <br/>for value in instance:</br>|
|Sequence protocol|\_\_len\_\_() , \_\_getitem\_\_()|Allows objects to be indexed with square bracket syntax and queried for length using a built-in function: <br/>item = instance[index]</br> length = len(instance)|

> The full list of all the dunder methods can be found in the official documentation of the Python data model (see  https://docs.python.org/3/reference/datamodel.html ).

# dunder attributes

  * **\_\_doc\_\_** : A writable attribute that holds the function's documentation. It is, by default, populated by the  docstring function.
  
  * **\_\_name\_\_** : A writable attribute that holds the function's name.
  
  * **\_\_qualname\_\_** : A writable attribute that holds the function's qualified name. The qualified name is a full dotted path to the object (with class names) in the global scope of the module where the object is defined.
  
  * **\_\_module\_\_** : A writable attribute that holds the name of the module that function belongs to.
  
  * **\_\_defaults\_\_** : A writable attribute that holds the default argument values if the function has any.
  
  * **\_\_code\_\_** : A writable attribute that holds the function's compile code object.
  
  * **\_\_globals\_\_** : A read-only attribute that holds the reference to the dictionary of global variables for that function's scope. The global scope for a function is the namespace of the module where this function is defined.
  
  * **\_\_dict\_\_** : A writable attribute that holds a dictionary of function attributes. Functions in Python are first-class objects, so they can have any arbitrary arguments defined, just like any other object.
  
  * **\_\_closure\_\_** : A read-only attribute that holds a tuple of cells with the function's free variables. Closure cells allow you to create parametrized function decorators.
  
  * **\_\_annotations\_\_** : A writable attribute that holds the function's argument and return annotations.
  
  * **\_\_kwdefaults\_\_** : A writable attribute that holds the default argument values for keyword-only arguments if the function has any.
  
  
