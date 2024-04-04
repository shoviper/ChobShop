import ZODB
import ZODB.FileStorage
import transaction
from BTrees.OOBTree import BTree
from app.db.model import *
from app.db.database import *

from app.backend.adminUser.products_admin import *


def addToCart(product_id):
    cart = root.LoggedInUser.user.cart
    product = get_product_by_id(product_id)
    if product.stock > 0:
        product.stock -= 1
        if product_id in cart:
            cart[product_id] += 1
        else:
            cart[product_id] = 1
        # transaction.commit()
        return True
    
def get_cart():
    user = root.LoggedInUser.user.username
    cart = root.LoggedInUser.user.cart
    cart_products = []
    for product_id, quantity in cart.items():
        product = get_product_by_id(product_id)
        cart_products.append((product, quantity))
    return cart_products