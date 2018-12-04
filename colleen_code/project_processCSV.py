import pandas as pd
from astrodbkit import astrodb

# import gaia csv
gaia_catalogue = pd.read_csv('gaia_data/all_catalog.csv')

# import bdnyc database
db = astrodb.Database('BDNYCdb_practice/bdnycdev_copy.db')


# create new empty dataframes to store gaia data

# matches for objects in BDNYC database
matches = pd.DataFrame()

# new_objects for objects that do not exist in BDNYC database
new_objects = pd.DataFrame()


# list all from sources into format of pandas stored as new variable
db_sources = db.query('SELECT * FROM sources', fmt='pandas')


# length of db_sources
len(db_sources)

for i in range(len(gaia_catalogue)):
    # print(i, gaia_catalogue['RA'].loc[[i]], gaia_catalogue['DEC'].loc[[i]])
    for j in range(len(db_sources)):
        # print(j) DONT PRINT THIS




gaia_catalogue.loc[[0]]
gaia_catalogue.head()
