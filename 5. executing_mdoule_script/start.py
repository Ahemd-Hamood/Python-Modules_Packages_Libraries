##########################################################
# >> 1 - Executing Modules as script
##########################################################

# In our sales.py module we have two defined functions, also we have a statement that can be executed the first time the sales module is loaded.
# If we import the sales.py module in our program execution, python will load this module only once then cache it in memory.

# Also we can add some statement with ecommerce/shopping/__init__.py

from ecommerce.shopping import sales

# output:
# Shopping Package initialize....
# sales Module is loaded....


from ecommerce.customer import contact

# output:
# contact Module is loaded....
# The __name__ : ecommerce.customer.contact


print(__name__)
# output:
# __main__
