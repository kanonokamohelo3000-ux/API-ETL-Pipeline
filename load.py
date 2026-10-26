from sqlalchemy import create_engine


def load_to_postgres(df, table_name): 
    try:
        engine = create_engine(f"postgresql: //{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    
        df.to_sql(table_name,
        engine,
        if_exists = "replace",
        index = False)
        
        print("Data Loaded To Postgres Successfully ")
       
       except Exception as e:
           print(f"Postgres Data Load Failed {e}")
           
        
    


