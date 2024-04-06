import numpy as np
from taipy.gui import Markdown, State
import plotly.express as px
import pandas as pd
import taipy.gui.builder as tgb
from data.data import overall, over_gender, over_time, over_time_gender, geojson

category = 'GSNI1'
selector_category = list((overall.columns[3:]).astype(str))
gnsi_map = None

def set_map(filterval):
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

gnsi_map = set_map(category)


def on_change_category(state : State):
    print(state.category)
    state.gnsi_map = set_map(state.category)


map_md = Markdown("pages/map/map.md")