CREATE DATABASE IF NOT EXISTS company;

USE company;

CREATE TABLE employees (

    id INT PRIMARY KEY AUTO_INCREMENT,

    name VARCHAR(100),

    department VARCHAR(100)

);

INSERT INTO employees (name, department)
VALUES
('Rahul','DevOps'),
('Priya','Testing'),
('Arjun','Development'),
('Sneha','HR'),
('Kiran','Cloud');
