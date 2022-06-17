#####################################################################
# >> The dir Function
#####################################################################

# We have a build-in function called "dir()", that get us a list of attributes and methods defined in an object.
# We have underscore attributes we call them magic attributes

# > import the contact object
from ecommerce.customer import contact
# > import the sales object
from ecommerce.shopping import sales

print(dir(contact))
# output:
# [
#   '__builtins__', 
#   '__cached__', 
#   '__doc__', 
#   '__file__', 
#   '__loader__',
#   '__name__', 
#   '__package__', 
#   '__spec__', 
#   'get_Contact'
# ]

print(dir(sales))
# output:
# [
#   '__builtins__', 
#   '__cached__', 
#   '__doc__', 
#   '__file__', 
#   '__loader__',
#   '__name__', 
#   '__package__', 
#   '__spec__', 
#   'cal_tax', 
#   'calc_shipping'
# ]


#####################################################################
# >> The Magic Attributes
#####################################################################


# from ecommerce.customer import contact
# from ecommerce.shopping import sales


# >> Get the name of our module 
print(sales.__name__)
# output:
# ecommerce.shopping.sales

# >> Also get the file name address location
print(sales.__file__)
# output:
# c:\Users\<username>\OneDrive\Python\Python_Notes\Python Modules_Packages_Libraries\4. build-in functions\ecommerce\shopping\sales.py

# >> Get the name of our package
print(sales.__package__)
# output:
# ecommerce.shopping

print(sales.__doc__)
# output:
# None