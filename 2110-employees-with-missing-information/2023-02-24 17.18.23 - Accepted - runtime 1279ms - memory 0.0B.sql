# Write your MySQL query statement below
# SELECT Employees.employee_id from Employees INNER JOIN Salaries on Employees.employee_id = Salaries.employee_id; 

select employee_id  from Employees where employee_id not in (select employee_id from Salaries)
union
select employee_id from Salaries where employee_id not in (select employee_id  from Employees) order by employee_id;