from taipy.gui import Gui 
import taipy.gui.builder as tgb
import taipy as tp
import numpy as np
from pages.home.home import home_md
from pages.country.cntry import cntry_md
from pages.map.map import map_md
from pages.world.world import world_md
from pages.root import root, selector_country, selector_category, to_text
from data.data import overall, over_gender, over_time, over_time_gender

pages = {
    "/":  root,
    "home": home_md, 
    "Country": cntry_md,
    "Map" : map_md,
    "World" : world_md
}


def to_text(val):
    return '{:,}'.format(int(val)).replace(',', ' ')

gui_multi_pages = Gui(pages=pages)

if __name__ == "__main__":
    tp.Core().run()
    gui_multi_pages.run(title='Breaking Down Bias')









