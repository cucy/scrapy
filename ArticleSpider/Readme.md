## 知乎表结构设计
### 问题表
```mysql
CREATE TABLE `zhihu_questions` (
	`zhihu_id` BIGINT(20) NOT NULL,
	`topics` VARCHAR(255) NULL DEFAULT NULL,
	`url` VARCHAR(300) NOT NULL,
	`title` VARCHAR(300) NOT NULL,
	`content` LONGTEXT NOT NULL,
	`create_time` DATETIME NULL DEFAULT NULL,
	`update_time` DATETIME NULL DEFAULT NULL,
	`answer_num` INT(11) NOT NULL DEFAULT '0',
	`comments_num` INT(11) NOT NULL DEFAULT '0' COMMENT '关注问题数量',
	`watch_user_num` INT(11) NOT NULL DEFAULT '0' COMMENT '查看数量',
	`click_num` INT(11) NOT NULL DEFAULT '0' COMMENT '点击数',
	`crawl_time` DATETIME NULL DEFAULT NULL COMMENT '爬取时间',
	`crawl_update_time` DATETIME NULL DEFAULT NULL,
	PRIMARY KEY (`zhihu_id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;

```
### 回复表
```mysql
CREATE TABLE `zhihu_answer` (
	`zhihu_id` BIGINT(20) NOT NULL,
	`url` VARCHAR(300) NOT NULL,
	`question_id` BIGINT(20) NOT NULL,
	`author_id` VARCHAR(100) NULL DEFAULT NULL,
	`content` LONGTEXT NOT NULL COMMENT '评论内容',
	`praise_num` INT(11) NOT NULL DEFAULT '0',
	`comments_num` INT(11) NOT NULL DEFAULT '0' COMMENT '评论数量',
	`create_time` DATE NOT NULL,
	`update_time` DATE NOT NULL,
	`crawl_time` DATETIME NOT NULL COMMENT '爬取时间',
	`crawl_update_time` DATETIME NULL DEFAULT NULL COMMENT '爬取更新时间',
	PRIMARY KEY (`zhihu_id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;

```