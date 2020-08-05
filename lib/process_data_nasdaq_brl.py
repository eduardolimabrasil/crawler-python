"""lib Class to Process Data by Request."""
from datetime import datetime

import pandas as pd
from sqlalchemy.sql import func
from sqlalchemy.orm.session import Session

from model.nasdaq import Nasdaq
from model.usd_brl import UsdBrl
from model.nasdaq_brl import NasdaqBrl
from connection_sqlite.sqlite_conn import BASE


class ProcessDataNasdaqBrl:
    """lib Class to Process Data by Request."""

    def __init__(self, session: Session, model: BASE):
        """"Class constructor."""
        self.__session = session
        self.__data_frame = pd.DataFrame()
        self.__model = model

    def process(self):
        """process."""
        usdbrl = self.__session.query(UsdBrl).\
            order_by(UsdBrl.id.desc()).\
            first()
        last_nasdaq_created_date = self.__session.query(
            func.max(Nasdaq.created_date)).\
            scalar()
        nasdaq_records = self.__session.query(Nasdaq).filter(
            Nasdaq.created_date == last_nasdaq_created_date
        )
        data_frame = pd.read_sql(nasdaq_records.statement,
                                 nasdaq_records.session.bind)
        data_frame['high_rs'] = data_frame['high_usd'] * usdbrl.value
        data_frame['low_rs'] = data_frame['low_usd'] * usdbrl.value
        data_frame['last_rs'] = data_frame['last_usd'] * usdbrl.value
        columns = [
            'name',
            'last_rs',
            'high_rs',
            'low_rs',
            'last_usd',
            'high_usd',
            'low_usd',
            'chg',
            'chg_perc',
            'vol',
            'time'
        ]
        data_frame.to_csv(
            f'{usdbrl.timestamp}.csv',
            columns=columns
        )

    def insert(self, nasdaq_id: int, usdbrl_id: int):
        """insert."""
        nbrl = NasdaqBrl(nasdaq_id=nasdaq_id,
                         usdbrl_id=usdbrl_id,
                         timestamp=datetime.now().timestamp())
        self.__session.add(nbrl)
