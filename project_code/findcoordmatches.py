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

def matches_sortCSV(gaia_catalogue, db, save=False):
    # ===============================================
    # create new empty dataframes to store gaia data
    # ===============================================

    # matches will store gaia data for objects in BDNYC database
    matches = pd.DataFrame(columns=np.insert(gaia_catalogue.columns.values, 0, 'source_id', axis=0))

    # new_objects will store gaia data for objects that do not exist in BDNYC database
    new_objects = pd.DataFrame(columns=gaia_catalogue.columns.values)
    # needs_review will store gaia data for objects that have too many matched in the database and need further review
    needs_review = pd.DataFrame(columns=gaia_catalogue.columns.values)

    # ===============================================
    # sort each row of gaia data into matches/new_objects using celestial coordinates: right ascension (ra/RA) and declination (dec/DEC)
    # ===============================================
    for i in range(len(gaia_catalogue)):
        results=db.search((gaia_catalogue['RA'][i], gaia_catalogue['DEC'][i]), 'sources', radius=0.00278, fetch=True)
        if len(results) == 1:
            matches = matches.append(gaia_catalogue.loc[[i]])
            matches['source_id'].loc[i]=results['id'][0]
        elif len(results)>1:
        # if there is MORE THAN ONE result, just print a note
            needs_review = needs_review.append(gaia_catalogue.loc[[i]])
        else:
            new_objects = new_objects.append(gaia_catalogue.loc[[i]])

    if save==True:
        saveCSVfiles(matches, new_objects, needs_review)
    return matches, new_objects

def saveCSVfiles(matches, new_objects, needs_review):
    matches.to_csv('matches.csv')
    new_objects.to_csv('new_objects.csv')
    needs_review.to_csv('needs_review.csv')
    print('matches, new_objects, and needs_review saved as CSV files.')

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
# matches = pd.read_csv('matches.csv', index_col=0)
# new_objects = pd.read_csv('new_objects.csv', index_col=0)


# ===============================================
# variables needed
# ===============================================

# list all from sources into format of pandas stored as new variable
# db_sources = db.query('SELECT * FROM sources', fmt='pandas')


# ===============================================
# sort data into matches and not matches and save as new csv files
# ===============================================

# matches, new_objects= matches_sortCSV(gaia_catalogue, db)


# ===============================================
# Workspace
# ===============================================


##################################################
# Parallax table
##################################################

# create new empty list to store data we want to add to database
parallax_data = list()

# append the column name (as it's written in the BDNYC database) to match on the appropriate column
parallax_data.append(['source_id','parallax', 'parallax_unc','publication_shortname', 'adopted','comments'])
parallax_data

for i in range(len(matches)):
    parallax_data.append([int(matches.iloc[[i]]['source_id'].values[0]), matches.iloc[[i]]['PARALLAX'].values[0], matches.iloc[[i]]['PARALLAX_ERROR'].values[0], 'GaiaDR2', 1, 'added by SpectreCell'])

parallax_data

# add data to BDNYC database
# db.search("added by SpectreCell", 'parallaxes')
# len(db.search("added by spectrecell", 'parallaxes', fetch=True))
# db.inventory(204)

# db.modify("DELETE FROM proper_motions WHERE comments='added by SpectreCell'")





##################################################
# Proper motions table
##################################################


# create new empty list to store data we want to add to database
propermotions_data = list()

# append the column name (as it's written in the BDNYC database) to match on the appropriate column
propermotions_data.append(['source_id','proper_motion_ra', 'proper_motion_ra_unc','proper_motion_dec', 'proper_motion_dec_unc','publication_shortname', 'comments'])
print(propermotions_data)

for i in range(len(matches)):
     propermotions_data.append([matches.iloc[[i]]['source_id'].values[0], matches.iloc[[i]]['PMRA'].values[0], matches.iloc[[i]]['PMRA_ERROR'].values[0], matches.iloc[[i]]['PMDEC'].values[0], matches.iloc[[i]]['PMDEC_ERROR'].values[0],'GaiaDR2','added by SpectreCell'])
propermotions_data

# add data to BDNYC database
db.add_data(propermotions_data, 'proper_motions')


matches.columns

##################################################
# Photomerty table
##################################################

# create new empty list to store data we want to add to databas
Photometry_dataBP = list()
# append the column name (as it's written in the BDNYC database) to match on the appropriate column
Photometry_dataBP.append(['source_id','magnitude','magnitude_unc','publication_shortname','band', 'comments'])
print(Photometry_dataBP)
for i in range(len(matches)):
     Photometry_dataBP.append([matches.iloc[[i]]['source_id'].values[0],matches.iloc[[i]]['PHOT_BP_MEAN_MAG'].values[0],matches.iloc[[i]]['PHOT_BP_MEAN_MAG_ERROR'].values[0],'GaiaDR2_BP','added by SpectreCell'])
len(Photometry_dataBP)

Photometry_dataG = list()
Photometry_dataG.append(['source_id','magnitude','magnitude_unc','publication_shortname','band', 'comments'])
print(Photometry_dataG)
for i in range(len(matches)):
     Photometry_dataG.append([matches.iloc[[i]]['source_id'].values[0],matches.iloc[[i]]['PHOT_G_MEAN_MAG'].values[0],matches.iloc[[i]]['PHOT_G_MEAN_MAG_ERROR'].values[0],'GaiaDR2_G','added by SpectreCell'])
len(Photometry_dataG)

Photometry_dataRP = list()
Photometry_dataRP.append(['source_id','magnitude','magnitude_unc','publication_shortname','band', 'comments'])
print(Photometry_dataRP)
for i in range(len(matches)):
    Photometry_dataRP.append([matches.iloc[[i]]['source_id'].values[0],  matches.iloc[[i]]['PHOT_RP_MEAN_MAG'].values[0],matches.iloc[[i]]['PHOT_RP_MEAN_MAG_ERROR'].values[0],'GaiaDR2_RP','added by SpectreCell'])
len(Photometry_dataRP)


# add data to BDNYC database
# db.add_data(Photomerty_data, 'Photomerty')
