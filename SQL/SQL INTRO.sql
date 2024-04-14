-- 1. Write a SQL query to find the average salary of employees who have been hired before year 2000 incl. 
-- Round it down to the nearest integer.
SELECT ROUND(AVG(Salary))
FROM employees
WHERE HireDate <= 200;

-- 1. Write a SQL query to find all town names that end with a vowel (a,o,u,e,i).

SELECT Name
FROM towns
WHERE Name REGEXP '[a,o,u,e,i]$';

-- 1. Write a SQL query to find all town names that start with a vowel (a,o,u,e,i).

SELECT Name
FROM towns
WHERE Name REGEXP '^[a,o,u,e,i]';

-- 1. Write a SQL query to find the name and the length of the name of the town with the longest name.
SELECT Name, LENGTH(NAME)
FROM towns
ORDER BY LENGTH(NAME) DESC
LIMIT 1;

-- 1. Write a SQL query to find the name and the length of the name of the town with the shortest name.
SELECT Name, LENGTH(NAME)
FROM TOWNS
ORDER BY length(NAME)
LIMIT 1;

-- 1. Write a SQL query to find all employees with even IDs.
SELECT *
FROM employees
WHERE EmployeeID%2=0;

-- 1. Write a SQL query to find the names and salaries of the employees that take the minimal salary in the company.

SELECT FirstName, Salary
FROM employees
Where salary = (select min(salary) from employees);

-- 1. Write a SQL query to find the names and salaries of the employees that have a 
-- salary that is up to 10% higher than the minimal salary for the company.

SELECT FirstName, LastName, Salary
FROM employees
WHERE Salary <= (SELECT MIN(Salary)*1.10 FROM employees);

-- 1. Write a SQL query to find the full name, salary and department of the employees that take the minimal salary in their department.

SELECT e.FirstName, e.LastName, e.salary, d.name
FROM employees e
JOIN departments d ON e.departmentid = d.departmentid
WHERE (e.salary, e.departmentid) IN (
    SELECT MIN(salary), departmentid
    FROM employees
    GROUP BY departmentid
);

-- 1. Write a SQL query to find the average salary in the department #1.

SELECT round(avg(SALARY))
FROM employees as e
JOIN departments as d on e.departmentid = d.DepartmentID
WHERE d.DepartmentID=1;


-- 1. Write a SQL query to find the average salary  in the "Sales" department.

SELECT AVG(SALARY)
FROM EMPLOYEES AS e
JOIN departments AS d on e.departmentid = d.DepartmentID
where d.name = "Sales";

-- 1. Write a SQL query to find the number of employees in the "Sales" department.

SELECT COUNT(*)
FROM EMPLOYEES AS e
Join departments as d on e.departmentid = d.departmentid
WHERE d.name = 'Sales';

-- 1. Write a SQL query to find the number of all employees that have manager.
SELECT COUNT(distinct EmployeeID)
FROM employees AS e
WHERE ManagerID is not null;

-- 1. Write a SQL query to find the number of all employees that have no manager.

SELECT COUNT(distinct EmployeeID)
FROM employees AS e
WHERE ManagerID is null;

-- 1. Write a SQL query to find all departments and the average salary for each of them.
SELECT AVG(SALARY), d.name
FROM employees as e
join departments as d on e.DepartmentID = d.DepartmentID
group by d.name;

-- 1. Write a SQL query to find all projects that took less than 1 year (365 days) to complete.
SELECT *
FROM projects as p
WHERE datediff(p.EndDate,p.StartDate)<365;

-- 1. Write a SQL query to find the count of all employees in each department and for each town.
SELECT d.Name, t.Name, COUNT(*) AS EmployeeCount
FROM employees AS e
JOIN departments AS d ON e.DepartmentID = d.DepartmentID
JOIN addresses AS a ON e.AddressID = a.AddressID
JOIN towns AS t ON a.TownID = t.TownID
GROUP BY d.DepartmentID, t.Name;

-- 1. Write a SQL query to find all managers that have exactly 5 employees. Display their first name and last name.

SELECT m.FirstName, m.LastName
FROM employees AS e
JOIN employees AS m ON e.ManagerID = m.EmployeeID
WHERE m.ManagerID is not null
GROUP BY m.FirstName, m.LastName
HAVING COUNT(*) = 5;

-- 1. Write a SQL query to find all employees along with their managers. For employees that do not have manager display the value "(no manager)".


SELECT m.FirstName, m.LastName, m.FirstName, m.LastName
FROM employees AS e
JOIN employees AS m ON e.ManagerID = m.EmployeeID
GROUP BY e.FirstName, e.LastName, m.FirstName, m.LastName;

-- 1. Write a SQL query to find the names of all employees whose last name is exactly 5 characters long.

SELECT e.LastName
from employees as e
WHERE length(e.LastName) = 5;

-- 1. Write a SQL query to display the current date and time in the following format 
-- "`day.month.year hour:minutes:seconds:milliseconds`".

SELECT date_format(now(), ('%d.%m.%Y %H:%i:%s:%f'));

-- 1. Write a SQL query to display the average employee salary by department and job title.

SELECT ROUND(AVG(e.Salary)), d.name, e.JobTitle
FROM employees as e
JOIN departments as d on d.DepartmentID = e.DepartmentID
GROUP BY d.Name, e.JobTitle;

-- 1. Write a SQL query to display the town where maximal number of employees work.
SELECT t.Name
FROM towns as t
JOIN addresses as a on a.TownID = t.TownID
JOIN employees as e on a.AddressID = e.AddressID
Group by t.Name
HAVING COUNT(*) = (
	SELECT COUNT(*)
    FROM employees
    group by AddressID
    order by count(*) desc
    limit 1
    );

-- 1. Write a SQL query to display the number of managers from each town.

SELECT t.Name AS TownName, 
       COUNT(*) AS NumberOfManagers
FROM employees AS e
JOIN addresses AS a ON e.AddressID = a.AddressID
JOIN towns AS t ON a.TownID = t.TownID
WHERE e.ManagerID is not null
GROUP BY t.Name;


-- 1. Write a SQL query to find the manager who is in charge of the most employees and their average salary.

SELECT CONCAT(m.FirstName, ' ', m.LastName) AS ManagerName,
       AVG(e.Salary) AS AverageSalary
FROM employees AS e
JOIN employees AS m ON e.ManagerID = m.EmployeeID
GROUP BY m.EmployeeID
ORDER BY COUNT(*) DESC
LIMIT 1;

-- 1. Write a SQL statement finds the names of the employees who have worked on the most projects.

SELECT e.FirstName, e.LastName
FROM employees AS e
JOIN employeesprojects AS a ON e.EmployeeID = a.EmployeeID
JOIN projects AS p ON a.ProjectID = p.ProjectID
GROUP BY e.EmployeeID
ORDER BY COUNT(DISTINCT p.ProjectID) DESC
LIMIT 10


