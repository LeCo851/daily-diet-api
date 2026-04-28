from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from flask_login import login_user, logout_user, login_required
from app.schemas.user_schema import user_schema
from app.services.user_service import UserService
from flasgger import swag_from

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
@swag_from('../docs/auth_register.yml')
def register():
    """
    Endpoin para criar nova conta de usuário
    """
    
    json_data = request.get_json()
    if not json_data:
        return jsonify({'erro': "Nenhum dado enviado"}), 400
    
    try:
        validated_data = user_schema.load(json_data)
        
        new_user = UserService.create_user(validated_data)
        
        result = user_schema.dump(new_user)
        
        return jsonify(result), 201
    
    except ValidationError as err:
        return jsonify({'erro_validacao': err.messages}),400
    except ValueError as err: 
        #captura erro de validacao do service
        return jsonify({"erro": str(err)}),400
    
@auth_bp.route('/login', methods=['POST'])
@swag_from('../docs/auth_login.yml')
def login():
        """
        Endpoint para autenticar o usuário e inicar a sessao
        """
        json_data = request.get_json()
        if not json_data or 'email' not in json_data or 'password' not in json_data:
            return jsonify({"erro": "Email e senha sao obrigatorios"}), 400
        
        user = UserService.authenticate_user(json_data['email'], json_data['password'])
        
        if user:
            login_user(user)
            return jsonify({"message": "Login realizado com sucesso", "username": user.username}), 200
    
        else:
            return jsonify({"error": "Credenciais invalidas"}), 401
        
@auth_bp.route('/logout', methods=['POST'])
@login_required
@swag_from('../docs/auth_logout.yml')
def logout():
    """
    Endpoint para encerrar a sessao do usuario
    """
    
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso"}), 200