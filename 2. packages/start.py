########################################################################
# >> 1 - Package create directory
########################################################################
# region

# Before we had all of our files or modules in the current directory, we will organize these files into sub-directories or simply inside other folders.

# > The different between Module and Package :-
# module -> it is a file that exist in the current directory/folder. all modules in one folder
# package -> it is a file that exist in sub-directory or other folders that exist in the current directory. all modules in different folders

# We will create a new file called "sales.py" and add it inside a directory called "ecommerce" -> "/ecommerce/sales.py"
# Now to import our sales file inside the ecommerce folder, we need to tell python that our ecommerce folder is a package.

# We create a new empty file called "__init__.py" inside the ecommerce folder "/ecommerce/__init__.py".
# The __init__.py will tell python to treat the ecommerce folder as a "package"

# >> a "package" is a container for one or more modules.
# >> In file system terms a "package" is mapped to a <directory>, and a "module" is mapped to a <file>

from ecommerce.shopping.items import get_items
import ecommerce.shopping
from ecommerce.shopping import items
import imp
from marketing.social import facebook
from marketing.social.facebook import fb_message
from marketing import revenue
import marketing.social.facebook
from ecommerce import sales
from marketing.revenue import message, get_revenue
from ecommerce.sales import Sales
import marketing.revenue
import ecommerce.sales

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# > Access Package with import only - Way 1
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# >> To access our "sales.py" module from the "ecommerce" folder, we use the dot operator as following :-
# >> To access our "revenue.py" module from the "marketing" folder, we use the dot operator as following :-
# >> To access our "facebook.py" module from the "marketing.social" sub-folder, we use the dot operator as following :-

# import marketing.revenue
# import marketing.social.facebook
# import ecommerce.sales

# >> Now to create a new Sales class instance :-

sales_1 = ecommerce.sales.Sales("Item1", 332)

sales_1.get_info()
# output:
# Item name: Item1, the price is 332

# >> Now to call he message function from the revenue module :-

marketing.revenue.message()
# output:
# This is a message

marketing.revenue.get_revenue()
# output:
# Revenue is 20,0000

marketing.social.facebook.fb_message()
# output:
# Facebook message


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# > Access Package with from-import - Way 2
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# from ecommerce.sales import Sales
# from marketing.revenue import message, get_revenue
# from marketing.social.facebook import fb_message

sales_2 = Sales("Item1", 332)

sales_2.get_info()
# output:
# Item name: Item1, the price is 332

# >> Now to call he message function from the revenue module :-

message()
# output:
# This is a message

get_revenue()
# output:
# Revenue is 20,0000

fb_message()
# output:
# Facebook message

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# > Access Package with from-import - Way 3
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# from ecommerce import sales
# from marketing import revenue
# from marketing.social import facebook

sales_3 = sales.Sales("Item1", 332)

sales_3.get_info()
# output:
# Item name: Item1, the price is 332

revenue.message()
# output:
# This is a message

revenue.get_revenue()
# output:
# Revenue is 20,0000

facebook.fb_message()
# output:
# Facebook message


# endregion

########################################################################
# >> 2 - Package create sub-packages
########################################################################
# region
print("#" * 50)

# >> Usually you want to break down you module packages into sub-packages or sub-directory.
# >> Add or break packages into sub-packages, a new folder inside a folder

# ecommerce > Sales.py  --> (File inside a directory)

# ecommerce > shopping > items.py --> (File inside a sub-directory)
# marketing > social > facebook.py --> (File inside a sub-directory)

# >> Don't forget to consider a folder as package, we need to add a new file called "__init__.py"
# >> To access sub-directory we use the dot operator

# >>>>>>>>>>>>>>>
# Way 1
# >>>>>>>>>>>>>>>

# from ecommerce.shopping import items

items.get_items()
# output:
# ['item1', 'item2', 'item3']

# >>>>>>>>>>>>>>>
# Way 2
# >>>>>>>>>>>>>>>

# import ecommerce.shopping

ecommerce.shopping.items.get_items()
# output:
# ['item1', 'item2', 'item3']

# >>>>>>>>>>>>>>>
# Way 3
# >>>>>>>>>>>>>>>

# from ecommerce.shopping.items import get_items
get_items()
# output:
# ['item1', 'item2', 'item3']


# endregion
