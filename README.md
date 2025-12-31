# FlexiMart Data Architecture Project

**Student Name:** [Riddhi Parmar]
**Student ID:** [25071184]
**Email:** [parmarriddhi1997@gmail.com]
**Date:** [31 Dec 2025]

## Project Overview

This project demonstrates the complete design and implementation of a data architecture solution for FlexiMart, covering transactional databases, ETL pipelines, NoSQL modeling, and data warehousing. The system cleans and loads raw CSV data into a relational database, performs analytical queries, explores NoSQL capabilities using MongoDB, and builds a star-schema-based data warehouse for business intelligence reporting.

The project is divided into three major parts: ETL & relational modeling, NoSQL analysis, and data warehouse analytics, showcasing real-world data engineering concepts and best practices.

## Repository Structure
├── part1-database-etl/
│   ├── etl_pipeline.py
│   ├── schema_documentation.md
│   ├── business_queries.sql
│   └── data_quality_report.txt
├── part2-nosql/
│   ├── nosql_analysis.md
│   ├── mongodb_operations.js
│   └── products_catalog.json
├── part3-datawarehouse/
│   ├── star_schema_design.md
│   ├── warehouse_schema.sql
│   ├── warehouse_data.sql
│   └── analytics_queries.sql
└── README.md

## Technologies Used

- Python 3.x
  - pandas
  - mysql-connector-python
- MySQL 8.0 (Relational Database & Data Warehouse)
- MongoDB 6.0 (NoSQL Database)
- JavaScript (MongoDB shell)
- CSV/JSON

## Setup Instructions

### Database Setup

```bash
# Create databases
mysql -u root -p -e "CREATE DATABASE fleximart;"
mysql -u root -p -e "CREATE DATABASE fleximart_dw;"

# Run Part 1 - ETL Pipeline
python part1-database-etl/etl_pipeline.py

# Run Part 1 - Business Queries
mysql -u root -p fleximart < part1-database-etl/business_queries.sql

# Run Part 3 - Data Warehouse
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_schema.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_data.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/analytics_queries.sql


### MongoDB Setup (part 2)

mongosh < part2-nosql/mongodb_operations.js

## Key Learnings

- Designed and implemented an end-to-end ETL pipeline

- Applied data cleaning and validation techniques

- Built normalized and dimensional database models

- Understood differences between OLTP and OLAP systems

- Implemented MongoDB document-based modeling

- Wrote advanced SQL queries using GROUP BY, CASE, and window functions

- Learned how data warehouses support business decision-making

## Challenges Faced

1. Handling inconsistent and missing raw data
  → Solved by standardizing formats, replacing nulls, and validating before loading.

2. Foreign key constraint errors during warehouse loading
  → Fixed by inserting dimension data before fact data and validating key references.

3. MongoDB setup and command-line execution issues
  → Resolved by installing MongoDB tools correctly and using mongosh.

4. Designing realistic analytical datasets
  → Addressed by modeling real-world sales patterns and controlled distributions.


