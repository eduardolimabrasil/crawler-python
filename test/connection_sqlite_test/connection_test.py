"""Connection Test."""
from unittest import TestCase

from sqlalchemy.orm.session import Session
from connection_sqlite.sqlite_conn import SQLiteConn

class AppTest(TestCase):
    def setUp(self) -> None:
        """Setup."""
        self.conn = SQLiteConn()

    def test_session_maker(self):
        """Session Maker."""
        result = self.conn.create_session()
        self.assertIsInstance(result, Session)

    def test_create_tables(self):
        """Create Tables."""
        result = self.conn.create_tables()
        self.assertTrue(result)
