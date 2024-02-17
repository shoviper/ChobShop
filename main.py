from app.db.database import *

if register("username", "email@example.com", "password"):
    print("User registered successfully")
else:
    print("User registration failed")

user = login(username="username", password="password")
if user:
    print("Login successful")
    print(user)
else:
    print("Login failed")
