from taipy.gui import Markdown 

import numpy as np

from data.data import overall, over_gender, over_time, over_time_gender

selector_country = list(np.sort(overall['Country or territory'].astype(str).unique()))
selector_category = list(["GSNI1","GSNI2","NB","Political","Educational","Economic","Physical"])
country_1 = 'United States'
country_2 = 'Canada'

def to_text(val):
    return '{:,}'.format(int(val)).replace(',', ' ')

root = Markdown("pages/root.md")