# imports pandas
import pandas as pd
# loads new csv file
Gaia = pd.read_csv('../../../../gaia_data/all_catalog.csv')
#
Gaia.head()
from astrodbkit import astrodb
BDNYC = astrodb.Database('../../../../BDNYCdb_practice/bdnycdev_copy.db')
pwd
