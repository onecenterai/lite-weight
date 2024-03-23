from app import ma
from app.order.model import *

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        exclude = ('is_deleted',)