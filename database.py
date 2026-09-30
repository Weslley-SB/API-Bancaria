#configuração do banco de dados
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db = create_engine("sqlite:///models/test.db")
Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db)