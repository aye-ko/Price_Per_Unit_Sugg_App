import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus
import requests

# Load environment variables from .env file
load_dotenv()
password = quote_plus(os.getenv('postgres_pwd'))
api_key = os.getenv('zip_code_annual_income_api_key')

zip_code_api_url = f'https://api.census.gov/data/2023/acs/acs5?get=B19013_001E&for=zip%20code%20tabulation%20area:*&key={api_key}'
# Create Engine connection to PostgreSQL database
engine  = create_engine(f'postgresql+psycopg2://postgres:{password}@localhost:5432/price_per_unit_sugg')
def fetch_zip_code_income_data(): 
    response = requests.get(zip_code_api_url) # pull data from api
    response.raise_for_status() # check for errors
    data = response.json()

    # convert data to dataframe adding date and source columns
    df = pd.DataFrame(data[1:], columns= 'average_annual_inc,zip_code'.split(',')) 

    # Add date and source columns
    df['data_date'] = '2023-12-31'
    df['data_source'] = 'Census Bureau API'
    
    # Replace -666666666 with null values
    df.replace('-666666666', pd.NA, inplace=True) # convert -666666666 into null values
    
    return df

# return dataframe and move to  postgres insertion step
df = fetch_zip_code_income_data()
table = 'zip_code'
# clear existing data and insert new data into postgres table
with engine.connect() as conn:
    conn.execute(f'TRUNCATE TABLE {table} CASCADE;')
    conn.commit()
    
df.to_sql(table, engine, if_exists='append', index=False)

# print confirmation message how many rows were inserted into which table
print(f'Inserted {len(df)} rows into {table} table.')
