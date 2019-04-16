from astropy import units as u
from astropy.coordinates import SkyCoord
import pandas as pd
from astrodbkit import astrodb
import numpy as np

db = astrodb.Database('BDNYCdb_practice/bdnycdev_copy.db')

celestialCoords = db.query('SELECT sources.id, ra, dec, sources.comments, shortname, parallax, parallax_unc FROM sources JOIN parallaxes ON sources.id = source_id', fmt='pandas')


pi = celestialCoords['parallax'] * u.arcsec / 1000.

sig_pi = celestialCoords['parallax_unc'] * u.arcsec / 1000.

celestialCoords['distance'] = (1 * u.pc * u.arcsec) / pi

celestialCoords['distance_unc'] = sig_pi * u.pc * u.arcsec / pi ** 2

spekCords = celestialCoords[["ra", "dec", "distance", "id"]].dropna()
spekCords["x"] = np.nan
spekCords["y"] = np.nan
spekCords["z"] = np.nan
i
c
c.cartesian.x
c.cartesian.y
c.cartesian.z


for i in spekCords.index:
    c = SkyCoord(ra = (spekCords["ra"][i] * u.arcsecond).to(u.degree), dec = (spekCords["dec"][i] * u.arcsecond).to(u.degree), distance = spekCords["distance"][i] * u.pc)
    spekCords["x"][i]= c.cartesian.x/u.pc
    spekCords["y"][i]= c.cartesian.y/u.pc
    spekCords["z"][i]= c.cartesian.z/u.pc

spekCords[["x","y","z"]].to_csv('BDNYCcoord.speck',header=None, index=None, sep=' ')
