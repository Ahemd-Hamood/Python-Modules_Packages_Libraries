########################################################################
# >> 1 -  import Modules
########################################################################
# region

# >> What is Module :-
# a module is a file that contains some line codes like functions, variables and classes we refer them as "objects".
# The start.py file will be our main module or the entry point to our program, from here we are going to import other modules.

# >> Module Naming Convention :-
# The naming convention of the module file, its like variable and function we use all lower case letters.
# If you multiple words to separate them we use under score for example - final result -> final_result

# We have two module files in the current directory :-
# >> 1- ./module_A.py  => (2) functions --> message() and get_total(num1, num2)
# >> 2- ./sales        => (2) functions --> cal_tax() and cal_shipping()

# ----------------------------------------------------------------------
#  Now we are going to import the sales module file as following :
# ----------------------------------------------------------------------

# >> Ways and Syntax :-

import sys
import marketing
from sales import cal_shipping, cal_tax
import sales
from sales import *
from sales import cal_shipping

# A. > Import Single Object :-
# Above we're only importing the cal_shipping functions from the sales module

# Syntax: from <module_name> import object

# from sales import cal_shipping

cal_shipping()
# output:
# calculate Shipping....

# ================================


# B. > Import Multiple Objects, we separate them using a comma :-
# Above we're importing both  cal_shipping, cal_tax functions from the sales module

# Syntax: from <module_name> import object1, object2, ....

# from sales import cal_shipping, cal_tax

cal_shipping()
# output:
# calculate Shipping....

cal_tax()
# output:
# calculate Tax....

# ================================

# C. > Import all objects from a module using asterisk "*"  :-
# >>>> Bad practice Because in our module we could have several different object like functions or variables,
# >>>> those object may overwrite the objects with the same name in the current module, so don't import all objects like this.

# Syntax: from <module_name> import *

# from sales import *

cal_shipping()
# output:
# calculate Shipping....

cal_tax()
# output:
# calculate Tax....

# ================================

# D. > Import entire module from the module itself only, by starting with import and then we add the name of the module.
# > From our module we can access its objects/members by using the dot "." operator.
# > Each Module has objects defined like functions, classes and variables. In sales module we have two objects/functions inside it.

# Syntax: import <module_name>

# import sales


sales.cal_shipping()
# output:
# calculate Shipping....

sales.cal_tax()
# output:
# calculate Tax....

# endregion

########################################################################
# >> 2 - Complied Python File "__pycache__"
########################################################################
# region

# As you know start.py is the main module or the entry point of our program.
# From start.py we import other modules like "sales.py" and "marketing.py" modules.

# import sales
# import marketing

marketing.message()

# The start.py import objects from the "sales.py" and "marketing.py" modules.
# When you run "python3 start.py" a new folder will be created "__pycache__", and in this folder we have the complied version of all modules that we import into our program.
# We have a complied version of the sales module "__pycache__/sales.cpython-310" that we imported inside the start.py program.

# The complied python files inside the __pycache__ folder are used to speed up module loading. the compiled file is written in binary
# So next time you run your program python will look at the content of the "__pycache__" folder, and look for the complied version of our imported modules like the sales module.
# If it finds the complied module version, python will simply load that complied version, and it will skip the compilation step and load the existed complied version faster.

# >>>>>>>>>>>>>>
# Note: Complied python file is used to speed up the loading of the module, but not the actual performance of the application.
# >>>>>>>>>>>>>

# Q1: How python know if this complied version is up to date with the latest code in this sales module ?
# Ans: Basically python checks the data/time of these two files the source module "sales.py" and the complied version "sales.cpython-310",
# if the datetime of this source file is newer, then it realizes that our source code is changed, so it will re-compile it and store it in this "__pycache__" folder.

# endregion

########################################################################
# >> 3 - Module Search Path
########################################################################
# region

# import sales

# >> When import the sales module, python will look a file called "sales.py" in the current directory.
# >> If python does not find the "sales.py" in the current directory, it will look in a different pre-defined search path directories that come with python installation.

# >> To view these pre-defined search path, we have an object variable called "path" that exist in the "sys" build-in module.
# >> We use our variable path to return the list of directories that python will look at to find a module.

# import sys

# >> Let's print our path result on the terminal, and see our pre-defined path search list as an array of strings.
# >> python will start searching for the imported module on each element inside our search list string from top to bottom till it finds it then the search stops there.

print(sys.path)

# Output: (Windows)
# [
#   'c:\\Users\\<user-name>\\OneDrive\\0-My Document Drive\\Python\\Python_Notes\\Python Modules_Packages_Libraries\\1. modules', 
#   'C:\\Users\\<user-name>\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip', 
#   'C:\\Users\\<user-name>\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 
#   'C:\\Users\\<user-name>\\AppData\\Local\\Programs\\Python\\Python310\\lib', 
#   'C:\\Users\\<user-name>\\AppData\\Local\\Programs\\Python\\Python310',
#   'C:\\Users\\<user-name>\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages', 
#   'C:\\Users\\<user-name>\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\win32', 
#   'C:\\Users\\<user-name>\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\win32\\lib', 
#   'C:\\Users\\<user-name>\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\Pythonwin'
# ]

# >> The first string element in the list is our current folder/directory
# >> Then we have build-in libraries inside the python installation folder of version 3.10


# endregion
