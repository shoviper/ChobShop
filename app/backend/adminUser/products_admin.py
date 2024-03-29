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
        p_id = 0
        if len(root.adminUsers[user].products) == 0:
            print("product: 0")
        else:
            for admin in root.adminUsers:
                print("admin: ", admin)
                print("idid: " ,root.adminUsers[admin].products[p_id].name)
                for product in root.adminUsers[admin].products:
                    print("products: ",root.adminUsers[admin].products[product].id, root.adminUsers[admin].products[product].name)
                    if root.adminUsers[admin].products[product].id >= p_id:
                        p_id = root.adminUsers[admin].products[p_id].id + 1
                        print("id: ", p_id)
        product = Product(p_id, productname, description, price, sizes, options, stock, categories)
        print("product: ", product, product.name)
        root.adminUsers[user].products[p_id] = product
        transaction.commit()
        return True