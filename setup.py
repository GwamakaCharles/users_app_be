"""
1. The first step is to create a folder called 'app' in the current folder.
2. The second step is to create a file called 'setup.py' in the 'app' folder.
3. The third step is to import the setuptools module and use the setup function to tell distutils how to build this package.
4. The fourth step is to tell distutils what the name of the package is, and where it can be found.
5. The fifth step is to tell distutils what files to include in the package.
6. The sixth step is to tell distutils to include any data files in the package.
7. The seventh step is to tell distutils to actually build the package. 
"""

from setuptools import setup


setup(
    name='users_app_be',
    packages=['app'],
    include_package_data=True
)

