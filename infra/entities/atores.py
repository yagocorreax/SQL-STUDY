from infra.configs.base import Base
from sqlalchemy import column, String, Integer, ForeignKey

class Atores(Base):
    __tablename__ = 'atores'

    id = column(Integer, primary_key = True)
    nome = column(String, nullable= False)
    titulo_filme = column(String, nullable= False)

    def __repr__(self):
         return f"Atores [nome={self.nome}, filme={self.titulo_filme}]"
    
