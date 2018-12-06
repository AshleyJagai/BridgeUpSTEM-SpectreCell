# ==============================================================================
# import libraries
# ==============================================================================
import pandas as pd
from astrodbkit import astrodb
import astropy.coordinates as coord
import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np

# ==============================================================================
# import files needed
# ==============================================================================

# import gaia csv
gaia_catalogue = pd.read_csv('gaia_data/all_catalog.csv')
# import bdnyc database
db = astrodb.Database('BDNYCdb_practice/bdnycdev_copy.db')


# ==============================================================================
# variables needed
# ==============================================================================

# list all from sources into format of pandas stored as new variable
db_sources = db.query('SELECT * FROM sources', fmt='pandas')

# ==============================================================================
# create new empty dataframes to store gaia data
# ==============================================================================

# matches will store gaia data for objects in BDNYC database
matches = pd.DataFrame(columns = gaia_catalogue.columns.values)
# new_objects will store gaia data for objects that do not exist in BDNYC database
new_objects = pd.DataFrame(columns = gaia_catalogue.columns.values)
matches.to_csv('project_code/matches.csv')
new_objects.to_csv('project_code/new_matches')
len(matches)

matches_test = pd.read_csv("project_code/matches.csv",index_col=0)

matches_test
len(new_objects)


# ==============================================================================
# sort each row of gaia data into matches/new_objects using celestial coordinates: right ascension (ra/RA) and declination (dec/DEC)
# ==============================================================================

for i in range(len(gaia_catalogue)):
    if len(db.search((gaia_catalogue["RA"][i], gaia_catalogue["DEC"][i]), 'sources', radius=0.00084, fetch = True > 0)):
        # Looking for the lenth of the list and it appends it if the radius is = to 0.00084, it'll label it to matches,if not then it'll label it to no matches
        # print (len(db.search((gaia_catalogue["RA"][i], gaia_catalogue["DEC"][i]), 'sources', radius=0.00084, fetch = True)))
        matches = matches.append(gaia_catalogue.loc[[i]])
    else:
        new_objects = new_objects.append(gaia_catalogue.loc[[i]])
gaia_catalogue.columns
gaia_catalogue["RA"][5]
gaia_catalogue["DEC"][5]

# ==============================================================================
# Workspace
# ==============================================================================

# length of db_sources
len(db_sources)

# prints single row of gaia_catalogue
gaia_catalogue.loc[[0]]

# prints first 5 rows of gaia_catalogue
gaia_catalogue.head()

matches.head()
matches
# ==============================================================================
# plotting
# ==============================================================================

# angle =translates to units u are using
# fillna = finds empty spaces and fills with np.nam(aka ignores it and skips it)
# pd.to numeric = turns db_sorces into a number bc it was a string b4
# converts munber to arc sec and arc mins
# reusing the same var to convert same number to wrap from -180 to 180 since thats the length of the map

#TURIS TO NUMBER, IGNORES EMPTY SPACES, AND MULTIPLIES IT TO THE DEGREES
db_ra = coord.Angle(pd.to_numeric(db_sources['ra']).fillna(np.nan).values*u.degree)
db_ra = db_ra.wrap_at(180*u.degree)
db_dec = coord.Angle(pd.to_numeric(db_sources['dec']).fillna(np.nan).values*u.degree)

fig= plt.figure(figsize=(14,12))
ax = fig.add_subplot(111, projection='mollweide')
ax.set_facecolor('#17303F')
plt.grid(True)

ax.scatter(db_ra.radian, db_dec.radian, color="#E5E5E5", alpha=.8, edgecolors='face')


matches_ra = coord.Angle(matches['RA'].values*u.degree)
matches_ra = matches_ra.wrap_at(180*u.degree)
matches_dec = coord.Angle(matches['DEC'].values*u.degree)

fig= plt.figure(figsize=(14,12))
ax = fig.add_subplot(111, projection='mollweide')
ax.set_facecolor('#8583a8')
plt.grid(True)


ax.scatter(db_ra.radian, db_dec.radian, color="#E5E5E5", alpha=.8, edgecolors='face')
ax.scatter(matches_ra.radian, matches_dec.radian, color="#2e269b")
plt.show()
