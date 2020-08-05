"""Classe SQLite Connection."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.declarative import declarative_base
from settings import DATABASE_PATH

BASE = declarative_base()


class SQLiteConn:
    """Performs database connection. Create a sqlAlchemy engine instance."""

    def __init__(self):
        """Perform database connection. Create a sqlAlchemy engine instance."""
        self.engine = create_engine(f'sqlite:///{DATABASE_PATH}', echo=True)

    def create_session(self) -> Session:
        """Create a new session."""
        session = sessionmaker(bind=self.engine)
        return session()

    def create_tables(self) -> bool:
        """Create new tables."""
        BASE.metadata.create_all(self.engine)
        return True
