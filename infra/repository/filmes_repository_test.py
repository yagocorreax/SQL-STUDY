from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from unittest.mock import MagicMock
from infra.entities.filmes import Filmes
from infra.repository.filmes_repository import FilmesRepository

# Criação do banco de dados virtual (Stub)
session = UnifiedAlchemyMagicMock(data=[
    (
        [MagicMock(side_effect=lambda *args, **kwargs: Filmes(titulo="Alice", genero="Drama", ano=12))], # Condição
        [Filmes(titulo="Alice", genero="Drama", ano=12)] # Dado de retorno
    ),
    (
        [MagicMock(side_effect=lambda *args, **kwargs: Filmes(titulo="Rafael", genero="Drama", ano=12))],
        [Filmes(titulo="Rafael", genero="Drama", ano=12)]
    )
])

# Classe fictícia para simular o Connection Handler
class DBConnectionHandlerMock:
    def __init__(self):
        self.session = session
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def test_select():
    # Injeção do Mock no repositório
    filme_repository = FilmesRepository(DBConnectionHandlerMock)
    response = filme_repository.select()
    
    print(response)
    assert isinstance(response, list)
    assert isinstance(response[0], Filmes)

def test_select_drama_filmes():
    filme_repository = FilmesRepository(DBConnectionHandlerMock)
    response = filme_repository.select_drama_filmes()
    
    print(response)
    assert response.titulo == "Rafael" # Verificação 

def test_insert():
    filme_repository = FilmesRepository(DBConnectionHandlerMock)
    response = filme_repository.insert("sampling", "genero", 33)
    
    print(response)
    assert response.titulo == "sampling"