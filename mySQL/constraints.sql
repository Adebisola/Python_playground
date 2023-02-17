-- practice constraints in mySQl
CREATE DATABASE IF NOT EXISTS `People`;
CREATE TABLE IF NOT EXISTS `People`.`user`(
	`id` INT,
	`Lastname` TEXT NOT NULL,
	`Firstname` TEXT NOT NULL,
	`City` VARCHAR(55)
);

INSERT INTO `user` VALUES(1, 'Kazeem', 'Babatunde', 'Ikirun');
SELECT * FROM user;
