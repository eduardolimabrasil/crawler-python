"""lib Class to Process Data by Request."""
import logging

import datetime as dt
from typing import Tuple

from utils.utils import request_soup
from model.usd_brl import UsdBrl
from .process_data import ProcessData


class ProcessDataCurrent(ProcessData):
    """ProcessDataCurrentHelper."""

    def __init__(self, **kwargs):
        """Class constructor."""
        super().__init__(**kwargs)

    def process(self) -> None:
        """process."""
        currency, value, perc, timestamp = self.__collect_data()
        self.insert(currency=currency,
                    value=value,
                    perc=perc,
                    timestamp=timestamp)

    def __collect_data(self) -> Tuple:
        """collect_data."""
        soup = request_soup(url=self._ProcessData__url)
        quotes_box_top = soup.find('div', 'quotesBoxTop')
        currency = 'USD'
        value = float(quotes_box_top.contents[1].contents[0])
        perc = float(quotes_box_top.contents[3].contents[5].
                     contents[0].replace('%', ''))
        pair_timestamp = soup.find('div', 'pairTimestamp')

        while True:
            try:
                aux_time = dt.datetime.strptime(
                    pair_timestamp.contents[3].contents[0], '%H:%M:%S'
                ).time()
                break
            except ValueError:
                pass

        timestamp = dt.datetime.combine(dt.date.today(), aux_time)
        return currency, value, perc, timestamp

    def insert(self, **kwargs) -> bool:
        """insert."""
        try:
            usdbrl = UsdBrl(currency=kwargs.get('currency'),
                            value=kwargs.get('value'),
                            perc=kwargs.get('perc'),
                            timestamp=kwargs.get('timestamp'))
            self.__session.add(usdbrl)
            return True
        except ValueError as val_error:
            logging.error(val_error)
            return False
        except ConnectionError as conn_error:
            logging.error(conn_error)
            return False
        except Exception as ex:
            logging.error(ex)
            return False
