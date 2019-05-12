/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50642
Source Host           : localhost:3306
Source Database       : demo1

Target Server Type    : MYSQL
Target Server Version : 50642
File Encoding         : 65001

Date: 2019-05-12 23:53:59
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('197bba1c1835');

-- ----------------------------
-- Table structure for city
-- ----------------------------
DROP TABLE IF EXISTS `city`;
CREATE TABLE `city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `pid` int(11) DEFAULT NULL,
  `path` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of city
-- ----------------------------
INSERT INTO `city` VALUES ('1', '北京', '0', '0,');
INSERT INTO `city` VALUES ('2', '河北', '0', '0,');
INSERT INTO `city` VALUES ('3', '石家庄', '2', '0,2,');
INSERT INTO `city` VALUES ('4', '海淀区', '1', '0,1,');
INSERT INTO `city` VALUES ('5', '河南省', '0', '0,');
INSERT INTO `city` VALUES ('6', '裕华区', '3', '0,2,3,');
INSERT INTO `city` VALUES ('7', '知春路', '4', '0,1,4,');
INSERT INTO `city` VALUES ('8', '保定市', '2', '0,2,');
INSERT INTO `city` VALUES ('9', '郑州市', '5', '0,5,');
INSERT INTO `city` VALUES ('10', 'laishui', '8', '0,2,8');
INSERT INTO `city` VALUES ('11', 'laishui', '8', '0,2,8');
INSERT INTO `city` VALUES ('12', 'laishui', '8', '0,2,8');
INSERT INTO `city` VALUES ('13', 'laishui', '8', '0,2,8');

-- ----------------------------
-- Table structure for tbl_role
-- ----------------------------
DROP TABLE IF EXISTS `tbl_role`;
CREATE TABLE `tbl_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tbl_role
-- ----------------------------
INSERT INTO `tbl_role` VALUES ('1', '管理员', '1', '2019-05-11 11:57:22');
INSERT INTO `tbl_role` VALUES ('5', '电视管理员', '1', '2019-05-12 10:23:38');

-- ----------------------------
-- Table structure for tbl_rule
-- ----------------------------
DROP TABLE IF EXISTS `tbl_rule`;
CREATE TABLE `tbl_rule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `src` varchar(128) DEFAULT NULL,
  `pid` int(11) DEFAULT NULL,
  `path` varchar(128) DEFAULT NULL,
  `menu` smallint(6) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tbl_rule
-- ----------------------------
INSERT INTO `tbl_rule` VALUES ('1', '用户管理', '/user', '0', '0,', '1', '1', '2019-05-12 16:47:08');
INSERT INTO `tbl_rule` VALUES ('2', '用户列表', '/user', '1', '0,1,', '1', '1', '2019-05-12 19:21:57');
INSERT INTO `tbl_rule` VALUES ('3', '添加用户', '/user/insert', '1', '0,1,', '1', '1', '2019-05-12 19:22:41');
INSERT INTO `tbl_rule` VALUES ('4', '编辑用户', '/user/update', '1', '0,1,', '0', '1', '2019-05-12 19:23:50');
INSERT INTO `tbl_rule` VALUES ('6', '套餐管理', '/taocan', '0', '0,', '1', '1', '2019-05-12 19:27:34');
INSERT INTO `tbl_rule` VALUES ('7', '套餐列表', '/taocan', '6', '0,6,', '1', '1', '2019-05-12 19:28:25');
INSERT INTO `tbl_rule` VALUES ('13', '删除套餐', '/taocan/del', '6', '0,6,', '0', '1', '2019-05-12 19:33:56');
INSERT INTO `tbl_rule` VALUES ('16', '跑马灯管理', '/marquee', '0', '0,', '1', '1', '2019-05-12 23:00:13');
INSERT INTO `tbl_rule` VALUES ('17', '跑马灯列表', '/marquee', '16', '0,16,', '1', '1', '2019-05-12 23:00:51');
INSERT INTO `tbl_rule` VALUES ('18', '添加跑马灯', '/marquee/insert', '16', '0,16,', '1', '1', '2019-05-12 23:02:16');

-- ----------------------------
-- Table structure for tbl_rule_role
-- ----------------------------
DROP TABLE IF EXISTS `tbl_rule_role`;
CREATE TABLE `tbl_rule_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `roleid` int(11) DEFAULT NULL,
  `ruleid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `roleid` (`roleid`),
  KEY `ruleid` (`ruleid`),
  CONSTRAINT `tbl_rule_role_ibfk_1` FOREIGN KEY (`roleid`) REFERENCES `tbl_role` (`id`),
  CONSTRAINT `tbl_rule_role_ibfk_2` FOREIGN KEY (`ruleid`) REFERENCES `tbl_rule` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of tbl_rule_role
-- ----------------------------

-- ----------------------------
-- Table structure for tbl_user
-- ----------------------------
DROP TABLE IF EXISTS `tbl_user`;
CREATE TABLE `tbl_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `password` varchar(128) NOT NULL,
  `status` smallint(6) DEFAULT '1',
  `addtime` datetime DEFAULT NULL,
  `roleid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `roleid` (`roleid`),
  CONSTRAINT `tbl_user_ibfk_1` FOREIGN KEY (`roleid`) REFERENCES `tbl_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tbl_user
-- ----------------------------
INSERT INTO `tbl_user` VALUES ('2', 'zhong', '1123456', '0', '2019-05-11 10:57:52', '1');
INSERT INTO `tbl_user` VALUES ('3', 'xiao', '1234561', '0', '2019-05-11 10:57:52', '1');
INSERT INTO `tbl_user` VALUES ('6', 'fuqiang', 'e10adc3949ba59abbe56e057f20f883e', '1', '2019-05-11 18:33:18', '5');
INSERT INTO `tbl_user` VALUES ('7', 'guoyuan', '0e9212587d373ca58e9bada0c15e6fe4', '1', '2019-05-11 18:39:38', '1');
