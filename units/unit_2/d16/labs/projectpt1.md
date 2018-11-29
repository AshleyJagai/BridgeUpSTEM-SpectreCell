# Getting started with GAIA

![GAIA map](https://3c1703fe8d.site.internapcdn.net/newman/gfx/news/hires/2018/astronomerso.jpg)

## Work Set-Up

[astrodbkit documentation](https://astrodbkit.readthedocs.io/en/latest/index.html)

1. From Terminal, open BridgeUP-STEM-SpectreCell directory in atom

    `atom .`

2. Navigate to today's code folder in Terminal

    `cd units/unit_2/d16/code`

3. copy `project_processCSV.py` from d15 code folder

    `cp ../../d15/code/project_processCSV.py .`

4. Open up the [BDNYCdb tutorial](https://github.com/BDNYC/BDNYCdb/blob/master/tutorial/tutorial.md) and the [pandas documentation](http://pandas.pydata.org/pandas-docs/stable/) as resources


## Project Pt. 1!

- Use your code to read the GAIA csv file and load the BDNYC database

- Print the column names for both datasets -- do they share any information? What can we use to crossmatch? How can we find the objects that exist in both datasets?

- Create two new empty pandas dataframes

  - one will store the objects that are already in the database

  - the other will store the new objects

  Be sure to give them descriptive variable names so we don't get confused (like `matches` and `new_objects`)

- Find a way to compare the datasets and store pre-existing objects in your matches array and the rest in your array of new objects

- Store your created dataframes as csv files (don't forget to give them descriptive names!)
