# Write your MySQL query statement below
select u.name, ifnull(sum(r.distance), 0) as travelled_distance 
from users as u left join rides as r on u.id = r.user_id
group by u.id
order by travelled_distance desc, name asc