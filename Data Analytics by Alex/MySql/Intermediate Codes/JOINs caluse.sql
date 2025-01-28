# Joins

SELECT * 
FROM employee_demographics;

SELECT *
FROM employee_salary;

SELECT dem.employee_id, age, occupation
FROM employee_demographics as dem
INNER JOIN employee_salary as sal
	ON dem.employee_id = sal.employee_id
;

SELECT *
FROM employee_demographics as dem
RIGHT JOIN employee_salary as sal
	ON dem.employee_id = sal.employee_id
;

# Self Join

SELECT emp1.employee_id as emp_santa,
emp1.first_name as first_name_santa,
emp1.last_name AS last_name_santa,
emp2.employee_id as emp_name,
emp2.first_name as emp_first_name,
emp2.last_name AS emp_last_name
FROM employee_salary emp1
JOIN employee_salary emp2 
	ON emp1.employee_id + 1 = emp2.employee_id
;

# Joining multiple tables 


SELECT *
FROM employee_demographics as dem
INNER JOIN employee_salary as sal
	ON dem.employee_id = sal.employee_id
INNER JOIN parks_departments pd
	ON sal.dept_id = pd.department_id
;
 SELECT *
 FROM parks_departments;