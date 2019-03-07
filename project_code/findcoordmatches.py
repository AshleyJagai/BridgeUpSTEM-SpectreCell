# ===============================================
# import libraries
# ===============================================
import pandas as pd
from astrodbkit import astrodb
import astropy.coordinates as coord
import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np
# ===============================================
# function definitions
# ===============================================
def matches_sortCSV(gaia_catalogue, db):
    # ===============================================
    # create new empty dataframes to store gaia data
    # ===============================================
    # matches will store gaia data for objects in BDNYC database
    matches = pd.DataFrame(columns=gaia_catalogue.columns.values)
    # new_objects will store gaia data for objects that do not exist in BDNYC database
    new_objects = pd.DataFrame(columns=gaia_catalogue.columns.values)
    needs_review = pd.DataFrame(columns=gaia_catalogue.columns.values)
    # ===============================================
    # sort each row of gaia data into matches/new_objects using celestial coordinates: right ascension (ra/RA) and declination (dec/DEC)
    # ===============================================
    for i in range(len(gaia_catalogue)):
        if len(db.search((gaia_catalogue['RA'][i], gaia_catalogue['DEC'][i]), 'sources', radius=0.00278, fetch=True)) == 1:
            matches = matches.append(gaia_catalogue.loc[[i]])
        elif len(db.search((gaia_catalogue['RA'][i], gaia_catalogue['DEC'][i]), 'sources', radius=0.00278, fetch=True)) > 1:
            needs_review = needs_review.append(gaia_catalogue.loc[[i]])
        else:
            new_objects = new_objects.append(gaia_catalogue.loc[[i]])
    return matches, new_objects, needs_review
def saveCSVfiles(matches, new_objects, needs_review):
    matches.to_csv('matches.csv')
    new_objects.to_csv('new_objects.csv')
    needs_review.to_csv('needs_review.csv')
    print('matches and new_objects saved as CSV files.')
def plotCoords(db_sources, matches, new_objects):
# ===============================================
# Plotting coordinates
# ===============================================
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
##################################################
# CODE STARTS HERE
##################################################
# ===============================================
# import files needed
# ===============================================
# import gaia csv
gaia_catalogue = pd.read_csv('gaia_data/all_catalog.csv')
# import bdnyc database
db = astrodb.Database('BDNYCdb_practice/bdnycdev_copy.db')
# load matches and new_objects csvs
matches = pd.read_csv('matches.csv', index_col=0)
new_objects = pd.read_csv('new_objects.csv', index_col=0)
needs_review = pd.read_csv('needs_review.csv', index_col=0)
matches.shape
# ===============================================
# variables needed
# ===============================================
# list all from sources into format of pandas stored as new variable
# db_sources = db.query('SELECT * FROM sources', fmt='pandas')
# ===============================================
# sort data into matches and not matches and save as new csv files
# ===============================================
# needs_review, matches, new_objects = matches_sortCSV(gaia_catalogue, db)
saveCSVfiles(needs_review, matches, new_objects)
# ===============================================
# Workspace
# ===============================================
#drop empty spaces and first character J from shortname
#matches.SHORTNAME = matches.SHORTNAME.str[2:]
# create new empty list to store data we want to add to database
# data = list()
# # append the column name (as it's written in the BDNYC database) to match on the appropriate column
# data.append(['source_id','parallax','parallax_unc','publication_shortname','adopted','comments'])
# data
# for i in range(len(matches)):
#    results = db.search((matches['RA'].iloc[i], matches['DEC'].iloc[i]), 'sources', radius=0.00278, fetch=True)
#    if len(results) == 1:
#        # matches = matches.append(gaia_catalogue.loc[[i]])
#        data.append([results['id'][0] , matches['PARALLAX'].iloc[i] , matches['PARALLAX_ERROR'].iloc[i] , "GaiaDR2", 1 ,"added by spectre cell"])
#    elif (len(results)>1):
#        # if there is MORE THAN ONE result, just print a note
#        print('more than one match')
#    else:
#        # if there are NO results, print a note
#        print('no matches')
#
# # add data to BDNYC database
# db.add_data(data, 'parallaxes')
# db.search("added by spectre cell", 'parallaxes')

data
gaia_catalogue.columns



data = list()
# append the column name (as it's written in the BDNYC database) to match on the appropriate column
data.append(['source_id','PMRA','PMRA_ERROR', 'PMDEC', 'PMDEC_ERROR', 'publication_shortname','comments'])
len(data)
for i in range(len(matches)):
   results = db.search((matches['RA'].iloc[i], matches['DEC'].iloc[i]), 'sources', radius=0.00278, fetch=True)
   if len(results) == 1:
       # matches = matches.append(gaia_catalogue.loc[[i]])
        data.append([results['id'][0] , matches['PMRA'].iloc[i], matches['PMRA_ERROR'].iloc[i], matches['PMDEC'].iloc[i] , matches['PMDEC_ERROR'].iloc[i], "GaiaDR2","added by spectre cell"])
   else:
       # if there are NO results, print a note
       print('no matches')

len(data)
data

# add data to BDNYC database
db.add_data(data, 'proper_motions')
