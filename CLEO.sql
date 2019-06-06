-- MySQL dump 10.13  Distrib 8.0.16, for macos10.14 (x86_64)
--
-- Host: 127.0.0.1    Database: cleodb
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=129 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can view permission',1,'view_permission'),(5,'Can add group',2,'add_group'),(6,'Can change group',2,'change_group'),(7,'Can delete group',2,'delete_group'),(8,'Can view group',2,'view_group'),(9,'Can add content type',3,'add_contenttype'),(10,'Can change content type',3,'change_contenttype'),(11,'Can delete content type',3,'delete_contenttype'),(12,'Can view content type',3,'view_contenttype'),(13,'Can add user',4,'add_customuser'),(14,'Can change user',4,'change_customuser'),(15,'Can delete user',4,'delete_customuser'),(16,'Can view user',4,'view_customuser'),(17,'Can add tipo empleado',5,'add_tipoempleado'),(18,'Can change tipo empleado',5,'change_tipoempleado'),(19,'Can delete tipo empleado',5,'delete_tipoempleado'),(20,'Can view tipo empleado',5,'view_tipoempleado'),(21,'Can add cliente',6,'add_cliente'),(22,'Can change cliente',6,'change_cliente'),(23,'Can delete cliente',6,'delete_cliente'),(24,'Can view cliente',6,'view_cliente'),(25,'Can add empleado',7,'add_empleado'),(26,'Can change empleado',7,'change_empleado'),(27,'Can delete empleado',7,'delete_empleado'),(28,'Can view empleado',7,'view_empleado'),(29,'Can add log entry',8,'add_logentry'),(30,'Can change log entry',8,'change_logentry'),(31,'Can delete log entry',8,'delete_logentry'),(32,'Can view log entry',8,'view_logentry'),(33,'Can add session',9,'add_session'),(34,'Can change session',9,'change_session'),(35,'Can delete session',9,'delete_session'),(36,'Can view session',9,'view_session'),(37,'Can add horario',10,'add_horario'),(38,'Can change horario',10,'change_horario'),(39,'Can delete horario',10,'delete_horario'),(40,'Can view horario',10,'view_horario'),(41,'Can add horarioempleado',11,'add_horarioempleado'),(42,'Can change horarioempleado',11,'change_horarioempleado'),(43,'Can delete horarioempleado',11,'delete_horarioempleado'),(44,'Can view horarioempleado',11,'view_horarioempleado'),(45,'Can add tipohorarioempleado',12,'add_tipohorarioempleado'),(46,'Can change tipohorarioempleado',12,'change_tipohorarioempleado'),(47,'Can delete tipohorarioempleado',12,'delete_tipohorarioempleado'),(48,'Can view tipohorarioempleado',12,'view_tipohorarioempleado'),(49,'Can add maquina',13,'add_maquina'),(50,'Can change maquina',13,'change_maquina'),(51,'Can delete maquina',13,'delete_maquina'),(52,'Can view maquina',13,'view_maquina'),(53,'Can add tipo zona',14,'add_tipozona'),(54,'Can change tipo zona',14,'change_tipozona'),(55,'Can delete tipo zona',14,'delete_tipozona'),(56,'Can view tipo zona',14,'view_tipozona'),(57,'Can add sala',15,'add_sala'),(58,'Can change sala',15,'change_sala'),(59,'Can delete sala',15,'delete_sala'),(60,'Can view sala',15,'view_sala'),(61,'Can add promocion',16,'add_promocion'),(62,'Can change promocion',16,'change_promocion'),(63,'Can delete promocion',16,'delete_promocion'),(64,'Can view promocion',16,'view_promocion'),(65,'Can add publicidad',17,'add_publicidad'),(66,'Can change publicidad',17,'change_publicidad'),(67,'Can delete publicidad',17,'delete_publicidad'),(68,'Can view publicidad',17,'view_publicidad'),(69,'Can add estadomensaje',18,'add_estadomensaje'),(70,'Can change estadomensaje',18,'change_estadomensaje'),(71,'Can delete estadomensaje',18,'delete_estadomensaje'),(72,'Can view estadomensaje',18,'view_estadomensaje'),(73,'Can add notificacion',19,'add_notificacion'),(74,'Can change notificacion',19,'change_notificacion'),(75,'Can delete notificacion',19,'delete_notificacion'),(76,'Can view notificacion',19,'view_notificacion'),(77,'Can add tipousuario',20,'add_tipousuario'),(78,'Can change tipousuario',20,'change_tipousuario'),(79,'Can delete tipousuario',20,'delete_tipousuario'),(80,'Can view tipousuario',20,'view_tipousuario'),(81,'Can add proveedor',21,'add_proveedor'),(82,'Can change proveedor',21,'change_proveedor'),(83,'Can delete proveedor',21,'delete_proveedor'),(84,'Can view proveedor',21,'view_proveedor'),(85,'Can add producto',22,'add_producto'),(86,'Can change producto',22,'change_producto'),(87,'Can delete producto',22,'delete_producto'),(88,'Can view producto',22,'view_producto'),(89,'Can add tipo producto',23,'add_tipoproducto'),(90,'Can change tipo producto',23,'change_tipoproducto'),(91,'Can delete tipo producto',23,'delete_tipoproducto'),(92,'Can view tipo producto',23,'view_tipoproducto'),(93,'Can add stock',24,'add_stock'),(94,'Can change stock',24,'change_stock'),(95,'Can delete stock',24,'delete_stock'),(96,'Can view stock',24,'view_stock'),(97,'Can add estado pedido',25,'add_estadopedido'),(98,'Can change estado pedido',25,'change_estadopedido'),(99,'Can delete estado pedido',25,'delete_estadopedido'),(100,'Can view estado pedido',25,'view_estadopedido'),(101,'Can add pedido',26,'add_pedido'),(102,'Can change pedido',26,'change_pedido'),(103,'Can delete pedido',26,'delete_pedido'),(104,'Can view pedido',26,'view_pedido'),(105,'Can add inventario',27,'add_inventario'),(106,'Can change inventario',27,'change_inventario'),(107,'Can delete inventario',27,'delete_inventario'),(108,'Can view inventario',27,'view_inventario'),(109,'Can add tratamiento',28,'add_tratamiento'),(110,'Can change tratamiento',28,'change_tratamiento'),(111,'Can delete tratamiento',28,'delete_tratamiento'),(112,'Can view tratamiento',28,'view_tratamiento'),(113,'Can add cita',29,'add_cita'),(114,'Can change cita',29,'change_cita'),(115,'Can delete cita',29,'delete_cita'),(116,'Can view cita',29,'view_cita'),(117,'Can add estadocita',30,'add_estadocita'),(118,'Can change estadocita',30,'change_estadocita'),(119,'Can delete estadocita',30,'delete_estadocita'),(120,'Can view estadocita',30,'view_estadocita'),(121,'Can add estadofactura',31,'add_estadofactura'),(122,'Can change estadofactura',31,'change_estadofactura'),(123,'Can delete estadofactura',31,'delete_estadofactura'),(124,'Can view estadofactura',31,'view_estadofactura'),(125,'Can add factura',32,'add_factura'),(126,'Can change factura',32,'change_factura'),(127,'Can delete factura',32,'delete_factura'),(128,'Can view factura',32,'view_factura');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cita`
--

