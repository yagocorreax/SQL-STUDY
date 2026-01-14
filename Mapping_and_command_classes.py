from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import column, String, Integer
from sqlalchemy.orm import sessionmaker

#configurações
engine = create_engine("mysql+pymysql://root:1234@localhost:3306/cinema")
Base = declarative_base()
Session= sessionmaker(bind=engine)
session = Session()

#Entidades
class filmes(Base):
    __tablename__='filmes'

    titulo = column(String, primary_key=True)
    genero = column(String, nullable = False)
    ano = column(Integer, nullable=False)

#função para formatação de print
    def __repr__(self):
        return f"Filme [titulo={self.titulo}, ano={self.ano}]"
    
    #insert
    data_isert = Filmes (titulo="jfasasufy", genero="Acao", ano=1111)
    session.add(data_isert)
    session.commit()

    #delete
    session.query(filmes).filter(filmes.titulo=="dracula").delete()
    session.commit()

    #update
    session.query(filmes).filter(filmes.genero=="drama").update({"ano": 2000})
    session.commit()

    #select
    data = session.query(filmes).all()
    print(data)
    print(data[0].titulo)

    session.close()



