"""model UsdBrl"""
from ConnectionSqlite.SQLiteConn import Base
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, column_property


class NasdaqBrl(Base):
    __tablename__ = 'Nasdaq_Brl'

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(Float)
    nasdaq_id = Column(Integer, ForeignKey('Nasdaq.id'))
    usdbrl_id = Column(Integer, ForeignKey('Usd_Brl.id'))

    # nasdaq = relationship("Nasdaq")
    # usdbrl = relationship("Usd_Brl")

    # name = column_property(nasdaq.name.expression)  # Column(String(length=50))

    # last_usd = column_property(nasdaq.last_usd)
    # high_usd = column_property(nasdaq.high_usd)
    # low_usd = column_property(nasdaq.low_usd)

    # last_rs = column_property(nasdaq.last_usd * usdbrl.currency)
    # high_rs = column_property(nasdaq.high_usd * usdbrl.currency)
    # low_rs = column_property(nasdaq.low_usd * usdbrl.currency)

    # chg = column_property(nasdaq.chg)  # Column(Float)
    # chg_perc = column_property(nasdaq.chg_perc)  # Column(Float)
    # vol = column_property(nasdaq.vol)  # Column(String)
    # time = column_property(nasdaq.time)  # Column(Integer)
