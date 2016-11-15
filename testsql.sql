use testdb;
-- SET SQL_SAFE_UPDATES = 0;  # 不要他妈的安全update模式了
-- 当一张表参照另一张表时,在该表中插入的信息的主键,在被参照表中必须有已存在的相应对照主键.
-- 就是插入的这条数据的主键若不存在与被参照表中,则拒绝执行.
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
*/
/*
create table 学生成绩信息
(
学号 char(20) not null,
姓名 char(20) not null,
数据库 smallint,
组成原理 smallint,
操作系统 smallint,
数据结构 smallint,
算法 smallint,
计算机网络 smallint,
高数 smallint,
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
values("1","王老大",61,62,63,64,65,66,67,68,69,"王老九");
*/
/*
insert into 学生基本信息
values("201402180","王2五","","",15445,"gfdg格式");
*/
/*
update 学生基本信息
set 姓名="王通过三国杀2五"
where 学号="201402180";
*/
/*
update 学生成绩信息
set 任课教师="26666661402kg180"
where 姓名="王通过三国杀2五";*/
/*
create table unandpassword_bck
(
username char(18) not null primary key,
password char(20)
);
*/
/*
insert into unandpassword
values('2014021073', '021073');*/
/*
create trigger info_bak
after update on unandpassword
for each row
begin
	insert into unandpassword_bck values(:old.username, :old.password)
end;
*/
/*
create table test(id int , name varchar(10));
create table test_bak(id int , name varchar(10));
*/
/*
insert into 学生基本信息
values("43","王小八", "xxx省xx市", "男", 23, "不知道");
*/
