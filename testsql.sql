use testdb;
SET SQL_SAFE_UPDATES = 0;  # 不要他妈的安全update模式了
/*
create table 学生基本信息
(
学号 char(20) not null,
姓名 char(20) not null,
家庭住址 char(40),
性别 char(10),
年龄 smallint,
基本情况 char(20),
primary key(学号,姓名)
);

create table 学生成绩信息
(
学号 char(20) not null,
姓名 char(20) not null,
成绩1 smallint,
成绩2 smallint,
成绩3 smallint,
成绩4 smallint,
成绩5 smallint,
成绩6 smallint,
成绩7 smallint,
总成绩 smallint,
平均成绩 smallint,
任课教师 char(20),
primary key(学号, 姓名),
CONSTRAINT  `学生成绩信息_ibfk_1` foreign key(学号,姓名) references 学生基本信息(学号,姓名)
on delete cascade
on update cascade
)
*/
/*  给第一张表建立外码.
alter table 学生基本信息
add
CONSTRAINT  `学生基本信息_ibfk_1` foreign key(学号,姓名) references 学生成绩信息(学号,姓名)
on delete cascade
on update cascade;
*/
/*
http://xuehu2009.iteye.com/blog/571138
*/
/*
insert into 学生成绩信息
values("201402180","王2五",1556,125,15445,12454,13254,1678,1514,71,125,"gfdg格式");
*/
/*
insert into 学生基本信息
values("201402180","王2五","1556","125",15445,"gfdg格式");*/
/*
update 学生基本信息
set 姓名="王通过三国杀2五"
where 学号="201402180";
*/
update 学生基本信息
set 学号="201402kg180"
where 姓名="王通过三国杀2五";