--  Temporary Tables


CREATE TEMPORARY TABLE temp_table
(first_name VARCHAR(50),
last_name VARCHAR(50),
favorite_movie varchar(100)
);



INSERT INTO temp_table
VALUES ('Msizi','Mthethwa','Avengers: Infinity War');


SELECT *
FROM temp_table;


SELECT *
FROM employee_salary;

CREATE TEMPORARY TABLE salary_over_50k
SELECT * 
FROM employee_salary
WHERE salary >= 50000;


SELECT * FROM salary_over_50k




