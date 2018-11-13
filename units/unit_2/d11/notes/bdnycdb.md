# Intros to SQLite3 in Terminal and the BDNYC database!

## But first!

  What is our project?



<hr>

## Let's get started with SQLite3!

1. Open Terminal

  - `cd` into your #SpectreCell repo if you're not already there
  - `git pull upstream master` if you haven't already

    *You should see two new directories, "BDNYCdb_practice" and "project_code"*


2. Navigate to the BDNYCdb_practice directory

  `cd BDNYCdb_practice`


3. In Terminal type `sqlite3` -- this opens up SQLite in command-line

4. `.help` will give us a list of SQLite commands

  `.databases` will show us a list of our databases and `.tables` will show our tables (we have none yet)

  `.quit` exits sqlite

5. Create a new database in terminal with `sqlite3 testDB.db`

  Now we can see our new database with `.databases`
  `.tables` is still empty

### Quick activity

Use your code from Khan Academy [Challenge: Playlist maker](https://www.khanacademy.org/computing/computer-programming/sql/more-advanced-sql-queries/pc/challenge-playlist-maker) to recreate the tables in terminal.

  *Helpful hint: change your settings to show data as columns and turn on headers (column names)*

    `.mode column`

    `.header on`


<hr>



# BDNYCdb

]**Question:** What is a database?

## Quick Overview of BDNYCdb
From [BDNYCdb repo](https://github.com/BDNYC/BDNYCdb/blob/master/tutorial/tutorial.md)

The BDNYC database is a SQL database. We use Structured Query Language (SQL) to interface with it; specifically we use SQLite, which has a few minor differences to SQL.

Data in the database is stored in tables; each data point is an entry or row of a table. For example, one brown dwarf would be a specific row in the sources table. Photometry for that source would be one or more rows in the photometry table.

Each table has a number of columns, at least one of which is considered a primary key, which uniquely identified the row. In most of our tables, the primary key is id, which is stored as an integer.

In addition to primary keys, several tables have foreign keys. These are special columns in one table that have been linked to to primary keys from another table. For example, the id primary key of the sources table is used as a foreign key in the spectra table as the source_id column. You cannot add a spectrum to the spectra table for a source_id that does not exist, nor can you delete a row from the sources table if data exist for it in other tables.

While you can use pure SQL commands to interface with our database (eg, the sqlite3 and sqlalchemy packages for Python), astrodbkit has a variety of tools to allow you to access the database contents with ease.

![BDNYC Database](https://raw.githubusercontent.com/BDNYC/BDNYCdb/master/tutorial/full_database.png)


## BDNYCdb with sqlite3

1. Open BDNYCdb in sqlite3

  `sqlite3 bdnycdev_copy.db` from terminal or `.open bdnycdev_copy.db` if sqlite3 is still open

2. Let's try `.databases`, `.tables`, and `.dbinfo` will list some information about the database

### Quick activity

Using what we learned with Khan Academy, complete the following tasks:

  1. Find out how many `publications` were written by Dr. Jackie Faherty

  2. List the first 10 entries (`LIMIT 10`) in the `sources` table

  3. Find out how many entries in the `spectra` table came from the instrument with the id "46".

  4. List only the Hubble Space Telescope (HST) row from the `telescopes` table.

  5. List the first 10 entries in the `spectra` table that came from HST by joining the `telescopes` table.

  6. List the shortname, band, and magnitude for each listing in the `sources` table that came from the Gemini South telescope by joining the `photometry` and `telescopes` tables


## BDNYCdb with astrodbkit

[astrodbkit documentation](https://astrodbkit.readthedocs.io/en/latest/index.html)

1. Install packages:
  - `pip install matplotlib`
  - `pip install pandas`
  - `pip install astrodbkit`
  - `pip install astrodbkit --upgrade`

2. Navigate to today's code folder

  `cd units/unit_2/d11/code`

3. create a new python file

  `touch database_tutorial.py`

4. Open new python file in atom

  `atom database_tutorial.py`

5. Follow along the [BDNYCdb tutorial](https://github.com/BDNYC/BDNYCdb/blob/master/tutorial/tutorial.md) starting with **Loading the Database**
