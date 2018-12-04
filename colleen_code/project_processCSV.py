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
matches = pd.DataFrame(columns=list(gaia_catalogue.columns.values))
# new_objects will store gaia data for objects that do not exist in BDNYC database
new_objects = pd.DataFrame(columns=list(gaia_catalogue.columns.values))




# ===============================================
# sort each row of gaia data into matches/new_objects using celestial coordinates: right ascension (ra/RA) and declination (dec/DEC)
# ===============================================

for i in range(len(gaia_catalogue.head(20))):
    if len(db.search((gaia_catalogue.RA[i], gaia_catalogue.DEC[i]), 'sources', radius=3, fetch=True)) > 0:
        db.search((gaia_catalogue.RA[i], gaia_catalogue.DEC[i]), 'sources', radius=3)
        matches = matches.append(gaia_catalogue.iloc[[i]])
    else:
        new_objects = new_objects.append(gaia_catalogue.iloc[[i]])




# ===============================================
# Workspace
# ===============================================



# length of db_sources
len(db_sources)

# prints single row of gaia_catalogue
gaia_catalogue.loc[[0]]
# prints first 5 rows of gaia_catalogue
gaia_catalogue.RA[0]
matches=matches.append(gaia_catalogue.iloc[[65]])
matches
gaia_catalogue.iloc[[0]]