DROP TABLE IF EXISTS `Cita`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Cita` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date DEFAULT NULL,
  `Cliente_id` int(11) NOT NULL,
  `Empleado_id` int(11) NOT NULL,
  `estadoCita_id` int(11) NOT NULL,
  `HorarioEntrada_id` int(11) NOT NULL,
  `HorarioSalida_id` int(11) NOT NULL,
  `Tratamiento_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Cita_id_estadoCita_id_Cliente_ed42159f_uniq` (`id`,`estadoCita_id`,`Cliente_id`,`Empleado_id`,`HorarioEntrada_id`,`HorarioSalida_id`,`Tratamiento_id`),
  KEY `Cita_Cliente_id_996f9c57_fk_cliente_user_id` (`Cliente_id`),
  KEY `Cita_Empleado_id_d169c98e_fk_empleado_user_id` (`Empleado_id`),
  KEY `Cita_estadoCita_id_62f366c6` (`estadoCita_id`),
  KEY `Cita_HorarioEntrada_id_7ff02a11` (`HorarioEntrada_id`),
  KEY `Cita_HorarioSalida_id_ce76719a` (`HorarioSalida_id`),
  KEY `Cita_Tratamiento_id_6fce2a0f` (`Tratamiento_id`),
  CONSTRAINT `Cita_Cliente_id_996f9c57_fk_cliente_user_id` FOREIGN KEY (`Cliente_id`) REFERENCES `cliente` (`user_id`),
  CONSTRAINT `Cita_Empleado_id_d169c98e_fk_empleado_user_id` FOREIGN KEY (`Empleado_id`) REFERENCES `empleado` (`user_id`),
  CONSTRAINT `Cita_HorarioEntrada_id_7ff02a11_fk_Horario_id` FOREIGN KEY (`HorarioEntrada_id`) REFERENCES `horario` (`id`),
  CONSTRAINT `Cita_HorarioSalida_id_ce76719a_fk_Horario_id` FOREIGN KEY (`HorarioSalida_id`) REFERENCES `horario` (`id`),
  CONSTRAINT `Cita_Tratamiento_id_6fce2a0f_fk_Tratamiento_id` FOREIGN KEY (`Tratamiento_id`) REFERENCES `tratamiento` (`id`),
  CONSTRAINT `Cita_estadoCita_id_62f366c6_fk_estadoCita_id` FOREIGN KEY (`estadoCita_id`) REFERENCES `estadocita` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cita`
