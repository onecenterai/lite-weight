from flask import Blueprint, request
from app.route_guard import auth_required

from app.agent.model import *
from app.agent.schema import *

bp = Blueprint('agent', __name__)

@bp.post('/agent')
@auth_required()
def create_agent():
    name = request.json.get('name')
    phone_number = request.json.get('phone_number')
    is_available = request.json.get('is_available')
    agent = Agent.create(name, phone_number, is_available)
    return AgentSchema().dump(agent), 201

@bp.get('/agent/<int:id>')
@auth_required()
def get_agent(id):
    agent = Agent.get_by_id(id)
    if agent is None:
        return {'message': 'Agent not found'}, 404
    return AgentSchema().dump(agent), 200

@bp.put('/agent/<int:id>')
@auth_required()
def update_agent(id):
    agent = Agent.get_by_id(id)
    if agent is None:
        return {'message': 'Agent not found'}, 404
    name = request.json.get('name')
    phone_number = request.json.get('phone_number')
    is_available = request.json.get('is_available')
    agent.update(name, phone_number, is_available)
    return AgentSchema().dump(agent), 200

@bp.delete('/agent/<int:id>')
@auth_required()
def delete_agent(id):
    agent = Agent.get_by_id(id)
    if agent is None:
        return {'message': 'Agent not found'}, 404
    agent.delete()
    return {'message': 'Agent deleted successfully'}, 200

@bp.get('/agents')
@auth_required()
def get_agents():
    agents = Agent.get_all()
    return AgentSchema(many=True).dump(agents), 200
