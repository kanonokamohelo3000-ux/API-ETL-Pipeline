import pandas as pd
import requests

BASE_URL = "www.fakeStoreApi.com"

    
def extract_all():
    url = f"{BASE_URL}/users"
    response = requests.get(url)
    response.raise_for_status
    data = response.json()
    user_df = pd.Dataframe(data)
    
    url = f"{BASE_URL}/products"
    response = requests.get(url)
    response.raise_for_status
    data = response.json()
    products_df = pd.Dataframe(data)
    
    return products_df
    return user_df
    
