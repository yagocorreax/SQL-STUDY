from infra.configs.connection import DBconnection_handler
from infra.entities.filmes import Filmes
from sqlalchemy.orm.exc import NoResultFound

class FilmesRepository:
    def select(self):
        with DBconnection_handler() as db:
            try:
                data = db.session.query(Filmes).all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def select_drama_filmes(self):
        with DBconnection_handler() as db:
            try:
                data = db.session.query(Filmes).filter(Filmes.genero=="Terror").one()
                return data
            except NoResultFound:
                return None
            except Exception as Exception:
                db.session.rollback()
                raise Exception
            
    def insert(self, titulo, genero, ano):
        with DBconnection_handler() as db:
            try:
                data_sert = Filmes(titulo=titulo, genero=genero, ano=ano)
                db.session.add(data_sert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def delete(self, titulo):
        with DBconnection_handler() as db:
            try:
                db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def update(self, titulo, ano):
        with DBconnection_handler() as db:
            try:
                db.session.query(Filmes).filter(Filmes.titulo == titulo).update({"ano": ano})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception