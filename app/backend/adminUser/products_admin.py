import ZODB
import ZODB.FileStorage
import transaction
from BTrees.OOBTree import BTree
from app.db.model import *
from app.db.database import *

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


def update_qrc_file(self, img_name):
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