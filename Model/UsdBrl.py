'''model UsdBrl'''
from Model.SQLiteConn import Base
from sqlalchemy import Column, Integer, Float, String


class UsdBrl(Base):
    __tablename__ = 'Usd_Brl'

    id = Column(Integer, primary_key=True, autoincrement=True)
    currency = Column(Float)
    value = Column(Float)
    perc = Column(Float)
    timestamp = Column(String)
