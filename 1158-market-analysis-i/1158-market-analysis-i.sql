# Write your MySQL query statement below
select u.user_id as buyer_id, u.join_date, ifnull(count(order_date), 0) as orders_in_2019
from users as u left join orders as o on year(order_date) = '2019' and u.user_id = o.buyer_id 
group by user_id;