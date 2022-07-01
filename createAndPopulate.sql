
DROP TABLE IF EXISTS `Transaction`;
DROP TABLE IF EXISTS `Order_item`;
DROP TABLE IF EXISTS `Order`;
DROP TABLE IF EXISTS `User`;
DROP TABLE IF EXISTS `Product`;

CREATE TABLE `User` (
	`user_id` INT(10) NOT NULL AUTO_INCREMENT,
	`first_name` varchar(30) NOT NULL,
	`last_name` varchar(50) NOT NULL,
	`email` varchar(100) NOT NULL UNIQUE,
	`address` varchar(200) NOT NULL,
	`city` varchar(100) NOT NULL,
	`telephone` varchar(10) NOT NULL,
	PRIMARY KEY (`user_id`)
);

CREATE TABLE `Product` (
	`product_id` INT(10) NOT NULL AUTO_INCREMENT,
	`name` varchar(100) NOT NULL,
	`description` TEXT,
	`price` DECIMAL(10) NOT NULL,
	`cost` DECIMAL(10) NOT NULL,
	`stock` INT(10) NOT NULL,
	`size` varchar(10) NOT NULL,
	`category` ENUM('Shoes', 'Hats', 'T-Shirts', 'Shorts', 'Equipment') NOT NULL,
	PRIMARY KEY (`product_id`)
);

CREATE TABLE `Order` (
	`user_id` INT(10) NOT NULL,
	`order_id` INT(10) NOT NULL AUTO_INCREMENT,
	`date` DATETIME NOT NULL,
	PRIMARY KEY (`order_id`),
	FOREIGN KEY (`user_id`) REFERENCES `User`(`user_id`) ON DELETE CASCADE
);

CREATE TABLE `Order_item` (
	`product_id` INT(10) NOT NULL,
	`order_id` INT NOT NULL,
	`quantity` INT NOT NULL,
	PRIMARY KEY (`product_id`, `order_id`),
	FOREIGN KEY (`product_id`) REFERENCES `Product`(`product_id`) ON DELETE CASCADE,
	FOREIGN KEY (`order_id`) REFERENCES `Order`(`order_id`) ON DELETE CASCADE
);

CREATE TABLE `Transaction` (
	`transaction_id` INT(10) NOT NULL AUTO_INCREMENT,
	`order_id` INT(10) NOT NULL,
	`amount` DECIMAL(10) NOT NULL,
	PRIMARY KEY (`transaction_id`),
	FOREIGN KEY (`order_id`) REFERENCES `Order`(`order_id`) ON DELETE CASCADE
);


/*POPULATE */

INSERT INTO `User` (`user_id`, `first_name`, `last_name`, `email`, `address`, `city`, `telephone`) VALUES
(1, 'Giorgos', 'Dimitriadis', 'dimitriadisg@gmail.com', 'Michalakopoulou 123', 'Athens', '6913141567'),
(2, 'John', 'Mayer', 'mayerjohn@gmail.com', 'Patreos 43', 'Patra', '6988866666'),
(3, 'Anna', 'Michailidou', 'mich_anna@gmail.com', 'Ioanninon 7', 'Patra', '6944467678'),
(4, 'Anja', 'Bugel', 'bugelanja@gmail.com', 'Zalogou 77', 'Thessaloniki', '6977788222');

