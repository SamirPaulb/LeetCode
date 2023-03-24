# select max(salary) as "SecondHighestSalary" from employee where salary not in (select max(salary) from employee);

select (select distinct salary from employee order by salary desc limit 1 offset 1) as SecondHighestSalary;

