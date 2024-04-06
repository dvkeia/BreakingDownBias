from taipy.gui import Gui 
import taipy.gui.builder as tgb
from math import cos, exp
from pandafuncs import read_data
from pages.home import home_md
from pages.country import country_md

pages = {"home": home_md, "country": country_md}

if __name__ == "__main__":
    Gui(pages=pages).run()









