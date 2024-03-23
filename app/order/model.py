from app import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    status = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())
    is_deleted = db.Column(db.Boolean, default=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, product_id=None, user_id=None, quantity=None, status=None):
        self.product_id = product_id or self.product_id
        self.user_id = user_id or self.user_id
        self.quantity = quantity or self.quantity
        self.status = status or self.status
        self.updated_at = db.func.now()
        db.session.commit()
    
    def delete(self):
        self.is_deleted = True
        self.updated_at = db.func.now()
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id, is_deleted=False).first()
    
    @classmethod
    def get_all(cls):
        return cls.query.filter_by(is_deleted=False).all()
    
    @classmethod
    def create(cls, product_id, user_id, quantity, status):
        order = cls(product_id=product_id, user_id=user_id, quantity=quantity, status=status)
        order.save()
        return order