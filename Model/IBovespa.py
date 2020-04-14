'''model IBovespa'''
from Model.SQLiteConn import Base
from sqlalchemy import Column, Integer, Float, String


class IBovespa(Base):
    __tablename__ = 'iBovespa'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50))
    last_rs = Column(Float)
    high_rs = Column(Float)
    low_rs = Column(Float)
    chg = Column(Float)
    chg_perc = Column(Float)
    vol = Column(String)
    time = Column(String)

