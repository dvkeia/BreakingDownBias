# import numpy as np
# import pandas as pd

# from taipy.gui import Markdown, State

# from data.data import overall, over_gender, over_time, over_time_gender

# count_1 = 'United States'
# count_2 = 'Canada'

# comp_data = None

# def comparison(count_1='United States', count_2='Canada'):
#     # comp_data = overall.groupby(["Country"])
#     comp_data = overall
#     # print(comp_data['Country or territory'])
#     # print(comp_data[comp_data['Country or territory']==nation_1])
#     comp_data = comp_data[(comp_data['Country or territory']==count_1) | (comp_data['Country or territory']==count_2)]
#     return comp_data

# # def switching(bar_graph):
# #     melted = pd.melt(bar_graph, id_vars=['Country or territory'], var_name='categories', value_name='values')
# #     print(melted)
# #     melted.reset_index(inplace=True)
# #     test = melted.pivot(index='categories', columns='Country or territory', values='values')
# #     test.reset_index(inplace=True)
# #     print(test)
# #     return test

# comp_data = comparison()
# bar_graph = pd.DataFrame(comp_data).drop(['ISO3', 'Period'], axis=1)
# # test = switching(bar_graph)


# def on_change_country(state : State):
#     print('Selected Country 1: ', state.count_1)
#     print('Selected Country 2: ', state.count_2)
#     state.comp_data = comparison(state.count_1, state.count_2)
#     state.bar_graph = pd.DataFrame(state.comp_data).drop(['ISO3', 'Period'], axis=1)
#     # state.test = switching(state.bar_graph)
#     # print(state.test)
#     # melted = pd.melt(state.comp_data, id_vars=['Country or territory'], var_name='categories', value_name='values')
#     # state.bar_graph = melted.pivot(index='categories', columns='Country or territory', values='values')

# count_md = Markdown("pages/country/count.md")