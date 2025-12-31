# Star Schema Design – FlexiMart Data Warehouse

## Section 1: Schema Overview

The FlexiMart data warehouse uses a **star schema** to support analytical reporting on historical sales data.  
The schema contains one central **fact table (`fact_sales`)** connected to three **dimension tables**: `dim_date`, `dim_product`, and `dim_customer`.

---

## FACT TABLE: fact_sales

**Business Process:** Sales transactions  
**Grain:** One row per product per order line item  

Each row represents the sale of a single product to a customer on a specific date.

### Measures (Numeric Facts)
- **quantity_sold** – Number of units sold
- **unit_price** – Selling price per unit
- **discount_amount** – Discount applied on the item
- **total_amount** – Final amount after discount  
  *(quantity_sold × unit_price − discount_amount)*

### Foreign Keys
- **date_key → dim_date**
- **product_key → dim_product**
- **customer_key → dim_customer**

---

## DIMENSION TABLES

### DIMENSION: dim_date

**Purpose:**  
Supports time-based analysis such as daily, monthly, quarterly, and yearly reporting.

**Attributes:**
- **date_key (PK):** Surrogate key in YYYYMMDD format  
- **full_date:** Actual calendar date  
- **day_of_week:** Name of the day (Monday–Sunday)  
- **day_of_month:** Day number in the month  
- **month:** Month number (1–12)  
- **month_name:** Month name (January–December)  
- **quarter:** Quarter of the year (Q1–Q4)  
- **year:** Calendar year  
- **is_weekend:** Boolean flag indicating weekend  

---

### DIMENSION: dim_product

**Purpose:**  
Stores descriptive information about products for category-level and product-level analysis.

**Attributes:**
- **product_key (PK):** Surrogate key  
- **product_id:** Business product identifier  
- **product_name:** Name of the product  
- **category:** Product category (e.g., Electronics, Fashion)  
- **subcategory:** More detailed product classification  
- **unit_price:** Standard selling price  

---

### DIMENSION: dim_customer

**Purpose:**  
Stores customer-related attributes used for demographic and behavioral analysis.

**Attributes:**
- **customer_key (PK):** Surrogate key  
- **customer_id:** Business customer identifier  
- **customer_name:** Full customer name  
- **city:** Customer city  
- **state:** Customer state  
- **customer_segment:** Segment such as Retail, Corporate, or Online  

---

## Section 2: Design Decisions

The star schema uses **transaction-level granularity**, meaning each record in the fact table represents a single product sold in a transaction. This level of detail enables flexible analysis such as daily sales trends, customer purchasing behavior, and product-level performance.

**Surrogate keys** are used instead of natural keys to improve performance, ensure uniqueness, and avoid dependency on business identifiers that may change over time. They also simplify joins between fact and dimension tables.

This schema supports **drill-down and roll-up operations** efficiently. Analysts can roll up sales from daily to monthly or yearly levels using the date dimension, or drill down from category-level sales to individual products. Similarly, customer segmentation and regional analysis are enabled through the customer dimension. The separation of facts and descriptive attributes improves query performance, scalability, and maintainability, making the design suitable for long-term analytical workloads.

---

## Section 3: Sample Data Flow

### Source Transaction (OLTP System)

Order ID: 101  
Customer: John Doe  
Product: Laptop  
Quantity: 2  
Unit Price: 50,000  
Order Date: 2024-01-15  

---

### Transformed Records in Data Warehouse

### fact_sales
{
  "date_key": 20240115,
  "product_key": 5,
  "customer_key": 12,
  "quantity_sold": 2,
  "unit_price": 50000,
  "discount_amount": 0,
  "total_amount": 100000
}

### dim_date
{
  "date_key": 20240115,
  "full_date": "2024-01-15",
  "day_of_week": "Monday",
  "day_of_month": 15,
  "month": 1,
  "month_name": "January",
  "quarter": "Q1",
  "year": 2024,
  "is_weekend": false
}

### dim_product
{
  "product_key": 5,
  "product_id": "P005",
  "product_name": "Laptop",
  "category": "Electronics",
  "subcategory": "Computers",
  "unit_price": 50000
}

### dim_customer
{
  "customer_key": 12,
  "customer_id": "C012",
  "customer_name": "John Doe",
  "city": "Mumbai",
  "state": "Maharashtra",
  "customer_segment": "Retail"
}
