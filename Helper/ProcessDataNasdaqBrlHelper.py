"""Helper Class to Process Data by Request"""
import pandas as pd
import datetime as dt
from Utils.utils import request_soup, save_file
from Model.Nasdaq import Nasdaq
from Model.UsdBrl import UsdBrl
from Model.NasdaqBrl import NasdaqBrl
from sqlalchemy.sql import func


class ProcessDataNasdaqBrlHelper(object):

    def __init__(self, session, model):
        self.__session = session
        self.__data_frame = pd.DataFrame()
        self.__model = model

    def process(self):
        usdbrl = self.__session.query(UsdBrl).order_by(UsdBrl.id.desc()).first()
        last_nasdaq_created_date = self.__session.query(func.max(Nasdaq.created_date)).scalar()
        nasdaq_records = self.__session.query(Nasdaq).filter(Nasdaq.created_date == last_nasdaq_created_date)
        df = pd.read_sql(nasdaq_records.statement, nasdaq_records.session.bind)
        df['high_rs'] = df['high_usd'] * usdbrl.value
        df['low_rs'] = df['low_usd'] * usdbrl.value
        df['last_rs'] = df['last_usd'] * usdbrl.value
        data = int(usdbrl.timestamp.timestamp())
        df.to_csv(f'data/{data}.csv', columns=['name', 'last_rs', 'high_rs', 'low_rs', 'last_usd', 'high_usd', 'low_usd', 'chg', 'chg_perc', 'vol', 'time'])

    def __insert(self, nasdaq_id, usdbrl_id):
        nbrl = NasdaqBrl(nasdaq_id=nasdaq_id,
                         usdbrl_id=usdbrl_id,
                         timestamp=dt.datetime.now().timestamp())
        self.__session.add(nbrl)
