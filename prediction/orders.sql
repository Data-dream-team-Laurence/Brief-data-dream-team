DELETE FROM `Orders` WHERE NOT order_status = "delivered";

CREATE TABLE `Customers_Duplicate` AS SELECT DISTINCT customer_id, customer_zip_code_prefix FROM `Customers`;
DROP TABLE `Customers`;
ALTER TABLE `Customers_Duplicate` RENAME TO `Customers`;

CREATE TABLE `Geolocations_Duplicate` AS SELECT DISTINCT geolocation_zip_code_prefix, geolocation_lat, geolocation_lng, geolocation_city, geolocation_state FROM `Geolocations`;
DROP TABLE `Geolocations`;
ALTER TABLE `Geolocations_Duplicate` RENAME TO `Geolocations`;

CREATE TABLE `Items_Duplicate` AS SELECT DISTINCT order_id, order_item_id, product_id, seller_id, shipping_limit_date, price, freight_value FROM `Items`;
DROP TABLE `Items`;
ALTER TABLE `Items_Duplicate` RENAME TO `Items`;

CREATE TABLE `Orders_Duplicate` AS SELECT DISTINCT order_id, customer_id, order_purchase_timestamp, order_approved_at, order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delivery_date FROM `Orders`;
DROP TABLE `Orders`;
ALTER TABLE `Orders_Duplicate` RENAME TO `Orders`;

CREATE TABLE `Payments_Duplicate` AS SELECT DISTINCT order_id, payment_sequential, payment_type, payment_installments, payment_value FROM `Payments`;
DROP TABLE `Payments`;
ALTER TABLE `Payments_Duplicate` RENAME TO `Payments`;

CREATE TABLE `Products_Duplicate` AS SELECT DISTINCT product_id, product_category_name, product_weight_g, product_length_cm, product_height_cm, product_width_cm FROM `Products`;
DROP TABLE `Products`;
ALTER TABLE `Products_Duplicate` RENAME TO `Products`;

CREATE TABLE `Reviews_Duplicate` AS SELECT DISTINCT review_id, order_id, review_score FROM `Reviews`;
DROP TABLE `Reviews`;
ALTER TABLE `Reviews_Duplicate` RENAME TO `Reviews`;

CREATE TABLE `Sellers_Duplicate` AS SELECT DISTINCT seller_id, seller_zip_code_prefix FROM `Sellers`;
DROP TABLE `Sellers`;
ALTER TABLE `Sellers_Duplicate` RENAME TO `Sellers`;