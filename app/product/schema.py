from app import ma
from app.product.model import *

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        exclude = ('is_deleted',)