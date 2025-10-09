# Write your MySQL query statement below
# select max(salary) as SecondHighestSalary from Employee
# where salary not in (select max(salary) from Employee);

select d.name as Department, e.name as Employee, salary 

from Employee e 
join Department d on e.departmentId = d.id 
where (departmentId, salary) in (select departmentId, max(salary) from Employee group by departmentId);

# select name, salary from Employee group by departmentId where 
