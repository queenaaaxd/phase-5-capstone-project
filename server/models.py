from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


# Models go here!
class User(db.Model, SerializerMixin) :
    __tablename__ = 'users'

    id = db.Column( db.Integer, primary_key = True)
    email = db.Column( db.String, nullable = False, unique = True )
    password = db.Column( db.String, nullable = False )
    admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add relationship
    cartitems = db.relationship('CartItem', back_populates='user', cascade='all, delete-orphan')
    transactions = db.relationship('Transaction', back_populates='user', cascade='all, delete-orphan')

    # relations Users - Products
    cart_products = association_proxy('cartitems', 'product', creator=lambda p: Product(product=p))
    transaction_products = association_proxy('transactions', 'product', creator=lambda t: Product(product=t))

    # Add serialization rules
    serialize_rules = ('-cartitems', '-transactions')

    def __repr__( self ):
        # print(f'<User email={self.email} id={self.id}>')
        return f"{{ User { self.id } }}"

    @validates( 'email' )
    def validate_email( self, key, email ):
        if type(email) is str and email and '@' in email and '.' in email:
            return email
        else:
            raise ValueError(f"{key} must be a valid email address.")

    # @validates( 'password' )
    # def validate_password(self, key, password):
    #     if len(password) > 6:
    #         return password
    #     else:
    #         raise ValueError(f"{key} must be more than 6 characters long.")

    # validation_errors = [] 

    # def get_validation_errors( self ):
    #     return list( set( self.validation_errors ))

    # @classmethod
    # def clear_validation_errors( cls ): 
    #     cls.validation_errors = []

    # #Password stuff for user model!
    # @hybrid_property
    # def password_hash( self ):
    #     return self._password_hash

    # @password_hash.setter
    # def password_hash( self, password):
    #     # ***password validation goes in here!!!***
    #     if type(password) is str and len(password) in range(8, 17):
    #         password_hash = bcrypt.generate_password_hash (password.encode( 'utf-8' ))
    #         self._password_hash = password_hash.decode( 'utf-8' )
    #     else:
    #         self.validation_errors.append( "Password validation error goes here!" )
    
    # def authenticate( self, password):
    #     return bcrypt.check_password_hash( self._password_hash, password.encode( 'utf-8' ))


class Transaction(db.Model, SerializerMixin):
    __tablename__ = 'transactions'

    id = db.Column( db.Integer, primary_key = True )

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    user_id = db.Column( db.Integer, db.ForeignKey('users.id') )
    product_id = db.Column( db.Integer, db.ForeignKey('products.id') )

    # Add relationships
    user = db.relationship('User', back_populates="transactions")
    product = db.relationship('Product', back_populates="transactions")

    # Add serialization rules
    serialize_rules = ('-user', '-product')

    def __repr__(self):
        return f'<Transaction user_id={self.user_id} product_id={self.product_id}>'


class CartItem(db.Model, SerializerMixin):
    __tablename__ = 'cartitems'

    id = db.Column( db.Integer, primary_key = True)
    created_at = db.Column( db.DateTime, server_default = db.func.now() )
    update_at = db.Column( db.DateTime, onupdate = db.func.now() )

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    # Add relationships
    user = db.relationship('User', back_populates="cartitems")
    product = db.relationship('Product', back_populates="cartitems")

    # Add serialization rules
    serialize_rules = ('-user', '-product')

    def __repr__( self ):
        return f'<CartItem user_id={self.user_id} product_id={self.product_id}>'
        # return f"{{ CartItem { self.id } }}"

class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'

    id = db.Column( db.Integer, primary_key = True)
    name  = db.Column ( db.String, nullable = False )
    price = db.Column ( db.Integer )
    description = db.Column ( db.String )
    units = db.Column ( db.Integer )
    units_sold = db.Column ( db.Integer )
    image= db.Column ( db.String )

    # Add relationships
    cartitems = db.relationship( 'CartItem', back_populates='product' )
    transactions = db.relationship( 'Transaction', back_populates='product' )

    serialize_rules = ( '-cartitems', '-transactions' )

    # created_at = db.Column( db.DateTime, server_default = db.func.now() )
    # update_at = db.Column( db.DateTime, onupdate = db.func.now() )

    def __repr__( self ):
        return f'<Product name= {self.name} price= {self.price} image= {self.image} units= {self.units}>'
        # return f"{{ Product { self.id } }}"

# Model templates!
# class NameOfClass (db.Model) :
#     __tablename__ = 'name of class plural'

#     id = db.Column( db.Integer, primary_key = True)
#     created_at = db.Column( db.DateTime, server_default = db.func.now() )
#     update_at = db.Column( db.DateTime, onupdate = db.func.now() )

#     table_column_id = db.Column( db.Integer, db.ForeignKey( 'table.id' ))

#     def __repr__( self ):
#         return f"{{ ModelName { self.id } }}"

#     validation_errors = []

#     def get_validation_errors( self ):
#         return list( set( self.validation_errors ))

#     @classmethod
#     def clear_validation_errors( cls ): 
#         cls.validation_errors = []

#     Password stuff for user model!
#     @hybrid_property
#     def password_hash( self ):
#         return self._password_hash

#     @password_hash.setter
#     def password_hash( self, password):
#         if ***password validation goes in here!!!***:
#             password_hash = bcrypt.generate_password_hash (password.encode( 'utf-8' ))
#             self._password_hash = password_hash.decode( 'utf-8' )
#         else:
#             self.validation_errors.append( "Password validation error goes here!" )
    
#     def authenticate( self, password):
#         return bcrypt.check_password_hash( self._password_hash, password.encode( 'utf-8' ))



# 07/26
# add at least two validations POST/UPDATE that effects
# - username 
# - name of username of first/last name

# full CRUD on Users
# Create post users/signup
# Get login/logout keeping user's logged in and log out
# Patch update user's info
# Delete user's account
# cookies

# built 5 routes 