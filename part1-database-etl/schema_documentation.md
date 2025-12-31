# Database Schema Documentation

## 1. Entity–Relationship Description
### ENTITY: customers

#### Purpose:
Stores information about registered customers who place orders on the platform.

#### Attributes:
- customer_id – Unique identifier for each customer (Primary Key)

- first_name – Customer’s first name

- last_name – Customer’s last name

- email – Customer’s email address (unique)

- phone – Customer contact number

- city – City where the customer resides

- registration_date – Date when the customer registered

#### Relationships:

- One customer can place many orders

    → Relationship: customers (1) → orders (M)

### ENTITY: products

#### Purpose:
Stores information about products available for sale.

#### Attributes:

- product_id – Unique identifier for each product (Primary Key)

- product_name – Name of the product

- category – Product category (e.g., Electronics, Fashion)

- price – Unit price of the product

- stock_quantity – Quantity available in inventory

#### Relationships:

One product can appear in many order items

      → Relationship: products (1) → order_items (M)

### ENTITY: orders

#### Purpose:
Stores high-level order transaction details made by customers.

#### Attributes:

- order_id – Unique identifier for each order (Primary Key)

- customer_id – References the customer who placed the order (Foreign Key)

- order_date – Date the order was placed

- total_amount – Total value of the order

- status – Order status (Pending, Completed, Cancelled)

#### Relationships:

- Each order belongs to one customer

- One order can contain many order items

### ENTITY: order_items

#### Purpose:
Stores line-item details for each order, linking products with orders.

#### Attributes:

- order_item_id – Unique identifier (Primary Key)

- order_id – References the related order (Foreign Key)

- product_id – References the purchased product (Foreign Key)

- quantity – Number of units ordered

- unit_price – Price per unit at the time of purchase

- subtotal – quantity × unit_price

#### Relationships:

- Many order_items belong to one order

- Many order_items reference one product

## 2. Normalization Explanation (Third Normal Form – 3NF)

The database design follows Third Normal Form (3NF) to ensure data integrity, reduce redundancy, and avoid anomalies.

### Functional Dependencies

- customer_id → first_name, last_name, email, phone, city, registration_date

- product_id → product_name, category, price, stock_quantity

- order_id → customer_id, order_date, total_amount, status

- order_item_id → order_id, product_id, quantity, unit_price, subtotal

Each non-key attribute depends only on the primary key, and not on other non-key attributes.

### Why the design is in 3NF

#### 1NF (First Normal Form)

- All tables contain atomic values

- No repeating groups or multi-valued attributes

#### 2NF (Second Normal Form)

- All non-key attributes depend fully on the whole primary key

- Composite dependencies are avoided by separating orders and order_items

#### 3NF (Third Normal Form)

- No transitive dependencies exist

- Customer details are not stored in the orders table

- Product details are not duplicated inside order_items

### Prevention of Anomalies

- Update anomaly avoided: Updating customer or product details requires change in only one table.

- Insert anomaly avoided: New customers or products can be added without requiring orders.

- Delete anomaly avoided: Deleting an order does not remove customer or product information.

Thus, the schema is clean, normalized, and scalable.

## 3. Sample Data Representation
### Customers (sample)


| customer_id | first_name | last_name | email | phone | city | registration_date |
|-------------|------------|-----------|-------|-------|------|-------------------|
|    C001     |   Rahul    |  Sharma   | rahul.sharma@gmail.com|+91-9876543210|Bangalore|2023-01-15|
|C002|Priya|Patel|priya.patel@yahoo.com|+91-9988776655|Mumbai|2023-02-20|

### Products (sample)

| product_id | product_name | category | price | stock_quantity | 
|------------|--------------|----------|-------|----------------|
|   P001     | Samsung Galaxy S21| Electronics| 45999.00| 150 |
| P002   |Nike Running Shoes|Fashion|3499.00|80|

### Orders (sample)

| order_id | customer_id | order_date | total_amount | status    |
| -------- | ----------- | ---------- | ------------ | --------- |
| 55       | 1           | 2024-01-15 | 45999.00     | Completed |
| 56       | 2           | 2024-01-16 | 5998.00      | Completed |

### Order Items (sample)

| order_item_id | order_id | product_id | quantity | unit_price | subtotal |
| ------------- | -------- | ---------- | -------- | ---------- | -------- |
| 1             | 55       | 1          | 1        | 45999.00   | 45999.00  |
| 2             | 56       | 4          | 2        | 2999.00    | 5998.00   |
