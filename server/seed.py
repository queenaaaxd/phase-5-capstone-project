#!/usr/bin/env python3
from random import randint
from app import app
from models import db, User, CartItem, Product, Transaction

with app.app_context():
    # clear all the tables!
    User.query.delete()
    Product.query.delete()
    Transaction.query.delete()
    CartItem.query.delete()
    print( 'Database wiped!')

    products = []
    products.append(Product(name='Essential Water 1 Liter - 12 Pack', price=25.00, description='Essentia Bottled Water, 1 Liter, 12-Pack, Ionized Alkaline Water:99.9% Pure, Infused With Electrolytes, 9.5 pH Or Higher With A Clean, Smooth Taste', units=100 , units_sold=25 , image='https://m.media-amazon.com/images/I/81QJejt5LrL._SL1500_.jpg'))
    products.append(Product(name='Essenital Water 20 Fl Oz - 24 Pack', price=35.00, description= 'Essentia Bottled Water, Ionized Alkaline Water; 99.9% Pure, Infused with Electrolytes, 9.5 pH or Higher with a Clean, Smooth Taste, 20 Fl Oz (Pack of 24)', units=100 , units_sold=15 , image='https://m.media-amazon.com/images/I/51T7dB9ujsS._SL1000_.jpg'))
    products.append(Product(name='Moutain Valley Spring Water 500 Ml - 12 Pack', price=22.00, description='500 Ml Spring Water in glass, 12-Pack.', units=100 , units_sold=10 , image='https://m.media-amazon.com/images/I/91IaV-i1m+L._SL1500_.jpg'))
    products.append(Product(name='Moutain Valley Sparkling Water 500 Ml - 12 Pack', price=22.00, description='500 Ml Sparkling Water in glass, 12-Pack.', units=100 , units_sold=25 , image='https://www.mountainvalleyspring.com/cdn/shop/products/Mountain_Valley_Sparkling_500_9ae86251-e37e-428b-bb1c-cd7d6002ed7a.jpg?v=1600706397'))
    products.append(Product(name='Celsius Sparkling Orange 12 Fl Oz - 12 Pack', price=21.00, description='CELSIUS provides essential energy and is clinically proven to accelerate metabolism and burn body fat when exercising.', units=1000 , units_sold=15 , image='https://m.media-amazon.com/images/I/81HsOzIZFCL._SL1500_.jpg'))
    products.append(Product(name='Celsius Sparklng Kiwi 12 Fl Oz - 12 Pack', price=21.00, description='CELSIUS provides essential energy and is clinically proven to accelerate metabolism and burn body fat when exercising', units=1000 , units_sold=20 , image='https://m.media-amazon.com/images/I/819ORCT10YL._SL1500_.jpg'))
    products.append(Product(name='Monster Energy + Juice - 24 Pack', price=57.00, description='A light, subtle flavor with hints of peach and nectarine, and a full load of our Monster Energy blend', units=1000 , units_sold=20 , image='https://m.media-amazon.com/images/I/91TPOR++DXL._SL1500_.jpg'))
    products.append(Product(name='Monster Energy Zero Ultra - 24 Pack', price=55.00, description='16 Fl Oz (Pack of 24) Light Refreshing Citrus, 10 calories, and zero sugar.', units=1000 , units_sold=50, image='https://m.media-amazon.com/images/I/913KMH1cDKL._SL1500_.jpg'))
    db.session.add_all(products)
    
    users = []
    users.append(User( email='admin1@gmail.com', password_hash='password', admin=True ))
    users.append(User( email='testing2@gmail.com', password_hash='password', admin=False ))
    users.append(User( email='testing3@gmail.com', password_hash='password', admin=False ))
    users.append(User( email='testing4@gmail.com', password_hash='password', admin=False ))
    users.append(User( email='testing5@gmail.com', password_hash='password', admin=False ))
    users.append(User( email='testing6@gmail.com', password_hash='password', admin=False ))
    users.append(User( email='testing7@gmail.com', password_hash='password', admin=False ))
    users.append(User( email='testing8@gmail.com', password_hash='password', admin=False ))
    users.append(User( email='testing9@gmail.com', password_hash='password', admin=False ))
    users.append(User( email='testing10@gmail.com', password_hash='password', admin=False ))
    db.session.add_all(users)


    transactions = []
    transactions.append(Transaction( user_id=randint(1,10), product_id=randint(1,8)) )
    transactions.append(Transaction( user_id=randint(1,10), product_id=randint(1,8)) )
    transactions.append(Transaction( user_id=randint(1,10), product_id=randint(1,8)) )
    transactions.append(Transaction( user_id=randint(1,10), product_id=randint(1,8)) )


    db.session.add_all(transactions)

    cartitems = []
    cartitems.append(CartItem(user_id=randint(1,10), product_id=randint(1,8)))
    cartitems.append(CartItem(user_id=randint(1,10), product_id=randint(1,8)))
    cartitems.append(CartItem(user_id=randint(1,10), product_id=randint(1,8)))
    cartitems.append(CartItem(user_id=randint(1,10), product_id=randint(1,8)))
    db.session.add_all(cartitems)

    db.session.commit()
    print( 'Information seeded!' )




