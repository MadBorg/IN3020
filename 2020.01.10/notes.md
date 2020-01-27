# SQL

Inter-galactic data-speak with several sub-speaks:

* Data definition language - DDL
    - Create
* Data Query langguage - DQL
    - Select
* Data Manipulation Language - DML
* Data Conroll language - DCL

Join redefines the search space.

## Joins
because we have the posibility of NULL then we need some more variarities of join.

* Join
* Right Join
* Left Join
* Full Join

Join puts together tables with tuples that setifies the conditions.

## Self Join

join with a condition to itself.

``` sql
    SELECT e.name, e.name FROM Employee e
        Join Manager ON empID = Id AND mgrId=Id;
```
This does not work. ^

``` sql
    SELECT e.name, s.name FROM Employee e
        JOIN Manager ON empID = Id
        JOIN Employee s ON s.Id = mgrId;
```
This will work. ^

## Join the loopholes

Not-very-helppful short form for join:

``` sql
    SELECT <something> FROM table1, table2, table3, WHERE <many many condittions>
```
Its easy to become lost.

## Conditions

Boolean expression.
NULL = NULL is false!

## The null problem

NULL = NULL is false is like dividing on zero.

x is null
x is not null

Manage null:

* COALESCE(expr1, ...), returns first argument that is not null; and null if all are Null
* NULLIF(expr1, ...), returns NULL if the args are the same, or returns Expr1.

## examle

Project(prnr, pname, customer, pmanager, startDate)
Employee(enr, name, title, bdate, pnr, empdate)
Timesheet(enr, date, prnr, hours)
customer(cnr, caname, address)

Find anem and title of the employee who worked on minimum one orject that started after 2014 and was ordered by customer "ABC"

Divide and Conquer:

see pp.

## Issues with null in aggregation

NULL vals is ignored in aggregation

* important in the case if count
* Exception is COUNT(*)

## sql - The general form

``` SQL
    SELECT [DESTINCT] <attrebutelist>
    FROM <tableexpresstion>
    [WHERE <where-conditions>]
        [GROUP BY <groupingattributes>
        [HAVING <aggregatiion-condititons>]
        ]
    [ORDER BY <attrebutes> [asc|desc][,
    <attrebute> [asc| desc] ] ...];
```


## Reqursive sql

``` SQL
    WITH REQURSIVE <tablename>(<attr-list>) AS (
        <non-reqursive term>
        UNION | UNION ALL -- pick one
        <recursive term>
    )
    SELECT * FROM <tablename>;
```
naca.a