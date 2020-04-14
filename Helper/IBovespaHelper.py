'''Classe Helper Ibovespa'''
import pandas as pd
from Utils.utils import request_soup, save_file
from Model.IBovespa import IBovespa
from settings import URL_IBOVESPA, COLUMNS_IBOVESPA, IBOVESPA_NAME_FILE

class IbovespaHelper(object):

    def __init__(self, session):
        self.session = session
        self.__data_frame = pd.DataFrame()

    def collect_data(self):
        soup_ibovespa = request_soup(URL_IBOVESPA)
        table = soup_ibovespa.find('table', id='cross_rate_markets_stocks_1')
        self.__create_data_frame(table)
        self.__insert()

    def __insert(self):
        self.session.bulk_insert_mappings(
            IBovespa,
            self.__data_frame.to_dict(orient='records')
        )

    def __create_data_frame(self, soup):
        self.__data_frame = pd.read_html(str(soup))[0]
        #rename columns by name table sqlite
        self.__data_frame = self.__data_frame.rename(columns=COLUMNS_IBOVESPA)
        self.__data_frame['chg_perc'] = self.__data_frame['chg_perc'].str.replace('%', '')
        save_file(IBOVESPA_NAME_FILE, self.__data_frame.to_string())
