"""
To run this program, this is the way to Organize the files to run properly.
10_Package
|--__init__.py
|--10.Packages.py
|--class1.py
|--class2.py
"""

from class1 import Class1
from class2 import Class2

obj1 = Class1("Mihir")
obj2 = Class2(22)

obj1.print_name()
obj2.print_age()