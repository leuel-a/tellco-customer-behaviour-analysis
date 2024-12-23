import os
import unittest
import pandas as pd
from unittest.mock import patch, MagicMock
from scripts.load_data import load_data_from_db


class TestLoadData(unittest.TestCase):
    """
    This module contains unit tests for verifying the functionality of loading data
    from a PostgreSQL database. The tests ensure the connection parameters are
    correctly provided via environment variables and that the returned data
    matches expected results.

    :class TestLoadData:
        A unittest.TestCase subclass that tests the load_data_from_db function.

        Methods
        -------
        test_load_data_from_db()
            Verifies that a mock DataFrame is returned from the database, and that
            the database engine and query are called with the correct arguments.
    """

    @patch.dict(
        os.environ,
        {
            "DB_USER": "leuel",
            "DB_HOST": "localhost",
            "DB_PORT": "5432",
            "DB_PASSWORD": "la@1993#",
            "DB_NAME": "tellco_db",
            "DB_TABLE_NAME": "xdr_data",
        },
    )
    @patch("scripts.load_data.create_engine")
    @patch("pandas.read_sql")
    def test_load_data_from_db(self, mock_read_sql, mock_create_engine):
        """
        Tests that the load_data_from_db function retrieves data from the specified
        database and returns the correct DataFrame.

        :param mock_read_sql: Mock object for pandas.read_sql, used to simulate querying the database.
        :param mock_create_engine: Mock object for sqlalchemy.create_engine, used to simulate creating a database engine.
        :returns: None
        """
        mock_df = pd.DataFrame({"column1": [1, 2], "column2": ["Value1", "Value2"]})
        mock_read_sql.return_value = mock_df

        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine

        result = load_data_from_db()

        mock_create_engine.assert_called_once_with(
            "postgres+psycopg2://leuel:la@1993#@localhost:5432/tellco_db"
        )

        mock_read_sql.assert_called_once_with("SELECT * FROM xdr_data", mock_engine)
        pd.testing.assert_frame_equal(result, mock_df)
