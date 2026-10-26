
import logging
import pandas as pd
import requests

BASE_URL = "https://fakestoreapi.com"


def extract_all():
    try:
        logging.info("Starting data extraction")

        # Extract users
        response = requests.get(
            f"{BASE_URL}/users",
            timeout=30
        )
        response.raise_for_status()
        user_df = pd.DataFrame(response.json())

        # Extract products
        response = requests.get(
            f"{BASE_URL}/products",
            timeout=30
        )
        response.raise_for_status()
        product_df = pd.DataFrame(response.json())

        logging.info(
            "Extracted %s users and %s products",
            len(user_df),
            len(product_df)
        )

        return user_df, product_df

    except requests.RequestException:
        logging.exception("Data extraction failed")
        raise
