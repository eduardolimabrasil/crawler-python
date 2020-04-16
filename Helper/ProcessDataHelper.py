"""Helper Class to Process Data by Request"""
import pandas as pd
from datetime import datetime
from Utils.utils import request_soup, save_file 


class ProcessDataHelper(object):

    def __init__(self, session, model, url, name_file, columns_name):
        self.__session = session
        self.__data_frame = pd.DataFrame()
        self.__model = model
        self.__url = url
        self.__name_file = name_file
        self.__columns_name = columns_name

    def process(self):
        self.__create_data_frame(self.__collect_data())
        self.__insert()

    def __collect_data(self):
        soup = request_soup(url=self.__url)
        return soup.find('table', id='cross_rate_markets_stocks_1')
    
    @staticmethod
    def __navigate_rows(soup):
        return [row.contents[8].attrs['data-value'] for row in soup.find('tbody').find_all('tr')]

    def __insert(self):
        self.__session.bulk_insert_mappings(
            self.__model,
            self.__data_frame.to_dict(orient='records')
        )

    def __create_data_frame(self, soup):
        """ Method to create a data frame """
        self.__data_frame = pd.read_html(str(soup))[0]
        timestamp = self.__navigate_rows(soup)
        # rename dataframe columns by columns name in sqlite
        self.__data_frame = self.__data_frame.rename(columns=self.__columns_name)
        self.__data_frame['time'] = pd.Series(timestamp)
        self.__data_frame['chg_perc'] = self.__data_frame['chg_perc'].str.replace('%', '')
        self.__data_frame['created_date'] = datetime.now()
        save_file(self.__name_file, self.__data_frame.to_string())
