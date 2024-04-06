# THIRD TIMES A CHARM

<|layout|columns=1 1 1|> <|{count_1}|selector|lov={selector_country}|on_change=on_change_country|dropdown|label=Country|>

<|layout|columns=2 2 2|> <|{count_2}|selector|lov={selector_country}|on_change=on_change_country|dropdown|label=Country|>

<|{count_1}|> && <|{count_2}|>

<|{bar_graph}|table|show_all|>

<|{g}|table|show_all|>

<|{g}|chart|type=bar|x=categories|y[1]={count_1}|y[2]={count_2}|>
