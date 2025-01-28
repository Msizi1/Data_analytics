-- Subqueries

-- IN the where clause

SELECT *
FROM employee_demographics
WHERE employee_id IN 
					( SELECT employee_id
						FROM employee_salary
                        WHERE dept_id = 1)
;


-- In a select statement

SELECT first_name, salary,
(SELECT AVG(salary)
FROM employee_salary) AS Average_salary
FROM employee_salary
GROUP BY first_name, salary;

-- IN the from statement

SELECT gender, AVG(age), MAX(age), MIN(age), COUNT(age)
FROM employee_demographics
GROUP BY gender;

SELECT AVG(avg_age)
FROM 
(SELECT gender,
 AVG(age) as avg_age ,
 MAX(age) as max_age,
 MIN(age) as min_age,
 COUNT(age) as count_age
FROM employee_demographics
GROUP BY gender) as  Agg_table
;





