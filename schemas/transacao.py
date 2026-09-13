from models.transacao import StatusTransacao
from pydantic import BaseModel

class TransacaoBase(BaseModel):
    id_remetente: int
    id_destinatario: int
    valor: float

class TransacaoCreate(TransacaoBase):
    pass

class TransacaoResponse(TransacaoBase):
    id: int
    data_hora: str
    status: StatusTransacao

    class Config:
        from_attributes = True