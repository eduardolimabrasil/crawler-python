import requests
import pandas as pd
from bs4 import BeautifulSoup
from Model.SQLiteConn import SQLiteConn
from Model.IBovespa import IBovespa
from settings import IBOVESPA, HEADERS, COLUMNS_IBOVESPA

def request_soup(url):
    req = requests.get(url, headers=HEADERS)
    return BeautifulSoup(req.content, "lxml")

def main():
    #Crawler IBOVESPA
    soup_ibovespa = request_soup(IBOVESPA)
    table = soup_ibovespa.find('table', id='cross_rate_markets_stocks_1')
    df_ibovespa = pd.read_html(str(table))[0]
    #rename columns by name table sqlite
    df_ibovespa = df_ibovespa.rename(columns=COLUMNS_IBOVESPA)
    df_ibovespa.reset_index(inplace=True)
    df_ibovespa['chg_perc'] = df_ibovespa['chg_perc'].str.replace('%', '')
    conn = SQLiteConn()
    session = conn.create_session()
    #Save dataframe to table
    session.bulk_insert_mappings(
        IBovespa,
        df_ibovespa.to_dict(orient='records')
    )
    all_rows = session.query(IBovespa).all()
    print(all_rows)
    session.commit()


if __name__ == '__main__':
    main()
