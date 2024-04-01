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

def addproduct(productname, description, price, sizes, options, stock, categories, img=[]):
    user = root.LoggedInUser.user.username
    print("productname: ", productname)
    print("description: ", description)
    print("price: ", price)
    print("sizes: ", sizes)
    print("options: ", options)
    print("category: ", categories)
    print("stock: ", stock, "\n=====================")
    
    
    if user not in root.adminUsers:
        return False
    else:
        print("productdb: ", root.ProductDatabase)

        # if len(root.adminUsers[user].products) == 0:
        #     print("product: 0")
        # else:
        
        # product = Product(p_id, productname, description, price, sizes, options, stock, categories)
        # print("product: ", product, product.name)
        # root.adminUsers[user].products[p_id] = product
        
        new_product_id = root.ProductDatabase.add_product(
            name=productname,
            description=description,
            price=price,
            sizes=sizes,
            options=options,
            stock=stock,
            categories=categories
        )
        
        for i in img:
            root.ProductDatabase.products[new_product_id].add_img(i)
        
        transaction.commit()
        
        # print("new_product_id: ", new_product_id)
        
        # print("++++++++++++++++++++++++++++++")
        # print("All products: ", root.ProductDatabase)

    return True