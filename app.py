"""App Crawler."""
import argparse
import logging

from sqlalchemy.orm.session import Session

from connection_sqlite.sqlite_conn import SQLiteConn
from model.ibovespa import IBovespa
from model.nasdaq import Nasdaq
from model.usd_brl import UsdBrl
from model.nasdaq_brl import NasdaqBrl
from lib.process_data import ProcessData
from lib.process_data_current import ProcessDataCurrent
from lib.process_data_nasdaq_brl import ProcessDataNasdaqBrl

from settings import URL_IBOVESPA, IBOVESPA_NAME_FILE, COLUMNS_IBOVESPA,\
    URL_NASDAQ, NASDAQ_NAME_FILE, COLUMNS_NASDAQ, URL_USD_BRL,\
    USD_BRL_NAME_FILE, COLUMNS_USD_BRL


def main_ibovespa(session: Session) -> None:
    """Ibovespa."""
    ibovespa_helper = ProcessData(
        session=session,
        model=IBovespa,
        url=URL_IBOVESPA,
        name_file=IBOVESPA_NAME_FILE,
        columns_name=COLUMNS_IBOVESPA
    )
    ibovespa_helper.process()


def main_nasdaq(session: Session):
    """Nasdaq."""
    nasdaq_helper = ProcessData(
        session=session,
        model=Nasdaq,
        url=URL_NASDAQ,
        name_file=NASDAQ_NAME_FILE,
        columns_name=COLUMNS_NASDAQ
    )
    nasdaq_helper.process()


def main_usd_brl(session: Session):
    """USD to BRL."""
    usd_brl_helper = ProcessDataCurrent(
        session=session,
        model=UsdBrl,
        url=URL_USD_BRL,
        name_file=USD_BRL_NAME_FILE,
        columns_name=COLUMNS_USD_BRL
    )
    usd_brl_helper.process()


def main_nasdaq_brl_file(session: Session):
    """nasdaq brl file."""
    nbrl_helper = ProcessDataNasdaqBrl(
        session=session,
        model=NasdaqBrl
    )
    nbrl_helper.process()


def main():
    """Main Function."""
    parser = argparse.ArgumentParser(description="crawler", prog="crawler")

    parser.add_argument(
        '--crawler',
        type=str,
        nargs=1,
        help='Target Crawler Name(ibovespa, nasdaq and usd_brl)'
    )
    parser.add_argument(
        '--crawler_file',
        type=str,
        nargs=0,
        help='Get file'
    )
    args = parser.parse_args()
    if args.crawler:
        conn = SQLiteConn()
        conn.create_tables()
        session = conn.create_session()
        options = {
            "ibovespa": main_ibovespa,
            "nasdaq": main_nasdaq,
            "usd_brl": main_usd_brl
        }
        if args.crawler[0] in options:
            options.get(args.crawler[0])(session=session)

        else:
            main_nasdaq_brl_file(session)  # print('Invalid option!')

        session.commit()
    else:
        parser.print_help()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as ex_ki:
        pass
    except SyntaxError as ex_se:
        pass
    except (ValueError, Exception) as ex:
        logging.error(ex)
