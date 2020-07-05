- Index all columns Used in `where`, `order by`, and `group by` clauses.
- Optimize `like` statements with `union` clause:
`select * from students where first_name like  'Ade%'  or last_name like 'Ade%' ;` 
is slower than 
`select  from students where first_name like  'Ade%'  union all select  from students where last_name like  'Ade%' ;`.
- Avoid Like Expressions With Leading Wildcards:
`select * from students where first_name like  '%Ade'  ;`
- Avoid NULL values since they are not indexed. A query like  `SELECT * FROM table WHERE column IS NULL` will always use full table scan since index doesn't cover the values you need.
- Denormalize.