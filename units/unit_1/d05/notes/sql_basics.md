# SQL Databases

## What is a database?
A database is an organized collection of data that is stored and accessed electronically.

A database is usually made up one or more tables. Each table is identified by a name (e.g. "Customers" or "Orders"). Tables contain records (rows) with data.

## What is SQL?
SQL stands for Structured Query Language.

It allows you to access and manipulate databases, which store data in tables. A table is a collection of related data entries and it consists of columns and rows..

## What can SQL do?

 - SQL can execute queries against (access) a database
 - SQL can retrieve data from a database
 - SQL can insert records in a database
 - SQL can update records in a database
 - SQL can delete records from a database
 - SQL can create new databases
 - SQL can create new tables in a database

 There are many different versions of SQL with minor differences, but they all share the same major commands (SELECT, UPDATE, INSERT, WHERE, etc.)

## Some of The Most Important SQL Commands
 - SELECT - extracts data from a database
 - UPDATE - updates data in a database
 - DELETE - deletes data from a database
 - INSERT INTO - inserts new data into a database
 - CREATE DATABASE - creates a new database
 - ALTER DATABASE - modifies a database
 - CREATE TABLE - creates a new table
 - ALTER TABLE - modifies a table
 - DROP TABLE - deletes a table
 - CREATE INDEX - creates an index (search key)
 - DROP INDEX - deletes an index

### Create a table
  ```
  CREATE TABLE foo (name varchar(20)); -- create a table called 'foo' with one column called 'name' which is a small text column
  DROP TABLE foo; -- drop a table (deletes it)
  CREATE TABLE users ( id int, name varchar(20), age int, email varchar(32) ); -- 'users' table has an id column, which is just an assigned number, and columns for name, age, and email.
  ```

### Insert into table
  ```
  INSERT INTO Customers (CustomerID, CustomerName, City/State, Homeworld) VALUES (3, 'Daria Morgendorffer', 'Lawndale, TX', "Earth");
  ```

### Select from table
  ```
  SELECT * FROM Customers;
  SELECT * FROM Customers WHERE CustomerID=1;
  ```

### Update a table
  ```
  UPDATE Customers SET CustomerName = 'Ahsoka Tano', Homeworld= 'Shili' WHERE CustomerID = 2;
  ```

### Delete from table
  ```
  DELETE FROM Customers WHERE CustomerName='Ned Stark';
  ```

## SQL Cheatsheet

![SQL cheatsheet](http://www.sqltutorial.org/wp-content/uploads/2016/04/SQL-Cheat-Sheet-2.png)
