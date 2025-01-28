# WHERE clause

select * 
from employee_salary
where first_name = 'Leslie'; 


select * 
from employee_salary
where salary <= 50000; 


select *
FROM employee_demographics
WHERE  birth_date > '1985-01-01';

# Logical operators in the where clause

select *
FROM employee_demographics
WHERE  birth_date > '1985-01-01'
OR NOT gender = 'male';

select *
FROM employee_demographics
WHERE  (first_name = 'Leslie' and age = 44)  or age > 55  # This is an isolated where clause or condition statement
OR NOT gender = 'male';

# Like statement
SELECT * 
FROM employee_demographics
WHERE first_name LIKE 'A___%';

SELECT * 
FROM employee_demographics
WHERE birth_date LIKE '1989%';