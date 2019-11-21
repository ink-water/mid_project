SET NAMES utf8;
drop database IF EXISTS `chat`;
create DATABASE `chat` CHARSET=utf8;
USE `chat`;

--
-- 公会聊天记录 so_chat
--

create TABLE `so_chat`(
    `id`    INT PRIMARY KEY AUTO_INCREMENT,
    `sid`   INT INDEX,
    `name`  VARCHAR(32) UNIQUE,
    `img`   MEDIUMBLOB,
    `content`   VARCHAR(64),
    `record_time`   DATATIME DEFAULT now()
);

--
-- 世界聊天记录 wo_chat
--

create TABLE `wo_chat`(
    `id`   INT PRIMARY KEY AUTO_INCREMENT,
    `name`  VARCHAR(32) UNIQUE,
    `img`   MEDIUMBLOB,
    `content`   VARCHAR(64),
    `record_time`   DATATIME DEFAULT now()
);

--
-- 系统公告 sys_msg
--

create TABLE `sys_msg`(
    `id`   INT PRIMARY KEY AUTO_INCREMENT,
    `content`   VARCHAR(64),
    `record_time`   DATATIME DEFAULT now()
);








