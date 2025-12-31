INSERT INTO dim_date
(date_key, full_date, day_of_week, day_of_month, month, month_name, quarter, year, is_weekend)
VALUES
(20240101,'2024-01-01','Monday',1,1,'January','Q1',2024,false),
(20240102,'2024-01-02','Tuesday',2,1,'January','Q1',2024,false),
(20240103,'2024-01-03','Wednesday',3,1,'January','Q1',2024,false),
(20240104,'2024-01-04','Thursday',4,1,'January','Q1',2024,false),
(20240105,'2024-01-05','Friday',5,1,'January','Q1',2024,false),
(20240106,'2024-01-06','Saturday',6,1,'January','Q1',2024,true),
(20240107,'2024-01-07','Sunday',7,1,'January','Q1',2024,true),
(20240108,'2024-01-08','Monday',8,1,'January','Q1',2024,false),
(20240109,'2024-01-09','Tuesday',9,1,'January','Q1',2024,false),
(20240110,'2024-01-10','Wednesday',10,1,'January','Q1',2024,false),
(20240111,'2024-01-11','Thursday',11,1,'January','Q1',2024,false),
(20240112,'2024-01-12','Friday',12,1,'January','Q1',2024,false),
(20240113,'2024-01-13','Saturday',13,1,'January','Q1',2024,true),
(20240114,'2024-01-14','Sunday',14,1,'January','Q1',2024,true),
(20240115,'2024-01-15','Monday',15,1,'January','Q1',2024,false),

(20240201,'2024-02-01','Thursday',1,2,'February','Q1',2024,false),
(20240202,'2024-02-02','Friday',2,2,'February','Q1',2024,false),
(20240203,'2024-02-03','Saturday',3,2,'February','Q1',2024,true),
(20240204,'2024-02-04','Sunday',4,2,'February','Q1',2024,true),
(20240205,'2024-02-05','Monday',5,2,'February','Q1',2024,false),
(20240206,'2024-02-06','Tuesday',6,2,'February','Q1',2024,false),
(20240207,'2024-02-07','Wednesday',7,2,'February','Q1',2024,false),
(20240208,'2024-02-08','Thursday',8,2,'February','Q1',2024,false),
(20240209,'2024-02-09','Friday',9,2,'February','Q1',2024,false),
(20240210,'2024-02-10','Saturday',10,2,'February','Q1',2024,true),
(20240211,'2024-02-11','Sunday',11,2,'February','Q1',2024,true),
(20240212,'2024-02-12','Monday',12,2,'February','Q1',2024,false),
(20240213,'2024-02-13','Tuesday',13,2,'February','Q1',2024,false),
(20240214,'2024-02-14','Wednesday',14,2,'February','Q1',2024,false),
(20240215,'2024-02-15','Thursday',15,2,'February','Q1',2024,false);

INSERT INTO dim_product 
(product_id, product_name, category, subcategory, unit_price) 
VALUES
('P001','Laptop','Electronics','Computers',55000),
('P002','Smartphone','Electronics','Mobiles',30000),
('P003','Tablet','Electronics','Tablets',25000),
('P004','Headphones','Electronics','Accessories',3000),
('P005','Smart TV','Electronics','Television',45000),

('P006','Jeans','Fashion','Clothing',2500),
('P007','T-Shirt','Fashion','Clothing',1200),
('P008','Jacket','Fashion','Outerwear',4500),
('P009','Shoes','Fashion','Footwear',3500),
('P010','Cap','Fashion','Accessories',800),

('P011','Rice 5kg','Groceries','Grains',600),
('P012','Wheat Flour','Groceries','Grains',450),
('P013','Cooking Oil','Groceries','Essentials',1200),
('P014','Sugar','Groceries','Essentials',300),
('P015','Tea Pack','Groceries','Beverages',550);

INSERT INTO dim_customer
(customer_id, customer_name, city, state, customer_segment)
VALUES
('C001', 'Rahul Sharma',   'Mumbai',      'Maharashtra', 'Retail'),
('C002', 'Amit Verma',     'Delhi',       'Delhi',       'Corporate'),
('C003', 'Neha Singh',     'Pune',        'Maharashtra', 'Retail'),
('C004', 'Riya Patel',     'Ahmedabad',   'Gujarat',     'Retail'),

('C005', 'Arjun Mehta',    'Bengaluru',    'Karnataka',   'Online'),
('C006', 'Karan Malhotra', 'Delhi',       'Delhi',       'Corporate'),
('C007', 'Sneha Iyer',     'Chennai',     'Tamil Nadu',  'Retail'),

('C008', 'Vikram Rao',     'Hyderabad',   'Telangana',   'Online'),
('C009', 'Pooja Nair',     'Kochi',       'Kerala',      'Retail'),

('C010', 'Aditya Jain',    'Jaipur',       'Rajasthan',  'Corporate'),
('C011', 'Nisha Kulkarni', 'Nagpur',       'Maharashtra','Retail'),
('C012', 'Rohit Kapoor',   'Noida',        'Uttar Pradesh','Online');


INSERT INTO fact_sales
(date_key, product_key, customer_key, quantity_sold, unit_price, discount_amount, total_amount)
VALUES
(20240101,1,1,1,55000,0,55000),
(20240102,2,2,2,30000,2000,58000),
(20240103,3,3,1,25000,0,25000),
(20240104,4,4,3,3000,0,9000),
(20240105,5,5,1,45000,5000,40000),

(20240106,6,6,4,2500,0,10000),
(20240107,7,7,5,1200,0,6000),
(20240108,8,8,2,4500,500,8500),
(20240109,9,9,3,3500,0,10500),
(20240110,10,10,4,800,0,3200),

(20240201,11,11,10,600,0,6000),
(20240202,12,12,5,450,0,2250),
(20240203,13,1,3,1200,0,3600),
(20240204,14,2,6,300,0,1800),
(20240205,15,3,4,550,0,2200),

(20240206,1,4,1,55000,2000,53000),
(20240207,2,5,2,30000,0,60000),
(20240208,3,6,1,25000,0,25000),
(20240209,4,7,3,3000,0,9000),
(20240210,5,8,1,45000,3000,42000),

(20240106,6,9,2,2500,0,5000),
(20240107,7,10,3,1200,0,3600),
(20240108,8,11,1,4500,0,4500),
(20240109,9,12,2,3500,0,7000),
(20240110,10,1,4,800,0,3200),

(20240201,11,2,6,600,0,3600),
(20240202,12,3,4,450,0,1800),
(20240203,13,4,5,1200,0,6000),
(20240204,14,5,6,300,0,1800),
(20240205,15,6,3,550,0,1650),

(20240206,1,7,1,55000,5000,50000),
(20240207,2,8,1,30000,0,30000),
(20240208,3,9,2,25000,0,50000),
(20240209,4,10,4,3000,0,12000),
(20240210,5,11,1,45000,2000,43000),

(20240120,3,2,2,24999,1000,48998),
(20240121,5,4,1,8999,0,8999),
(20240122,7,6,3,1200,150,3450),
(20240125,10,8,1,45999,2000,43999),
(20240202,12,10,2,3499,0,6998);