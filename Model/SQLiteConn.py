from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class SQLiteConn(object):

    def __init__(self):
        """
        Performs database connection.
        Create a sqlAlchemy engine instance
        """
        self.engine = create_engine(r'sqlite:///crawler.db', echo=True)

    def create_session(self):
        """
        Create a new session.
        """
        session = sessionmaker(bind=self.engine)
        return session()

    def create_tables(self):
        """
        Create new tables.
        """
        Base.metadata.create_all(self.engine)