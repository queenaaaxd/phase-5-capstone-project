#!/usr/bin/env python3

import ipdb

from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
# from flask_bcrypt import Bcrypt

from models import db, User, CartItem, Product, Transaction

app = Flask(__name__)

app.secret_key = "ABC123"; # signature for Flask session

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///beverages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# bcrypt = Bcrypt(app)

migrate = Migrate(app, db)

db.init_app(app)

CORS(app)

api = Api(app)

@app.route('/')
def index():
    return "Simply beverage's"

class Products(Resource):
    
    def get(self):
        products = Product.query.all()

        response_body = []

        for product in products:
            response_body.append(product.to_dict(only = ("id", "name", "description", "price", "image", "units")))
        
        return make_response(jsonify(response_body), 200)
    
    def post(self):
        json_data = request.get_json()
        new_product = Product(name=json_data.get('name'), description=json_data.get('description'), price=json_data.get('price'), image=json_data.get('image'), units=json_data.get('units'))
        db.session.add(new_product)
        db.session.commit()

        response_body = new_product.to_dict()

        return make_response(jsonify(response_body), 201)

api.add_resource(Products, "/products")

class ProductById(Resource):
    def get(self, id):
        product = Product.query.filter(Product.id == id).first()

        if not product:
            response_body = {
                "error": "product not found"
            }
            status = 404
        else:
            response_body = product.to_dict(only=('id','name','description', 'price', 'image', 'units'))
            status = 200
        
        return make_response(jsonify(response_body), status)
    
    def patch(self, id):
        product = Product.query.filter(Product.id == id).first()

        if not user:
            response_body = {
                "error": "product not found"
            }
            status = 404
        else:
            json_data = request.get_json()

            for key in json_data:
                setattr(product, key, json_data.get(key))

                db.session.commit()

                response_body = product.to_dict()
                status = 200
            
            return make_response(jsonify(response_body), status)
        
    def delete(self, id):
        product = Product.query.filter(Product.id == id).first()

        if not product:

            response_body = {
                "error": "product not found"
            }
            status = 404

        else:

            db.session.delete(product)
            db.session.commit()

            response_body = {}

            status = 204

        return make_response(jsonify(response_body), status)

api.add_resource(ProductById, '/products/<int:id>')


class Users(Resource):
    def get(self):
        users = User.query.all()

        response_body = []

        for user in users:
            response_body.append(user.to_dict(only = ('id', 'email', 'password', 'admin' )))

        return make_response(jsonify(response_body), 200)
        
    def post(self):
        json_data = request.get_json()
        new_user = User(email=json_data.get('email'), password=json_data.get('password'), admin=json_data.get('admin'))
        db.session.add(new_user)
        db.session.commit()

        response_body = new_user.to_dict()

        return make_response(jsonify(response_body), 201)

api.add_resource(Users, '/users')

class UsersById(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()

        if not user:
            response_body = {
                "error": "user not found"
            }
            status = 404
        else:
            response_body = user.to_dict(only=('id','email','admin'))
            status = 200
        
        return make_response(jsonify(response_body), status)
    
    def patch(self, id):
        user = User.query.filter(User.id == id).first()

        if not user:
            response_body = {
                "error": "user not found"
            }
            status = 404
        else:
            json_data = request.get_json()

            for key in json_data:
                setattr(user, key, json_data.get(key))

                db.session.commit()

                response_body = user.to_dict()
                status = 200
            
            return make_response(jsonify(response_body), status)
        
    def delete(self, id):
        user = User.query.filter(User.id == id).first()

        if not user:

            response_body = {
                "error": "user not found"
            }
            status = 404

        else:

            db.session.delete(user)
            db.session.commit()

            response_body = {}

            status = 204

        return make_response(jsonify(response_body), status)

api.add_resource(UsersById, '/users/<int:id>')


class CartItems(Resource):

    def get(self):
        cartitems = CartItem.query.all()

        response_body = []

        for cartitem in cartitems:
            response_body.append(cartitem.to_dict())
        
        return make_response(jsonify(response_body), 200)

    def post(self):
        
        new_cartitem = CartItem(
            product_id = request.json['product_id'],
        )
        db.session.add(new_cartitem)
        db.session.commit()

        cart_item_dict = new_cartitem.to_dict()
        
        response = make_response(
            cart_item_dict,
            201
        )
        return response
        
api.add_resource(CartItems, '/cartitems')

class Cart_ItemsByID(Resource):
    def get(self, id):
        cartitem = CartItem.query.filter(CartItem.id == id).first()

        if not user:
            response_body = {
                "error": "cart item not found"
            }
            status = 404
        else:
            response_body = cartitem.to_dict(only=('product_id'))
            status = 200
        
        return make_response(jsonify(response_body), status)
        return {"error": "Cart item not found"}, 404

    def delete(self, id):

        cartitem = Cart_Item.query.filter_by(id = id).first()

        if cartitem:
            db.session.delete(cartitem)
            db.session.commit()

            response = make_response(
                "",
                204
            )

            return response
        
        return {"error": "Cart item not found"}, 404

api.add_resource(Cart_ItemsByID, '/cartitems/<int:id>')


class Login(Resource):
    def post(self):
        json_data = request.get_json()
        # ipdb.set_trace()

        user = User.query.filter( User.email == json_data.get( "email" ) ).first()
        if user: 
            response_body = user.to_dict(only=('id','email','admin'))
            status = 200

        else: 
            response_body = {
                "error" : "login invalid email"
            }

            status = 401
        
        return make_response(jsonify(response_body), status)

api.add_resource(Login, '/login')


# class CartItems(Resource):
    # def get(self):
    #     cart_items_dict = [cart_items.to_dict() for cart_items in Cart_Item.query.all()]

    #     response = make_response(
    #         cart_items_dict,
    #         200
    #     )

    #     return response

    # def post(self):
        
    #     new_cart_item = Cart_Item(
    #         product_id = request.json['product_id'],
    #         shopping_session_id = request.json['shopping_session_id']
    #     )

    #     db.session.add(new_cart_item)
    #     db.session.commit()

    #     cart_item_dict = new_cart_item.to_dict()
        
    #     response = make_response(
    #         cart_item_dict,
    #         201
    #     )
    #     return response
        
# api.add_resource(Cart_Items, '/cart_items')
    # pass

class Transactions(Resource):
    pass

# make


if __name__ == '__main__':
    app.run(port=5555, debug=True)