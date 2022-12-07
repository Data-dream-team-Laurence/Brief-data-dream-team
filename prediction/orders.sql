ALTER TABLE `Customers` DROP customer_unique_id, customer_city, customer_state;

ALTER TABLE `Geolocations` DROP geolocation_lat, geolocation_lng;

ALTER TABLE `Products` DROP product_name_lenght, product_description_lenght, product_photos_qty;

ALTER TABLE `Reviews` DROP review_comment_title, review_comment_message, review_creation_date, review_answer_timestamp;

ALTER TABLE `Sellers` DROP seller_city, seller_state;

DELETE FROM `Orders` WHERE NOT order_status = "delivered";