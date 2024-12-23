import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# load the enviroment variables
load_dotenv()

DB_USER = os.environ.get("DB_USER", "")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
DB_HOST = os.environ.get("DB_HOST", "")
DB_PORT = os.environ.get("DB_PORT", "")
DB_NAME = os.environ.get("DB_NAME", "")
DB_TABLE_NAME = os.environ.get("DB_TABLE_NAME", "")


def load_data_from_db() -> pd.DataFrame:
    """
    Loads data from a PostgreSQL database into a pandas DataFrame.

    This function connects to a PostgreSQL database using credentials and connection
    details specified in the environment variables or configuration. It then executes
    a SQL query to retrieve all records from a specified table and loads the results
    into a pandas DataFrame.

    :returns: a DataFrame containing the data retrieved from the database.
    :rtype: pd.DataFrame

    :raises:
        sqlalchemy.exc.SQLAlchemyError: If there is an error connecting to the database
                                        or executing the SQL query.
    """
    """Loads the data from the database to a pandas.DataFrame"""
    db_url = (
        f"postgres+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    engine = create_engine(db_url)
    return pd.read_sql(f"SELECT * FROM {DB_TABLE_NAME}", engine)
