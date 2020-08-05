"""App Test."""
from unittest import TestCase
from unittest.mock import patch

from sqlalchemy.orm.session import Session

from app import main_ibovespa, main_nasdaq, main_usd_brl, main_nasdaq_brl_file
from lib.process_data import ProcessData
from lib.process_data_current import ProcessDataCurrent
from lib.process_data_nasdaq_brl import ProcessDataNasdaqBrl


class AppTest(TestCase):
    """App Test."""
    def setUp(self) -> None:
        """SetUp."""
        pass

    @patch.object(ProcessData , 'process')
    def test_ibovespa(self, process_data):
        """Test ibovespa."""
        process_data.return_value = None
        self.assertIsNone(main_ibovespa(Session()))

    @patch.object(ProcessData , 'process')
    def test_main_nasdaq(self, process_data):
        """Test main_nasdaq."""
        process_data.return_value = None
        self.assertIsNone(main_nasdaq(Session()))

    @patch.object(ProcessDataCurrent , 'process')
    def test_main_usd_brl(self, process_data):
        """Test main_usd_brl."""
        process_data.return_value = None
        self.assertIsNone(main_usd_brl(Session()))

    @patch.object(ProcessDataNasdaqBrl , 'process')
    def test_main_nasdaq_brl_file(self, process_data):
        """Test main_nasdaq_brl_file."""
        process_data.return_value = None
        self.assertIsNone(main_nasdaq_brl_file(Session()))
