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

def generateMatchtables(matches):

    parallax_data = list()
    propermotions_data = list()
    Photometry_data = list()

    parallax_data.append(['source_id','parallax', 'parallax_unc','publication_shortname', 'adopted','comments'])
    propermotions_data.append(['source_id','proper_motion_ra', 'proper_motion_ra_unc','proper_motion_dec', 'proper_motion_dec_unc','publication_shortname', 'comments'])
    Photometry_data.append(['source_id','band','magnitude','magnitude_unc','publication_shortname', 'comments'])

    for i in range(len(matches)):
        parallax_data.append([int(matches.iloc[[i]]['source_id'].values[0]),
        matches.iloc[[i]]['PARALLAX'].values[0],
        matches.iloc[[i]]['PARALLAX_ERROR'].values[0],
        'GaiaDR2', 1, 'added by SpectreCell'])

        propermotions_data.append([matches.iloc[[i]]['source_id'].values[0],
        matches.iloc[[i]]['PMRA'].values[0],
        matches.iloc[[i]]['PMRA_ERROR'].values[0],
        matches.iloc[[i]]['PMDEC'].values[0],
        matches.iloc[[i]]['PMDEC_ERROR'].values[0],
        'GaiaDR2','added by SpectreCell'])

        Photometry_data.append([matches.iloc[[i]]['source_id'].values[0], 'GaiaDR2_G', matches.iloc[[i]]['PHOT_G_MEAN_MAG'].values[0], matches.iloc[[i]]['PHOT_G_MEAN_MAG_ERROR'].values[0], 'GaiaDR2', 'added by SpectreCell'])

        Photometry_data.append([matches.iloc[[i]]['source_id'].values[0], 'GaiaDR2_BP', matches.iloc[[i]]['PHOT_BP_MEAN_MAG'].values[0], matches.iloc[[i]]['PHOT_BP_MEAN_MAG_ERROR'].values[0], 'GaiaDR2', 'added by SpectreCell'])

        Photometry_data.append([matches.iloc[[i]]['source_id'].values[0], 'GaiaDR2_RP', matches.iloc[[i]]['PHOT_RP_MEAN_MAG'].values[0], matches.iloc[[i]]['PHOT_RP_MEAN_MAG_ERROR'].values[0], 'GaiaDR2', 'added by SpectreCell'])

    return parallax_data, propermotions_data, Photometry_data
    # db.add_data(parallax_data, 'parallaxes')
    # db.add_data(propermotions_data, 'proper_motions')
    # db.add_data(propermotions_data, 'proper_motions')

