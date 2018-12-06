# imports pandas
import pandas as pd
from astrodbkit import astrodb


# loads new csv file
Gaia = pd.read_csv('gaia_data/all_catalog.csv')


# import bdnyc Database
db = astrodb.Database('BDNYCdb_practice/bdnycdev_copy.db')


# create new empty DataFrame to store gaia data


# matches objects in bdnyc Database
matches = pd.DataFrame()


# new_objects for objects that do not exist in BDNYC Database
new_objects = pd.DataFrame()


# list all from sources into format of pandas stored as new variable
db_sorces = db.query('SELECT * FROM sources', fmt='pandas')


# length of db_sorces, ra = column name
len(db_sorces)

for i in range(len(Gaia)):
    # print(i, Gaia['RA'].loc[[i]],Gaia['DEC'].loc[[i]])
    for j in range(len(db_sorces.ra)):
    # Print(j) DONT PRINT THIS

Gaia.loc[[0]]
Gaia.head()
db.search((338.673, 40.694), 'sources', radius=5)
