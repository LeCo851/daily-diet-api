from flask import Flask
from app.database import db,login_manager,bcrypt
from dotenv import load_dotenv
import os
from app.controllers.meal_controller import meal_bp
from app.controllers.auth_controller import auth_bp
from app.services.user_service import UserService

load_dotenv()


def create_app():
    """App factory: Cria e configura a instancia do flask
    """
    app= Flask(__name__)
    
    secret_key = os.getenv('SECRET_KEY')
    if not secret_key:
        raise ValueError("A variável de ambiente SECRET_KEY não está configurada.")
    app.config['SECRET_KEY'] = secret_key
    
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        raise ValueError("Variável de ambiente não configurada")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(auth_bp)
    app.register_blueprint(meal_bp)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return UserService.get_user_by_id(int(user_id))
    
    db.init_app(app)
    with app.app_context():
        db.create_all() # cria as tabelas no banco para n precisar usar flask shell
        
    
    return app