# Breaking Down Bias
## By: Devika Kumar & Elle Strauss

## Citations: 
GSNI Data Set: https://hdr.undp.org/content/2023-gender-social-norms-index-gsni#/indicies/GSNI

Taipy Dashbaord Reference: https://github.com/Avaiga/demo-covid-dashboard

## DEMO Breaking Down Bias!
Link: https://breakingdownbias.taipy.cloud/
Using Taipy Cloud. Much Faster!!!

Link: https://delightful-ocean-a03f55f0c7594b37b4a442bfd1fce055.azurewebsites.net/
Deploy via Microsoft Azure. A little (very) slow, but it works! So be patient!

## Inspiration
We wanted to try something new at the hackathon that pushed us outside our comfort zone. When we saw Taipy, we thought it would be a perfect way to learn something new and refresh our skills in python. For the project, we decided to use a data set on gender bias throughout the world to create data visualizations to help people understand biases against women. Breaking Down Bias offers a exploration of bias through data visualization to empower users to understand and address societal inequalities and biases.

## What it does
Breaking Down Bias has three main features (Country Comparator, World View, and World Map) for the user to interact with and our home screen, which explains the importance of the topic and a quick break down of the categories studied. 
With the Country Comparator feature, users can compare the impact of bias between two different nations, gaining insights into the unique challenges each country faces. Breaking Down Bias sheds light on the disparities affecting communities worldwide.
Delve deeper with the World View feature, where we dissect the four dimensions of bias (political, physical, educational, and economic) and illustrate how each gender perceives them. Through interactive charts and analysis, users gain a comprehensive understanding of the nuanced layers of societal prejudice and how even women themselves can hold these biases.
Navigate the landscape of bias with ease using the World Map function, allowing users to filter and visualize bias percentages across the globe. The filter feature enable us to observe closely the percentages of bias, whether it no bias, at least one bias in the dimension, or specific dimension bias. 

## How we built it
We built Breaking Down Bias with Taipy and Python, leveraging pandas for seamless data management and Taipy for easy to create dashboards with data visualization. We transformed the Excel sheets from 2023 Gender Social Norms Index Report into CSV files, reforming the sheets to only include the tables of data without any merged cells or unnecessary cells to make it easy to read through pandas. We used markdown to format the pages and display the graphs and information.

## Challenges we ran into
**Learning Curve with Taipy:** The team encountered difficulties due to being new to Taipy, with limited examples available to guide them through the development process.
**Data Manipulation Issues:** Initially, the team struggled with manipulating the dataset for the country comparator feature, where we used pandas melt and pivot functions to convert the data of the two countries into an easy to use format for graphing. Despite successfully updating the data, the graph wouldn't display correctly when passed through to markdown. After revisiting their approach, they found a better solution, although continuous updates to Taipy still posed challenges.
**Buggy Taipy Layout Component:** The Taipy layout component used in markdown presented unexpected errors initially, which eventually resolved itself, as errors would be thrown with the correct formatting. The team found this puzzling as they were using the same code that previously caused issues.
**Keyword Conflict:** The team encountered issues when using a variable called "filter" in our Map code as we did not realize it conflicted with a keyword that already existed in Python. Debugging and researching took several hours to help resolve the conflict.
**API Key Challenges:** Initially, we intended to use the college scorecard data set; however, we faced difficulties due to the large CSV files, leading them to use an API key instead. Our lack of experience with API keys and handling JSON data, especially dealing with multiple pages, proved challenging, leading us to pivot to a different project.

## Accomplishments that we're proud of
The accomplishment we are the most proud of are learning a new library to use with python and finishing the project. For both of us, Taipy is very new and we never heard of it before, which was fun to get to spend time experimenting with it as we probably would have never touched. We are thrilled that we were able to finish the project and have some results to share with you all. Also, we are extremely proud of figuring out the data manipulation issue and filter issue, which we spent some much time mess around with and removing code, adding it back to see what works. 

## What we learned
This was an amazing learning experience, especially with understanding how to do data visualization. We learned how to use Taipy and pandas in python, which was a lot of fun getting to play with the code to change the data we used. Planning things out is wonderful, at the end of Friday, we set a plan in motion which definitely helped keep us on track for our Saturday time of coding and completing the project. We learned how read through documentation and reference resources that Taipy provide to develop our dashboard.

## What's next for Breaking Down Bias
In the future, we would love to add styling to make it more on theme with the logo we developed and make the text more organized and neat. We would love to add a filter or feature to show the change over time as some countries participated in multiple waves of the index, which would be interesting to see whether biases have shifted or stayed steady. We think adding a resources tab would be great to provide resources on further research into this topic or ways you can get involved with reducing biases towards women in the 4 main dimensions.
