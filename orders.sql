DROP TABLE IF EXISTS "Customers";
DROP TABLE IF EXISTS "Items";
DROP TABLE IF EXISTS "Products";
DROP TABLE IF EXISTS "Geolocation";
DROP TABLE IF EXISTS "Orders";
DROP TABLE IF EXISTS "Payments";
DROP TABLE IF EXISTS "Reviews";
DROP TABLE IF EXISTS "Sellers";

CREATE TABLE IF NOT EXISTS "Customers" (
  "customer_id" VARCHAR(42),
  "customer_unique_id" VARCHAR(42),
  "customer_zip_code_prefix" VARCHAR(42),
  "customer_city" VARCHAR(42),
  "customer_state" VARCHAR(42),
  PRIMARY KEY ("customer_id")
);

CREATE TABLE IF NOT EXISTS "Geolocation" (
  "id_geolocation" VARCHAR(42),
  "geolocation_zip_code_prefix" VARCHAR(42),
  "geolocation_lat" VARCHAR(42),
  "geolocation_lng" VARCHAR(42),
  "geolocation_city" VARCHAR(42),
  "geolocation_state" VARCHAR(42),
  PRIMARY KEY ("id_geolocation")
);

CREATE TABLE IF NOT EXISTS "Items" (
  "id_items" VARCHAR(42),
  "order_id" VARCHAR(42),
  "order_item_id" VARCHAR(42),
  "product_id" VARCHAR(42),
  "seller_id" VARCHAR(42),
  "shipping_limit_date" DATETIME,
  "price" VARCHAR(42),
  "freight_value" VARCHAR(42),
  PRIMARY KEY ("id_items")
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
  "id_payments" VARCHAR(42),
  "order_id" VARCHAR(42),
  "payment_sequential" VARCHAR(42),
  "payment_type" VARCHAR(42),
  "payment_installments" VARCHAR(42),
  "payment_value" VARCHAR(42),
  PRIMARY KEY ("id_payments")
);

CREATE TABLE IF NOT EXISTS "Products" (
  "product_id" VARCHAR(42),
  "product_category_name" VARCHAR(42),
  "product_name_lenght" VARCHAR(42),
  "product_description_lenght" VARCHAR(42),
  "product_photos_qty" VARCHAR(42),
  "product_weight_g" VARCHAR(42),
  "product_length_cm" VARCHAR(42),
  "product_height_cm" VARCHAR(42),
  "product_width_cm" VARCHAR(42),
  PRIMARY KEY ("product_id")
);

CREATE TABLE IF NOT EXISTS "Reviews" (
  "review_unique_id" VARCHAR(42),
  "review_id" VARCHAR(42),
  "order_id" VARCHAR(42),
  "review_score" VARCHAR(42),
  "review_comment_title" VARCHAR(42),
  "review_comment_message" VARCHAR(42),
  "review_creation_date" DATETIME,
  "review_answer_timestamp" DATETIME,
  PRIMARY KEY ("review_unique_id")
);

CREATE TABLE IF NOT EXISTS "Sellers" (
  "seller_id" VARCHAR(42),
  "seller_zip_code_prefix" VARCHAR(42),
  "seller_city" VARCHAR(42),
  "seller_state" VARCHAR(42),
  PRIMARY KEY ("seller_id")
);
