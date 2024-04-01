import persistent
import datetime
import BTrees.OOBTree

from .database import *

class Product(persistent.Persistent):
    def __init__(self, id, name, description, price, sizes, options, stock, categories) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.sizes = sizes
        self.options = options
        self.stock = stock
        self.categories = categories
        self.sold = 0
        self.reviews = []
        self.publishedDate = datetime.datetime.now()

    def add_review(self, review):
        self.reviews[datetime.datetime.now()] = review

    def toJSON(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "category": self.category,
            "stock": self.stock,
            "sold": self.sold,
            "reviews": self.reviews,
            "publishedDate": self.publishedDate
        }
    
    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}, price: {self.price}, description: {self.description}, categories: {self.categories}, stock: {self.stock}, sold: {self.sold}, reviews: {self.reviews}\n"

class ProductDatabase(persistent.Persistent):
    def __init__(self):
        self.products = {}
        self.next_id = 1

    def add_product(self, name, description, price, sizes, options, stock, categories):
        product_id = self.next_id
        product = Product(product_id, name, description, price, sizes, options, stock, categories)
        self.products[product_id] = product
        self.next_id += 1
        return product_id

    def get_product(self, product_id):
        return self.products.get(product_id, None)

    def update_product(self, product_id, **kwargs):
        product = self.products.get(product_id)
        if product:
            for key, value in kwargs.items():
                if hasattr(product, key):
                    setattr(product, key, value)
            return True
        return False

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            return True
        else:
            return False
    
    def toJSON(self):
        return {
            "products": self.products,
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
        return f"username: {self.username}, email: {self.email}, name: {self.name}, lastname: {self.lastname}, address: {self.address}, birthday: {self.birthday}, phone: {self.phone}, admin: {self.admin}"

class Admin(GeneralUser):
    def __init__(self, username, shopname, name, lastname, description, address, email, phone, password) -> None:
        super().__init__(username, email, password)
        self.shopname = shopname
        self.name = name
        self.lastname = lastname
        self.description = description
        self.address = address
        self.phone = phone
        self.products = {}
        self.admin = True

    def add_product(self, product):
        self.products[product.id] = product

    def remove_product(self, product):
        if product in self.products:
            del self.products[product.id]

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
        return super().__str__()
    
class Customer(GeneralUser):
    def __init__(self, username, email, password) -> None:
        super().__init__(username, email, password)
        self.favorites = []
        self.cart = []
        self.orders = []
        self.reviews = None
        self.admin = False

    def add_to_cart(self, product, quantity):
        if product in self.cart:
            self.cart[product] += quantity
        else:
            self.cart[product] = quantity

    def remove_from_cart(self, product, quantity):
        if product in self.cart:
            if self.cart[product] > quantity:
                self.cart[product] -= quantity
            else:
                del self.cart[product]

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
        return f"user: {self.user}, logged_in: {self.logged_in}"

class Order(persistent.Persistent):
    def __init__(self, products, total) -> None:
        self.products = products
        self.total = total
        self.status = "Processing"
        self.date = datetime.datetime.now()

    def cancel_order(self):
        self.status = "Cancelled"

    def ship_order(self):
        self.status = "Shipped"

    def complete_order(self):
        self.status = "Completed"

    def toJSON(self):
        return {
            "products": self.products,
            "total": self.total,
            "status": self.status,
            "date": self.date
        }
    
    def __str__(self) -> str:
        return f"products: {self.products}, total: {self.total}, status: {self.status}, date: {self.date}"
    
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
    