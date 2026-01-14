from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBconnection_handler:

    def __init__(self) -> None:
        self._connection_string = 'mysql+pymysql://root:1234@localhost:3306/cinema'
        self._engine = self._create_database_engine()
        self.session = None

    def _create_database_engine(self):
        return create_engine(self._connection_string)

    def get_engine(self):
        return self._engine

    def __enter__(self):
        Session_make = sessionmaker(bind=self._engine)
        self.session = Session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()



