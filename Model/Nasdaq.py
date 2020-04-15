"""model Nasdaq"""
from ConnectionSqlite.SQLiteConn import Base
from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime


class Nasdaq(Base):
    __tablename__ = 'Nasdaq'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50))
    last_usd = Column(Float)
    high_usd = Column(Float)
    low_usd = Column(Float)
    chg = Column(Float)
    chg_perc = Column(Float)
    vol = Column(String)
    time = Column(Integer)
    created_date = Column(DateTime)
