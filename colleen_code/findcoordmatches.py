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
matches = pd.DataFrame(columns=gaia_catalogue.columns.values)
# new_objects will store gaia data for objects that do not exist in BDNYC database
new_objects = pd.DataFrame(columns=gaia_catalogue.columns.values)


# ===============================================
# sort each row of gaia data into matches/new_objects using celestial coordinates: right ascension (ra/RA) and declination (dec/DEC)
# ===============================================

for i in range(len(gaia_catalogue)):
    if len(db.search((gaia_catalogue['RA'][i], gaia_catalogue['DEC'][i]), 'sources', radius=0.00084, fetch=True)) > 0:
        matches = matches.append(gaia_catalogue.loc[[i]])
        # print(len(db.search((gaia_catalogue['RA'][i], gaia_catalogue['DEC'][i]), 'sources', radius=0.00084, fetch=True)))
    else:
        new_objects = new_objects.append(gaia_catalogue.loc[[i]])

gaia_catalogue

# ===============================================
# Workspace
# ===============================================



# length of db_sources
len(db_sources)

# prints single row of gaia_catalogue
gaia_catalogue.loc[[0]]
# prints first 5 rows of gaia_catalogue
gaia_catalogue.head()

# ===============================================
# Plotting coordinates
# ===============================================

import astropy.coordinates as coord
import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np


#
db_ra = coord.Angle(pd.to_numeric(db_sources['ra']).fillna(np.nan).values*u.degree)
db_ra = db_ra.wrap_at(180*u.degree)
db_dec = coord.Angle(pd.to_numeric(db_sources['dec']).fillna(np.nan).values*u.degree)


matches_ra = coord.Angle(matches['RA'].values*u.degree)
matches_ra = matches_ra.wrap_at(180*u.degree)
matches_dec = coord.Angle(matches['DEC'].values*u.degree)

new_objects_ra = coord.Angle(new_objects['RA'].values*u.degree)
new_objects_ra = new_objects_ra.wrap_at(180*u.degree)
new_objects_dec = coord.Angle(new_objects['DEC'].values*u.degree)



fig = plt.figure(figsize=(14,12))
ax = fig.add_subplot(111, projection="mollweide")
ax.set_facecolor('#17303F')
plt.grid(True)

ax.scatter(db_ra.radian, db_dec.radian, color="#E5E5E5", alpha=.8, edgecolors='face')
ax.scatter(matches_ra.radian, matches_dec.radian, color="#F24333")
ax.scatter(new_objects_ra.radian, new_objects_dec.radian, color="#E3B505")
