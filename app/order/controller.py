from flask import Blueprint, request
from app.route_guard import auth_required

from app.order.model import *
from app.order.schema import *
from app.agent.model import *

bp = Blueprint('order', __name__)

ORDER_STATUS = ['RECEIVED', 'ENROUTE', 'DELIVERED', 'RETURNED']

@bp.post('/order')
@auth_required()
def create_order():
    product_id = request.json.get('product_id')
    user_id = request.json.get('user_id')
    quantity = request.json.get('quantity')
    status = request.json.get('status')
    order = Order.create(product_id, user_id, quantity, status)
    return OrderSchema().dump(order), 201

@bp.get('/order/<int:id>')
@auth_required()
def get_order(id):
    order = Order.get_by_id(id)
    if order is None:
        return {'message': 'Order not found'}, 404
    return OrderSchema().dump(order), 200

@bp.put('/order/<int:id>/update_status')
@auth_required()
def update_order(id):
    order = Order.get_by_id(id)
    if order is None:
        return {'message': 'Order not found'}, 404
    status = request.json.get('status')
    if status not in ORDER_STATUS:
        return {'message': 'Invalid Order Status'}
    order.update(status)
    return OrderSchema().dump(order), 200

@bp.delete('/order/<int:id>')
@auth_required()
def delete_order(id):
    order = Order.get_by_id(id)
    if order is None:
        return {'message': 'Order not found'}, 404
    order.delete()
    return {'message': 'Order deleted successfully'}, 200

@bp.get('/orders')
@auth_required()
def get_orders():
    orders = Order.get_all()
    return OrderSchema(many=True).dump(orders), 200

@bp.get('/order_status')
@auth_required()
def get_order_status(id):
    order = Order.get_by_id(id)
    if order is None:
        return {'message': 'Order not found'}, 404
    return {'message': order.status}

@bp.post('/return_order')
@auth_required()
def return_order(id):
    order = Order.get_by_id(id)
    if order is None:
        return {'message': 'Order not found'}, 404
    if order.status != 'DELIVERED':
        return {'message': 'Order not delivered yet'}, 400
    
    available_agent = Agent.get_available_agent()
    available_agent.is_available = False
    available_agent.current_task_code = 3
    available_agent.save()

    return {'message': 'Product will be picked up by an Agent soon', 
            'Agent Details': {'name': available_agent.name, 'phone_number': available_agent.phone_number}}
    
