-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         5.7.33 - MySQL Community Server (GPL)
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para db_sistemapos
CREATE DATABASE IF NOT EXISTS `db_sistemapos` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci */;
USE `db_sistemapos`;

-- Volcando estructura para tabla db_sistemapos.categoria
CREATE TABLE IF NOT EXISTS `categoria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL DEFAULT '',
  KEY `pk_categoria_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Volcando datos para la tabla db_sistemapos.categoria: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` (`id`, `nombre`) VALUES
	(1, 'Software'),
	(2, 'Libros'),
	(3, 'Fotografía');
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;

-- Volcando estructura para tabla db_sistemapos.clientes
CREATE TABLE IF NOT EXISTS `clientes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_doc_ide_id` int(11) NOT NULL DEFAULT '0',
  `nro_doc` varchar(20) COLLATE utf8_spanish_ci NOT NULL DEFAULT '',
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL DEFAULT '',
  `telefono` varchar(20) COLLATE utf8_spanish_ci DEFAULT '',
  `email` varchar(20) COLLATE utf8_spanish_ci DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `u_documento` (`tipo_doc_ide_id`,`nro_doc`),
  CONSTRAINT `fk_clientes_tipo_doc_id` FOREIGN KEY (`tipo_doc_ide_id`) REFERENCES `tipo_doc_ide` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Volcando datos para la tabla db_sistemapos.clientes: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` (`id`, `tipo_doc_ide_id`, `nro_doc`, `nombre`, `telefono`, `email`) VALUES
	(1, 1, '44565656', 'Lenin Bifnavent', '9454544951', 'lbifnavent@gmail.com'),
	(2, 2, '20415506818', 'Safiro SRL', '01502070', 'info@safirosrl.pe'),
	(4, 1, '878787878', 'Juan Perez', '', '');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;

-- Volcando estructura para tabla db_sistemapos.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL DEFAULT '',
  `precio` decimal(10,2) NOT NULL DEFAULT '0.00',
  `stock` bigint(20) NOT NULL DEFAULT '0',
  `categoria_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `FK_productos_categorias` (`categoria_id`),
  CONSTRAINT `FK_productos_categorias` FOREIGN KEY (`categoria_id`) REFERENCES `categoria` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Volcando datos para la tabla db_sistemapos.productos: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` (`id`, `nombre`, `precio`, `stock`, `categoria_id`) VALUES
	(1, 'Hama Filtro ultravioleta de 52 mm', 15.00, 10, 3),
	(2, 'Spotify', 10.00, 2, 1),
	(3, 'Divina comedia', 15.00, 4, 2);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;

-- Volcando estructura para tabla db_sistemapos.tipo_doc_ide
CREATE TABLE IF NOT EXISTS `tipo_doc_ide` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL DEFAULT '',
  KEY `pk_tipo_doc_ide_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Volcando datos para la tabla db_sistemapos.tipo_doc_ide: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `tipo_doc_ide` DISABLE KEYS */;
INSERT INTO `tipo_doc_ide` (`id`, `nombre`) VALUES
	(1, 'DNI'),
	(2, 'RUC'),
	(3, 'CARNET EXTANJERIA');
/*!40000 ALTER TABLE `tipo_doc_ide` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
