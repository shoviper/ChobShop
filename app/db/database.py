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

def register(username, email, password):
    if username in root.generalUsers or email in root.generalUsers:
        return False
    else:
        user = Customer(username, email, password)
        root.customerUsers[username] = user
        transaction.commit()
        return True
    
def login(username=None, email=None, password=None):
    if password is None or (username is None and email is None):
        return False
    
    user = None
    if username is not None:
        if username in root.customerUsers:
            user = root.customerUsers[username]
        elif username in root.adminUsers:
            user = root.adminUsers[username]
    elif email is not None:
        if email in root.customerUsers:
            user = root.customerUsers[email]
        elif email in root.adminUsers:
            user = root.adminUsers[email]
    
    if user and user.password == password:
        return True
    else:
        return False
