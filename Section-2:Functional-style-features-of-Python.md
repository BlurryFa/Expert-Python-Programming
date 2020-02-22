# Programming paradigm

  * **Imperative paradigms**, in which the programmer is mostly concerned about the program state and the program itself is a definition of how the computer should manipulate its state to generate the expected result
  
  * **Declarative paradigms**, in which the programmer is concerned mostly about a formal definition of the problem or properties of the desired result and not defining how this result should be computed
  
# Functional programming

  * **Side-effects**: A function is said to have a side-effect if it modifies the state outside
    of its local environment. In other words, a side-effect is any observable change
    outside of the function scope that happens as a result of a function call. An
    example of such side-effects could be the modification of a global variable, the
    modification of an attribute or object that is available outside of the function
    scope, or saving data to some external service. Side-effects are the core of the
    concept of object-oriented programming, where class instances are objects that
    are used to encapsulate the state of application, and methods are functions
    bound to those objects that are supposed to manipulate the state of these objects.

  * **Referential transparency**: When a function or expression is referentially
    transparent, it can be replaced with the value that corresponds to its inputs
    without changing the behavior of the program. So, a lack of side effects is a
    requirement for referential transparency, but not every function that lacks side-
    effects is a referentially transparent function. For instance, Python's built-in
    pow(x, y) function is referentially transparent, because it lacks side effects, and
    for every x and y argument, it can be replaced with the value of x
    y . On the other hand, the  datetime.now() constructor method of the  datetime type does not
    seem to have observable side-effects, but will return a different value every time
    it is called. So, it is referentially opaque.
    
  * **Pure functions**: A pure function is a function that does not have any side-effects
    and which always returns the same value for the same set of input arguments. In
    other words, it is a function that is referentially transparent. Every mathematical
    function is, by definition, a pure function.
    
  * **First-class functions**: Language is said to contain first-class functions if functions
    in this language can be treated as any other value or entity. First-class functions
    can be passed as arguments to other functions, returned as function return
    values, and assigned to variables. In other words, a language that has first-class
    functions is a language that treats functions as first-class citizens. Functions in
    Python are first-class functions.

# Lambda functions

# map(), filter(), and reduce()

** map() and  filter() can work on infinite sequences.**

``` Python
>>> list(map(lambda x: x**2, range(10)))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

``` Python
>>> evens = filter(lambda number: number % 2 == 0, range(10))
>>> odds = filter(lambda number: number % 2 == 1, range(10))
```

``` Python
>>> from functools import reduce
>>> reduce(lambda a, b: a + b, [2, 2])
4
>>> reduce(lambda a, b: a + b, [2, 2, 2])
6
>>> reduce(lambda a, b: a + b, range(100))
4950
```

# Partial objects and partial() functions

``` Python
>>> from functools import partial
>>> powers_of_2 = partial(pow, 2)
>>> powers_of_2(2)
4
>>> powers_of_2(5)
32
>>> powers_of_2(10)
1024
```

# Generator expressions

> (item for item in iterable_expression)

# Function and variable annotations

``` Python
>>> def f(ham: str, eggs: str = 'eggs') -> str:
... pass
...
>>> print(f.__annotations__)
{'return': <class 'str'>, 'eggs': <class 'str'>, 'ham': <class 'str'>}
```

## Use cases
  * Type checking
  * Let IDEs show what types a function expects and returns
  * Function overloading/generic functions
  * Foreign language bridges
  * Adaptation
  * Predicate logic functions
  * Database query mapping
  * RPC parameter marshaling
  * Documentation for parameters and return values

# The for ... else ... statement

``` Python
>>> for number in range(1):
... break
... else:
... print("no break")
...
>>> for number in range(1):
... pass
... else:
... print("no break")
...
no break
```
# Keyword-only arguments

``` Python
def process_order(
order, client,
*, # * 隔开 keyword arguments 和 positional arguments
suppress_notifications=False,
suppress_payment=False,
):
...
```

