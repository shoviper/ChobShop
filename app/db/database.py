import ZODB
import ZODB.FileStorage
import transaction
from BTrees.OOBTree import BTree
from .model import *

storage = ZODB.FileStorage.FileStorage('app/db/mydata.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

if not hasattr(root, 'generalUsers'):
    root.generalUsers = BTree()
if not hasattr(root, 'adminUsers'):
    root.adminUsers = BTree()
if not hasattr(root, 'customerUsers'):
    root.customerUsers = BTree()
if not hasattr(root, 'LoggedInUser'):
    root.LoggedInUser = LoggedInUser(None)

def register(username, email, password):
    if username in root.customerUsers or email in root.customerUsers:
        # print("User already exists")
        if username in root.customerUsers:
            print("Username already exists")
            # print_database_contents(username)
        return False
    else:
        user = Customer(username, email, password)
        root.customerUsers[username] = user
        transaction.commit()
        return True
    
#-------------------Admin Register------------------------
#-------------------Not yet tested
def registerAdmin(username, shopname, name, lastname, description, address, email, phone, password):
    if shopname in root.adminUsers:
        # print("User already exists")
        if shopname in root.adminUsers:
            print("Shop's name already exists")
        return False
    else:
        user = Admin(username, shopname, name, lastname, description, address, email, phone, password)
        root.adminUsers[username] = user
        transaction.commit()
        return True
#-------------------------------------------------------------
    
def login(username, password, admin=False):
    if password is None or (username is None):
        if password is None:
            print("Password is None")
        return False
    if username.find('@') != -1:
        email = username
        username = None
    user = None
    if username is not None:
        if username in root.customerUsers and not admin:
            user = root.customerUsers[username]
        elif username in root.adminUsers and admin:
            user = root.adminUsers[username]
    elif email is not None:
        if email in root.customerUsers and not admin:
            user = root.customerUsers[email]
        elif email in root.adminUsers and admin:
            user = root.adminUsers[email]
    
    if user and user.password == password:
        root.LoggedInUser = LoggedInUser(user)
        root.LoggedInUser.logged_in = True
        return True
    else:
        return False
    
def logout(username):
    if username in root.customerUsers or username in root.adminUsers:
        root.LoggedInUser.logged_in = False
    else:
        return False
    return True


def print_all_users():
    print("Users:")
    for user in root.customerUsers.values():
        print("--------------------------------")
        print(f"Username: {user.username}")
        print(f"Email: {user.email}")
        print(f"Name: {user.name}")
        print(f"Lastname: {user.lastname}")
        print(f"Address: {user.address}")
        print(f"Phone: {user.phone}")
        print(f"Admin: {user.admin}")


def print_database_contents(username):
    print("General Users:")
    # for user in root.customerUsers[username]:
    # for user in username.values():
    if username in root.customerUsers:
        user = root.customerUsers[username]
        print(f"Username: {user.username}")
        print(f"Password: {user.password}")
        print(f"Email: {user.email}")
        print(f"Name: {user.name}")
        print(f"Lastname: {user.lastname}")
        print(f"Address: {user.address}")
        print(f"Phone: {user.phone}")
        print(f"Admin: {user.admin}")
        print(f"Cart: {user.cart}")
        print(f"Orders: {user.orders}")
        
#-------------------------------------------------------------
def printAdminContent(username):
    print("Admin Users:")
    if username in root.adminUsers:
        user = root.adminUsers[username]
        print(f"Username: {user.username}")
        print(f"Password: {user.password}")
        print(f"Email: {user.email}")
        print(f"Name: {user.name}")
        print(f"Lastname: {user.lastname}")
        print(f"Address: {user.address}")
        print(f"Phone: {user.phone}")
        print(f"Admin: {user.admin}")
        print(f"Cart: {user.cart}")
        print(f"Orders: {user.orders}")    
#-------------------------------------------------------------

# class Connection():
# storage = ZODB.FileStorage.FileStorage('app/db/mydata.fs')
# db = ZODB.DB(storage)
# connection = db.open()
# root = connection.root()

# def __init__(self):
# self.connection = Connection.connection
# self.root = Connection.root  # Assign the class attribute to instance attribute
# if not hasattr(root, 'generalUsers'):
#     root.generalUsers = BTree()
# if not hasattr(root, 'adminUsers'):
#     root.adminUsers = BTree()
# if not hasattr(root, 'customerUsers'):
#     root.customerUsers = BTree()


# class Account(persistent.Persistent):    
#     def __init__(self):
#         self.root = root
    
#     def register(self, username, email, password):
#         if username in root.customerUsers or email in root.customerUsers:
#             return False
#         else:
#             user = Customer(username, email, password)
#             root.customerUsers[username] = user
#             transaction.commit()
#             return True
    
#     def login(self, username=None, email=None, password=None):
#         if password is None or (username is None and email is None):
#             if password is None:
#                 print("o")
#             if username is None and email is None:
#                 print("u")
#             return False
        
#         user = None
#         if username is not None:
#             if username in root.customerUsers:
#                 user = root.customerUsers[username]
#             elif username in root.adminUsers:
#                 user = root.adminUsers[username]
#         elif email is not None:
#             if email in root.customerUsers:
#                 user = root.customerUsers[email]
#             elif email in root.adminUsers:
#                 user = root.adminUsers[email]
        
#         if user and user.password == password:
#             return True
#         else:
#             print("1")
#             return False
        
    
#     def print_database_contents(self, username):
#         print("General Users:")
#         for user in self.
#             print(f"Username: {user.username}")
#             print(f"Email: {user.email}")
#             print(f"Name: {user.name}")
#             print(f"Surname: {user.surname}")
#             print(f"Address: {user.address}")
#             print(f"Phone: {user.phone}")
#             print(f"Admin: {user.admin}")
#             print(f"Cart: {user.cart}")
#             print(f"Orders: {user.orders}")