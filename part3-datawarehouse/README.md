# Part 3: Data Warehouse and Analytics
## Overview

This part focuses on designing and implementing a Data Warehouse for FlexiMart to support analytical reporting and decision-making. A star schema is used to organize historical sales data efficiently, enabling fast aggregation, drill-down, and trend analysis. The implementation includes dimension tables, a fact table, sample warehouse data, and analytical SQL queries.

## Objectives

- Design a star schema suitable for analytical workloads

- Populate dimension and fact tables with realistic data

- Support time-based, product-based, and customer-based analysis

- Write OLAP queries for business insights

- Demonstrate understanding of dimensional modeling concepts

## Star Schema Overview

The warehouse uses one fact table connected to three dimension tables.

### Fact Table

__fact_sales__

Represents sales transactions at the line-item level.

Measures:

- quantity_sold
- unit_price
- discount_amount
- total_amount

Foreign Keys:

- date_key → dim_date

- product_key → dim_product

- customer_key → dim_customer

### Dimension Tables
__dim_date__

Stores calendar-related attributes used for time analysis.

Attributes include:

- date_key (YYYYMMDD)
- full_date
- day_of_week
- day_of_month
- month
- month_name
- quarter
- year
- is_weekend

Used for yearly, quarterly, monthly, and weekday analysis.

__dim_product__

Stores product descriptive information.

Attributes:

- product_id
- product_name
- category
- subcategory
- unit_price

Used to analyze product and category performance.

__dim_customer__

Stores customer-related details.

Attributes:

- customer_id
- customer_name
- city
- state
- customer_segment

Used for customer segmentation and regional analysis.

## Data Population Summary

The warehouse is populated using SQL scripts with realistic sample data:

- dim_date → 30 records (January–February 2024)

- dim_product → 15 products across multiple categories

- dim_customer → 12 customers from different cities and states

- fact_sales → 40 sales transactions

Data characteristics:

- Includes weekday and weekend sales
- Prices range from ₹100 to ₹100,000
- Varying quantities and discounts
- All foreign key constraints satisfied

## OLAP Analytics Queries

The project includes analytical SQL queries that demonstrate business intelligence use cases.

### 1. Monthly Sales Drill-Down

Analyzes sales performance by:

- Year
- Quarter
- Month

Shows:

- year 
- quarter 
- month_name 
- Total sales
- Total quantity sold

Used to demonstrate drill-down analysis.

### 2. Product Performance Analysis

Identifies top-performing products using:

- Total revenue
- Units sold
- Revenue contribution percentage

Uses:

- JOINs
- Aggregations
- Window functions

### 3. Customer Segmentation Analysis

Segments customers into:

- High Value (> ₹50,000)
- Medium Value (₹20,000–₹50,000)
- Low Value (< ₹20,000)

Displays:

- Customer count
- Total revenue
- Average revenue per customer

Uses:

- CASE statements
- GROUP BY
- Aggregations

Files Included
Part_3/
├── README.md
├── warehouse_schema.sql
├── warehouse_data.sql
├── analytics_queries.sql

### Key Learning Outcomes

- Understanding of star schema design
- Use of surrogate keys in data warehouses
- Difference between OLTP and OLAP systems
- Implementation of dimensional modeling
- Writing advanced SQL analytics queries
- Applying business logic to data analysis

### Conclusion

Part 3 demonstrates the complete process of building a data warehouse for analytical purposes. By designing a star schema, loading structured data, and executing OLAP queries, the solution enables efficient reporting and supports business decision-making. This implementation reflects real-world data warehousing practices used in enterprise analytics systems.