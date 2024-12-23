import persistent
import datetime
import BTrees.OOBTree
import uuid

from .database import *

class Product(persistent.Persistent):
    def __init__(self, id, name, description, price, sizes, options, stock, categories, img) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.sizes = sizes
        self.options = options
        self.stock = stock
        self.categories = categories
        self.img = img
        self.sold = 0
        self.reviews = []
        self.publishedDate = datetime.datetime.now()

    def add_review(self, review):
        self.reviews[datetime.datetime.now()] = review
        
    def add_img(self, img_path):
        self.img.append(img_path)

    def toJSON(self):
        return {
            # "account": self.account,
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "sizes": self.sizes,
            "category": self.categories,
            "stock": self.stock,
            "sold": self.sold,
            "reviews": self.reviews,
            "publishedDate": self.publishedDate
        }
    
    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}, price: {self.price}, description: {self.description}, categories: {self.categories}, stock: {self.stock}, sold: {self.sold}, reviews: {self.reviews}, img: {self.img}\n"

class ProductDatabase(persistent.Persistent):
    def __init__(self):
        self.products = {}
        self.next_id = 1

    def add_product(self, user, name, description, price, sizes, options, stock, categories, img):
        product_id = self.next_id
        product = Product(product_id, name, description, price, sizes, options, stock, categories, img)
        if user not in self.products:
            self.products[user] = []
        self.products[user].append(product)
        self.next_id += 1
        return product_id
    
    def get_user_from_product(self, product_id):
        for user, products in self.products.items():
            for product in products:
                if product.id == product_id:
                    return user
        return None

    def get_products_for_user(self, user):
        return self.products.get(user, [])
    
    def get_products_id_for_user(self, user):
        user_products = self.products.get(user, [])
        return [product.id for product in user_products]

    def get_product(self, user, product_id):
        user_products = self.products.get(user, [])
        for product in user_products:
            if product.id == product_id:
                return product
        return None
    
    def drecrease_stock(self, user, product_id, quantity):
        user_products = self.products.get(user, [])
        for product in user_products:
            if product.id == product_id:
                product.stock -= quantity
                product.sold += quantity
                return True
        return False

    def update_product(self, user, product_id, **kwargs):
        user_products = self.products.get(user, [])
        for product in user_products:
            if product.id == product_id:
                for key, value in kwargs.items():
                    if hasattr(product, key):
                        setattr(product, key, value)
                return True
        return False

    def remove_product(self, user, product_id):
        user_products = self.products.get(user, [])
        for i, product in enumerate(user_products):
            if product.id == product_id:
                del user_products[i]
                print("product removed")
                return True
        
        return False
    
    def remove_product_by_id(self, product_id):
        for user, products in self.products.items():
            for i, product in enumerate(products):
                if product.id == product_id:
                    del products[i]
                    print("product removed")
                    return True
        return False

    
    def toJSON(self):
        return {
            "products": {user: [p.toJSON() for p in products] for user, products in self.products.items()},
            "next_id": self.next_id
        }
    
    def __str__(self) -> str:
        return f"products: {self.products}, next_id: {self.next_id}"

class Cart(persistent.Persistent):
    def __init__(self, products) -> None:
        self.products = products
        self.total = len(products)

    def add_product(self, product):
        self.products.append(product)
        self.total += 1

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            self.total -= 1

    def toJSON(self):
        return {
            "products": self.products,
            "total": self.total
        }
    
    def __str__(self) -> str:
        return f"products: {self.products}, total: {self.total}"


class GeneralUser(persistent.Persistent):
    def __init__(self, username, email, password) -> None:
        self.username = username
        self.email = email
        self.password = password
        self.gender = None
        self.name = None
        self.lastname = None
        self.address = None
        self.birthday = None
        self.phone = None
        self.admin = False
        self.profile_img = None

    def toJSON(self):
        return {
            "username": self.username,
            "email": self.email,
            "name": self.name,
            "lastname": self.lastname,
            "address": self.address,
            "birthday": self.birthday,
            "phone": self.phone,
            "admin": self.admin
        }
    
    def __str__(self) -> str:
        return f"\nusername: {self.username}, \nemail: {self.email}, \nname: {self.name}, \nlastname: {self.lastname}, \naddress: {self.address}, \nbirthday: {self.birthday}, \nphone: {self.phone}, \nadmin: {self.admin}"
    
