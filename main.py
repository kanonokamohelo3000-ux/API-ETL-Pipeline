import logging
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_to_postgres

# LOGGING SETUP
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler("pipeline.log"),
        logging.StreamHandler()
    ]
)

def run_pipeline():
    try:
        logging.info("--- PIPELINE STARTED ---")
        
        df = extract_data("Practice_Table.csv")
        clean_df = transform_data(df)
        load_to_postgres(clean_df, "practice_table")
        
        logging.info("--- PIPELINE SUCCESS ---")
    except Exception as e:
        logging.error(f"--- PIPELINE FAILED: {e} ---", exc_info=True)

if __name__ == "__main__":
    run_pipeline()
    
