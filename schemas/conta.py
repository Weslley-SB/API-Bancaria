from pydantic import BaseModel

class ContaBase(BaseModel):
    id_usuarios: int

class ContaCreate(ContaBase):
    pass

class ContaResponse(ContaBase):
    id: int
    numero_conta = str
    saldo: float

    class config:
        from_attributes = True