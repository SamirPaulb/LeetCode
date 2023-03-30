# Write your MySQL query statement below
select u.name, sum(t.amount) as balance
from users as u left join transactions as t
on u.account = t.account
group by u.account having balance > 10000;