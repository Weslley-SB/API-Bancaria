#configuração do banco de dados
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base #tem o sessionmaker aqui ainda hein!!
db = create_engine("sqlite:///models/test.db")
Base = declarative_base()

