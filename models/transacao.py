import enum
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum
from database import Base
import datetime

class StatusTransacao(enum.Enum): #Opçoes do status das transações
    pendente = "pendente"
    completa = "completa"
    falha = "falha"

class Transacoes(Base):
    __tablename__ = "transacoes"

    id = Column()
    id_remetente = Column(Integer, ForeignKey("contas.id"), nullable=False, index=True)
    id_destinatario = Column(Integer, ForeignKey("contas.id"), nullable=False, index=True)
    valor = Column(Float, nullable=False)
    data_hora = Column(String, default=lambda: datetime.datetime.now().isoformat())
    status = Column(Enum(StatusTransacao), default=StatusTransacao.pendente, nullable=False)