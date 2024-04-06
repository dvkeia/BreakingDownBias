from taipy.gui import Gui 
import taipy.gui.builder as tgb
import taipy as tp
from math import cos, exp
from pandafuncs import read_data
from pages.home import home_md
from pages.country import country_md
from pages.map import map_md
from pages.world import world_md
from pages.root import root, country_1, country_2, selector_country, to_text

pages = {
    "/":  root,
    "home": home_md, 
    "country": country_md,
    "map" : map_md,
    "world" : world_md
    }

gui_multi_pages = Gui(pages=pages)

if __name__ == "__main__":
    tp.Core().run()
    Gui(pages=pages).run(title='Breaking Down Bias')









