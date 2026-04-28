from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    """
    Schema para usuário.
    """
    
    id = fields.Int(dump_only=True)
    
    username= fields.Str(
        required=True,
        validate=validate.Length(min=3, max=80),
        error_messages={"required": "O nome de usuário é obrigatório"}
    )
    
    email = fields.Email(
        required= True,
        error_messages = {
            "required": "O e-mail é obrigatório.",
            "invalid": "E-mail inválido."
        }
    )
    
    password = fields.Str(
        required=True,
        load_only=True,
        validate=validate.Length(min=6),
        error_messages={"required": "A senha é obrigatória"}
    )
    
user_schema = UserSchema()
users_schema = UserSchema(many=True)