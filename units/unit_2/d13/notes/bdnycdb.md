# BDNYC database with SQLite3 in Terminal (review) and astrodbkit

![BDNYC Database](https://raw.githubusercontent.com/BDNYC/BDNYCdb/master/tutorial/full_database.png)


## BDNYCdb with sqlite3

1. Navigate to the BDNYCdb_practice directory

    `cd BDNYCdb_practice`

2. Open BDNYCdb in sqlite3

    `sqlite3 bdnycdev_copy.db`


### Let's review!

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
    - `pip install astrodbkit --upgrade` to get the most recent version

2. Navigate to today's code folder

    `cd units/unit_2/d12/code`

3. create a new python file

    `touch database_tutorial.py`

4. Open new python file in atom

    `atom database_tutorial.py`

5. Follow along the [BDNYCdb tutorial](https://github.com/BDNYC/BDNYCdb/blob/master/tutorial/tutorial.md) starting with **Loading the Database**


### Quick Activity

Use astrodbkit to complete each task (are there any other solutions?):

  1. Find out how many `publications` were written by Dr. Jackie Faherty

  2. List the first 10 entries (`LIMIT 10`) in the `sources` table

  3. Find out how many entries in the `spectra` table came from the instrument with the id "46".

  4. List only the Hubble Space Telescope (HST) row from the `telescopes` table.

  5. List the first 10 entries in the `spectra` table that came from HST by joining the `telescopes` table.

  6. List the shortname, band, and magnitude for each listing in the `sources` table that came from the Gemini South telescope by joining the `photometry` and `telescopes` tables
