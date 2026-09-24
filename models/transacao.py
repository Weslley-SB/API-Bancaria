import enum
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime
from database import Base
import datetime
class StatusTransacao(enum.Enum): #Opçoes do status das transações
    pendente = "pendente"
    completa = "completa"
    falha = "falha"

class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True, index=True)
    id_remetente = Column(Integer, ForeignKey("contas.id"), nullable=False, index=True)
    id_destinatario = Column(Integer, ForeignKey("contas.id"), nullable=False, index=True)
    valor = Column(Float, nullable=False)
    data_hora = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    status = Column(Enum(StatusTransacao), default=StatusTransacao.pendente, nullable=False)