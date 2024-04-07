# Country Comparator {:.color-primary}
Living a world with various cultures and diversity, societal norms and biases toward women can vary from country to country. Comparing countries allows us to uncover these nuances and understand the unique challenges faced by women in different cultural contexts. By examining how gender bias manifests in various societies, we gain valuable insights into the root causes of inequality and can develop more targeted strategies for promoting gender equity worldwide. Also, you might be surprised about how your country compares to others or just general how your country views these norms and biases.

### Select two countries from each drop down to begin comparing to understand how bias impacts all of us!

<|layout|columns=1 1 2|
<|{count_1}|selector|lov={selector_country}|on_change=on_change_country|dropdown|label=Country|>

<|{count_2}|selector|lov={selector_country}|on_change=on_change_country|dropdown|label=Country|>

Download Table: <|{file}|file_download|don't bypass_preview|>
|> 

### Bar Graph Comparison
<|{g}|chart|type=bar|x=categories|y[1]={count_1}|y[2]={count_2}|>

### Table Value Comparison 
<|{bar_graph}|table|show_all|>