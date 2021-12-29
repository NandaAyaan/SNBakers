-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: snbakers
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart` (
  `CartNo` int NOT NULL AUTO_INCREMENT,
  `CustEmail` varchar(25) DEFAULT NULL,
  `items` mediumint DEFAULT NULL,
  PRIMARY KEY (`CartNo`),
  KEY `EFK_idx` (`CustEmail`),
  CONSTRAINT `EFK` FOREIGN KEY (`CustEmail`) REFERENCES `customer` (`CustEmail`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
INSERT INTO `cart` VALUES (2,'sng@gmail.com',7),(3,'sng@gmail.com',-1),(4,'ayaan@gmail.com',4),(5,'ayaan@gmail.com',-1),(6,'ayaan@gmail.com',-1),(8,'sng@gmail.com',0),(9,'ayaan@gmail.com',0),(10,'ayaan@gmail.com',0),(11,'ayaan@gmail.com',0),(12,'ayaan@gmail.com',0),(13,'sng@gmail.com',0),(14,'sng@gmail.com',0),(15,'ayaan@gmail.com',0),(16,'ayaan@gmail.com',0),(17,'ayaan@gmail.com',0),(18,'ayaan@gmail.com',0),(19,'ayaan@gmail.com',0),(20,'ayaan@gmail.com',0),(21,'ayaan@gmail.com',0),(22,'ayaan@gmail.com',0),(23,'ayaan@gmail.com',0),(24,'ayaan@gmail.com',0),(25,'sng@gmail.com',0),(26,'sng@gmail.com',0),(27,'ayaan@gmail.com',0),(28,'ayaan@gmail.com',0);
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-29 18:49:32
