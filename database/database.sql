CREATE TABLE `products` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50),
  `price` DECIMAL(12,2),
  PRIMARY KEY (`id`)
);

INSERT INTO `products` (`name`, `price`) VALUES ('Mobile', 100);
INSERT INTO `products` (`name`, `price`) VALUES ('Tablet', 200);
INSERT INTO `products` (`name`, `price`) VALUES ('Labtop', 300.00);
INSERT INTO `products` (`name`, `price`) VALUES ('Desktop', 400);
INSERT INTO `products` (`name`, `price`) VALUES ('Server', 500);