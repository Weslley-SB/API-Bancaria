from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base
class Conta(Base):
    __tablename__ = "contas"

    id = Column(Integer, primary_key=True, index=True)
    numero_conta = Column(String, unique=True, nullable=False, index=True )
    id_usuarios = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    saldo = Column(Float, default=0.0)