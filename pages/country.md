# Breaking Down Bias - Country Comparison Statistics
Select two countries to compare their gender bias indices

<|layout|columns=1 1 1|> <|{country_1}|selector|lov={selector_country}|on_change=on_change_country|dropdown|label=Country|>

<|layout|columns=2 2 2|> <|{country_2}|selector|lov={selector_country}|on_change=on_change_country_2|dropdown|label=Country|>

<|{bar_graph}|chart|type=bar|x=categories|y=Percent|y[1]={country_1}|y[2]={country_2}|title=Comparison of Gender Bias between Men and Women|> |>