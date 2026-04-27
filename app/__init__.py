from flask import Flask
from app.database import db
from dotenv import load_dotenv
import os

load_dotenv()


def create_app():
    """App factory: Cria e configura a instancia do flask
    """
    app= Flask(__name__)
    
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        raise ValueError("Variável de ambiente não configurada")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all() # cria as tabelas no banco para n precisar usar flask shell
    
    return app