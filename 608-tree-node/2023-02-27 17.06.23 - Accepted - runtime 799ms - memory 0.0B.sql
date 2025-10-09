# Write your MySQL query statement below
select id, "Root" as type from Tree where p_id is null
union
select id, "Leaf" as type from Tree where id NOT IN (select p_id from Tree where p_id IS NOT NULL) and p_id is not null
union
select id, "Inner" as type from Tree where id IN (select p_id from Tree where p_id IS NOT NULL) and p_id is not null;