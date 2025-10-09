# Write your MySQL query statement below
select e1.employee_id,
    case 
        WHEN (e1.employee_id % 2 != 0 and e1.name  not like "m%") then e1.salary
        else 0
    END as bonus
from Employees e1 order by e1.employee_id; 