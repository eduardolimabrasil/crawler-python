"""model UsdBrl"""
from ConnectionSqlite.SQLiteConn import Base
from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.orm import relationship


class UsdBrl(Base):
    __tablename__ = 'Usd_Brl'

    id = Column(Integer, primary_key=True, autoincrement=True)
    currency = Column(String)
    value = Column(Float)
    perc = Column(Float)
    timestamp = Column(DateTime)

    # parents = relationship("Nasdaq_Brl")
