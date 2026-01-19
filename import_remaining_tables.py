import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus
import requests
import json
from sqlalchemy import text

# Load enviroment variables  from .env
load_dotenv()
password = quote_plus(os.getenv('postgres_pwd'))

engine = create_engine(f'postgresql://postgres:{password}@localhost:5432/price_per_unit_sugg')

with open('dataset_opentable-reviews-cheerio_2026-01-18_19-07-52-355.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)


restaurant_data = [] #list for restaurant data
restaurant_value_ratings = [] #list for restaurant value ratings
menu_items =[] # this creates a list of the menu items and I import the data into here as a list of lists

# The line `restaurant_data.append({restaurant_item_data})` is appending a dictionary containing
# restaurant item data to the `restaurant_data` list. The `restaurant_item_data` dictionary is
# being enclosed in curly braces `{}` to create a single-item dictionary before appending it to
# the `restaurant_data` list.

# for loop goes here
for restaurant in data:

    restaurant_item_data = {        
        'restaurant_id': restaurant['id'],
        'restaurant_name' : restaurant['name'],
        'restaurant_zip_code' : restaurant['postalCode'].split('-')[0],
        'cuisine_type' : next((c['name'] for c in restaurant['cuisines'] if c['primary'] == True), 'Unknown'),
        'restaurant_review_count' : restaurant['reviews']['count'],
        'restaurant_value' : restaurant['reviews']['value'],
        'restaurant_price_tier': restaurant['priceBand']['label'],
        'scraped_date' : pd.to_datetime('today').date()
        }
    restaurant_data.append(restaurant_item_data)

    for rating in restaurant['reviews']['distribution']:
        rating_data = {
            'restaurant_id': restaurant['id'],
            'rating_value': rating['value'],
            'rating_count': rating['count'],
            'scraped_date': pd.to_datetime('today').date()
            }
        restaurant_value_ratings.append(rating_data)
            
    for menu in restaurant['menus']:
        for section in menu['sections']:
            category = section['title']
            for item in section ['items']:
                item_data = {
                    'restaurant_id': restaurant['id'],
                    'item_name' : item['title'],
                    'item_desc' : item.get('desc', ''),
                    'item_price' : float(item.get('price', 0)),
                    'item_category': category,
                    'item_price_date': pd.to_datetime('today').date()
                    }
                menu_items.append(item_data)

print(f"Restaurants: {len(restaurant_data)}")
print(f"Ratings: {len(restaurant_value_ratings)}")
print(f"Menu items: {len(menu_items)}")

df_restaurants = pd.DataFrame(restaurant_data)
df_menu_items = pd.DataFrame(menu_items)
df_ratings = pd.DataFrame(restaurant_value_ratings)

restaurant_table = 'restaurant'
menu_items_table = 'menu_item'
ratings_table = 'restaurant_value_rating'


with engine.connect() as conn:
    conn.execute(text((f'TRUNCATE TABLE {restaurant_table} CASCADE;')))
    conn.execute(text((f'TRUNCATE TABLE {menu_items_table} CASCADE;')))
    conn.execute(text((f'TRUNCATE TABLE {ratings_table} CASCADE;')))
    conn.commit()
    
df_restaurants.to_sql('restaurant', engine, if_exists='append', index=False)
df_menu_items.to_sql('menu_item', engine, if_exists='append', index=False)
df_ratings.to_sql('restaurant_value_rating', engine, if_exists='append', index=False)

print(f'Inserted {len(df_restaurants)} rows into restaurants table.')
print(f'Inserted {len(df_menu_items)} rows into menu_items table.')
print(f'Inserted {len(df_ratings)} rows into ratings table.')
