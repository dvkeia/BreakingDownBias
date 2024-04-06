# Breaking Down Bias - Country Comparison Statistics
Select two countries to compare their gender bias indices

<|{country_1}|>

<|layout|columns=1 1 1|> <|{country_1}|selector|lov={selector_country}|on_change=on_change_country|dropdown|label=Country|>

<|layout|columns=2 2 2|> <|{country_2}|selector|lov={selector_country}|on_change=on_change_country|dropdown|label=Country|>

BAR GRAPH DATA:
<|{bar_graph}|>

<|{bar_graph}|chart|type=bar|x=categories|y=Percent|y[1]={country_1}|y[2]={country_2}|title=Comparison of Gender Bias between Men and Women|> 

<|{pie_graph}|chart|type=pie|values=values|labels=labels|title={country_1} bias chart|>
<|{pie_graph_2}|chart|type=pie|values=values|labels=labels|title={country_2} bias chart|>