import ZODB
import ZODB.FileStorage
import transaction
from BTrees.OOBTree import BTree
from app.db.model import *
from app.db.database import *

def openshop():
    user = root.LoggedInUser.user.username
    if user not in root.adminUsers:
        return False
    else:
        return True
    
def changeLoggedinUser(username):
    root.LoggedInUser.user = root.adminUsers[username]
    transaction.commit()
    return True