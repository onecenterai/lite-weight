from app import db

TASK_CODE_MAPPING = {0:'No Task', 1:'Delivery Task', 2:'Pickup Task', 3:'Return Task'}

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone_number = db.Column(db.Integer)
    is_available = db.Column(db.Boolean, default=True)
    current_task_code = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())
    is_deleted = db.Column(db.Boolean, default=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, name=None, phone_number=None, is_available=None):
        self.name = name or self.name
        self.phone_number = phone_number or self.phone_number
        self.is_available = is_available or self.is_available
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
    def create(cls, name, phone_number, is_available):
        agent = cls(name=name, phone_number=phone_number, is_available=is_available)
        agent.save()
        return agent
    
    @classmethod
    def get_available_agent(cls):
        return cls.query.filter_by(is_deleted=False, is_available=True).first()