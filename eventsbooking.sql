-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 20, 2024 at 09:37 PM
-- Server version: 8.3.0
-- PHP Version: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `eventsbooking`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add user', 2, 'add_user'),
(6, 'Can change user', 2, 'change_user'),
(7, 'Can delete user', 2, 'delete_user'),
(8, 'Can view user', 2, 'view_user'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add permission', 4, 'add_permission'),
(14, 'Can change permission', 4, 'change_permission'),
(15, 'Can delete permission', 4, 'delete_permission'),
(16, 'Can view permission', 4, 'view_permission'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add ticket type', 7, 'add_tickettype'),
(26, 'Can change ticket type', 7, 'change_tickettype'),
(27, 'Can delete ticket type', 7, 'delete_tickettype'),
(28, 'Can view ticket type', 7, 'view_tickettype'),
(29, 'Can add event category', 8, 'add_eventcategory'),
(30, 'Can change event category', 8, 'change_eventcategory'),
(31, 'Can delete event category', 8, 'delete_eventcategory'),
(32, 'Can view event category', 8, 'view_eventcategory'),
(33, 'Can add event', 9, 'add_event'),
(34, 'Can change event', 9, 'change_event'),
(35, 'Can delete event', 9, 'delete_event'),
(36, 'Can view event', 9, 'view_event'),
(37, 'Can add booking', 10, 'add_booking'),
(38, 'Can change booking', 10, 'change_booking'),
(39, 'Can delete booking', 10, 'delete_booking'),
(40, 'Can view booking', 10, 'view_booking');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$870000$4FGzE0CTXxwC2uHMLTdWIr$Hkh7mka6uyVGL9iit5EEraOutITTvtkTWIoCmw0JXpg=', '2024-11-20 21:36:09.891492', 1, 'paulmp', '', '', 'paulmbui1@outlook.com', 1, 1, '2024-11-20 19:44:59.804634');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-11-20 19:46:20.116115', '1', 'music', 1, '[{\"added\": {}}]', 8, 1),
(2, '2024-11-20 19:46:40.886074', '2', 'proffesional', 1, '[{\"added\": {}}]', 8, 1),
(3, '2024-11-20 19:46:56.129724', '3', 'tech', 1, '[{\"added\": {}}]', 8, 1),
(4, '2024-11-20 19:56:50.424879', '1', 'Amakulture', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Regular - Amakulture (1500 KSH)\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"VIP - Amakulture (3000 KSH)\"}}]', 9, 1),
(5, '2024-11-20 20:01:01.659389', '2', 'Staff Finance Wellness Training & Personalized Money Coaching', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Regular - Staff Finance Wellness Training & Personalized Money Coaching (2000 KSH)\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Early Bird - Staff Finance Wellness Training & Personalized Money Coaching (1800 KSH)\"}}]', 9, 1),
(6, '2024-11-20 20:03:18.800563', '2', 'Finance Wellness Training', 2, '[{\"changed\": {\"fields\": [\"Name\", \"Category\"]}}]', 9, 1),
(7, '2024-11-20 20:06:08.846063', '3', 'Murima Sundowner', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Advanced - Murima Sundowner (1000 KSH)\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Regular - Murima Sundowner (1500 KSH)\"}}]', 9, 1),
(8, '2024-11-20 20:12:36.301167', '4', 'K-POP FEST KE 2024', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Regular - K-POP FEST KE 2024 (1000 KSH)\"}}]', 9, 1),
(9, '2024-11-20 20:15:16.740762', '5', 'East Africa Community Festivals', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"VIP - East Africa Community Festivals (3000 KSH)\"}}]', 9, 1),
(10, '2024-11-20 20:19:50.456531', '6', 'Son of Royalty 2', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Regular - Son of Royalty 2 (1500 KSH)\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Couple - Son of Royalty 2 (2600 KSH)\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Group of 5 - Son of Royalty 2 (6000 KSH)\"}}]', 9, 1),
(11, '2024-11-20 20:20:33.983767', '5', 'EAC Festivals', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 9, 1),
(12, '2024-11-20 20:24:20.197159', '7', 'Motown in Nairobi', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Advanced - Motown in Nairobi (3500 KSH)\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Regular - Motown in Nairobi (3700 KSH)\"}}]', 9, 1),
(13, '2024-11-20 20:33:03.289727', '8', '2024 IRSK Conference', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"IRSK Members - 2024 IRSK Conference (8000 KSH)\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Non-Members - 2024 IRSK Conference (10000 KSH)\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"International Participants - 2024 IRSK Conference (13000 KSH)\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Students - 2024 IRSK Conference (4000 KSH)\"}}]', 9, 1),
(14, '2024-11-20 20:34:25.728623', '4', 'comedy', 1, '[{\"added\": {}}]', 8, 1),
(15, '2024-11-20 20:40:41.966688', '9', 'An Evening with Muthaka 4', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Couples Ticket - An Evening with Muthaka 4 (2000 KSH)\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Advance Ticket - An Evening with Muthaka 4 (2500 KSH)\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Super Sunshiner Ticket - An Evening with Muthaka 4 (3000 KSH)\"}}]', 9, 1),
(16, '2024-11-20 20:42:41.601827', '5', 'movie', 1, '[{\"added\": {}}]', 8, 1),
(17, '2024-11-20 20:43:06.424615', '6', 'game', 1, '[{\"added\": {}}]', 8, 1),
(18, '2024-11-20 20:52:22.001718', '10', 'Tunes from Africa', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"VIP - Tunes from Africa (3000 KSH)\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"VVIP - Tunes from Africa (5000 KSH)\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Regular - Tunes from Africa (1000 KSH)\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Student - with ID - Tunes from Africa (500 KSH)\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Student with ID - group of 3 - Tunes from Africa (1300 KSH)\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Student with ID - group of 4 - Tunes from Africa (1700 KSH)\"}}]', 9, 1),
(19, '2024-11-20 21:28:02.068425', '11', 'Pandora\'s Box', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Regular - Pandora\'s Box (1000 KSH)\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"VIP - Pandora\'s Box (2000 KSH)\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Group of 5 Ticket - Pandora\'s Box (4000 KSH)\"}}]', 9, 1),
(20, '2024-11-20 21:33:12.959096', '12', 'Ties that Bind', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Advance Flashsale - Ties that Bind (700 KSH)\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Student Ticket - Ties that Bind (500 KSH)\"}}, {\"added\": {\"name\": \"ticket type\", \"object\": \"Regular - Ties that Bind (1000 KSH)\"}}]', 9, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'user'),
(3, 'auth', 'group'),
(4, 'auth', 'permission'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'events', 'tickettype'),
(8, 'events', 'eventcategory'),
(9, 'events', 'event'),
(10, 'events', 'booking');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-11-20 19:05:29.659845'),
(2, 'auth', '0001_initial', '2024-11-20 19:05:36.851303'),
(3, 'admin', '0001_initial', '2024-11-20 19:05:40.952723'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-11-20 19:05:40.963329'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-11-20 19:05:40.970622'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-11-20 19:05:42.330222'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-11-20 19:05:42.532259'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-11-20 19:05:42.684500'),
(9, 'auth', '0004_alter_user_username_opts', '2024-11-20 19:05:42.691920'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-11-20 19:05:42.952009'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-11-20 19:05:42.953090'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-11-20 19:05:42.979642'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-11-20 19:05:43.153733'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-11-20 19:05:43.727443'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-11-20 19:05:44.062404'),
(16, 'auth', '0011_update_proxy_permissions', '2024-11-20 19:05:44.071202'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-11-20 19:05:44.388840'),
(18, 'events', '0001_initial', '2024-11-20 19:26:35.181585'),
(19, 'sessions', '0001_initial', '2024-11-20 19:26:35.335647');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('ziysogu649v6vpweemnnmg8pbqeqf93a', '.eJxVjMsOwiAQRf-FtSFAeQwu3fsNBIZBqgaS0q6M_65NutDtPefcFwtxW2vYBi1hzuzMJDv9binig9oO8j22W-fY27rMie8KP-jg157peTncv4MaR_3WUaIv5AREcjKBIUMaJ4VQfDaJgIRVQkiYbMq2oPeASiVj_SRAa-3Y-wPy_DeI:1tDqdd:z1B7-iy1kZ_JxTCE7ps41ZBuU5ICC6scOe4mG7GPdgE', '2024-12-04 19:45:21.625733'),
('h1wf7u3kagzgvw0cgn3ned93l67l3xuv', '.eJxVjMsOwiAQRf-FtSFAeQwu3fsNBIZBqgaS0q6M_65NutDtPefcFwtxW2vYBi1hzuzMJDv9binig9oO8j22W-fY27rMie8KP-jg157peTncv4MaR_3WUaIv5AREcjKBIUMaJ4VQfDaJgIRVQkiYbMq2oPeASiVj_SRAa-3Y-wPy_DeI:1tDsMr:98xW5Buhm95PgJHbxe_ISb1MHq7jNfdQ9G36iRCP1zs', '2024-12-04 21:36:09.893344');

-- --------------------------------------------------------

--
-- Table structure for table `events_booking`
--

DROP TABLE IF EXISTS `events_booking`;
CREATE TABLE IF NOT EXISTS `events_booking` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(65) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `booked_on` datetime(6) NOT NULL,
  `number_of_tickets` int UNSIGNED NOT NULL,
  `total_price` decimal(10,2) DEFAULT NULL,
  `status` varchar(50) NOT NULL,
  `event_id` bigint NOT NULL,
  `ticket_type_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `events_booking_event_id_e3561e88` (`event_id`),
  KEY `events_booking_ticket_type_id_12168215` (`ticket_type_id`)
) ;

--
-- Dumping data for table `events_booking`
--

INSERT INTO `events_booking` (`id`, `name`, `email`, `phone`, `booked_on`, `number_of_tickets`, `total_price`, `status`, `event_id`, `ticket_type_id`) VALUES
(1, 'Paul mbui', 'paulmbui1@outlook.com', '0110048030', '2024-11-20 21:17:36.909827', 1, 1500.00, 'Pending', 1, 1),
(2, 'Paul mbui', 'paulmbui1@outlook.com', '0110048030', '2024-11-20 21:18:57.060195', 1, 3000.00, 'Pending', 1, 2),
(3, 'everline moige', 'faradaymayaka722@gmail.com', '0718219902', '2024-11-20 21:22:39.193566', 1, 3000.00, 'Pending', 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `events_event`
--

DROP TABLE IF EXISTS `events_event`;
CREATE TABLE IF NOT EXISTS `events_event` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(65) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `location` varchar(65) NOT NULL,
  `image` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `slug` varchar(50) NOT NULL,
  `user_id` int NOT NULL,
  `category_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `events_event_user_id_39865209` (`user_id`),
  KEY `events_event_category_id_01d3a3ab` (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `events_event`
--

INSERT INTO `events_event` (`id`, `name`, `date`, `time`, `location`, `image`, `description`, `slug`, `user_id`, `category_id`) VALUES
(1, 'Amakulture', '2024-12-06', '16:00:00.000000', 'Masshouse, Ngong Racecourse', 'events/main_photo_1731926984.jpeg', 'Amakulture at Masshouse, Ngong Racecourse hosted by Rave kenya From: Friday, December 6, 2024, 16:00\r\n\r\nTo: Saturday, December 7, 2024', 'Amakulture', 1, 3),
(2, 'Finance Wellness Training', '2024-12-30', '17:00:00.000000', 'Online', 'events/main_photo_1731672072.jpg', 'Staff Finance Wellness Training & Personalized Money Coaching\r\nFrom: Monday, November 18, 2024, 07:00\r\n\r\nTo: December 20, 2024, 17:00\r\n\r\nVenue: Online\r\n\r\nHost: Attique Money Academy\r\n\r\nDescription:', 'staff-finance-wellness-training-personalized-money', 1, 2),
(3, 'Murima Sundowner', '2024-11-14', '18:00:00.000000', 'Kisementi Gardens, Limuru', 'events/1731321475.jpeg', 'Step into a serene, cultural haven with our Kikuyu Park & Chill Sundowner, a unique event celebrating Kikuyu heritage with an enchanting twist of modern chill vibes. Join us on December 14th, 2024, at the picturesque Kisementi Gardens in Limuru for an unforgettable evening filled with music, relaxation, and tradition under the warm hues of the setting sun.\r\nSettle down for a cozy picnic or bring along friends to enjoy the rich atmosphere of Kikuyu culture. We’ve got the ultimate Mugithi experience lined up with none other than DJ Dibul, the best in the Mugithi scene, who will have everyone on their feet, dancing the evening away!\r\nEvent Details:\r\n•⁠  ⁠Date: December 14th, 2024\r\n•⁠  ⁠Location: Kisementi Gardens, Limuru\r\n•⁠  ⁠Time: 3 PM – 10 PM', 'murima-sundowner', 1, 1),
(4, 'K-POP FEST KE 2024', '2024-12-07', '17:00:00.000000', 'TBA', 'events/gev_874_banner_pic_1.png', 'From live K-pop dance performances to interactive K-drama sessions and exclusive K-beauty demonstrations, this event promises an immersive experience for all K-culture enthusiasts. Expect fun activities and an authentic taste of Korea’s most popular cultural elements—all in one place!', 'k-pop-fest-ke-2024', 1, 1),
(5, 'EAC Festivals', '2024-12-05', '20:00:00.000000', 'Hyatt Regency Nairobi Westlands', 'events/gev_872_banner_pic.png', 'East Africa Community Silver Jubilee Celebrations', 'east-africa-community-festivals', 1, 2),
(6, 'Son of Royalty 2', '2024-11-30', '16:00:00.000000', 'daystar university', 'events/gev_855_banner_pic.jpg', 'With his dynamic stage presence and unique sound, Dalian will take you on a musical journey that blends contemporary beats with classic influences, creating a truly immersive experience. Whether you\'re a long-time fan or new to his music, this is your chance to witness a one-of-a-kind concert that promises to be nothing short of extraordinary. Don’t miss out on this', 'son-of-royalty-2', 1, 1),
(7, 'Motown in Nairobi', '2024-11-30', '19:00:00.000000', 'The Waterfront Karen', 'events/gev_869_banner_pic.jpg', 'Motown in Nairobi explores music from the Motown record label, through the decades, performed by carefully selected singers and instrumentalists, who are really fun performers to watch.', 'motown-in-nairobi', 1, 1),
(8, '2024 IRSK Conference', '2024-11-22', '08:00:00.000000', 'Hyatt Regency Nairobi Westlands', 'events/gev_830_banner_pic.jpg', 'COMESA, IRSK, ACCORD and ACSUS, will host the Second IRSK Annual Conference from November 20-22, 2024, in Nairobi. The conference is themed \"Fostering Integration and Cooperation in the COMESA Region', '2024-irsk-conference', 1, 3),
(9, 'An Evening with Muthaka 4', '2024-12-07', '18:00:00.000000', 'Baraza Media Lab, Riverside', 'events/EveningMuthaka.jpeg', 'An Evening with Muthaka 4\r\n Baraza Media Lab, Riverside\r\n\r\n 7th December 2024\r\n\r\n 1500', 'an-evening-with-muthaka-4', 1, 4),
(10, 'Tunes from Africa', '2024-11-23', '16:30:00.000000', 'Nairobi Cinema', 'events/TunesfromAfrica.jpeg', 'Wazalendo Concert', 'tunes-from-africa', 1, 1),
(11, 'Pandora\'s Box', '2024-12-07', '15:00:00.000000', 'Nimpa Theatre,Zimmerman', 'events/Pandora.jpeg', 'Pandora\'s Box\r\n Nimpa Theatre,Zimmerman\r\n\r\n 7th & 8th December 2024', 'pandoras-box', 1, 5),
(12, 'Ties that Bind', '2024-11-30', '15:00:00.000000', 'Jalaram Auditorium', 'events/TiesBind.jpeg', 'Ties that Bind\r\n Jalaram Auditorium\r\n\r\n Sat 30th Nov 2024', 'ties-that-bind', 1, 5);

-- --------------------------------------------------------

--
-- Table structure for table `events_eventcategory`
--

DROP TABLE IF EXISTS `events_eventcategory`;
CREATE TABLE IF NOT EXISTS `events_eventcategory` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(65) NOT NULL,
  `description` longtext,
  `slug` varchar(65) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `events_eventcategory`
--

INSERT INTO `events_eventcategory` (`id`, `name`, `description`, `slug`) VALUES
(1, 'music', '', 'music'),
(2, 'proffesional', '', 'professional'),
(3, 'tech', '', 'tech'),
(4, 'comedy', '', 'comedy'),
(5, 'movie', '', 'movie'),
(6, 'game', '', 'game');

-- --------------------------------------------------------

--
-- Table structure for table `events_tickettype`
--

DROP TABLE IF EXISTS `events_tickettype`;
CREATE TABLE IF NOT EXISTS `events_tickettype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(65) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `available_quantity` int UNSIGNED NOT NULL,
  `event_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `events_tickettype_event_id_9ef8a4b2` (`event_id`)
) ;

--
-- Dumping data for table `events_tickettype`
--

INSERT INTO `events_tickettype` (`id`, `name`, `price`, `available_quantity`, `event_id`) VALUES
(1, 'Regular', 1500.00, 49, 1),
(2, 'VIP', 3000.00, 8, 1),
(3, 'Regular', 2000.00, 50, 2),
(4, 'Early Bird', 1800.00, 5, 2),
(5, 'Advanced', 1000.00, 10, 3),
(6, 'Regular', 1500.00, 40, 3),
(7, 'Regular', 1000.00, 150, 4),
(8, 'VIP', 3000.00, 50, 5),
(9, 'Regular', 1500.00, 100, 6),
(10, 'Couple', 2600.00, 30, 6),
(11, 'Group of 5', 6000.00, 10, 6),
(12, 'Advanced', 3500.00, 20, 7),
(13, 'Regular', 3700.00, 30, 7),
(14, 'IRSK Members', 8000.00, 50, 8),
(15, 'Non-Members', 10000.00, 30, 8),
(16, 'International Participants', 13000.00, 30, 8),
(17, 'Students', 4000.00, 40, 8),
(18, 'Couples Ticket', 2000.00, 10, 9),
(19, 'Advance Ticket', 2500.00, 10, 9),
(20, 'Super Sunshiner Ticket', 3000.00, 20, 9),
(21, 'VIP', 3000.00, 20, 10),
(22, 'VVIP', 5000.00, 10, 10),
(23, 'Regular', 1000.00, 50, 10),
(24, 'Student - with ID', 500.00, 20, 10),
(25, 'Student with ID - group of 3', 1300.00, 10, 10),
(26, 'Student with ID - group of 4', 1700.00, 5, 10),
(27, 'Regular', 1000.00, 40, 11),
(28, 'VIP', 2000.00, 20, 11),
(29, 'Group of 5 Ticket', 4000.00, 10, 11),
(30, 'Advance Flashsale', 700.00, 20, 12),
(31, 'Student Ticket', 500.00, 30, 12),
(32, 'Regular', 1000.00, 50, 12);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
