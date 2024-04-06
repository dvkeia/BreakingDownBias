import pandas as pd
import json

overall = pd.read_csv('data/A1.csv')

over_gender = pd.read_csv('data/A2.csv')

over_time = pd.read_csv('data/A3a.csv')

over_time_gender = pd.read_csv('data/A3b.csv')

with open("data/countries.geojson") as f:
    geojson = json.load(f)