'''model Nasdaq'''
from Model.SQLiteConn import Base
from sqlalchemy import Column, Integer, Float, String


class Nasdaq(Base):
    __tablename__ = 'Nasdaq'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    last_usd = Column(Float)
    high_usd = Column(Float)
    low_usd = Column(Float)
    chg = Column(Float)
    chg_perc = Column(Float)
    vol = Column(String)
    time = Column(String)
