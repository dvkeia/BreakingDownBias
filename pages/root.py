from taipy.gui import Markdown

import numpy as np

from data.data import overall, over_gender, over_time, over_time_gender

selector_country = list(np.sort(overall['Country or territory'].astype(str).unique()))
selector_category = list(np.sort(overall.columns).astype(str))
print(selector_category)
# country_1 = 'United States'
# country_2 = 'Canada'
# category = 'GSNI1'

def to_text(val):
    return '{:,}'.format(int(val)).replace(',', ' ')

root = Markdown("pages/root.md")