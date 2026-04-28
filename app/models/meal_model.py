from app.database import db
from datetime import datetime

class Meal(db.Model):
    """
    Entidade Meal
    Mapeia a tabela 'meals' no banco de dados PostgreSQL com SQLAlchemy
    """
    
    __tablename__ = 'meals' # define o nome da tabela para o SQLAlchemy
    
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(100), nullable=False)
    
    description = db.Column(db.Text, nullable=False)
    
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    is_on_diet = db.Column(db.Boolean, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    
    def __init__(self, name, description, date_time, is_on_diet, user_id):
        self.name = name
        self.description = description
        self.is_on_diet = is_on_diet
        self.user_id = user_id
        if date_time:
            self.date_time = date_time
    
        
