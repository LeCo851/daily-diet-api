from app.database import db
from app.models.user_model import User

class UserService:
    """
    Camada de serviço para a entidade user
    """
    
    @staticmethod
    def create_user(data):
        """
        Registra um novo usuário no sistema
        """
        
        if User.query.filter_by(email=data['email']).first():
            raise ValueError("Este e-mail já está cadastrado.")
        
        if User.query.filter_by(username=data['username']).first():
            raise ValueError("Este nome de usuário já está cadastrado.")
        
        
        new_user = User(
            username = data['username'],
            email=data['email']
            
        )
        
        new_user.set_password(data['password'])
        
        db.session.add(new_user)
        db.session.commit()
        
        return new_user
        
    @staticmethod
    def authenticate_user(email, password):
        """
        Verifica se as credenciais sao validas
        """
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            return user
        
        return None
    
    @staticmethod
    def get_user_by_id(user_id):
        """
        método auxiliar para o flask-login carregar o usuário da sessão ativa.
        """
        
        return User.query.get(user_id)