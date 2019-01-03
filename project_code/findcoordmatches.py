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


# load matches and new_objects csvs
# insert code here
#
#
#


# ===============================================
# variables needed
# ===============================================

# list all from sources into format of pandas stored as new variable
db_sources = db.query('SELECT * FROM sources', fmt='pandas')



# ===============================================
# create new empty dataframes to store gaia data
# ===============================================

# matches will store gaia data for objects in BDNYC database
<<<<<<< HEAD
matches = pd.DataFrame(columns = gaia_catalogue.columns.values)
<<<<<<< HEAD:colleen_code/findcoordmatches_day3.py
# new_objects will store gaia data for objects that do not exist in BDNYC database
new_objects = pd.DataFrame(columns = gaia_catalogue.columns.values)

=======
print (matches.columns)
# new_objects will store gaia data for objects that do not exist in BDNYC database
new_objects = pd.DataFrame(columns = gaia_catalogue.columns.values)
print (new_objects.columns)
>>>>>>> aa7cf98f67b8624fda66dec5d3918af6a03802cb:project_code/findcoordmatches.py

matches


new_objects
=======
matches = pd.DataFrame(columns=gaia_catalogue.columns.values)
# new_objects will store gaia data for objects that do not exist in BDNYC database
new_objects = pd.DataFrame(columns=gaia_catalogue.columns.values)
>>>>>>> 9ac50e2b824dec96adc0ec609b1222516ef0b266


# ===============================================
# sort each row of gaia data into matches/new_objects using celestial coordinates: right ascension (ra/RA) and declination (dec/DEC)
# ===============================================

for i in range(len(gaia_catalogue)):
<<<<<<< HEAD
<<<<<<< HEAD:colleen_code/findcoordmatches_day3.py
    if len(db.search((gaia_catalogue["RA"][i], gaia_catalogue["DEC"][i]), 'sources', radius=0.00084, fetch = True > 0)):
        # print (len(db.search((gaia_catalogue["RA"][i], gaia_catalogue["DEC"][i]), 'sources', radius=0.00084, fetch = True)))
        matches = matches.append(gaia_catalogue.loc[[i]])
    else:
        new_objects = new_objects.append(gaia_catalogue.loc[[i]])
gaia_catalogue.columns
gaia_catalogue["RA"][5]
gaia_catalogue["DEC"][5]


=======
    #db.search((338.673, 40.694), "sources", radius=5)
    #print (gaia_catalogue["RA"][i],gaia_catalogue["DEC"][i])
    if (len(db.search((gaia_catalogue["RA"][i],gaia_catalogue["DEC"][i]),"sources",radius = 0.00084, fetch = True))) > 0:
        #print (len(db.search((gaia_catalogue["RA"][i],gaia_catalogue["DEC"][i]),"sources",radius = 0.00084, fetch = True)))
=======
    if len(db.search((gaia_catalogue['RA'][i], gaia_catalogue['DEC'][i]), 'sources', radius=0.00084, fetch=True)) > 0:
>>>>>>> 9ac50e2b824dec96adc0ec609b1222516ef0b266
        matches = matches.append(gaia_catalogue.loc[[i]])
        # print(len(db.search((gaia_catalogue['RA'][i], gaia_catalogue['DEC'][i]), 'sources', radius=0.00084, fetch=True)))
    else:
        new_objects = new_objects.append(gaia_catalogue.loc[[i]])
<<<<<<< HEAD
print (matches.head)
len(matches)
>>>>>>> aa7cf98f67b8624fda66dec5d3918af6a03802cb:project_code/findcoordmatches.py
=======

>>>>>>> 9ac50e2b824dec96adc0ec609b1222516ef0b266

# ===============================================
# Workspace
# ===============================================
# length of db_sources
# len(db_sources)

# prints single row of gaia_catalogue
<<<<<<< HEAD
gaia_catalogue.loc[[0]]

# prints first 5 rows of gaia_catalogue
gaia_catalogue.head()

matches.head()
matches
=======
# gaia_catalogue.loc[[0]]
# prints first 5 rows of gaia_catalogue
# gaia_catalogue.head()

# ===============================================
# Plotting coordinates
# ===============================================

import astropy.coordinates as coord
import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np

# converting BDNYC database coordinates for plot
db_ra = coord.Angle(pd.to_numeric(db_sources['ra']).fillna(np.nan).values*u.degree)
db_ra = db_ra.wrap_at(180*u.degree)
db_dec = coord.Angle(pd.to_numeric(db_sources['dec']).fillna(np.nan).values*u.degree)

# converting matches csv coordinates
matches_ra = coord.Angle(matches['RA'].values*u.degree)
matches_ra = matches_ra.wrap_at(180*u.degree)
matches_dec = coord.Angle(matches['DEC'].values*u.degree)

# converting new_objects csv coordinates
new_objects_ra = coord.Angle(new_objects['RA'].values*u.degree)
new_objects_ra = new_objects_ra.wrap_at(180*u.degree)
new_objects_dec = coord.Angle(new_objects['DEC'].values*u.degree)


fig = plt.figure(figsize=(14,12))
ax = fig.add_subplot(111, projection="mollweide")
ax.set_facecolor('#17303F')
plt.grid(True)
ax.scatter(db_ra.radian, db_dec.radian, color="#E5E5E5", alpha=.8, edgecolors='face', label='in BDNYC database')
ax.scatter(matches_ra.radian, matches_dec.radian, color="#F24333", label='in BDNYC database and GAIA dataset')
ax.scatter(new_objects_ra.radian, new_objects_dec.radian, color="#E3B505", label='in GAIA dataset')
ax.legend(loc=4)
>>>>>>> 9ac50e2b824dec96adc0ec609b1222516ef0b266
