import pandas as pd
from astrodbkit import astrodb

# import gaia csv
gaia_catalogue = pd.read_csv('gaia_data/all_catalog.csv')

# import bdnyc database
db = astrodb.Database('BDNYCdb_practice/bdnycdev_copy.db')

db.query('select source_id from sources')


