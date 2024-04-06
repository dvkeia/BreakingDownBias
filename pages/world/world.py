import numpy as np
import pandas as pd

from taipy.gui import Markdown, State

from data.data import overall, over_gender, over_time, over_time_gender

comp_data = over_gender
countries = over_gender['Country or territory'].to_list()
politics_w = over_gender['PoliticalW'].to_list()
politics_m = over_gender['PoliticalM'].to_list()
politics_mNeg = [-1 * value for value in politics_m]
physical_w = over_gender['PhysicalW'].to_list()
physical_m = over_gender['PhysicalM'].to_list()
physical_mNeg = [-1 * value for value in physical_m]
edu_w = over_gender['EducationalW'].to_list()
edu_m = over_gender['EducationalM'].to_list()
edu_mNeg = [-1 * value for value in edu_m]
eco_w = over_gender['EconomicW'].to_list()
eco_m = over_gender['EconomicM'].to_list()
eco_mNeg = [-1 * value for value in eco_m]

physical = pd.DataFrame({
    'Country': countries,
    'Female': physical_w,
    'Male': physical_mNeg
})

politics = pd.DataFrame({
    'Country': countries,
    'Female': politics_w,
    'Male': politics_mNeg
})

edu = pd.DataFrame({
    'Country': countries,
    'Female': edu_w,
    'Male': edu_mNeg
})

eco = pd.DataFrame({
    'Country': countries,
    'Female': eco_w,
    'Male': eco_mNeg
})


properties = {
    # Shared y values
    "y":              "Country",
    # Bars for the female data set
    "x[1]":           "Female",
    "color[1]":       "#c26391",
    # Bars for the male data set
    "x[2]":           "Male",
    "color[2]":       "#5c91de",
    # Both data sets are represented with an horizontal orientation
    "orientation":    "h",
    # 
    "layout": {
        "barmode": "overlay",
        # Set a relevant title for the x axis
        "xaxis": { "title": "Percent By Gender" },
        # Hide the legend
        "showlegend": False
    }
}


world_md = Markdown("pages/world/world.md")