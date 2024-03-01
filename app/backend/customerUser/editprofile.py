import ZODB
import ZODB.FileStorage
import transaction
from BTrees.OOBTree import BTree
from app.db.model import *
from app.db.database import *

def editProfile(username, name, lastname, gender, birthday, email, phone):
    if username in root.customerUsers:
        user = root.customerUsers[username]
        user.name = name
        user.lastname = lastname
        user.gender = gender
        user.birthday = birthday
        user.email = email
        user.phone = phone
        transaction.commit()
        return True

