# ===============================================
# import libraries
# ===============================================
import pandas as pd
from astrodbkit import astrodb




# ===============================================
# import files needed
# ===============================================

# import gaia csv
gaia_catalogue = pd.read_csv('gaia_data/all_catalog.csv')
# import bdnyc database
db = astrodb.Database('BDNYCdb_practice/bdnycdev_copy.db')




# ===============================================
# variables needed
# ===============================================

# list all from sources into format of pandas stored as new variable
db_sources = db.query('SELECT * FROM sources', fmt='pandas')





# ===============================================
# create new empty dataframes to store gaia data
# ===============================================

# matches will store gaia data for objects in BDNYC database
matches = pd.DataFrame()
# new_objects will store gaia data for objects that do not exist in BDNYC database
new_objects = pd.DataFrame()




# ===============================================
# sort each row of gaia data into matches/new_objects using celestial coordinates: right ascension (ra/RA) and declination (dec/DEC)
# ===============================================

for i in range(len(gaia_catalogue)):
    # print(i, gaia_catalogue['RA'].loc[[i]], gaia_catalogue['DEC'].loc[[i]])
    for j in range(len(db_sources)):
        # print(j) DONT PRINT THIS




# ===============================================
# Workspace
# ===============================================



# length of db_sources
len(db_sources)

# prints single row of gaia_catalogue
gaia_catalogue.loc[[0]]
# prints first 5 rows of gaia_catalogue
gaia_catalogue.head()
