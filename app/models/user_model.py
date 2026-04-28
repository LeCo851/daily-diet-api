from app.database import db,bcrypt
from flask_login import UserMixin

class User(db.Model, UserMixin):
    """
    Entidade User
    Herda de db.Model para mapeamento de banco e UserMixin para compatiblidade com flask-login.
    """
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    password_hash = db.Column(db.String(128), nullable= False)
    
    meals = db.relationship('Meal', backref='user', lazy=True)
    
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        
    
    
    def set_password(self, password):
        """
        Aplica o hash bcrypt na senha recebida e salva na entidade.
        """
        
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        
        
    def check_password(self, password):
        """
        Verifica se a senha em texto plano fornecida no login bate com o hash armazenado
        """
        return bcrypt.check_password_hash(self.password_hash, password)