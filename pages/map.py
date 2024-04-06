import numpy as np
from taipy.gui import Markdown
import plotly.express as px

from data.data import overall, over_gender, over_time, over_time_gender, geojson

filter = 'GSNI1'
# selector_filter= ['GSNI1','GSNI2','NB','Political','Educational','Economic','Physical']
gnsi_map = None

def set_map(filterval='GSNI1'):
    gnsi_map = px.choropleth_mapbox(
        overall,
        geojson=geojson, 
        featureidkey="id",
        locations="ISO3",
        color=filterval,
        zoom=1,
        center={"lat": 0, "lon": 0},
        mapbox_style="carto-positron", 
        title=f'{filterval} by Country'
    )  
    return gnsi_map

gnsi_map = set_map()


def on_change_filter(state):
    print(state.filter)
    state.gnsi_map = set_map(state.filter)


map_md = Markdown("pages/map.md")