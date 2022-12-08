DROP TABLE IF EXISTS "Customers";
DROP TABLE IF EXISTS "Items";
DROP TABLE IF EXISTS "Products";
DROP TABLE IF EXISTS "Geolocations";
DROP TABLE IF EXISTS "Orders";
DROP TABLE IF EXISTS "Payments";
DROP TABLE IF EXISTS "Reviews";
DROP TABLE IF EXISTS "Sellers";

CREATE TABLE IF NOT EXISTS "Customers" (
  "customer_id" VARCHAR(50),
  "customer_unique_id" VARCHAR(50),
  "customer_zip_code_prefix" INTEGER(50),
  "customer_city" VARCHAR(50),
  "customer_state" VARCHAR(50),
  PRIMARY KEY ("customer_id")
);

CREATE TABLE IF NOT EXISTS "Geolocations" (
  "id_geolocation" INTEGER PRIMARY KEY AUTOINCREMENT,
  "geolocation_zip_code_prefix" INTEGER(50),
  "geolocation_lat" float,
  "geolocation_lng" float,
  "geolocation_city" VARCHAR(50),
  "geolocation_state" VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS "Items" (
  "id_items" INTEGER PRIMARY KEY AUTOINCREMENT,
  "order_id" VARCHAR(50),
  "order_item_id" INTEGER,
  "product_id" VARCHAR(50),
  "seller_id" VARCHAR(50),
  "shipping_limit_date" DATETIME,
  "price" float,
  "freight_value" float
);

CREATE TABLE IF NOT EXISTS "Orders" (
  "order_id" VARCHAR(42),
  "customer_id" VARCHAR(42),
  "order_status" VARCHAR(42),
  "order_purchase_timestamp" DATETIME,
  "order_approved_at" DATETIME,
  "order_delivered_carrier_date" DATETIME,
  "order_delivered_customer_date" DATETIME,
  "order_estimated_delivery_date" DATETIME,
  PRIMARY KEY ("order_id")
);

CREATE TABLE IF NOT EXISTS "Payments" (
  "id_payments" INTEGER PRIMARY KEY AUTOINCREMENT,
  "order_id" VARCHAR(50),
  "payment_sequential" INTEGER,
  "payment_type" VARCHAR(50),
  "payment_installments" INTEGER,
  "payment_value" float
);

CREATE TABLE IF NOT EXISTS "Products" (
  "product_id" VARCHAR(50),
  "product_category_name" VARCHAR(50),
  "product_name_lenght" float,
  "product_description_lenght" float,
  "product_photos_qty" float,
  "product_weight_g" float,
  "product_length_cm" float,
  "product_height_cm" float,
  "product_width_cm" float,
  PRIMARY KEY ("product_id")
);

CREATE TABLE IF NOT EXISTS "Reviews" (
  "review_unique_id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "review_id" VARCHAR(50),
  "order_id" VARCHAR(50),
  "review_score" INTEGER,
  "review_comment_title" VARCHAR(50),
  "review_comment_message" VARCHAR(50),
  "review_creation_date" DATETIME,
  "review_answer_timestamp" DATETIME
);

CREATE TABLE IF NOT EXISTS "Sellers" (
  "seller_id" VARCHAR(50),
  "seller_zip_code_prefix" INTEGER,
  "seller_city" VARCHAR(50),
  "seller_state" VARCHAR(50),
  PRIMARY KEY ("seller_id")
);