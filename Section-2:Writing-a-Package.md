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
