# Part 2: NoSQL Database Analysis – Overview

## Introduction
This part focuses on evaluating the suitability of a NoSQL database (MongoDB) for managing FlexiMart’s expanding and diverse product catalog. As product attributes vary across categories and evolve frequently, a document-based database provides better flexibility compared to traditional relational databases.

Part 2 is divided into two main tasks:
- **Task 2.1:** NoSQL justification and theoretical analysis  
- **Task 2.2:** Practical MongoDB implementation using sample product data  

---

## Objectives

The main objectives of Part 2 are:

- Understand the limitations of relational databases when handling highly flexible product data
- Explain how MongoDB overcomes these limitations
- Work with document-based data structures
- Perform basic MongoDB CRUD and aggregation operations
- Analyze product data using NoSQL queries

---

## Tools & Technologies Used

- **Database:** MongoDB
- **Query Language:** MongoDB Query Language (MQL)
- **Shell:** mongosh
- **Data Format:** JSON
- **Files Used:**
  - `products_catalog.json`
  - `mongodb_operations.js`
  - `nosql_analysis.md`

---

## Task 2.1: NoSQL Justification (Theory)

This task explains:
- Why relational databases struggle with flexible product attributes
- How MongoDB supports schema-less design
- Use of embedded documents for reviews
- Horizontal scalability using collections
- Trade-offs of using MongoDB instead of MySQL

The explanation is provided in the file: __nosql_analysis.md__


---

## Task 2.2: MongoDB Implementation (Practical)

This task demonstrates basic MongoDB operations using real product data.

### Operations Implemented

1. **Load Data**
   - Import `products_catalog.json` into MongoDB collection `products`
   - Database used: `fleximart`

2. **Basic Query**
   - Fetch all products in the *Electronics* category
   - Filter products with price < 50000
   - Return only name, price, and stock

3. **Review Analysis**
   - Calculate average rating for each product
   - Return only products with average rating ≥ 4.0

4. **Update Operation**
   - Add a new review to product `ELEC001`
   - Review includes user, rating, comment, and date

5. **Complex Aggregation**
   - Compute average price by category
   - Count total products per category
   - Sort results by average price (descending)

All MongoDB commands are written in:
 __mongodb_operations.js__