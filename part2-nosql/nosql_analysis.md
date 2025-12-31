# NoSQL Analysis for FlexiMart
## Part 2: NoSQL Database Analysis
### Section A: Limitations of RDBMS

Relational databases such as MySQL work best when data follows a fixed and well-defined schema. However, in a product catalog like FlexiMart’s, different product types often have very different attributes. For example, laptops may require fields such as RAM, processor, and storage, while shoes need size, color, and material. Representing these variations in a relational model requires either adding many nullable columns or creating multiple auxiliary tables, both of which increase complexity.

Frequent schema changes also become difficult in relational systems. Adding new product attributes requires altering table structures, which can be costly and disruptive for large datasets. Additionally, storing nested or hierarchical data such as customer reviews, ratings, and comments is inefficient in RDBMS because it requires multiple related tables and joins.

These limitations make relational databases less flexible and harder to scale when managing highly diverse and evolving product data.

### Section B: Benefits of Using MongoDB 

MongoDB addresses these limitations by using a flexible, document-based data model. Each product is stored as a JSON-like document, allowing different products to have different attributes without modifying the overall schema. For example, a laptop document can include RAM and processor fields, while a shoe document can include size and color fields.

MongoDB also supports embedded documents, which makes it ideal for storing customer reviews directly inside the product document. This avoids expensive joins and improves read performance when retrieving complete product information.

In addition, MongoDB supports horizontal scalability through sharding, allowing data to be distributed across multiple servers. This makes it suitable for large and rapidly growing product catalogs. Its schema flexibility and scalability enable faster development, easier evolution of product models, and better performance for read-heavy applications.

### Section C: Trade-offs of Using MongoDB

Despite its flexibility, MongoDB has some disadvantages compared to relational databases. First, it does not enforce strong relational constraints such as foreign keys, which can lead to data inconsistency if not carefully managed at the application level. Second, complex transactions involving multiple collections are more difficult to manage and may not be as efficient as in MySQL, especially when strong ACID guarantees are required. Additionally, performing complex analytical queries with joins and aggregations can be more challenging and less optimized compared to SQL-based systems. Therefore, MongoDB is best suited for flexible and scalable data models, while relational databases remain preferable for transactional consistency.