CREATE TABLE IF NOT EXISTS `purbeurre_db`.`Category` (`id` INT UNSIGNED NOT NULL AUTO_INCREMENT,`name` VARCHAR(20) NULL,PRIMARY KEY (`id`),UNIQUE INDEX `ind_uni_cat` (`name`)) ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS `purbeurre_db`.`Product` (`id` INT UNSIGNED NOT NULL AUTO_INCREMENT,`name` VARCHAR(255) NULL,`description` VARCHAR(255) NULL,`nutrition_grade` CHAR(1) NULL,`barcode` VARCHAR(255) NOT NULL,`url` VARCHAR(255) NULL,`store` VARCHAR(255) NULL,`prd_cat` INT(2) NOT NULL,`fat` DECIMAL(5,2) NULL,`saturated_fat` DECIMAL(5,2) NULL,`sugar` DECIMAL(5,2) NULL,`salt` DECIMAL(5,2) NULL,PRIMARY KEY (`id`)) ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS `purbeurre_db`.`Category_Product` (`category_id` INT UNSIGNED NOT NULL,`product_id` INT UNSIGNED NOT NULL,PRIMARY KEY (`category_id`, `product_id`),CONSTRAINT `fk_Category_Product_category` FOREIGN KEY (`category_id`) REFERENCES `purbeurre`.`Category` (`id`),CONSTRAINT `fk_Category_Product_product` FOREIGN KEY (`product_id`) REFERENCES `purbeurre`.`Product` (`id`)) ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS `purbeurre_db`.`Favourite` (`new_prd_barcode` VARCHAR(255) NOT NULL,`Category_Product_category_id` INT UNSIGNED NOT NULL,`Category_Product_product_id` INT UNSIGNED NOT NULL,UNIQUE INDEX `ind_uni_favourite_cat_prd` (`new_prd_barcode`,`Category_Product_category_id`,`Category_Product_product_id`),CONSTRAINT `fk_Favourite_category_product` FOREIGN KEY (`Category_Product_category_id`,`Category_Product_product_id`) REFERENCES `purbeurre`.`Category_Product` (`category_id`,`product_id`)) ENGINE = InnoDB;
