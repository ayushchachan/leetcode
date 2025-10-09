# Write your MySQL query statement below
update Salary
set sex = (CASE when sex = 'm' then 'f' else 'm' end);