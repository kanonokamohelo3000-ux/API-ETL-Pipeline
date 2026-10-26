
import logging

from dotenv import load_dotenv

from etl.extract import extract_all
from etl.transform import transform_product, transform_user
from etl.load import load_to_postgres


load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("pipeline.log"),
        logging.StreamHandler()
    ]
)


def run_pipeline():
    logging.info("ETL PIPELINE STARTED")

    try:
        # Extract
        user_df, product_df = extract_all()

        # Transform
        clean_users = transform_user(user_df)
        clean_products = transform_product(product_df)

        # Load
        load_to_postgres(clean_users, "users")
        load_to_postgres(clean_products, "products")

        logging.info("ETL PIPELINE COMPLETED SUCCESSFULLY")

    except Exception:
        logging.exception("ETL PIPELINE FAILED")
        raise


if __name__ == "__main__":
    run_pipeline()
