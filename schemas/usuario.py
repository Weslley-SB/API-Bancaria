from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel): #valida se o usuario criado tem nome, email e senha
    nome: str
    email: EmailStr

class UsuarioCreate(UsuarioBase): #Apos validar e der certo, aqui o preenchimento ao sqlalchemy é feito
    senha: str

class UsuarioResponse(UsuarioBase): #Aqui é enviado o JSON sem a senha para o usuario
    id: int

class Config:
    from_attributes = True