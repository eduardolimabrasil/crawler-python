"""Helper Class to Process Data by Request"""
import pandas as pd
import datetime as dt
from Utils.utils import request_soup, save_file
from Model.UsdBrl import UsdBrl


class ProcessDataCurrentHelper(object):

    def __init__(self, session, model, url, name_file, columns_name):
        self.__session = session
        self.__data_frame = pd.DataFrame()
        self.__model = model
        self.__url = url
        self.__name_file = name_file
        self.__columns_name = columns_name

    def process(self):
        currency, value, perc, timestamp = self.__collect_data()
        self.__insert(currency, value, perc, timestamp)

    def __collect_data(self):
        soup = request_soup(url=self.__url)
        quotes_box_top = soup.find('div', 'quotesBoxTop')
        currency = 'USD'
        value = float(quotes_box_top.contents[1].contents[0])
        perc = float(quotes_box_top.contents[3].contents[5].contents[0].replace('%', ''))
        pair_timestamp = soup.find('div', 'pairTimestamp')

        aux_time = dt.datetime.strptime(pair_timestamp.contents[3].contents[0], '%H:%M:%S').time()

        timestamp = dt.datetime.combine(dt.date.today(), aux_time)
        return currency, value, perc, timestamp

    def __insert(self, currency, value, perc, timestamp):
        usdbrl = UsdBrl(currency=currency,
                        value=value,
                        perc=perc,
                        timestamp=timestamp)
        self.__session.add(usdbrl)
