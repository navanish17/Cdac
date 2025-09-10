use test;

create table student (
roll_no int primary key,
name varchar(50),
age int,
gender varchar(50)
);

insert into student (roll_no, name, age, gender) 
values (101, "Nimesh", 51, "Male"),
(102, "Nilesh", 31, "Male"),
(103, "Anjali", 28, "Female"),
(104, "Pranay", 21, "Male");

select * from student;

select name from student; 

select name from student where age > 25;

update student
set age  = 30 
where roll_no = 103;

select * from student;

delete from student 
where roll_no = 102;

select * from student;

alter table student add marks int;

describe student;

update student set marks = 50 where roll_no = 101;
update student set marks = 98 where roll_no = 103;
update student set marks = 89 where roll_no = 104;

select * from student;

select name, marks from student where marks > 60;

select * from student order by age asc;
select * from student order by marks desc;

select * from student order by marks asc limit 2;

select count(*) from student;

select avg(marks) from student;

select min(marks) from student;
select max(marks) from student;

select gender, count(*) from student group by gender;

select avg(marks) as avg_marks from student;

-- Table 1: students
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    course_id INT
);

INSERT INTO students (id, name, course_id) VALUES
(1, 'Alice', 101),
(2, 'Bob', 102),
(3, 'Charlie', 103),
(4, 'David', NULL);

CREATE TABLE courses (
    id INT PRIMARY KEY,
    course_name VARCHAR(50)
);

INSERT INTO courses (id, course_name) VALUES
(101, 'Math'),
(102, 'Science'),
(104, 'History');

select students.name, courses.course_name
from students
inner join courses
on students.course_id = courses.id;

select students.name, courses.course_name
from students
right join courses
on students.course_id = courses.id;

select students.name, courses.course_name
from students
left join courses
on students.course_id = courses.id;

select name, marks
from student
where marks =  (select max(marks) from student);

select name, marks
from student
where marks between 51 and 100;

select name from students where name like '%b%';

select name
from students
where id in (2);

create database lab;
use lab;

drop table client_master;

create table client_master(
clientno varchar(6) primary key,
name1 varchar(20) not null,
city varchar(15),
pincode numeric(8,0),
state varchar(15),
baldue numeric(10,0),
constraint client_name check(clientno like 'C%')
);

insert into client_master (clientno,name1,city,pincode,state,baldue)
values ('C00001', 'Ivan Bayross', 'Mumbai', 400054, 'Maharashtra', 15000),
('C00003', 'Chhaya Bankar', 'Mumbai', 400057, 'Maharashtra', 5000),
('C00004', 'Ashwini Joshi', 'Banglore', 560001, 'Karnataka', 0),
('C00005', 'Hansel colaco', 'Mumbai', 400060, 'Maharashtra', 2000),
('C00006', 'Deepak sharma', 'Manglore', 560050, 'Karnataka', 0);

select * from PRODUCT_MASTER;

create table client_master(
PRODUCTNO varchar(6) primary key,
name1 varchar(20) not null,
city varchar(15),
pincode numeric(8,0),
state varchar(15),
baldue numeric(10,0),
constraint client_name check(clientno like 'P%')
);





 










