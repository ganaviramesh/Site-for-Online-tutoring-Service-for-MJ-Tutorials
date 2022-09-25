# mj-tutorials
site for mj tutorials

1)install pycharm and create virtual environment 
2)install flask
3)install flask-sessions
4)install cx_oracle
5)install oracle instant client from oracle website
6)install oracle database(we have used 11g)


we have done html templates in jinja templates which supports python and data from database,these templates are not suitable for viewing normally


sql quaries to create tables in database


create table users (
user_id  int primary key,
email varchar(50),
name varchar(50),
password varchar(10));

create table instructor (
inst_id int primary key,
email varchar(50),
name varchar(50)  ,
password varchar(10));

create table courses (
course_id int primary key,
name varchar(20),
descrip varchar(200),
duration int,
inst_id references instructor (inst_id) on delete set null);

create table files(
file_id int,
course_id references courses(course_id) on delete cascade,
links int,
orders int,
file_name varchar(100),
primary key(file_id,course_id));

create table selects(
user_id references users(user_id) on delete cascade,
course_id references courses(course_id) on delete cascade,
start_date date,
primary key(user_id,course_id));



![image](https://user-images.githubusercontent.com/52595620/192143793-88efb64b-d47a-4a75-acb4-748da0dbdd50.png)
login page

![image](https://user-images.githubusercontent.com/52595620/192143851-f80470e3-624a-40e9-bcd9-37798abb3cf3.png)
Registration page 

![image](https://user-images.githubusercontent.com/52595620/192143864-6256c7ec-48d1-4d11-8f35-ce0a8086d448.png)
Home page

![image](https://user-images.githubusercontent.com/52595620/192143873-97fdc5bd-29cc-4f44-a6a7-8b4e3122bb2e.png)
Content page

![image](https://user-images.githubusercontent.com/52595620/192143885-3aafdef8-6a38-4336-979d-4b703f251ddf.png)
Inserting courses page
