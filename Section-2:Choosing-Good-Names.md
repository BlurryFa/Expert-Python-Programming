# PEP8 and naming best practices

PEP 8 ( http://www.python.org/dev/peps/pep-0008 ) provides a style guide for writing
Python code. Besides some basic rules, such as indentation, maximum line length, and
other details concerning the code layout, PEP 8 also provides a section on naming
conventions that most of the code bases follow. 

# Naming styles
  
  * CamelCase
  
  * mixedCase
  
  * UPPERCASE and  UPPER_CASE_WITH_UNDERSCORES
  
  * lowercase and  lower_case_with_underscores
  
  * _leading and  trailing_ underscores, and sometimes  __doubled__ underscores

These styles are applied to the following

  * Variables
  
  * Functions and methods
  
  * Properties
  
  * Classes
  
  * Modules
  
  * Packages
  
# Variable

* **Constants**: These define values that are not supposed to change during program execution

* **Public and private variables**: These hold the state of applications that can change during program execution

## Constant

**an uppercase with an underscore**

`Abbreviated names obfuscate the code most of the time. Don't be afraid of
using complete words when an abbreviation seems unclear.`

* A good practice is to gather all the constants in a single file in the package.

* Another approach is to use a configuration file that can be parsed with the  **ConfigParser** module

## Public and private variables

* > global variables(when not protected): lowercase letter with an underscore

* > private variables: leading underscore

* > variable located in functions and methods: lowercase letter with an underscore

* > class variables used only internally: leading underscore(private)

## Functions and methods

**Lowercase with underscores**

# The private controversy

**Name mangling**

# Special methods

**Dunder**

# Properties

**lowercase with underscores**

# Classes

**CamelCase**

having a leading underscore when private

# Modules and packages

**Lowercase**

# The naming guide

## Using the has/is prefixes for Boolean elements

> is_connected = False

> has_cache = False

## Using plurals for variables that are collections

> connected_users = ['Tarek']

> tables = {'Customer':['id', 'first_name', 'last_name']}

## Using explicit names for dictionaries

> persons_addresses = {'Bill': '6565 Monty Road', 'Pamela': '45 Python street'}

## Avoid generic names and redundancy

``` Python
def compute(data): # too generic
    for element in data:
        yield element ** 2
        
        
def squares(numbers): # better
    for number in numbers:
        yield number ** 2
```

Jeff Atwood, the co-founder of Discourse and Stack Overflow, has a very good
article on this topic and it can be found on his blog at  http://blog.codinghorror.com/i-
shall-call-it-somethingmanager/

Following names should be avoided in function and class names

* Manager

* Object

* Do, handle, or perform

## Avoiding existing names

**use a trailing underscore to avoid name collision**

**_class_ keyword is often replaced by  _klass_ or  _cls_**

# Best practices for arguments

* Build arguments by iterative design.

* Trust the arguments and your tests.

* Use  \*args and  \*\*kwargs magic arguments carefully.

## Building arguments by iterative design

If you want to extend the signature of the function or method with new arguments in a
way that preserves backward compatibility, you should provide default values for these
arguments

## Trusting the arguments and your tests

There are 2 drawbacks of Design by Contract (DbC) programming(use assertions at the top of their functions and methods to make sure the arguments have proper content)

* DbC's code explains how it should be used, making it less readable

* This can make it slower, since the assertions are made on each call


## Using \*args and \*\*kwargs magic arguments carefully

# Class names

A common practice is to use a suffix that informs about its type or nature, for example:

* SQLEngine

* MimeTypes

* StringWidget

* TestCase

For base or abstract classes, a Base or Abstract prefix can be used as follows:

* BaseCookie

* AbstractFormatter

Try to avoid redundancy between the class and its attributes' names as follows:

` >>> SMTP.smtp_send() # redundant information in the namespace`

` >>> SMTP.send() # more readable and mnemoni`

# Module and package names

They are often suffixed with  lib if they are implementing a protocol, as in the following:

``` Python
import smtplib
import urllib
import telnetlib
```
When choosing a name for a module, always consider its content and limit the amount
of redundancy within the whole namespace, for example:

``` Python
from widgets.stringwidgets import TextWidget # bad
from widgets.strings import TextWidget # better
```

# Useful tools

* _pylint_ : This is a very flexible source code analyzer, giving following information

  * Code duplication metrics
  
  * Unused variables and imports
  
  * Missing function, method, or class docstrings
  
  * Too long function signatures

* _pycodestyle_ and  _flake8_ : This is a small code style checker and a wrapper that
  adds to it some more useful features, such as static analysis and complexity
  measurement
  

