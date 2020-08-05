"""model NasdaqBrl."""
from sqlalchemy import Column, Integer, Float, ForeignKey
from connection_sqlite.sqlite_conn import BASE


class NasdaqBrl(BASE):
    """model NasdaqBrl."""

    __tablename__ = 'Nasdaq_Brl'

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(Float)
    nasdaq_id = Column(Integer, ForeignKey('Nasdaq.id'))
    usdbrl_id = Column(Integer, ForeignKey('Usd_Brl.id'))
