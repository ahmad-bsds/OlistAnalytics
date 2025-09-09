import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# Define base folder
base_path = Path("./Data/2/").resolve()

# Connect to PostgreSQL
engine = create_engine("postgresql+psycopg2://postgres:1567@127.0.0.1:5432/postgres")

# Map file names to table names
files = {
    "olist_orders_dataset.csv": "orders",
    "olist_customers_dataset.csv": "customers",
    "olist_order_items_dataset.csv": "order_items",
    "olist_products_dataset.csv": "products",
    "olist_sellers_dataset.csv": "sellers",
    "olist_geolocation_dataset.csv": "geolocation",
    "olist_order_payments_dataset.csv": "order_payments",
    "olist_order_reviews_dataset.csv": "order_reviews",
}

# Loop through files and insert into PostgreSQL
for file_name, table_name in files.items():
    file_path = base_path / file_name
    if file_path.exists():
        print(f"📥 Loading {file_name} into {table_name}...")
        df = pd.read_csv(file_path)
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f"✅ {table_name} table created with {len(df)} rows")
    else:
        print(f"⚠️ File not found: {file_path}")
