
import logging
import os

from sqlalchemy import create_engine
from sqlalchemy.engine import URL


def load_to_postgres(df, table_name):
    engine = None

    try:
        connection_url = URL.create(
            drivername="postgresql+psycopg2",
            username=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "5432")),
            database=os.environ["DB_NAME"]
        )

        engine = create_engine(connection_url)

        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",
            index=False
        )

        logging.info(
            "Successfully loaded %s rows into %s",
            len(df),
            table_name
        )

    except Exception:
        logging.exception(
            "Failed to load data into %s",
            table_name
        )
        raise

    finally:
        if engine is not None:
            engine.dispose()
