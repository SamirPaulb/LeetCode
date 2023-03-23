# Write your MySQL query statement below
select user_id, concat(upper(substring(name, 1, 1)), lower(substring(name, 2, length(name)))) as name from Users order by user_id asc;