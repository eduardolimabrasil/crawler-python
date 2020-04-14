from Model.SQLiteConn import SQLiteConn
from Model.IBovespa import IBovespa
from Model.Nasdaq import Nasdaq
from Model.UsdBrl import UsdBrl

import requests


def main():
    #Cria a base de dados e tabelas
    conn = SQLiteConn()
    conn.create_tables()

    session = conn.create_session()
    bovespa = IBovespa(name='Daenerys Targaryen')
    session.add(bovespa)
    bovespa = IBovespa(name='John Snow')
    session.add(bovespa)

    session.commit()

    result = session.query(IBovespa).all()
    for item in result:
        print(item.name)


if __name__ == '__main__':
    main()
