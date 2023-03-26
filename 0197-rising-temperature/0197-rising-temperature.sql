# Write your MySQL query statement below
select w1.id as id 
from Weather w1 join Weather w2 
where w1.temperature > w2.temperature 
and datediff(w1.recorddate, w2.recorddate) = 1;