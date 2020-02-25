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

**lowercase with underscores**

# The private controversy

**name mangling**

# Special methods

**dunder**

# Properties

**lowercase with underscores**

# Classes

**CamelCase**

having a leading underscore when private

# Modules and packages

**lowercase**






