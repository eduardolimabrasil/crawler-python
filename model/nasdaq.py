"""model Nasdaq."""
from sqlalchemy import Column, Integer, Float, String, DateTime

from connection_sqlite.sqlite_conn import BASE



class Nasdaq(BASE):
    """Nasdaq."""

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
