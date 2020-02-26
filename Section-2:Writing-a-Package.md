# Creating a package

## The confusing state of Python packaging tools

The **Python Packaging User Guide** ( https://packaging.python.org ),
maintained by PyPA, is the authoritative source of information about the latest packaging
tools and best practices.

All of
PyPA's projects can be found under a single organization on GitHub:  https://github.com/
pypa.

## Tool recommendations

* Tools for installing packages
  
  * Use  **_pip_** for installing packages from PyPI.
  
  * Use  **_virtualenv_** or  **_venv_** for application-level isolation of the Python runtime
    environment.

* Tools for package creation and distribution

  * Use  **_setuptools_** to define projects and create source distributions.
  
  * Use **_wheels_** in favor of **_eggs_** to create built distributions.
  
  * Use  **_twine_** to upload package distributions to PyPI.

# Project configuration

## setup.py

The root directory of a package that has to be distributed contains a  _setup.py_ script.
It defines all metadata. It is actually recommended to use the  _setuptools_.

Therefore, the minimum content for this file is as follows:

``` Python
from setuptools import setup

setup(
    name='mypackage',
)
```

The script provides several commands that can be listed with the  --help-commands option, as shown in the following code:

> python3 setup.py --help-commands

**Standard commands** are the built-in commands provided
by  _distutils_ , whereas **extra commands** are the ones provided by third-party packages,
such as  _setuptools_ or any other package that defines and registers a new command.

## setup.cfg

The  _setup.cfg_ file contains default options for commands of the  _setup.py_ script.

Here
is an example of the  _setup.cfg_ configuration file that provides some  _global_ ,  _sdist_ ,
and  _bdist\_wheel_ commands' defaults:

``` Python
[global]
quiet=1

[sdist]
formats=zip,tar

[bdist_wheel]
universal=1
```

This example configuration will ensure that source distributions ( sdist section) will
always be created in two formats (ZIP and TAR) and the built  wheel distributions
( bdist\_wheel section) will be created as universal wheels that are independent from the
Python version. Also most of the output will be suppressed on every command by the
global  --quiet switch. Note that this option is included here only for demonstration
purposes and it may not be a reasonable choice to suppress the output for every command
by default.


## MANIFEST.in

When building a distribution with the  sdist command, the  distutils module browses
the package directory looking for files to include in the archive. By default  distutils will
include the following:

* All Python source files implied by the  _py\_modules_ ,  _packages_ , and  _scripts_
  arguments

* All C source files listed in the  _ext\_modules_ argument

* Files that match the glob pattern  _test/test\*.py_

* Files named  _README_ ,  _README.txt_ ,  _setup.py_ , and  _setup.cfg_

Besides that, if your package is versioned with a version control system such as Subversion,
Mercurial, or Git, there is the possibility to auto-include all version controlled files using
additional  _setuptools_ extensions such as  _setuptools-svn_ ,  _setuptools-hg_ ,
and  _setuptools-git_ . Integration with other version control systems is also possible
through other custom extensions. No matter if it is the default built-in collection strategy or
one defined by custom extension, the  _sdist_ will create a  _MANIFEST_ file that lists all files
and will include them in the final archive.

Let's say you are not using any extra extensions, and you need to include in your package
distribution some files that are not captured by default. You can define a template
called  _MANIFEST.in_ in your package root directory (the same directory as  _setup.py_ file).
This template directs the  sdist command on which files to include.

This  MANIFEST.in template defines one inclusion or exclusion rule per line:

``` Python
include HISTORY.txt
include README.txt
include CHANGES.txt
include CONTRIBUTORS.txt
include LICENSE
recursive-include *.txt *.py
```

The full list of the  _MANIFEST.in_ commands can be found in the official  _distutils_
documentation.


## Most important metadata

Besides the name and the version of the package being distributed, the most important
arguments that the  _setup()_ function can receive are as follows:

* _description_ : This includes a few sentences to describe the package.

* _long\_description_ : This includes a full description that can be in
  _reStructuredText_ (default) or other supported markup languages.
  
* _long\_description\_content\_type_ : this defines **MIME** type of long
  description; it is used to tell the package repository what kind of markup
  language is used for the package description.
  
* _keywords_ : This is a list of keywords that define the package and allow for better
  indexing in the package repository.
  
* _author_ : This is the name of the package author or organization that takes care of
  it.
  
* _author\_email_ : This is the contact email address.

* _url_ : This is the URL of the project.

* _license_ : This is the name of the license (GPL, LGPL, and so on) under which the
  package is distributed.
  
* _packages_ : This is a list of all package names in the package
  distribution;  setuptools provides a small function called  find\_packages that
  can automatically find package names to include.

* _namespace\_packages_ : This is a list of namespace packages within package
  distribution.

