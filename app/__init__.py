from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager

# App Config
app = Flask(__name__, )
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)
JWTManager(app)

# Celery
from app.celery import make_celery
celery = make_celery(app)

# Database
from config import secret
app.secret_key = secret
migrate = Migrate(app, db)


# Controllers
from app.user.controller import bp as user_bp
app.register_blueprint(user_bp)
from app.product.controller import bp as product_bp
app.register_blueprint(product_bp)
from app.order.controller import bp as order_bp
app.register_blueprint(order_bp)
from app.agent.controller import bp as agent_bp
app.register_blueprint(agent_bp)

# Error handlers
from .error_handlers import *