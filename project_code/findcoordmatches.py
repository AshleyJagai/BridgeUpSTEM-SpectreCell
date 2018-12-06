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
matches = pd.DataFrame(columns = gaia_catalogue.columns.values)
print (matches.columns)
# new_objects will store gaia data for objects that do not exist in BDNYC database
new_objects = pd.DataFrame(columns = gaia_catalogue.columns.values)
print (new_objects.columns)



# ===============================================
# sort each row of gaia data into matches/new_objects using celestial coordinates: right ascension (ra/RA) and declination (dec/DEC)
# ===============================================

for i in range(len(gaia_catalogue)):
    #db.search((338.673, 40.694), "sources", radius=5)
    #print (gaia_catalogue["RA"][i],gaia_catalogue["DEC"][i])
    if (len(db.search((gaia_catalogue["RA"][i],gaia_catalogue["DEC"][i]),"sources",radius = 0.00084, fetch = True))) > 0:
        #print (len(db.search((gaia_catalogue["RA"][i],gaia_catalogue["DEC"][i]),"sources",radius = 0.00084, fetch = True)))
        matches = matches.append(gaia_catalogue.loc[[i]])
    else:
        new_objects = new_objects.append(gaia_catalogue.loc[[i]])
print (matches.head)
len(matches)

# ===============================================
# Workspace
# ===============================================

# length of db_sources
len(db_sources)

# prints single row of gaia_catalogue
gaia_catalogue.loc[[0]]
# prints first 5 rows of gaia_catalogue
gaia_catalogue.head()
