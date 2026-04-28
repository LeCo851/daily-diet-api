from app.database import db
from app.models.meal_model import Meal

class MealService:
    """
    Camada de serviço para a entidade meal.
    Isola a regra de negócio e as operações de banco de dados do Controller
    """
    
    @staticmethod
    def create_meal(data,user_id):
        """
        Cria uma nova refeição no banco de dados
        :param data: Dicionário contendo os dados validados pelo Schema
        """
        
        new_meal = Meal(
            name = data['name'],
            description=data['description'],
            is_on_diet=data['is_on_diet'],
            date_time=data.get('date_time'),
            user_id=user_id
        )
        
        db.session.add(new_meal)
        db.session.commit()
        
        return new_meal
    
    @staticmethod
    def get_all_meals(user_id):
        """
        Retorna todas as refeições do banco de dados
        """
        
        return Meal.query.filter_by(user_id = user_id).all()
    

    @staticmethod
    def get_meal_by_id(meal_id,user_id):
        """
        Busca refeiçao por ID
        """
        
        return Meal.query.filter_by(id=meal_id, user_id=user_id).first()
    
    @staticmethod
    def update_meal(meal_id, user_id,data):
        """
        Atualiza uma refeição no banco de dados
        :param meal_id: ID da refeição a ser atualizada
        """
        
        meal = Meal.query.filter_by(id=meal_id, user_id=user_id).first()
        
        if not meal:
            return None
        
        meal.name = data.get('name', meal.name)
        meal.description = data.get('description', meal.description)
        meal.is_on_diet = data.get('is_on_diet', meal.is_on_diet)

        if 'date_time' in data:
            meal.date_time = data['date_time']
        
        db.session.commit()
        
        return meal

    @staticmethod
    def delete_meal(meal_id, user_id):
        """
        Deleta uma refeição do banco de dados
        :param meal_id: ID da refeição a ser deletada
        """
        
        meal = Meal.query.filter_by(id=meal_id, user_id=user_id).first()
        
        if not meal:
            return False
        
        db.session.delete(meal)
        db.session.commit()
        
        return True
    

        