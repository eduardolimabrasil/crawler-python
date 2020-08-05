"""lib Class to Process Data by Request."""
from datetime import datetime

import pandas as pd

from utils.utils import request_soup


class ProcessData:
    """lib Class to Process Data by Request."""

    def __init__(self, **kwargs):
        """Class constructor."""
        self.__session = kwargs.get('session')
        self.__data_frame = pd.DataFrame()
        self.__model = kwargs.get('model')
        self.__url = kwargs.get('url')
        self.__name_file = kwargs.get('name_file')
        self.__columns_name = kwargs.get('columns_name')

    def process(self):
        """process."""
        self.__create_data_frame(self.__collect_data())
        self.insert_bulk()

    def __collect_data(self):
        """collect_data."""
        soup = request_soup(url=self.__url)
        return soup.find('table', id='cross_rate_markets_stocks_1')

    @staticmethod
    def __navigate_rows(soup):
        """__navigate_rows."""
        result = []
        for row in soup.find('tbody').find_all('tr'):
            result.append(row.contents[8].attrs['data-value'])
        return result

    def insert_bulk(self):
        """insert."""
        self.__session.bulk_insert_mappings(
            self.__model,
            self.__data_frame.to_dict(orient='records')
        )

    def __create_data_frame(self, soup):
        """Method to create a data frame."""
        self.__data_frame = pd.read_html(str(soup))[0]
        timestamp = self.__navigate_rows(soup)
        # rename dataframe columns by columns name in sqlite
        self.__data_frame = self.__data_frame.rename(
            columns=self.__columns_name)
        self.__data_frame['time'] = pd.Series(timestamp)
        self.__data_frame['chg_perc'] = self.__data_frame['chg_perc'].\
            str.replace('%', '')
        self.__data_frame['created_date'] = datetime.now()
        # save_file(self.__name_file, self.__data_frame.to_string())
