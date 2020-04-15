"""model IBovespa"""
from ConnectionSqlite.SQLiteConn import Base
from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime


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
    time = Column(Integer)
    created_date = Column(DateTime)

