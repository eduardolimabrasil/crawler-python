import sys

from ConnectionSqlite.SQLiteConn import SQLiteConn
from Model.IBovespa import IBovespa
from Model.Nasdaq import Nasdaq
from Model.UsdBrl import UsdBrl
from Model.NasdaqBrl import NasdaqBrl
from Helper.ProcessDataHelper import ProcessDataHelper
from Helper.ProcessDataCurrentHelper import ProcessDataCurrentHelper
from Helper.ProcessDataNasdaqBrlHelper import ProcessDataNasdaqBrlHelper

from settings import *


def main_ibovespa(session):
    ibovespa_helper = ProcessDataHelper(
        session=session,
        model=IBovespa,
        url=URL_IBOVESPA,
        name_file=IBOVESPA_NAME_FILE,
        columns_name=COLUMNS_IBOVESPA
    )
    ibovespa_helper.process()


def main_nasdaq(session):
    nasdaq_helper = ProcessDataHelper(
        session=session,
        model=Nasdaq,
        url=URL_NASDAQ,
        name_file=NASDAQ_NAME_FILE,
        columns_name=COLUMNS_NASDAQ
    )
    nasdaq_helper.process()


def main_usd_brl(session):
    usdbrl_helper = ProcessDataCurrentHelper(
        session=session,
        model=UsdBrl,
        url=URL_USD_BRL,
        name_file=USD_BRL_NAME_FILE,
        columns_name=COLUMNS_USD_BRL
    )
    usdbrl_helper.process()


def main_nasdaq_brl_file(session):
    nbrl_helper = ProcessDataNasdaqBrlHelper(
        session=session,
        model=NasdaqBrl
    )
    nbrl_helper.process()


if __name__ == '__main__':
    conn = SQLiteConn()
    conn.create_tables()
    session = conn.create_session()
    if len(sys.argv) > 1:
        _, option = sys.argv
        options = {
            "ibovespa": main_ibovespa,
            "nasdaq": main_nasdaq,
            "usd_brl": main_usd_brl,
        }
        if options.get(option):
            options.get(option)(session=session)

    else:
        main_nasdaq_brl_file(session)  # print('Invalid option!')

    session.commit()