class Customer(GeneralUser):
    def __init__(self, username, email, password) -> None:
        super().__init__(username, email, password)
        self.favorites = []
        self.cart = []
        self.orders = []
        self.reviews = None
        self.admin = False
                
    def add_to_cart_by_product_id(self, product_id, quantity, size, option):
        for item in self.cart:
            if item[0] == product_id:
                item[1] += quantity
                return
        self.cart.append([product_id, quantity, size, option])
                
    def remove_from_cart_by_product_id(self, product_id):
        for item in self.cart:
            if item[0] == product_id:
                self.cart.remove(item)
                return
            
    def generate_tracking_number(self):
        # Generate a unique tracking number using UUID and timestamp
        unique_id = uuid.uuid4()
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        return f"{timestamp}-{unique_id}"
            
    def add_to_order(self, product_id, quantity, size, option):
        self.remove_from_cart_by_product_id(product_id)
        self.orders.append([product_id, quantity, size, option, "", "Processing"])

    def add_to_fav(self, product):
        self.favorites.append(product)

    def remove_from_fav(self, product):
        if product in self.favorites:
            self.favorites.remove(product)

    def add_review(self, product, review):
        self.reviews[product] = review

    def add_order(self, order):
        self.orders[order] = datetime.datetime.now()

    def toJSON(self):
        return {
            "username": self.username,
            "email": self.email,
            "name": self.name,
            "lastname": self.lastname,
            "address": self.address,
            "phone": self.phone,
            "admin": self.admin,
            "cart": self.cart,
            "orders": self.orders,
        }
    
    def __str__(self) -> str:
        return f"username: {self.username}, email: {self.email}, name: {self.name}, lastname: {self.lastname}, address: {self.address}, phone: {self.phone}, admin: {self.admin},cart: {self.cart}, orders: {self.orders}"


class Admin(GeneralUser):
    def __init__(self, username, shopname, name, lastname, description, address, email, phone, password) -> None:
        super().__init__(username, email, password)
        self.shopname = shopname
        self.name = name
        self.lastname = lastname
        self.description = description
        self.address = address
        self.products = []
        self.admin = True
        self.dateregistered = datetime.datetime.now()

    def add_review(self, product, review):
        self.reviews[product] = review

    def add_order(self, order):
        self.orders[order] = datetime.datetime.now()

    def toJSON(self):
        return {
            "username": self.username,
            "shopname": self.shopname,
            "name": self.name,
            "lastname": self.lastname,
            "description": self.description,
            "address": self.address,
            "email": self.email,
            "phone": self.phone,
            "admin": self.admin
        }
    
    def __str__(self) -> str:
        return f"username: {self.username}, shopname: {self.shopname}, name: {self.name}, lastname: {self.lastname}, description: {self.description}, address: {self.address}, email: {self.email}, phone: {self.phone}, admin: {self.admin}"


class LoggedInUser(persistent.Persistent):
    def __init__(self, user=None) -> None:
        self.user = user
        self.logged_in = False

    def toJSON(self):
        return {
            "user": self.user,
            "logged_in": self.logged_in
        }
    
    def __str__(self) -> str:
        return f"\nuser: {self.user}, \nlogged_in: {self.logged_in}"

class Category(persistent.Persistent):
    def __init__(self, product, category) -> None:
        self.category = category
        self.product = product

    def toJSON(self):
        return {
            "product": self.product,
            "category": self.category
        }
    
    def __str__(self) -> str:
        return f"product: {self.product}, category: {self.category}"
# class Order(persistent.Persistent):
#     last_order_id = 0
#     def __init__(self, products, total) -> None:
#         self.products = products
#         self.total = total
#         self.status = "Processing"
#         self.tracking_number = None
#         self.order_id = None
#         self.date = datetime.datetime.now()
    
#     @classmethod
#     def get_next_order_id(cls):
#         cls.last_order_id += 1  # Increment the last_order_id
#         return cls.last_order_id  # Return the new order_id

#     def ship_order(self):
#         self.status = "Shipped"

#     def toJSON(self):
#         return {
#             "products": self.products,
#             "total": self.total,
#             "status": self.status,
#             "date": self.date
#         }
    
#     def __str__(self) -> str:
#         return f"products: {self.products}, total: {self.total}, status: {self.status}, date: {self.date}"
    
