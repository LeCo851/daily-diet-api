from marshmallow import Schema, fields, validate

class MealSchema(Schema):
    """
    Schema de validação e serialização de dados para a entidade Meal
    Tranforma JSON em objetos Python válidos e vice-versa
    """
    
    id = fields.Int(dump_only=True)
    
    name = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=100),
        error_messages={"required": "O nome da refeição é obrigatório."}
    )
    
    description = fields.Str(
        required=True,
        validate=validate.Length(min=5, max=200),
        error_messages={"required": "A descrição da refeição é obrigatória."}
    )
    
    date_time = fields.DateTime(format='%Y-%m-%d %H:%M:%S', load_default=None)
    
    is_on_diet = fields.Bool(
        required=True,
        error_messages={
            "required": "É necessário informar se a refeição está dentro da dieta (true ou false).",
            "invalid": "O valor deve ser um booleano (true ou false)."}
    )
    
meal_schema = MealSchema()
meals_schema = MealSchema(many=True)
    
