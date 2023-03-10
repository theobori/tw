CREATE DATABASE IF NOT EXISTS teeworlds;

USE `teeworlds`;

DROP TABLE IF EXISTS `record_mapinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `record_mapinfo` (
  `Map` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `Width` int(11) DEFAULT 0,
  `Height` int(11) DEFAULT 0,
  `DEATH` tinyint(1) DEFAULT 0,
  `THROUGH` tinyint(1) DEFAULT 0,
  `JUMP` tinyint(1) DEFAULT 0,
  `DFREEZE` tinyint(1) DEFAULT 0,
  `EHOOK_START` tinyint(1) DEFAULT 0,
  `HIT_END` tinyint(1) DEFAULT 0,
  `SOLO_START` tinyint(1) DEFAULT 0,
  `TELE_GUN` tinyint(1) DEFAULT 0,
  `TELE_GRENADE` tinyint(1) DEFAULT 0,
  `TELE_LASER` tinyint(1) DEFAULT 0,
  `NPC_START` tinyint(1) DEFAULT 0,
  `SUPER_START` tinyint(1) DEFAULT 0,
  `JETPACK_START` tinyint(1) DEFAULT 0,
  `WALLJUMP` tinyint(1) DEFAULT 0,
  `NPH_START` tinyint(1) DEFAULT 0,
  `WEAPON_SHOTGUN` tinyint(1) DEFAULT 0,
  `WEAPON_GRENADE` tinyint(1) DEFAULT 0,
  `POWERUP_NINJA` tinyint(1) DEFAULT 0,
  `WEAPON_RIFLE` tinyint(1) DEFAULT 0,
  `LASER_STOP` tinyint(1) DEFAULT 0,
  `CRAZY_SHOTGUN` tinyint(1) DEFAULT 0,
  `DRAGGER` tinyint(1) DEFAULT 0,
  `DOOR` tinyint(1) DEFAULT 0,
  `SWITCH_TIMED` tinyint(1) DEFAULT 0,
  `SWITCH` tinyint(1) DEFAULT 0,
  `STOP` tinyint(1) DEFAULT 0,
  `THROUGH_ALL` tinyint(1) DEFAULT 0,
  `TUNE` tinyint(1) DEFAULT 0,
  `OLDLASER` tinyint(1) DEFAULT 0,
  `TELEINEVIL` tinyint(1) DEFAULT 0,
  `TELEIN` tinyint(1) DEFAULT 0,
  `TELECHECK` tinyint(1) DEFAULT 0,
  `TELEINWEAPON` tinyint(1) DEFAULT 0,
  `TELEINHOOK` tinyint(1) DEFAULT 0,
  `CHECKPOINT_FIRST` tinyint(1) DEFAULT 0,
  `BONUS` tinyint(1) DEFAULT 0,
  `BOOST` tinyint(1) DEFAULT 0,
  `PLASMAF` tinyint(1) DEFAULT 0,
  `PLASMAE` tinyint(1) DEFAULT 0,
  `PLASMAU` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`Map`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
-- MariaDB dump 10.19  Distrib 10.5.18-MariaDB, for debian-linux-gnu (x86_64)
-- Host: localhost    Database: teeworlds
-- ------------------------------------------------------
-- Server version	10.5.18-MariaDB-0+deb11u1-log
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
-- Table structure for table `record_race`
DROP TABLE IF EXISTS `record_race`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `record_race` (
  `Map` varchar(128) NOT NULL,
  `Name` varchar(16) NOT NULL,
  `Timestamp` timestamp NOT NULL DEFAULT current_timestamp(),
  `Time` float NOT NULL DEFAULT 0,
  `Server` char(4) NOT NULL DEFAULT '',
  `cp1` float NOT NULL DEFAULT 0,
  `cp2` float NOT NULL DEFAULT 0,
  `cp3` float NOT NULL DEFAULT 0,
  `cp4` float NOT NULL DEFAULT 0,
  `cp5` float NOT NULL DEFAULT 0,
  `cp6` float NOT NULL DEFAULT 0,
  `cp7` float NOT NULL DEFAULT 0,
  `cp8` float NOT NULL DEFAULT 0,
  `cp9` float NOT NULL DEFAULT 0,
  `cp10` float NOT NULL DEFAULT 0,
  `cp11` float NOT NULL DEFAULT 0,
  `cp12` float NOT NULL DEFAULT 0,
  `cp13` float NOT NULL DEFAULT 0,
  `cp14` float NOT NULL DEFAULT 0,
  `cp15` float NOT NULL DEFAULT 0,
  `cp16` float NOT NULL DEFAULT 0,
  `cp17` float NOT NULL DEFAULT 0,
  `cp18` float NOT NULL DEFAULT 0,
  `cp19` float NOT NULL DEFAULT 0,
  `cp20` float NOT NULL DEFAULT 0,
  `cp21` float NOT NULL DEFAULT 0,
  `cp22` float NOT NULL DEFAULT 0,
  `cp23` float NOT NULL DEFAULT 0,
  `cp24` float NOT NULL DEFAULT 0,
  `cp25` float NOT NULL DEFAULT 0,
  `GameID` varchar(64) DEFAULT NULL,
  `DDNet7` tinyint(1) DEFAULT 0,
  UNIQUE KEY `Map` (`Map`,`Name`,`Time`,`Timestamp`,`Server`),
  KEY `Map_2` (`Map`,`Name`),
  KEY `Name` (`Name`,`Timestamp`),
  KEY `Server` (`Server`),
  KEY `MapTimestamp` (`Map`,`Timestamp`),
  KEY `Timestamp` (`Timestamp`),
  KEY `Server_2` (`Server`,`Timestamp`),
  KEY `idx_Timestamp` (`Timestamp`),
  KEY `idx_Server_Timestamp` (`Server`,`Timestamp`),
  KEY `MapNameTime` (`Map`,`Name`,`Time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;
-- Dumping data for table `record_race`
-- MariaDB dump 10.19  Distrib 10.5.18-MariaDB, for debian-linux-gnu (x86_64)
-- Host: localhost    Database: teeworlds
-- ------------------------------------------------------
-- Server version	10.5.18-MariaDB-0+deb11u1-log
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
-- Table structure for table `record_teamrace`
DROP TABLE IF EXISTS `record_teamrace`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `record_teamrace` (
  `Map` varchar(128) NOT NULL,
  `Name` varchar(16) NOT NULL,
  `Timestamp` timestamp NOT NULL DEFAULT current_timestamp(),
  `Time` float NOT NULL DEFAULT 0,
  `ID` varbinary(16) NOT NULL,
  `GameID` varchar(64) DEFAULT NULL,
  `DDNet7` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`Map`,`Name`,`Timestamp`,`Time`,`ID`),
  UNIQUE KEY `Name` (`Name`,`ID`),
  KEY `Map` (`Map`),
  KEY `ID` (`ID`),
  KEY `MapID` (`Map`,`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;
-- Dumping data for table `record_teamrace`
