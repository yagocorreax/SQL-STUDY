from infra.configs.base import Base
from sqlalchemy import column, String, Integer
from sqlalchemy.orm import relationship

class Filmes(Base):
    __tablename__ = "filmes"

    titulo = column(String, primary_key=True)
    genero = column(String, nullable = False)
    ano = column(Integer, nullable=False)
    atores = relationship("Atores", backref="atores", lazy="subquery")
    
    def __repr__(self):
        return f"Filme [titulo={self.titulo}, ano={self.ano}]"