--

LOCK TABLES `Cita` WRITE;
/*!40000 ALTER TABLE `Cita` DISABLE KEYS */;
/*!40000 ALTER TABLE `Cita` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `cliente` (
  `user_id` int(11) NOT NULL,
  `dni` varchar(9) NOT NULL,
  `direccion` varchar(45) DEFAULT NULL,
  `telefono` varchar(9) DEFAULT NULL,
  `puntuacion` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `dni` (`dni`),
  CONSTRAINT `cliente_user_id_e7dabcb3_fk_usuarios_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `usuarios_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_usuarios_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_usuarios_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `usuarios_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-05-12 17:06:49.874116','1','  Perfil',1,'[{\"added\": {}}]',7,1),(2,'2019-05-12 17:09:06.966817','1','  Perfil',3,'',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (8,'admin','logentry'),(2,'auth','group'),(1,'auth','permission'),(29,'cita','cita'),(30,'cita','estadocita'),(3,'contenttypes','contenttype'),(31,'factura','estadofactura'),(32,'factura','factura'),(10,'horarioEmpleado','horario'),(11,'horarioEmpleado','horarioempleado'),(12,'horarioEmpleado','tipohorarioempleado'),(27,'inventario','inventario'),(13,'maquina','maquina'),(14,'maquina','tipozona'),(18,'notificacion','estadomensaje'),(19,'notificacion','notificacion'),(20,'notificacion','tipousuario'),(25,'pedido','estadopedido'),(26,'pedido','pedido'),(22,'producto','producto'),(23,'producto','tipoproducto'),(16,'promocion','promocion'),(21,'proveedor','proveedor'),(17,'publicidad','publicidad'),(15,'sala','sala'),(9,'sessions','session'),(24,'stock','stock'),(28,'tratamiento','tratamiento'),(6,'usuarios','cliente'),(4,'usuarios','customuser'),(7,'usuarios','empleado'),(5,'usuarios','tipoempleado');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-05-12 12:11:34.162440'),(2,'contenttypes','0002_remove_content_type_name','2019-05-12 12:11:34.208555'),(3,'auth','0001_initial','2019-05-12 12:11:34.342375'),(4,'auth','0002_alter_permission_name_max_length','2019-05-12 12:11:34.373534'),(5,'auth','0003_alter_user_email_max_length','2019-05-12 12:11:34.381028'),(6,'auth','0004_alter_user_username_opts','2019-05-12 12:11:34.390244'),(7,'auth','0005_alter_user_last_login_null','2019-05-12 12:11:34.397262'),(8,'auth','0006_require_contenttypes_0002','2019-05-12 12:11:34.400626'),(9,'auth','0007_alter_validators_add_error_messages','2019-05-12 12:11:34.412100'),(10,'auth','0008_alter_user_username_max_length','2019-05-12 12:11:34.423741'),(11,'auth','0009_alter_user_last_name_max_length','2019-05-12 12:11:34.433673'),(12,'usuarios','0001_initial','2019-05-12 12:11:34.630070'),(13,'admin','0001_initial','2019-05-12 12:15:35.161548'),(14,'admin','0002_logentry_remove_auto_add','2019-05-12 12:15:35.172040'),(15,'admin','0003_logentry_add_action_flag_choices','2019-05-12 12:15:35.183145'),(16,'sessions','0001_initial','2019-05-12 12:15:35.218450'),(17,'horarioEmpleado','0001_initial','2019-05-12 12:18:57.440278'),(18,'maquina','0001_initial','2019-05-12 12:20:24.231070'),(19,'sala','0001_initial','2019-05-12 12:24:42.153338'),(20,'promocion','0001_initial','2019-05-12 12:29:10.995866'),(21,'publicidad','0001_initial','2019-05-12 12:34:03.103597'),(22,'notificacion','0001_initial','2019-05-12 14:41:50.450339'),(23,'proveedor','0001_initial','2019-05-12 15:58:31.330864'),(24,'producto','0001_initial','2019-05-12 15:59:59.836648'),(25,'stock','0001_initial','2019-05-12 16:01:12.002779'),(26,'pedido','0001_initial','2019-05-12 16:02:33.658611'),(27,'inventario','0001_initial','2019-05-12 16:05:53.185489'),(28,'tratamiento','0001_initial','2019-05-12 16:09:10.419064'),(29,'cita','0001_initial','2019-05-12 16:12:40.465151'),(30,'factura','0001_initial','2019-05-12 16:16:01.681104'),(31,'pedido','0002_auto_20190512_1832','2019-05-12 16:32:41.814313'),(32,'maquina','0002_auto_20190512_1837','2019-05-12 16:37:53.417661');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('k0ylvxjwougd2p8s4za13mp58t5a55ny','Y2JmMTQwY2RjMmM4NWY1YWQwYzZmMDBjZDBmZTI1YWRjODIyYjkyYjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkMzFiYjdmODQ5NmM2ZmVhZDE4NDllMDNmY2I2ZWM1ZThkNDBjYTFjIn0=','2019-05-26 15:13:59.321583');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleado`
--

DROP TABLE IF EXISTS `empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `empleado` (
  `user_id` int(11) NOT NULL,
  `dni` varchar(9) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `direccion` varchar(45) DEFAULT NULL,
  `telefono` varchar(9) DEFAULT NULL,
  `tipoEmpleado_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `dni` (`dni`),
  UNIQUE KEY `empleado_tipoEmpleado_id_dni_15f3fc34_uniq` (`tipoEmpleado_id`,`dni`),
  CONSTRAINT `empleado_tipoEmpleado_id_3d15facc_fk_tipoempleado_id` FOREIGN KEY (`tipoEmpleado_id`) REFERENCES `tipoempleado` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleado`
--

LOCK TABLES `empleado` WRITE;
/*!40000 ALTER TABLE `empleado` DISABLE KEYS */;
/*!40000 ALTER TABLE `empleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estadoCita`
--

DROP TABLE IF EXISTS `estadoCita`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `estadoCita` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estadoCita`
--

LOCK TABLES `estadoCita` WRITE;
/*!40000 ALTER TABLE `estadoCita` DISABLE KEYS */;
INSERT INTO `estadoCita` VALUES (1,'Confirmada'),(2,'No confirmada');
/*!40000 ALTER TABLE `estadoCita` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estadoFactura`
--

DROP TABLE IF EXISTS `estadoFactura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `estadoFactura` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estadoFactura`
--

LOCK TABLES `estadoFactura` WRITE;
/*!40000 ALTER TABLE `estadoFactura` DISABLE KEYS */;
INSERT INTO `estadoFactura` VALUES (1,'Pagado'),(2,'Pendiente');
/*!40000 ALTER TABLE `estadoFactura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estadomensaje`
--

DROP TABLE IF EXISTS `estadomensaje`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `estadomensaje` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estadomensaje`
--

LOCK TABLES `estadomensaje` WRITE;
/*!40000 ALTER TABLE `estadomensaje` DISABLE KEYS */;
INSERT INTO `estadomensaje` VALUES (1,'Leido'),(2,' No leido');
/*!40000 ALTER TABLE `estadomensaje` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estadopedido`
--

DROP TABLE IF EXISTS `estadopedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `estadopedido` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estadopedido`
--

LOCK TABLES `estadopedido` WRITE;
/*!40000 ALTER TABLE `estadopedido` DISABLE KEYS */;
INSERT INTO `estadopedido` VALUES (1,'Entregado'),(2,'En proceso'),(3,'Cancelado');
/*!40000 ALTER TABLE `estadopedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Factura`
--

DROP TABLE IF EXISTS `Factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Factura` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `costePorCobrar` double DEFAULT NULL,
  `total` double DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `Cita_id` int(11) NOT NULL,
  `estadoFactura_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Factura_id_estadoFactura_id_Cita_id_dad8bee4_uniq` (`id`,`estadoFactura_id`,`Cita_id`),
  KEY `Factura_Cita_id_4d19ee00_fk_Cita_id` (`Cita_id`),
  KEY `Factura_estadoFactura_id_0f527ea9_fk_estadoFactura_id` (`estadoFactura_id`),
  CONSTRAINT `Factura_Cita_id_4d19ee00_fk_Cita_id` FOREIGN KEY (`Cita_id`) REFERENCES `cita` (`id`),
  CONSTRAINT `Factura_estadoFactura_id_0f527ea9_fk_estadoFactura_id` FOREIGN KEY (`estadoFactura_id`) REFERENCES `estadofactura` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Factura`
--

LOCK TABLES `Factura` WRITE;
/*!40000 ALTER TABLE `Factura` DISABLE KEYS */;
/*!40000 ALTER TABLE `Factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Horario`
--

DROP TABLE IF EXISTS `Horario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Horario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hora` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Horario`
--

LOCK TABLES `Horario` WRITE;
/*!40000 ALTER TABLE `Horario` DISABLE KEYS */;
/*!40000 ALTER TABLE `Horario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `HorarioEmpleado`
--

DROP TABLE IF EXISTS `HorarioEmpleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `HorarioEmpleado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `inicio` date DEFAULT NULL,
  `fin` date DEFAULT NULL,
  `Empleado_id` int(11) NOT NULL,
  `tipoHorarioEmpleado_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `HorarioEmpleado_id_Empleado_id_tipoHorar_3de4c7f0_uniq` (`id`,`Empleado_id`,`tipoHorarioEmpleado_id`),
  KEY `HorarioEmpleado_Empleado_id_f31c909b_fk_empleado_user_id` (`Empleado_id`),
  KEY `HorarioEmpleado_tipoHorarioEmpleado_id_c70553a1` (`tipoHorarioEmpleado_id`),
  CONSTRAINT `HorarioEmpleado_Empleado_id_f31c909b_fk_empleado_user_id` FOREIGN KEY (`Empleado_id`) REFERENCES `empleado` (`user_id`),
  CONSTRAINT `HorarioEmpleado_tipoHorarioEmpleado__c70553a1_fk_tipoHorar` FOREIGN KEY (`tipoHorarioEmpleado_id`) REFERENCES `tipohorarioempleado` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HorarioEmpleado`
--

LOCK TABLES `HorarioEmpleado` WRITE;
/*!40000 ALTER TABLE `HorarioEmpleado` DISABLE KEYS */;
/*!40000 ALTER TABLE `HorarioEmpleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Inventario`
--

DROP TABLE IF EXISTS `Inventario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Inventario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `coste` double DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `fechaEntrada` date DEFAULT NULL,
  `fechaFin` date DEFAULT NULL,
  `Pedido_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Inventario_id_Pedido_id_b22065a5_uniq` (`id`,`Pedido_id`),
  KEY `Inventario_Pedido_id_b2c9b226_fk_pedido_id` (`Pedido_id`),
  CONSTRAINT `Inventario_Pedido_id_b2c9b226_fk_pedido_id` FOREIGN KEY (`Pedido_id`) REFERENCES `pedido` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Inventario`
--

LOCK TABLES `Inventario` WRITE;
/*!40000 ALTER TABLE `Inventario` DISABLE KEYS */;
/*!40000 ALTER TABLE `Inventario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Maquina`
--

DROP TABLE IF EXISTS `Maquina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Maquina` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `fechaIngreso` date DEFAULT NULL,
  `tipoZona_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Maquina_TipoZona_id_edc19918_uniq` (`tipoZona_id`),
  KEY `Maquina_TipoZona_id_edc19918` (`tipoZona_id`),
  CONSTRAINT `Maquina_TipoZona_id_edc19918_fk_tipoZona_id` FOREIGN KEY (`tipoZona_id`) REFERENCES `tipozona` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Maquina`
--

LOCK TABLES `Maquina` WRITE;
/*!40000 ALTER TABLE `Maquina` DISABLE KEYS */;
/*!40000 ALTER TABLE `Maquina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notificacion`
--

DROP TABLE IF EXISTS `notificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `notificacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mensaje` longtext,
  `estadoMensaje_id` int(11) NOT NULL,
  `tipoUsuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `notificacion_id_estadoMensaje_id_tipoUsuario_id_ee2e0206_uniq` (`id`,`estadoMensaje_id`,`tipoUsuario_id`),
  KEY `notificacion_estadoMensaje_id_b682a0d1_fk_estadomensaje_id` (`estadoMensaje_id`),
  KEY `notificacion_tipoUsuario_id_96c7274e` (`tipoUsuario_id`),
  CONSTRAINT `notificacion_estadoMensaje_id_b682a0d1_fk_estadomensaje_id` FOREIGN KEY (`estadoMensaje_id`) REFERENCES `estadomensaje` (`id`),
  CONSTRAINT `notificacion_tipoUsuario_id_96c7274e_fk_tipousuario_id` FOREIGN KEY (`tipoUsuario_id`) REFERENCES `tipousuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notificacion`
--

LOCK TABLES `notificacion` WRITE;
/*!40000 ALTER TABLE `notificacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `notificacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pedido`
--

DROP TABLE IF EXISTS `Pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Pedido` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` int(11) DEFAULT NULL,
  `total` double DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `estadoPedido_id` int(11) NOT NULL,
  `Producto_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pedido_id_estadoPedido_id_Producto_id_ba77ddd3_uniq` (`id`,`estadoPedido_id`,`Producto_id`),
  KEY `pedido_estadoPedido_id_9a0f7df6_fk_estadopedido_id` (`estadoPedido_id`),
  KEY `pedido_Producto_id_405e6646_fk_Producto_id` (`Producto_id`),
  CONSTRAINT `pedido_Producto_id_405e6646_fk_Producto_id` FOREIGN KEY (`Producto_id`) REFERENCES `producto` (`id`),
  CONSTRAINT `pedido_estadoPedido_id_9a0f7df6_fk_estadopedido_id` FOREIGN KEY (`estadoPedido_id`) REFERENCES `estadopedido` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pedido`
--

LOCK TABLES `Pedido` WRITE;
/*!40000 ALTER TABLE `Pedido` DISABLE KEYS */;
/*!40000 ALTER TABLE `Pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Producto`
--

DROP TABLE IF EXISTS `Producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Producto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(45) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `precio` double DEFAULT NULL,
  `borrado` int(11) DEFAULT NULL,
  `Proveedor_id` int(11) NOT NULL,
  `tipoProducto_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Producto_id_codigo_tipoProducto_id_Proveedor_id_fc530ea1_uniq` (`id`,`codigo`,`tipoProducto_id`,`Proveedor_id`),
  KEY `Producto_Proveedor_id_b2f7b150_fk_Proveedor_id` (`Proveedor_id`),
  KEY `Producto_tipoProducto_id_f396921b` (`tipoProducto_id`),
  CONSTRAINT `Producto_Proveedor_id_b2f7b150_fk_Proveedor_id` FOREIGN KEY (`Proveedor_id`) REFERENCES `proveedor` (`id`),
  CONSTRAINT `Producto_tipoProducto_id_f396921b_fk_tipoProducto_id` FOREIGN KEY (`tipoProducto_id`) REFERENCES `tipoproducto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Producto`
--

LOCK TABLES `Producto` WRITE;
/*!40000 ALTER TABLE `Producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `Producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Promocion`
--

DROP TABLE IF EXISTS `Promocion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Promocion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(45) DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `observaciones` longtext,
  `descuento` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `codigo` (`codigo`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `Promocion_codigo_nombre_840c8e37_uniq` (`codigo`,`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Promocion`
--

LOCK TABLES `Promocion` WRITE;
/*!40000 ALTER TABLE `Promocion` DISABLE KEYS */;
/*!40000 ALTER TABLE `Promocion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Proveedor`
--

DROP TABLE IF EXISTS `Proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Proveedor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `contacto` varchar(45) DEFAULT NULL,
  `descripcion` varchar(45) DEFAULT NULL,
  `borrado` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `Proveedor_id_nombre_890229d8_uniq` (`id`,`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Proveedor`
--

LOCK TABLES `Proveedor` WRITE;
/*!40000 ALTER TABLE `Proveedor` DISABLE KEYS */;
/*!40000 ALTER TABLE `Proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Publicidad`
--

DROP TABLE IF EXISTS `Publicidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Publicidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fechaInicio` date DEFAULT NULL,
  `fechaFin` date DEFAULT NULL,
  `Promocion_id` int(11) NOT NULL,
  `Cliente_id` int(11) NOT NULL,
  PRIMARY KEY (`id`,`Cliente_id`,`Promocion_id`),
  KEY `fk_PublicidadCliente_Promocion1_idx` (`Promocion_id`),
  KEY `fk_PublicidadCliente_Cliente1_idx` (`Cliente_id`),
  CONSTRAINT `fk_PublicidadCliente_Cliente1` FOREIGN KEY (`Cliente_id`) REFERENCES `cliente` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_PublicidadCliente_Promocion1` FOREIGN KEY (`Promocion_id`) REFERENCES `promocion` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Publicidad`
--

LOCK TABLES `Publicidad` WRITE;
/*!40000 ALTER TABLE `Publicidad` DISABLE KEYS */;
/*!40000 ALTER TABLE `Publicidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Sala`
--

DROP TABLE IF EXISTS `Sala`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Sala` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `Sala_id_nombre_bc326327_uniq` (`id`,`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Sala`
--

LOCK TABLES `Sala` WRITE;
/*!40000 ALTER TABLE `Sala` DISABLE KEYS */;
/*!40000 ALTER TABLE `Sala` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Stock`
--

DROP TABLE IF EXISTS `Stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Stock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantProv` int(11) DEFAULT NULL,
  `cantTotal` int(11) DEFAULT NULL,
  `Producto_id` int(11) NOT NULL,
  `Proveedor_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Stock_id_Proveedor_id_Producto_id_8c0fd827_uniq` (`id`,`Proveedor_id`,`Producto_id`),
  KEY `Stock_Producto_id_432a478e_fk_Producto_id` (`Producto_id`),
  KEY `Stock_Proveedor_id_0a4bb0d0_fk_Proveedor_id` (`Proveedor_id`),
  CONSTRAINT `Stock_Producto_id_432a478e_fk_Producto_id` FOREIGN KEY (`Producto_id`) REFERENCES `producto` (`id`),
  CONSTRAINT `Stock_Proveedor_id_0a4bb0d0_fk_Proveedor_id` FOREIGN KEY (`Proveedor_id`) REFERENCES `proveedor` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Stock`
--

LOCK TABLES `Stock` WRITE;
/*!40000 ALTER TABLE `Stock` DISABLE KEYS */;
/*!40000 ALTER TABLE `Stock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipoempleado`
--

DROP TABLE IF EXISTS `tipoempleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tipoempleado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipoempleado`
--

LOCK TABLES `tipoempleado` WRITE;
/*!40000 ALTER TABLE `tipoempleado` DISABLE KEYS */;
INSERT INTO `tipoempleado` VALUES (1,'Encargado'),(2,'Basico');
/*!40000 ALTER TABLE `tipoempleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipoHorarioEmpleado`
--

DROP TABLE IF EXISTS `tipoHorarioEmpleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tipoHorarioEmpleado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipoHorarioEmpleado`
--

LOCK TABLES `tipoHorarioEmpleado` WRITE;
/*!40000 ALTER TABLE `tipoHorarioEmpleado` DISABLE KEYS */;
INSERT INTO `tipoHorarioEmpleado` VALUES (1,'Mañana'),(2,'Tarde'),(3,'Libra'),(4,'Dobla');
/*!40000 ALTER TABLE `tipoHorarioEmpleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipoProducto`
--

DROP TABLE IF EXISTS `tipoProducto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tipoProducto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipoProducto`
--

LOCK TABLES `tipoProducto` WRITE;
/*!40000 ALTER TABLE `tipoProducto` DISABLE KEYS */;
INSERT INTO `tipoProducto` VALUES (1,'Uso'),(2,'Venta');
/*!40000 ALTER TABLE `tipoProducto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipousuario`
--

DROP TABLE IF EXISTS `tipousuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tipousuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipousuario`
--

LOCK TABLES `tipousuario` WRITE;
/*!40000 ALTER TABLE `tipousuario` DISABLE KEYS */;
INSERT INTO `tipousuario` VALUES (1,'Cliente'),(2,'Encargado');
/*!40000 ALTER TABLE `tipousuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TipoZona`
--

DROP TABLE IF EXISTS `TipoZona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `TipoZona` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TipoZona`
--

LOCK TABLES `TipoZona` WRITE;
/*!40000 ALTER TABLE `TipoZona` DISABLE KEYS */;
INSERT INTO `TipoZona` VALUES (1,'Facial'),(2,'Corporal');
/*!40000 ALTER TABLE `TipoZona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tratamiento`
--

DROP TABLE IF EXISTS `Tratamiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Tratamiento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `descripcion` longtext,
  `duracion` int(11) DEFAULT NULL,
  `precio` double DEFAULT NULL,
  `espera` int(11) DEFAULT NULL,
  `Maquina_id` int(11) NOT NULL,
  `Producto_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `Tratamiento_id_nombre_Maquina_id_Producto_id_dabde96c_uniq` (`id`,`nombre`,`Maquina_id`,`Producto_id`),
  KEY `Tratamiento_Maquina_id_dfb35914_fk_Maquina_id` (`Maquina_id`),
  KEY `Tratamiento_Producto_id_8a4cba22_fk_Producto_id` (`Producto_id`),
  CONSTRAINT `Tratamiento_Maquina_id_dfb35914_fk_Maquina_id` FOREIGN KEY (`Maquina_id`) REFERENCES `maquina` (`id`),
  CONSTRAINT `Tratamiento_Producto_id_8a4cba22_fk_Producto_id` FOREIGN KEY (`Producto_id`) REFERENCES `producto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tratamiento`
--

LOCK TABLES `Tratamiento` WRITE;
/*!40000 ALTER TABLE `Tratamiento` DISABLE KEYS */;
/*!40000 ALTER TABLE `Tratamiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_customuser`
--

DROP TABLE IF EXISTS `usuarios_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `usuarios_customuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_client` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_customuser`
--

LOCK TABLES `usuarios_customuser` WRITE;
/*!40000 ALTER TABLE `usuarios_customuser` DISABLE KEYS */;
INSERT INTO `usuarios_customuser` VALUES (1,'pbkdf2_sha256$120000$0nmWXkTJfblS$ts9lJfTpGOIJHulm5NOjvLXYjdXRUZeiGxYyPc0Ivak=','2019-05-12 17:05:00.810293',1,'admin','','','admin@cleo.com',1,1,'2019-05-12 12:17:20.214268',0);
/*!40000 ALTER TABLE `usuarios_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_customuser_groups`
--

DROP TABLE IF EXISTS `usuarios_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `usuarios_customuser_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuarios_customuser_groups_customuser_id_group_id_aace3972_uniq` (`customuser_id`,`group_id`),
  KEY `usuarios_customuser_groups_group_id_155d554c_fk_auth_group_id` (`group_id`),
  CONSTRAINT `usuarios_customuser__customuser_id_9e05d670_fk_usuarios_` FOREIGN KEY (`customuser_id`) REFERENCES `usuarios_customuser` (`id`),
  CONSTRAINT `usuarios_customuser_groups_group_id_155d554c_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_customuser_groups`
--

LOCK TABLES `usuarios_customuser_groups` WRITE;
/*!40000 ALTER TABLE `usuarios_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_customuser_user_permissions`
--

DROP TABLE IF EXISTS `usuarios_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `usuarios_customuser_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customuser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuarios_customuser_user_customuser_id_permission_8dac6e14_uniq` (`customuser_id`,`permission_id`),
  KEY `usuarios_customuser__permission_id_9a10b097_fk_auth_perm` (`permission_id`),
  CONSTRAINT `usuarios_customuser__customuser_id_c016378e_fk_usuarios_` FOREIGN KEY (`customuser_id`) REFERENCES `usuarios_customuser` (`id`),
  CONSTRAINT `usuarios_customuser__permission_id_9a10b097_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_customuser_user_permissions`
--

LOCK TABLES `usuarios_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `usuarios_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-12 22:56:30
