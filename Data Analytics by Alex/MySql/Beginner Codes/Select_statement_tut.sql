SELECT * 
FROM parks_and_recreation.employee_demographics;

SELECT first_name,
 last_name,
 birth_date,
 age,
 (age + 10) * 10 + 10
FROM parks_and_recreation.employee_demographics;
# Math and calulations are run in SQL USING PEMDAS

SELECT DISTINCT first_name, gender
FROM parks_and_recreation.employee_demographics;