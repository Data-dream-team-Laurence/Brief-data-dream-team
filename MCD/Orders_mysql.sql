CREATE DATABASE IF NOT EXISTS `ORDERS` DEFAULT CHARACTER SET UTF8MB4 COLLATE utf8_general_ci;
USE `ORDERS`;

CREATE TABLE `CUSTOMERS` (
  `customer_id` VARCHAR(42),
  `customer_unique_id` VARCHAR(42),
  `customer_zip_code_prefix` VARCHAR(42),
  `customer_city` VARCHAR(42),
  `customer_state` VARCHAR(42),
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `GEOLOCATION` (
  `id_geolocation` VARCHAR(42),
  `geolocation_zip_code_prefix` VARCHAR(42),
  `geolocation_lat` VARCHAR(42),
  `geolocation_ing` VARCHAR(42),
  `geolocation_city` VARCHAR(42),
  `geolocation_state` VARCHAR(42),
  PRIMARY KEY (`id_geolocation`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `ITEMS` (
  `id_items` VARCHAR(42),
  `order_id` VARCHAR(42),
  `order_item_id` VARCHAR(42),
  `product_id` VARCHAR(42),
  `seller_id` VARCHAR(42),
  `shipping_limit_date` VARCHAR(42),
  `price` VARCHAR(42),
  `freight_value` VARCHAR(42),
  PRIMARY KEY (`id_items`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `ORDER` (
  `order_id` VARCHAR(42),
  `customer_id` VARCHAR(42),
  `order_status` VARCHAR(42),
  `order_purchase_timestamp` VARCHAR(42),
  `order_approved_at` VARCHAR(42),
  `order_delivered_carrier_date` VARCHAR(42),
  `order_delivered_customer_date` VARCHAR(42),
  `order_estimated_delivery_date` VARCHAR(42),
  `seller_id` VARCHAR(42),
  `id_geolocation` VARCHAR(42),
  `customer_id_1` VARCHAR(42),
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `PAYMENTS` (
  `id_payments` VARCHAR(42),
  `order_id` VARCHAR(42),
  `payment_sequential` VARCHAR(42),
  `payment_type` VARCHAR(42),
  `payment_installments` VARCHAR(42),
  `payment_value` VARCHAR(42),
  PRIMARY KEY (`id_payments`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `PRODUCT` (
  `product_id` VARCHAR(42),
  `product_category_name` VARCHAR(42),
  `product_name_lenght` VARCHAR(42),
  `product_description_lenght` VARCHAR(42),
  `product_photos_qty` VARCHAR(42),
  `product_weight_g` VARCHAR(42),
  `product_lenght_cm` VARCHAR(42),
  `product_height_cm` VARCHAR(42),
  `product_width_cm` VARCHAR(42),
  `id_items` VARCHAR(42),
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `REVIEWS` (
  `review_unique_id` VARCHAR(42),
  `review_id` VARCHAR(42),
  `order_id` VARCHAR(42),
  `review_score` VARCHAR(42),
  `review_comment_title` VARCHAR(42),
  `review_comment_message` VARCHAR(42),
  `review_creation_date` VARCHAR(42),
  `review_answer_timestamp` VARCHAR(42),
  PRIMARY KEY (`review_unique_id`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `SELLERS` (
  `seller_id` VARCHAR(42),
  `seller_zip_code_prefix` VARCHAR(42),
  `seller_city` VARCHAR(42),
  `seller_state` VARCHAR(42),
  PRIMARY KEY (`seller_id`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `TRANSLATE` (
  `id_translate` VARCHAR(42),
  `product_category_name` VARCHAR(42),
  `product_category_name_english` VARCHAR(42),
  PRIMARY KEY (`id_translate`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `ACHETE` (
  `id_payments` VARCHAR(42),
  `order_id` VARCHAR(42),
  `order_id_1` VARCHAR(42),
  `id_payments_1` VARCHAR(42),
  PRIMARY KEY (`id_payments`, `order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `APPARTIENT` (
  `order_id` VARCHAR(42),
  `id_items` VARCHAR(42),
  `id_items_1` VARCHAR(42),
  `order_id_1` VARCHAR(42),
  PRIMARY KEY (`order_id`, `id_items`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `COMMENTE` (
  `review_unique_id` VARCHAR(42),
  `order_id` VARCHAR(42),
  `order_id_1` VARCHAR(42),
  `review_unique_id_1` VARCHAR(42),
  PRIMARY KEY (`review_unique_id`, `order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

ALTER TABLE `ORDER` ADD FOREIGN KEY (`customer_id_1`) REFERENCES `CUSTOMERS` (`customer_id`);
ALTER TABLE `ORDER` ADD FOREIGN KEY (`id_geolocation`) REFERENCES `GEOLOCATION` (`id_geolocation`);
ALTER TABLE `ORDER` ADD FOREIGN KEY (`seller_id`) REFERENCES `SELLERS` (`seller_id`);
ALTER TABLE `PRODUCT` ADD FOREIGN KEY (`id_items`) REFERENCES `ITEMS` (`id_items`);
ALTER TABLE `ACHETE` ADD FOREIGN KEY (`order_id`) REFERENCES `ORDER` (`order_id`);
ALTER TABLE `ACHETE` ADD FOREIGN KEY (`id_payments`) REFERENCES `PAYMENTS` (`id_payments`);
ALTER TABLE `APPARTIENT` ADD FOREIGN KEY (`id_items`) REFERENCES `ITEMS` (`id_items`);
ALTER TABLE `APPARTIENT` ADD FOREIGN KEY (`order_id`) REFERENCES `ORDER` (`order_id`);
ALTER TABLE `COMMENTE` ADD FOREIGN KEY (`order_id`) REFERENCES `ORDER` (`order_id`);
ALTER TABLE `COMMENTE` ADD FOREIGN KEY (`review_unique_id`) REFERENCES `REVIEWS` (`review_unique_id`);