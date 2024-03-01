import ZODB
import ZODB.FileStorage
import transaction
from BTrees.OOBTree import BTree
from app.db.model import *
from app.db.database import *

def editProfile(username, newusername=None, name=None, lastname=None, gender=None, birthday=None, email=None, phone=None):
    if username in root.customerUsers:
        user = root.customerUsers[username]
        user.name = name
        user.lastname = lastname
        user.gender = gender
        user.birthday = birthday
        user.email = email
        user.phone = phone
        if newusername != username:
            user.key = newusername
        transaction.commit()
        return True
    return False

