from infra.configs.connection import DBconnection_handler
from infra.entities.atores import Atores
from infra.entities.filmes import Filmes

class AtoresRepository:
    def select(self):
        with DBconnection_handler() as db:
            data = db.session\
            .query(Atores)\
            .join(Filmes, Atores.titulo_filme == Filmes.titulo)\
            .with_entities(
                Atores.nome,
                Filmes.genero,
                Filmes.titulo
            )\
            .all()
            return data