"""model IBovespa."""
from sqlalchemy import Column, Integer, Float, String, DateTime

from connection_sqlite.sqlite_conn import BASE


class IBovespa(BASE):
    """model IBovespa."""

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

