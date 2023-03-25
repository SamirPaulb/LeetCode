# Write your MySQL query statement below
select firstName, lastname, city, state from Person left join Address on Person.personId = Address.personId;
