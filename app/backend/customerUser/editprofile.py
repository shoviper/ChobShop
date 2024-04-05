import ZODB
import ZODB.FileStorage
import transaction
from BTrees.OOBTree import BTree
from app.db.model import *
from app.db.database import *

def deleteProfile(username):
    if username not in root.customerUsers:
        print("username not in root.customerUsers:")
        return False
    del root.customerUsers[username]
    transaction.commit()
    return True

def changePassword(username, oldpassword, newpassword):
    if username not in root.customerUsers:
        print("username not in root.customerUsers:")
        return
    user = root.customerUsers[username]
    if user.password != oldpassword:
        print("user.password != oldpassword:")
        return
    user.password = newpassword
    transaction.commit()
    return

def editProfile(username, name=None, lastname=None, gender=None, birthday=None, email=None, phone=None):
    if username not in root.customerUsers:
        print("username not in root.customerUsers:")
        return False
    user = root.customerUsers[username]
    
    if email != None:
        if email in root.customerUsers:
            if email == user.email:
                pass
            else:
                print("email in root.customerUsers:")
                return False
        elif email == "":
            print("email == '':")
            return False
        else:
            user.email = email
    if name != None:
        user.name = name
    if lastname != None:
        user.lastname = lastname
    if gender != None:
        user.gender = gender
    if birthday != None:
        user.birthday = birthday
    if phone != None:
        user.phone = phone
    
    transaction.commit()
    return True