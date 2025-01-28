# Limiting and Aliasing

SELECT *
FROM employee_demographics
order by age desc
LIMIT 2, 1 ;

# Aliasing 

SELECT gender, AVG(age) AS avg_age
FROM employee_demographics
GROUP BY gender
HAVING avg_age > 40;