INSERT INTO `Product` (`product_id`, `name`, `description`, `price`, `cost`, `stock`, `size`, `category`) VALUES
(1, 'Nike Jockey Hat', 'Sportswear H86 Nk Metal Swoosh', '20', '8', 50, 'N/A', 'Hats'),
(2, 'Jordan Boy`s Ele Elite Jacquard Snapback Cap', 'Metal JORDAN jumpman flight logo on front of hat. All-over embroidered elephant print on base and brim. Adjustable strap on back of hat for ultimate comfort and performance.', '35', '15', 15, 'N/A', 'Hats'),
(NULL, 'Champion Mens T-Shirt', 'Classic Script, 100% Cotton', '15', '6.5', '10', 'Small', 'T-Shirts'),
(NULL, 'Champion Mens T-Shirt', 'Classic Script, 100% Cotton', '15', '6.5', '8', 'Medium', 'T-Shirts'),
(NULL, 'Champion Mens T-Shirt', 'Classic Script, 100% Cotton', '15', '6.5', '10', 'Large', 'T-Shirts'),
(NULL, 'Champion Mens T-Shirt', 'Classic Script, 100% Cotton', '15', '6.5', '5', 'X-Large', 'T-Shirts'),
(NULL, 'Adidas Originals Men`s 3-Stripes T-Shirt', 'Men`s tee for casual wear. Crewneck for comfortable fit', '25', '12', '25', 'Small', 'T-Shirts'),
(NULL, 'Adidas Originals Men`s 3-Stripes T-Shirt', 'Men`s tee for casual wear. Crewneck for comfortable fit', '25', '12', '20', 'Medium', 'T-Shirts'),
(NULL, 'Adidas Originals Men`s 3-Stripes T-Shirt', 'Men`s tee for casual wear. Crewneck for comfortable fit', '25', '12', '9', 'Large', 'T-Shirts'),
(NULL, 'Adidas Originals Men`s 3-Stripes T-Shirt', 'Men`s tee for casual wear. Crewneck for comfortable fit', '25', '12', '10', 'X-Large', 'T-Shirts'),
(NULL, 'Under Armour Men`s Launch Stretch Woven 7-inch Shorts', 'New encased elastic waistband with internal drawcord', '30', '15', '20', 'Small', 'Shorts'),
(NULL, 'Under Armour Men`s Launch Stretch Woven 7-inch Shorts', 'New encased elastic waistband with internal drawcord', '30', '15', '25', 'Medium', 'Shorts'),
(NULL, 'Under Armour Men`s Launch Stretch Woven 7-inch Shorts', 'New encased elastic waistband with internal drawcord', '30', '15', '14', 'Large', 'Shorts'),
(NULL, 'Under Armour Men`s Launch Stretch Woven 7-inch Shorts', 'New encased elastic waistband with internal drawcord', '30', '15', '10', 'X-Large', 'Shorts'),
(NULL, 'Nike Women`s Stroke Running Shoe', 'Rubber sole\r\nRunning Shoes\r\nLightweight and padded design\r\nSupport and cushioning', '85', '42', '5', '37', 'Shoes'),
(NULL, 'Nike Women`s Stroke Running Shoe', 'Rubber sole\r\nRunning Shoes\r\nLightweight and padded design\r\nSupport and cushioning', '85', '42', '5', '38', 'Shoes'),
(NULL, 'Nike Women`s Stroke Running Shoe', 'Rubber sole\r\nRunning Shoes\r\nLightweight and padded design\r\nSupport and cushioning', '85', '42', '5', '39', 'Shoes'),
(NULL, 'Nike Women`s Stroke Running Shoe', 'Rubber sole\r\nRunning Shoes\r\nLightweight and padded design\r\nSupport and cushioning', '85', '42', '5', '40', 'Shoes'),
(NULL, 'Nike Women`s Stroke Running Shoe', 'Rubber sole\r\nRunning Shoes\r\nLightweight and padded design\r\nSupport and cushioning', '85', '42', '5', '41', 'Shoes'),
(NULL, 'NordicTrack T Series Treadmills', 'SMART-Response Motor for effective speed, interval, and endurance training; 20” x 55” tread belt offers plenty of leg and elbow space as you run; FlexSelect deck cushioning protects your joints', '1899', '1100', '3', 'N/A', 'Equipment'),
(NULL, 'Cap Barbell 150-Pound Dumbbell Set with Rack', 'SET INCLUDES – A pair of 5-pound, 10-pound, 15-pound, 20-pound, and 25-pound rubber hex dumbbells with a black A-frame dumbbell rack to store the weights.', '150', '60', 10, 'N/A', 'Equipment')
;


