import ZODB
import ZODB.FileStorage
import transaction
from BTrees.OOBTree import BTree
from app.db.model import *
from app.db.database import *

def editProfile(username, newusername=None, name=None, lastname=None, gender=None, birthday=None, email=None, phone=None):
    if username not in root.customerUsers:
        print("username: ", username)
        print("username not in root.customerUsers:")
        return False
    user = root.customerUsers[username]
    print("user.key: ", user.key)
    print("username: ", username)
    print("newusername: ", newusername)
    print(root.LoggedInUser.user.username)
        
    if newusername != username:
        if newusername in root.customerUsers:
            print("newusername in root.customerUsers:")
            return False
        elif newusername == "":
            print("newusername == '':")
            return False
        elif newusername == None:
            print("newusername == None:")
            return False
        else:
            user.username = newusername
            
    if email != None:
        if email in root.customerUsers:
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

def deleteProfile(username):
    if username not in root.customerUsers:
        print("username not in root.customerUsers:")
        return False
    del root.customerUsers[username]
    transaction.commit()
    return True