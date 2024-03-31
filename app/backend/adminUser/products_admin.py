import ZODB
import ZODB.FileStorage
import transaction
from BTrees.OOBTree import BTree
from app.db.model import *
from app.db.database import *



def addproduct(productname, description, price, sizes, options, stock, categories):
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
        transaction.commit()
        
    
        print("new_product_id: ", new_product_id)
        
        print("++++++++++++++++++++++++++++++")
        print("All products: ", root.ProductDatabase.get_all_products())

    return True