import numpy as np
import pandas as pd

from taipy.gui import Markdown, State

from data.data import overall, over_gender, over_time, over_time_gender

count_1 = 'United States'
count_2 = 'Canada'

comp_data = None

# layout = {'barmode':'stack', "hovermode":"x"}

def comparison(count_1='United States', count_2='Canada'):
    comp_data = overall
    comp_data = comp_data[(comp_data['Country or territory']==count_1) | (comp_data['Country or territory']==count_2)]
    return comp_data

def create_df(bar_graph, count_1, count_2):
    row1 = bar_graph[bar_graph['Country or territory'] == count_1]
    row2 = bar_graph[bar_graph['Country or territory'] == count_2]
    print(row1)
    cat = bar_graph.columns[1:]
    test = pd.DataFrame(index=cat)
     # Add data for count_1 and count_2 as columns
    test[count_1] = row1.iloc[0, 1:].values
    test[count_2] = row2.iloc[0, 1:].values

    # Reset index to turn categories into a regular column
    test.reset_index(inplace=True)
    test.rename(columns={'index': 'categories'}, inplace=True)
    return test

comp_data = comparison()
bar_graph = pd.DataFrame(comp_data).drop(['ISO3', 'Period'], axis=1)
print(bar_graph)
g = create_df(bar_graph, count_1, count_2)
# print(g)
# name = 'compare'+count_1+'AND'+count_2+'.csv'
# g.to_csv('download.csv', index=False)
file = 'download.xlsx'
try:
    # Convert DataFrame to CSV
    g.to_excel(file, index=False)
    print(f"CSV file '{file}' has been successfully written.")
except Exception as e:
    print(f"Error occurred while writing the CSV file: {str(e)}")

def on_change_country(state : State):
    print('Selected Country 1: ', state.count_1)
    print('Selected Country 2: ', state.count_2)
    state.comp_data = comparison(state.count_1, state.count_2)
    state.bar_graph = pd.DataFrame(state.comp_data).drop(['ISO3', 'Period'], axis=1)
    test = create_df(state.bar_graph, state.count_1, state.count_2)
    state.g = test
    # name = 'compare'+state.count_1+'AND'+state.count_2+'.csv'
    state.g.to_excel(file, index=False)
    # print(state.g)

cntry_md = Markdown("pages/country/cntry.md")