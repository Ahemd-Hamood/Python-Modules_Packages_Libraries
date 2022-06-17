# Absolute Import (pep-8 recommend using absolute import) :-
from ecommerce.customer import contact

# Relative Import :-
from ..customer import contact

# from .  --> this represent the current package
# from .. --> this represent one level up

def calc_shipping():
    print("Shipping calculate....")
    print("shipping to customer with contact number:")
    contact.get_Contact()


def cal_tax():
    print("Tax calculate....")
