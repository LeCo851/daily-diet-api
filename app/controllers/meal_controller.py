from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.schemas.meal_schema import meal_schema, meals_schema
from app.services.meal_service import MealService
from flask_login import login_required, current_user

meal_bp = Blueprint('meal_bp', __name__, url_prefix='/meals')

@meal_bp.route('/', methods=['POST'])
@login_required
def create_meal():
    """
    Endpoint para criar uma nova refeição
    """
    json_data = request.get_json()
    
    if not json_data:
        return jsonify({'message': 'nenhum dado enviado'}), 400
    
    try:
        validated_data= meal_schema.load(json_data)
        
        new_meal = MealService.create_meal(validated_data,current_user.id)
        
        result = meal_schema.dump(new_meal)
        
        return jsonify(result), 201
    
    except ValidationError as err:
        return jsonify({"message": err.messages}),400
    
@meal_bp.route('/', methods=['GET'])
@login_required
def list_meals():
    """
    Endpoint para listar todas as refeições
    """
        
    meals = MealService.get_all_meals(current_user.id)
    
    result = meals_schema.dump(meals)
    
    return jsonify(result), 200

@meal_bp.route('/<int:meal_id>', methods=['GET'])
@login_required
def list_meals_by_id(meal_id):
    """
    Endpoint para listar refeiçao por id
    """
    meal = MealService.get_meal_by_id(meal_id,current_user.id)
    if not meal:
        return jsonify({"erro": "Refeição não encontrada"}), 404
    
    result = meal_schema.dump(meal)
    
    return jsonify(result), 200




@meal_bp.route('/<int:meal_id>', methods=['PUT'])
@login_required
def update_meal(meal_id):
    """
    Endpoint para atualizar todos os dados de uma refeição
    """
    
    json_data = request.get_json()
    
    try:
        validated_data= meal_schema.load(json_data)
        
        updated_meal = MealService.update_meal(meal_id, current_user.id, validated_data)
        
        if not updated_meal:
            return jsonify({"message": "Refeição não encontrada"}),404
        
        result = meal_schema.dump(updated_meal)
        
        return jsonify(result), 200
    
    except ValidationError as err:
        return jsonify({"erros_de_validacao": err.messages}),400
    
@meal_bp.route('/<int:meal_id>', methods=['DELETE'])
@login_required
def delete_meal(meal_id):
    """
    Endpoint para deletar uma refeição
    """
    
    success = MealService.delete_meal(meal_id, current_user.id)
    
    if not success:
        return jsonify({"erro": "Refeição não encontrada"}),404
    
    return '',204
        
    
    

        