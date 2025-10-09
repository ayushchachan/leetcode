select t.employee_id from 
(select employee_id from Employees union select employee_id from Salaries) as t where t.employee_id
not in 
(select Employees.employee_id from Employees JOIN Salaries on Employees.employee_id = Salaries.employee_id) order by  t.employee_id;
