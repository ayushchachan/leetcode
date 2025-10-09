select MAX(salary) AS SecondHighestSalary from Employee where salary <> (select MAX(salary) from Employee);



# select salary from Employee where salary != (MAX(select salary from Employee));