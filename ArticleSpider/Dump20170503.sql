CREATE DATABASE  IF NOT EXISTS `article_spider` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `article_spider`;
-- MySQL dump 10.13  Distrib 5.6.17, for Win32 (x86)
--
-- Host: 127.0.0.1    Database: article_spider
-- ------------------------------------------------------
-- Server version	5.6.35-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `jobbole_article`
--

DROP TABLE IF EXISTS `jobbole_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobbole_article` (
  `title` varchar(200) DEFAULT NULL,
  `create_date` date NOT NULL,
  `url` varchar(512) DEFAULT NULL,
  `url_object_id` varchar(50) DEFAULT NULL,
  `front_image_url` varchar(300) DEFAULT NULL,
  `front_image_path` varchar(200) DEFAULT NULL,
  `praise_nums` int(11) NOT NULL DEFAULT '0',
  `comment_nums` int(11) NOT NULL DEFAULT '0',
  `fav_nums` int(11) NOT NULL DEFAULT '0',
  `tags` varchar(256) DEFAULT NULL,
  `content` longtext
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobbole_article`
--

LOCK TABLES `jobbole_article` WRITE;
/*!40000 ALTER TABLE `jobbole_article` DISABLE KEYS */;
INSERT INTO `jobbole_article` VALUES ('致敬！这些老外的开源技术养活了一票国产软件-jobbole','2017-05-02','http://blog.jobbole.com/111056/',NULL,NULL,NULL,0,0,0,NULL,NULL),('Linux 下网络协议分析器 Wireshark 使用基础-jobbole','2017-05-02','http://blog.jobbole.com/111051/',NULL,NULL,NULL,0,0,1,NULL,NULL),('不惜一切代价，远离这 10 种不靠谱的同事-jobbole','2017-05-02','http://blog.jobbole.com/111020/',NULL,NULL,NULL,0,0,1,NULL,NULL),('关于 Linux 进程你所需要知道的一切-jobbole','2017-05-02','http://blog.jobbole.com/111053/',NULL,NULL,NULL,0,0,3,NULL,NULL),('最大成人网站的安全做得比某些安全公司还要好！-jobbole','2017-05-02','http://blog.jobbole.com/111025/',NULL,NULL,NULL,0,0,1,NULL,NULL),('Ubuntu 放弃战斗，Linux 桌面的悲哀-jobbole','2017-05-02','http://blog.jobbole.com/111038/',NULL,NULL,NULL,0,0,2,NULL,NULL),('我为什么不在乎人工智能-jobbole','2017-05-02','http://blog.jobbole.com/111027/',NULL,NULL,NULL,0,0,1,NULL,NULL),('25 个常用的 Linux iptables 规则-jobbole','2017-05-02','http://blog.jobbole.com/108468/',NULL,NULL,NULL,0,0,7,NULL,NULL),('Windows 纸牌游戏是我开发的，但我没从中拿到一分钱-jobbole','2017-05-02','http://blog.jobbole.com/111005/',NULL,NULL,NULL,0,0,0,NULL,NULL),('2016 年度顶级开源创作工具-jobbole','2017-05-02','http://blog.jobbole.com/111012/',NULL,NULL,NULL,0,0,3,NULL,NULL),('数据工程师的崛起-jobbole','2017-05-02','http://blog.jobbole.com/110985/',NULL,NULL,NULL,0,0,5,NULL,NULL),('这个时代会残酷惩罚不肯改变的人-jobbole','2017-05-02','http://blog.jobbole.com/111017/',NULL,NULL,NULL,0,0,10,NULL,NULL),('谷歌人工智能背后的大脑-jobbole','2017-05-02','http://blog.jobbole.com/110925/',NULL,NULL,NULL,0,0,2,NULL,NULL),('边工作边带娃，我是如何在 1 年内拿到第 2 个学位和 5 个开发者认证的-jobbole','2017-05-02','http://blog.jobbole.com/110986/',NULL,NULL,NULL,0,0,11,NULL,NULL),('在苹果工作 12 年学到的创新经验-jobbole','2017-05-02','http://blog.jobbole.com/110957/',NULL,NULL,NULL,0,0,1,NULL,NULL),('千万千万不要运行的 Linux 命令-jobbole','2017-05-02','http://blog.jobbole.com/110923/',NULL,NULL,NULL,0,0,7,NULL,NULL),('通过这 9 本开源书，学好 C++-jobbole','2017-05-02','http://blog.jobbole.com/110975/',NULL,NULL,NULL,0,0,21,NULL,NULL),('机器学习流行趋势一览-jobbole','2017-05-02','http://blog.jobbole.com/110976/',NULL,NULL,NULL,0,0,2,NULL,NULL),('35，40 甚至 50 岁转行做软件开发晚吗？看这 10 个成功故事-jobbole','2017-05-02','http://blog.jobbole.com/110962/',NULL,NULL,NULL,0,0,6,NULL,NULL),('趣文：什么时候该加入创业公司？-jobbole','2017-05-02','http://blog.jobbole.com/111034/',NULL,NULL,NULL,0,0,3,NULL,NULL);
/*!40000 ALTER TABLE `jobbole_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhihu_answer`
--

DROP TABLE IF EXISTS `zhihu_answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhihu_answer` (
  `zhihu_id` bigint(20) NOT NULL,
  `url` varchar(300) NOT NULL,
  `question_id` bigint(20) NOT NULL,
  `author_id` varchar(100) DEFAULT NULL,
  `content` longtext NOT NULL COMMENT '评论内容',
  `praise_num` int(11) NOT NULL DEFAULT '0',
  `comments_num` int(11) NOT NULL DEFAULT '0' COMMENT '评论数量',
  `create_time` date NOT NULL,
  `update_time` date NOT NULL,
  `crawl_time` datetime NOT NULL COMMENT '爬取时间',
  `crawl_update_time` datetime DEFAULT NULL COMMENT '爬取更新时间',
  PRIMARY KEY (`zhihu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhihu_answer`
--

LOCK TABLES `zhihu_answer` WRITE;
/*!40000 ALTER TABLE `zhihu_answer` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhihu_answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zhihu_questions`
--

DROP TABLE IF EXISTS `zhihu_questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zhihu_questions` (
  `zhihu_id` bigint(20) NOT NULL,
  `topics` varchar(255) DEFAULT NULL,
  `url` varchar(300) NOT NULL,
  `title` varchar(300) NOT NULL,
  `content` longtext NOT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `answer_num` int(11) NOT NULL DEFAULT '0',
  `comments_num` int(11) NOT NULL DEFAULT '0' COMMENT '关注问题数量',
  `watch_user_num` int(11) NOT NULL DEFAULT '0' COMMENT '查看数量',
  `click_num` int(11) NOT NULL DEFAULT '0' COMMENT '点击数',
  `crawl_time` datetime DEFAULT NULL COMMENT '爬取时间',
  `crawl_update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`zhihu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zhihu_questions`
--

LOCK TABLES `zhihu_questions` WRITE;
/*!40000 ALTER TABLE `zhihu_questions` DISABLE KEYS */;
/*!40000 ALTER TABLE `zhihu_questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'article_spider'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-05-03 17:42:19