def generateNewObjtables(new_objects, db, addSourceTable=False):
    NOparallax_data = list()
    NOpropermotions_data = list()
    NOphotometry_data = list()


    NOparallax_data.append(['source_id','parallax', 'parallax_unc','publication_shortname', 'adopted','comments'])
    NOphotometry_data.append(['source_id','band', 'magnitude','magnitude_unc', 'publication_shortname', 'comments'])
    NOpropermotions_data.append(['source_id','proper_motion_ra', 'proper_motion_ra_unc','proper_motion_dec', 'proper_motion_dec_unc','publication_shortname', 'comments'])

    for i in range(len(new_objects)):
        db_sourceid=db.search((new_objects.iloc[i]['RA'], new_objects.iloc[i]['DEC']), 'sources', radius=0.00278, fetch=True)['id'][0]
        # parallax data
        NOparallax_data.append([db_sourceid, new_objects.iloc[[i]]['PARALLAX'].values[0], new_objects.iloc[[i]]['PARALLAX_ERROR'].values[0], 'GaiaDR2', 1, 'added by SpectreCell'])
        #proper_motions data
        NOpropermotions_data.append([db_sourceid,
        new_objects.iloc[[i]]['PMRA'].values[0],
        new_objects.iloc[[i]]['PMRA_ERROR'].values[0],
        new_objects.iloc[[i]]['PMDEC'].values[0],
        new_objects.iloc[[i]]['PMDEC_ERROR'].values[0],
        'GaiaDR2', 'added by SpectreCell'])
        # photometry data
        NOphotometry_data.append([db_sourceid, 'GaiaDR2_G',
        new_objects.iloc[[i]]['PHOT_G_MEAN_MAG'].values[0],
        new_objects.iloc[[i]]['PHOT_G_MEAN_MAG_ERROR'].values[0],
        'GaiaDR2', 'added by SpectreCell'])

        NOphotometry_data.append([db_sourceid, 'GaiaDR2_BP',
        new_objects.iloc[[i]]['PHOT_BP_MEAN_MAG'].values[0],
        new_objects.iloc[[i]]['PHOT_BP_MEAN_MAG_ERROR'].values[0],
        'GaiaDR2', 'added by SpectreCell'])

        NOphotometry_data.append([db_sourceid, 'GaiaDR2_RP',
        new_objects.iloc[[i]]['PHOT_RP_MEAN_MAG'].values[0],
        new_objects.iloc[[i]]['PHOT_RP_MEAN_MAG_ERROR'].values[0],
        'GaiaDR2', 'added by SpectreCell'])

        NOphotometry_data.append([db_sourceid, '2MASS_J',
        new_objects.iloc[[i]]['TMASSJ'].values[0],
        new_objects.iloc[[i]]['TMASSJERR'].values[0],
        'GaiaDR2', 'added by SpectreCell'])

        NOphotometry_data.append([db_sourceid, '2MASS_H',
        new_objects.iloc[[i]]['TMASSH'].values[0],
        new_objects.iloc[[i]]['TMASSHERR'].values[0],
        'GaiaDR2', 'added by SpectreCell'])

        NOphotometry_data.append([db_sourceid, '2MASS_K',
        new_objects.iloc[[i]]['TMASSK'].values[0],
        new_objects.iloc[[i]]['TMASSKERR'].values[0],
        'GaiaDR2', 'added by SpectreCell'])

        NOphotometry_data.append([db_sourceid, 'WISE_W1',
        new_objects.iloc[[i]]['WISEW1'].values[0],
        new_objects.iloc[[i]]['WISEW1ERR'].values[0],
        'GaiaDR2', 'added by SpectreCell'])

        NOphotometry_data.append([db_sourceid, 'WISE_W2',
        new_objects.iloc[[i]]['WISEW2'].values[0],
        new_objects.iloc[[i]]['WISEW2ERR'].values[0],
        'GaiaDR2', 'added by SpectreCell'])

        NOphotometry_data.append([db_sourceid, 'WISE_W3',
        new_objects.iloc[[i]]['WISEW3'].values[0],
        new_objects.iloc[[i]]['WISEW3ERR'].values[0],
        'GaiaDR2', 'added by SpectreCell'])

        NOphotometry_data.append([db_sourceid, 'GUNNG',
        new_objects.iloc[[i]]['GUNNG'].values[0],
        new_objects.iloc[[i]]['GUNNGERR'].values[0],
        'GaiaDR2', 'added by SpectreCell'])

        NOphotometry_data.append([db_sourceid, 'GUNNR',
        new_objects.iloc[[i]]['GUNNR'].values[0],
        new_objects.iloc[[i]]['GUNNRERR'].values[0],
        'GaiaDR2', 'added by SpectreCell'])

        NOphotometry_data.append([db_sourceid, 'GUNNI',
        new_objects.iloc[[i]]['GUNNI'].values[0],
        new_objects.iloc[[i]]['GUNNIERR'].values[0],
        'GaiaDR2', 'added by SpectreCell'])

        NOphotometry_data.append([db_sourceid, 'GUNNZ',
        new_objects.iloc[[i]]['GUNNZ'].values[0],
        new_objects.iloc[[i]]['GUNNZERR'].values[0],
        'GaiaDR2', 'added by SpectreCell'])

        NOphotometry_data.append([db_sourceid, 'GUNNY',
        new_objects.iloc[[i]]['GUNNY'].values[0],
        new_objects.iloc[[i]]['GUNNYERR'].values[0],
        'GaiaDR2', 'added by SpectreCell'])
    return NOparallax_data, NOpropermotions_data, NOphotometry_data

    # db.add_data(Noparallax_data, 'parallaxes')
    # db.add_data(NOpropermotions_data, 'proper_motions')
    # db.add_data(NOpropermotions_data, 'proper_motions')
    len(NOparallax_data)
    len(NOpropermotions_data)
    len(NOphotometry_data)

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

matches = pd.read_csv('matches.csv', index_col=0)
new_objects = pd.read_csv('new_objects.csv', index_col=0)
# ===============================================
# import files needed
# ===============================================
# import gaia csv
gaia_catalogue = pd.read_csv('/Users/ashley/Documents/BridgeUP-STEM-SpectreCell/GUCDScat.csv')
# import bdnyc database
db = astrodb.Database('BDNYCdb_practice/bdnycdev_copy.db')

# ===============================================
# sort data into matches and not matches and save as new csv files
# ===============================================

# matches, new_objects= matches_sortCSV(gaia_catalogue, db, save=True)
# ===============================================
# Workspace
# ===============================================

 Parallax_data, Propermotions_data, Photometry_data = generateMatchtables(matches)
 len(Parallax_data)
NOparallax_data, NOpropermotions_data, NOphotometry_data= generateNewObjtables(new_objects, db)
 len(NOparallax_data)
# create new empty list to store data we want to add to database

# db.search("added by SpectreCell", 'parallaxes')
# len(db.search("added by spectrecell", 'parallaxes', fetch=True))
# db.inventory(204)

# db.modify("DELETE FROM Photometry WHERE comments='added by SpectreCell'")

 len(db.query("SELECT * FROM photometry WHERE magnitude = -99999.0 AND comments='added by SpectreCell'"))

db.modify("DELETE FROM photometry WHERE magnitude = -99999.0 AND comments ='added by SpectreCell'")
