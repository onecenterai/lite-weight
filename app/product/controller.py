from flask import Blueprint, request
from app.route_guard import auth_required

from app.product.model import *
from app.product.schema import *

bp = Blueprint('product', __name__)

@bp.post('/product')
#@auth_required()
def create_product():
    name = request.json.get('name')
    price = request.json.get('price')
    category = request.json.get('category')
    product = Product.create(name, price, category)
    return ProductSchema().dump(product), 201

@bp.get('/product/<int:id>')
@auth_required()
def get_product(id):
    product = Product.get_by_id(id)
    if product is None:
        return {'message': 'Product not found'}, 404
    return ProductSchema().dump(product), 200

@bp.put('/product/<int:id>')
@auth_required()
def update_product(id):
    product = Product.get_by_id(id)
    if product is None:
        return {'message': 'Product not found'}, 404
    name = request.json.get('name')
    price = request.json.get('price')
    category = request.json.get('category')
    product.update(name, price, category)
    return ProductSchema().dump(product), 200

@bp.delete('/product/<int:id>')
@auth_required()
def delete_product(id):
    product = Product.get_by_id(id)
    if product is None:
        return {'message': 'Product not found'}, 404
    product.delete()
    return {'message': 'Product deleted successfully'}, 200

@bp.get('/products')
@auth_required()
def get_products():
    products = Product.get_all()
    return ProductSchema(many=True).dump(products), 200