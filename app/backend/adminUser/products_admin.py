import ZODB
import ZODB.FileStorage
import transaction
from BTrees.OOBTree import BTree
from app.db.model import *
from app.db.database import *
import random as r
import datetime

if not hasattr(root, 'Product'):
    root.Product = BTree()
if not hasattr(root, 'ProductDatabase'):
    root.ProductDatabase = ProductDatabase()
else:
    print("ProductDatabase already exists")
    for product_id, product in root.ProductDatabase.products.items():
        print(product_id, product)
        
def count_products_for_user(username):
        user_products = root.ProductDatabase.get_products_for_user(username)
        return len(user_products)
    
def get_products_for_user(username):
    user_products = root.ProductDatabase.get_products_for_user(username)
    return user_products

def get_all_products():
    all_products = []
    for user, products in root.ProductDatabase.products.items():
        for product in products:
            all_products.append(product)
    return all_products

def get_shopname_by_product_id(product_id):
    for user, products in root.ProductDatabase.products.items():
        for product in products:
            if product.id == product_id:
                return root.adminUsers[user].shopname
    return None

def get_shop_allproducts_by_product_id(product_id):
    for user, products in root.ProductDatabase.products.items():
        for product in products:
            if product.id == product_id:
                return products
    return None

def get_shop_date_registered_by_product_id(product_id):
    for user, products in root.ProductDatabase.products.items():
        for product in products:
            if product.id == product_id:
                return root.adminUsers[user].dateregistered
    return None

def get_shop_reviews_by_product_id(product_id):
    review = 0
    shopname = get_shopname_by_product_id(product_id)
    shopowner = ""
    for admin in root.adminUsers:
        if root.adminUsers[admin].shopname == shopname:
            shopowner = root.adminUsers[admin].username
            break
    for product in root.adminUsers[shopowner].products:
        review += product.reviews
    len_products = len(root.adminUsers[shopowner].products)
    if len_products == 0:
        return 0
    return review // len_products

def get_all_product_name_and_id():
    all_products = get_all_products()
    product_name_and_id = []
    for product in all_products:
        product_name_and_id.append((product.name, product.id))
    return product_name_and_id

def get_random_product_id():
    all_products = get_all_products()
    random_product = r.choice(all_products)
    return random_product.id

def get_product_by_id(product_id):
    for product in get_all_products():
        if product.id == product_id:
            return product
    return None

def get_img_for_product(product_id):
    for product in get_all_products():
        if product.id == product_id:
            return product.img
    return None

def get_first_img_for_product(product_id):
    for product in get_all_products():
        if product.id == product_id:
            return product.img[0]
    return None

def get_product_name_by_id(product_id):
    for product in get_all_products():
        if product.id == product_id:
            return product.name
    return None

def get_product_price_by_id(product_id):
    for product in get_all_products():
        if product.id == product_id:
            return product.price
    return None

def get_product_description_by_id(product_id):
    for product in get_all_products():
        if product.id == product_id:
            return product.description
    return None

def get_product_sizes_by_id(product_id):
    for product in get_all_products():
        if product.id == product_id:
            return product.sizes
    return None

def get_product_stock_by_id(product_id):
    for product in get_all_products():
        if product.id == product_id:
            return product.stock
    return None

def get_product_options_by_id(product_id):
    for product in get_all_products():
        if product.id == product_id:
            return product.options
    return None

def get_product_categories_by_id(product_id):
    for product in get_all_products():
        if product.id == product_id:
            return product.categories
    return None

def get_product_publishedDate_by_id(product_id):
    for product in get_all_products():
        if product.id == product_id:
            return product.publishedDate
    return None

def get_product_reviews_by_id(product_id):
    for product in get_all_products():
        if product.id == product_id:
            return product.reviews
    return None

def get_product_sold_by_id(product_id):
    for product in get_all_products():
        if product.id == product_id:
            return product.sold
    return None

def get_product_img_by_id(product_id):
    for product in get_all_products():
        if product.id == product_id:
            return product.img
    return None

def get_first_product_img(username, product_id):
    user_products = root.ProductDatabase.get_products_for_user(username)
    for product in user_products:
        if product.id == product_id:
            return product.img[0]
    return None

def get_product_name(username, product_id):
    user_products = root.ProductDatabase.get_products_for_user(username)
    for product in user_products:
        if product.id == product_id:
            return product.name
    return None

def get_product_price(username, product_id):
    user_products = root.ProductDatabase.get_products_for_user(username)
    for product in user_products:
        if product.id == product_id:
            return product.price
    return None
    
def delete_product(username, product_id):
    if root.ProductDatabase.remove_product(root.LoggedInUser.user.username, product_id):
        transaction.commit()
        return True
    return False

def delete_product_by_id(product_id):
    if root.ProductDatabase.remove_product_by_id(product_id):
        transaction.commit()
        return True
    return False

def addproduct(productname, description, price, sizes, options, stock, categories, img):
    user = root.LoggedInUser.user.username
    print("user: ", user)
    print("productname: ", productname)
    print("description: ", description)
    print("price: ", price)
    print("sizes: ", sizes)
    print("options: ", options)
    print("category: ", categories)
    print("img: ", img)
    print("stock: ", stock, "\n=====================")
    
    
    if user not in root.adminUsers:
        return False
    else:
        print("productdb: ", root.ProductDatabase)
        
        new_product_id = root.ProductDatabase.add_product(
            user=user,
            name=productname,
            description=description,
            price=price,
            sizes=sizes,
            options=options,
            stock=stock,
            categories=categories,
            img=img
        )
        
        transaction.commit()

    return True


def update_qrc_file(img_name):
    qrc_file_path = 'app/assets/realsourceimg/realpicforuse.qrc'  
    try:
        with open(qrc_file_path, 'r') as file:
            lines = file.readlines()
    except IOError as e:
        print(f"Error reading .qrc file: {e}")
        return

    updated_lines = [line for line in lines if img_name not in line]

    try:
        with open(qrc_file_path, 'w') as file:
            file.writelines(updated_lines)
        print(f"Updated .qrc file: {qrc_file_path}")
    except IOError as e:
        print(f"Error writing .qrc file: {e}")
        
        
# ----------------------------- CART --------------------------------

def addToCart(product_id, size, option):
    print("size and option: ", size, option)
    user = root.LoggedInUser.user
    try:
        user.add_to_cart_by_product_id(product_id, 1, size, option)
        transaction.commit()
        return True
    except Exception as e:
        print("Error adding to cart: ", e)
        return False


def get_user_cart():
    cart = root.LoggedInUser.user.cart
    # print("cart: ", cart) 
    cart_products_id = []
    for product_id, quantity, s, o in cart:
        cart_products_id.append([product_id, quantity, s, o])
    # print("cart_products_id: ", cart_products_id)
    return cart_products_id
    # return [[1,2], [2,3], [3,4]]

def removeFromCart(product_id):
    user = root.LoggedInUser.user.username
    root.LoggedInUser.user.remove_from_cart_by_product_id(product_id)
    transaction.commit()
    return True


# -------------------------------------------------------------

def addToOrder(product_id, quantity, size, option):
    user = root.LoggedInUser.user
    user.add_to_order(product_id, quantity, size, option)
    transaction.commit()
    return True

def get_user_order():
    order = root.LoggedInUser.user.orders
    order_products_id = []
    for product_id, quantity, s, o, t in order:
        order_products_id.append([product_id, quantity, s, o, t])
    return order_products_id

def decrese_from_stock(product_id, quantity):
    if root.ProductDatabase.drecrease_stock(product_id, quantity):
        transaction.commit()
        return True