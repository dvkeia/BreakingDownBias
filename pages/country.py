import numpy as np
import pandas as pd

from taipy.gui import Markdown
import taipy.gui.builder as tgb

from data.data import overall, over_gender, over_time, over_time_gender

country_1 = 'United States'
country_2 = 'Canada'

comp_data = None

layout = {'barmode':'stack', "hovermode":"x"}
options = {"unselected":{"marker":{"opacity":0.5}}}

def comparison(country_1='United States', country_2='Canada'):
    # comp_data = overall.groupby(["Country"])
    comp_data = overall
    # print(comp_data['Country or territory'])
    # print(comp_data[comp_data['Country or territory']==nation_1])
    comp_data = comp_data[(comp_data['Country or territory']==country_1) | (comp_data['Country or territory']==country_2)]
    return comp_data

comp_data = comparison()
# bar_graph = pd.DataFrame(comp_data)
# Melting dataframe, aka pivot longer
melted = pd.melt(comp_data, id_vars=['Country or territory'], var_name='categories', value_name='values')
bar_graph = melted.pivot(index='categories', columns='Country or territory', values='values')
bar_graph.reset_index(inplace=True)


def on_change_country(state):
    print('Selected Country 1: ', state.country_1)
    print('Selected Country 2: ', state.country_2)
    state.comp_data = comparison(state.country_1, state.country_2)
    state.melted = pd.melt(state.comp_data, id_vars=['Country or territory'], var_name='categories', value_name='values')
    state.bar_graph = state.melted.pivot(index='categories', columns='Country or territory', values='values')
    state.bar_graph.reset_index(inplace=True)

def on_change_country_2(state):
    print('Selected Country 1: ', state.country_1)
    print('Selected Country 2: ', state.country_2)
    state.comp_data = comparison(state.country_1, state.country_2)
    state.melted = pd.melt(state.comp_data, id_vars=['Country or territory'], var_name='categories', value_name='values')
    state.bar_graph = state.melted.pivot(index='categories', columns='Country or territory', values='values')
    state.bar_graph.reset_index(inplace=True)

# tgb.chart("{bar_graph}", type="bar", x="GNSI", y="%")


country_md = Markdown("pages/country.md")