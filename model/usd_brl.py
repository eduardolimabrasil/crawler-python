"""model UsdBrl."""
from sqlalchemy import Column, Integer, Float, String, DateTime

from connection_sqlite.sqlite_conn import BASE


class UsdBrl(BASE):
    """model UsdBrl."""

    __tablename__ = 'Usd_Brl'

    id = Column(Integer, primary_key=True, autoincrement=True)
    currency = Column(String)
    value = Column(Float)
    perc = Column(Float)
    timestamp = Column(DateTime)
