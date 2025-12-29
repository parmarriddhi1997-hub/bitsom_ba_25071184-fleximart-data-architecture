"""
FlexiMart ETL Pipeline
---------------------
Extract data from raw CSV files
Transform data to fix quality issues
Load clean data into MySQL database
"""
# =========================
# 1. IMPORT LIBRARIES
# =========================
import os
import pandas as pd
import numpy as np
import mysql.connector
from dateutil import parser
import re

# -------------------------
# 2.  PATH CONFIGURATION
# -------------------------
BASE_DIR = r"C:\Users\dell\Documents\GitHub\AI Data Architecture Design and Implementation\bitsom_ba_25071184-fleximart-data-architecture"
DATA_DIR = os.path.join(BASE_DIR, "data")

customers = pd.read_csv(os.path.join(DATA_DIR, "customers_raw.csv"))
products = pd.read_csv(os.path.join(DATA_DIR, "products_raw.csv"))
sales = pd.read_csv(os.path.join(DATA_DIR, "sales_raw.csv"))

# -------------------------
# 3. DATABASE CONNECTION
# -------------------------

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Scooby@2025",
    database="fleximart",
    autocommit=True  # CRITICAL
)

cursor = conn.cursor(dictionary=True)

# =========================
# 4. DATA QUALITY LOG
# =========================
data_quality_log = []

# -------------------------
# 5. Helper Functions
# -------------------------
def standardize_phone(phone):
    if pd.isna(phone):
        return None
    digits = re.sub(r'\D', '', phone)
    if digits.startswith("91") and len(digits) > 10:
        digits = digits[2:]
    elif digits.startswith("0") and len(digits) > 10:
        digits = digits[1:]
    if len(digits) == 10:
        return f"+91-{digits}"
    return None

def parse_date(date_value):
    try:
        return parser.parse(str(date_value)).date()
    except:
        return None


# -------------------------
# TRANSFORM – CUSTOMERS
# -------------------------

# Strip column names and string values
customers.columns = customers.columns.str.strip()
customers = customers.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Remove rows with missing emails
customers.dropna(subset=["email"], inplace=True)

# Remove duplicates based on email
customers.drop_duplicates(subset=["email"], inplace=True)

# Standardize phone numbers
customers["phone"] = customers["phone"].apply(standardize_phone)

# Standardize registration_date
customers["registration_date"] = customers["registration_date"].apply(parse_date)

# Standardize city
customers["city"] = customers["city"].str.title()

# reset_index
customers.reset_index(drop=True, inplace=True)

# -------------------------
# TRANSFORM – PRODUCTS
# -------------------------
# Strip column names and string values
products.columns = products.columns.str.strip()
products = products.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Fill missing prices
products['price'] = products['price'].fillna(0)

# Fill missing stock_quantity
products['stock_quantity'] = products['stock_quantity'].fillna(0).astype(int)

# Standardize category names
products['category'] = products['category'].str.strip().str.title()

# Standardize product_name
products['product_name'] = products['product_name'].str.strip()

# reset_index
products.reset_index(drop=True, inplace=True)

# -------------------------
# TRANSFORM – SALES
# -------------------------
# Strip column names and string values
sales.columns = sales.columns.str.strip()
sales = sales.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Remove duplicate transactions
sales.drop_duplicates(subset=["transaction_id"], keep='first', inplace=True)

# Drop rows with missing customer_id or product_id
sales.dropna(subset=["customer_id", "product_id"], inplace=True)

# Standardize transaction dates
sales["transaction_date"] = sales["transaction_date"].apply(parse_date)
sales.dropna(subset=["transaction_date"], inplace=True)

# Calculate total_amount (subtotal)
sales["quantity"] = sales["quantity"].astype(int)
sales["unit_price"] = sales["unit_price"].astype(float)
sales["subtotal"] = sales["quantity"] * sales["unit_price"]
sales['total_amount'] = sales.groupby("transaction_id")["subtotal"].transform('sum')

# ----------------------------------
# Split into orders and order_items
# ----------------------------------
orders = sales[["transaction_id","customer_id","transaction_date","total_amount","status"]].drop_duplicates()
order_items = sales[["transaction_id","product_id","quantity","unit_price","subtotal"]]

orders["customer_id"] = orders["customer_id"].str.replace("C","").astype(int)
order_items["product_id"] = order_items["product_id"].str.replace("P","").astype(int)

# -------------------------
# LOAD – CUSTOMERS
# -------------------------
# Prepare list of tuples
data = [(
    row['first_name'], row['last_name'], row['email'], 
    row['phone'], row['city'], row['registration_date']
) for _, row in customers.iterrows()]

# Execute batch insert
cursor.executemany("""
    INSERT IGNORE INTO customers (first_name, last_name, email, phone, city, registration_date)
    VALUES (%s, %s, %s, %s, %s, %s)
""", data)

conn.commit()
cursor.close()
conn.close()

# -------------------------
# LOAD – PRODUCTS
# -------------------------
# Prepare list of tuples for batch insert
data = [
    (
        row['product_name'],
        row['category'],
        float(row['price']),
        int(row['stock_quantity'])
    )
    for _, row in products.iterrows()
]

# Batch insert using executemany()
cursor.executemany("""
    INSERT INTO products (product_name, category, price, stock_quantity)
    VALUES (%s, %s, %s, %s)
""", data)

# Commit and close
conn.commit()
cursor.close()
conn.close()


# -------------------------
# LOAD – ORDERS & ORDER_ITEMS
# -------------------------
try:
    # ---------------------------
    # Load reference keys
    # ---------------------------
    cursor.execute("SELECT customer_id FROM customers")
    customer_ids = {r["customer_id"] for r in cursor.fetchall()}

    cursor.execute("SELECT product_id FROM products")
    product_ids = {r["product_id"] for r in cursor.fetchall()}

    # ---------------------------
    # Insert orders
    # ---------------------------
    insert_order_sql = """
        INSERT INTO orders (customer_id, order_date, total_amount, status)
        VALUES (%s, %s, %s, %s)
    """

    order_map = {}

    for _, r in orders.iterrows():
        if r.customer_id not in customer_ids:
            continue

        cursor.execute(
            insert_order_sql,
            (
                int(r.customer_id),
                r.transaction_date,
                float(r.total_amount),
                r.status
            )
        )

        order_map[r.transaction_id] = cursor.lastrowid

    # ---------------------------
    # Insert order items
    # ---------------------------
    insert_item_sql = """
        INSERT INTO order_items
        (order_id, product_id, quantity, unit_price, subtotal)
        VALUES (%s, %s, %s, %s, %s)
    """

    for _, r in order_items.iterrows():
        order_id = order_map.get(r.transaction_id)

        if order_id is None:
            continue

        if r.product_id not in product_ids:
            continue

        cursor.execute(
            insert_item_sql,
            (
                order_id,
                int(r.product_id),
                int(r.quantity),
                float(r.unit_price),
                float(r.subtotal)
            )
        )

    print("✅ Orders and order_items loaded successfully")

except Exception as e:
    print("❌ Error occurred:", e)

finally:
    cursor.close()
    conn.close()