# Food Business Unit Pricing Suggestion App

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://nameyourprice.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

## Overview
An app where Bakers, Chefs, Restaurateurs, and people in similar fields set the price of a single item to optimize their profit margins. They enter their recipes, their zip code, their overhead (employees' wages, rent, etc), expected monthly customer number, and their desired profit margin, and it returns how much they should make and the price they should charge for each item, and how much to buy to meet that demand. It also returns the market tolerance for that price, the best-case and worst-case profit margins for that month, and the month's average profit margin. 

## Live Demo
[Link - placeholder for now]

## Business Problem
New food entrepreneurs struggle to set prices for their products. They guess, overprice, spend money on tools to do it for them, or spend weeks researching.


## How It Works
User Inputs the following: 

- Recipe name
- Ingredients + costs (manual entry for MVP)
- Number of servings
- Desired profit margin
- Overhead costs (labor rate × hours)
- Zip code
- Experience level (beginner/intermediate/experienced)
- Expected number of customers

App outputs the following:

- Price per unit
- Batch price
- Competitor price range (min, median, max)
- User's percentile ("higher than 75% of competitors")
- Market fit rating (High / Medium / Low)
- Probability of reaching profit goal (Monte Carlo)

## Key Features
- Unit Price Calculator
- Market Price Comparison
- Monte Carlo Profit Simulation

## Data Sources
- Open Table via Apify
- Rapid Food Ingredient Measurement API
- Census.gov
- User Inputs

## Methodology
The app uses ***Deterministic Unit Economics Math*** to determine the price per plate based on the User Entry of their costs, overhead, and recipe, along with their desired profit margins, to return the unit price that achieves the desired profit margin. 
Using competitor prices in the area provides the probability of market tolerance for that price. A Monte Carlo Simulation reports the probability of hitting the profit margins for a best-case, most likely, and worst-case scenario to provide some predictability and planning.

## Tech Stack
- PostgreSQL with DBeaver for Database Management to handle large volumes of data cleaning and manipulation
- Python and necessary libraries for data manipulation, web scraping, model training, and Monte Carlo simulation for its ease of use and versatility
- Streamlit to deploy the app
- GitHub for Version control

## Database Schema

## Database Schema

### Table: zip_code
| Column | Type | Description |
|--------|------|-------------|
| zip_code | VARCHAR | Primary key |
| annual_income | Decimal(10,2) | median annual income

### Table: restaurant
| Column | Type | Description |
|--------|------|-------------|
| restaurant_id | Serial INT | Primary key |
| restaurant_name | VARCHAR | Business name |
| restaurant_zip_code | VARCHAR | Foreign key to zip_code |
| cuisine_type | VARCHAR | Bakery, Italian restaurant, meal prep, etc. |
| restaurant_review_count | int | Number of reviews |
| restaurant_value | Decimal (10,2) | 4.1, 3.8, 4.5 |
| restaurant_price_tier | VARCHAR | $, $$, $$$, $$$$ |
| scraped_date | DATE | When data was collected |

### Table: menu_item
| Column | Type | Description |
|--------|------|-------------|
| item_id | Serial INT | Primary key |
| restaurant_id | INT | foreign key to restaurant |
| item_name | VARCHAR | Item name |
| item_desc | VARCHAR | Description of the item |
| item_price | Decimal(10,2) | Price of the item |
| item_category | VARCHAR | dessert, vegan, gluten-free, etc |
| item_price_date | DATE | When data was collected |

### Table: restaurant_value_rating
| Column | Type | Description |
|--------|------|-------------|
| rating_id | Serial INT | Primary key |
| restaurant_id | Int | foreign key to restaurant |
| rating_value | int | 1,2,3,4,5 |
| rating_count | Integer | number of reviews of each value |


## Project Phases

**Phase 1: Planning**
- Define scope, write documentation,

**Phase 2: Data Infrastructure**
- Build database framework
- Set up data pipeline
- Web scrape competitor pricing (Yelp, menus)
- Populate Database

**Phase 3: Exploration & Validation**
- Explore data, check for gaps
- Validate data quality

**Phase 4: Model Development**
- Build a deterministic unit economics function
- Build Market comparison tool
- Build a Monte Carlo simulation
- Test each component

**Phase 5: User Interface**
- Build Streamlit UI

**Phase 6: Testing + Bug Fixes**
- Test for bugs and address any bugs

**Phase 7: Add Machine Learning Features**
- Bayesian Regression for market tolerance

**Phase 8: Polish and Deploy

Repeat testing, tune the model, add features like caching, load balancing, etc to improve UI and UX experience and increase uptime. 

## Limitations
- This tool is not going to predict the price that you are going to sell at.
- This tool will not predict your sales for you.
- The best and worst case scenarios are based on the numbers and competitors in the areas only; we have no say on whether your product is of good quality or not.
- This tool is not going to get you customers.
- This is not an oracle; it is a tool, not a replacement for a Business Intelligence analyst. 

## Future Enhancements (v2)
- Subscription with Churn prediction for those with an existing customer base
- More accurate market tolerance for those with an existing customer base
- Monte Carlo simulations for those with prior sales records.
- Integration with Inventory Management systems for better deterministic pricing.
- New York City, Hell's Kitchen Area

## Contact
Onyedikachukwu Okonkwo
okonkwo.employee@gmail.com
