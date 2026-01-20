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
An app where Bakers, Chefs, Restaurateurs, and people in similar fields set the price of a single item to optimize their profit margins. They enter their recipes, their zip code, their overhead (employees' wages, rent, etc), expected monthly customer number, and their desired profit margin, and it returns price they should charge for each item. It also returns the market tolerance for that price, the best-case and worst-case profit margins for that month, and the month's average profit margin. 

## Live Demo
[Link - placeholder for now]

## Business Problem
Bakers, chefs, and the like know how to make delicious food, but often lack business sense when it comes to pricing their products to make the most bang for their buck. The time invested in setting their prices is usually tedious, takes away from their craft, or capital they could invest in other things. 
The idea is to save them time and money, while offering them some predictability in an otherwise unpredictable field. 

## How It Works
They enter their recipes, their zip code, their overhead (rent, bills etc), the time it takes to make, how many employees(or their self), their expertise level and their desired profit margin. The app determines the price per serving and the batch serving price to achieve this goal.It also gives an idea of the market tolerance for this price. 
It also returns the best-case, most likely, and worst-case profit margin to provide some predictability and planning.

## Key Features
- Unit Price Calculator
- Market Price Comparison
- Bayesian Price Tolerance Comparison
- Monte Carlo Profit Simulation

## Data Sources
- Opentable.com via web-scraper API
- Bureau of Labor Statistics
- Census.gov

## Methodology
The app uses ***Deterministic Unit Economics Math*** to determine the price per serving and batch serving price,and the user's entries to determine the cost. 
Furthermore, a Bayesian Regression Model trained on competitor prices in the area provides the probability of market tolerance for that price.
A Monte Carlo Simulation reports the profit margins for a best-case, most likely, and worst-case scenario to provide some predictability and planning, while accounting for waste based on the experience level of the user. 

## Tech Stack
- PostgreSQL with DBeaver for Database Management to handle large volumes of data cleaning and manipulation
- Python and necessary libraries for data manipulation, web scraping, model training, and Monte Carlo simulation for its ease of use and versatility
- Streamlit to deploy the app
- GitHub for Version control

## Database Schema

## Database Schema

### Table: ingredients
| Column | Type | Description |
|--------|------|-------------|
| ingredient_id | INT | Primary key |
| name | VARCHAR | Ingredient name (flour, butter, etc.) |
| price | DECIMAL | Price per unit |
| unit | VARCHAR | Unit of measure (lb, oz, each) |
| min_purchase_qty | DECIMAL | Minimum wholesale purchase quantity |
| min_purchase_unit | VARCHAR | Unit for minimum purchase |
| source | VARCHAR | Where price came from (USDA, WhatChefsWant, etc.) |
| last_updated | DATE | When price was last updated |

### Table: zip_codes
| Column | Type | Description |
|--------|------|-------------|
| zip_code | VARCHAR | Primary key |
| city | VARCHAR | City name |
| median_income | INT | Median household income |
| avg_rent_commercial | DECIMAL | Average commercial rent per sq ft |
| avg_wage_food_service | DECIMAL | Average food service wage |
| population | INT | Population |
| source | VARCHAR | Data source (Census, BLS) |

### Table: competitors
| Column | Type | Description |
|--------|------|-------------|
| competitor_id | INT | Primary key |
| name | VARCHAR | Business name |
| zip_code | VARCHAR | Foreign key to zip_codes |
| business_type | VARCHAR | Bakery, restaurant, meal prep, etc. |
| item_name | VARCHAR | Menu item |
| item_price | DECIMAL | Price charged |
| source | VARCHAR | Yelp, Google, menu scrape |
| scraped_date | DATE | When data was collected |

## Project Phases

**Phase 1: Planning**
- Define scope, write documentation, design database schema

**Phase 2: Data Infrastructure**
- Build database framework
- Set up data pipeline
- Web scrape competitor pricing (Yelp, menus)
- Populate Database with ingredients, zip codes, wages

**Phase 3: Exploration & Validation**
- Explore data, check for gaps
- Validate data quality

**Phase 4: Model Development**
- Build a deterministic unit economics function
- Build and train a Bayesian regression model
- Build a Monte Carlo simulation
- Test each component

**Phase 5: Deployment**
- Build Streamlit app
- Deploy and test end-to-end
- Monitor for drift, optimize latency, gather feedback

Repeat testing, tune the model, monitor for drift, check logs constantly for errors, tune and optimize latency, and listen for user feedback. Continue to fine-tune the model. 

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
