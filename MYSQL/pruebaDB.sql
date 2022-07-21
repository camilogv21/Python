SELECT * FROM  categoria;
-- -----------------------------------------------------
-- Schema pruebaDB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pruebaDB` DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci ;
USE `pruebaDB` ;

-- -----------------------------------------------------
-- Table `categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `categoria` (
  `idcategoria` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`idcategoria`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_spanish_ci;


-- -----------------------------------------------------
-- Table `producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `producto` (
  `idproductos` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(45) NULL,
  `precio` INT NOT NULL,
  `categoria_idcategoria` INT NOT NULL,
  PRIMARY KEY (`idproductos`),
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC),
  INDEX `fk_producto_categoria_idx` (`categoria_idcategoria` ASC),
  CONSTRAINT `fk_producto_categoria`
    FOREIGN KEY (`categoria_idcategoria`)
    REFERENCES `categoria` (`idcategoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_spanish_ci;


-- -----------------------------------------------------
-- Data for table `categoria`
-- -----------------------------------------------------
START TRANSACTION;
USE `pruebaDB`;
INSERT INTO `categoria` (`idcategoria`, `nombre`) VALUES (1, 'Libros');
INSERT INTO `categoria` (`idcategoria`, `nombre`) VALUES (2, 'Revistas');
INSERT INTO `categoria` (`idcategoria`, `nombre`) VALUES (3, 'Cartillas');

COMMIT;


-- -----------------------------------------------------
-- Data for table `producto`
-- -----------------------------------------------------
START TRANSACTION;
USE `pruebaDB`;
INSERT INTO `producto` (`idproductos`, `nombre`, `descripcion`, `precio`, `categoria_idcategoria`) VALUES (1, 'El viejo y el mar', 'Novela fantástica drama', 20000, 1);
INSERT INTO `producto` (`idproductos`, `nombre`, `descripcion`, `precio`, `categoria_idcategoria`) VALUES (2, 'El principito', 'Fantasía infantil', 25600, 1);

COMMIT;

