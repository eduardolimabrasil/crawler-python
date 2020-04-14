from Model.SQLiteConn import SQLiteConn
from helper.IBovespaHelper import IbovespaHelper


def main():
    conn = SQLiteConn()
    session = conn.create_session()
    ibovespa_helper = IbovespaHelper(session=session)
    ibovespa_helper.collect_data()
    session.commit()

if __name__ == '__main__':
    main()
