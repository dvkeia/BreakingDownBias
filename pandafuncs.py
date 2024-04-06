import pandas as pd
import requests
import json
import os

def read_json(file):
    with open(file, 'r') as json_file:
        return json.load(json_file)
        # if 'metadata' in data:
        #     return data['results']
        # else:
        #     return data
    
def read_data(file):
    # Main function to access data from different pages
    # Read JSON data from the file
    json_data = read_json(file)

    # Check if the JSON data contains metadata
    if 'metadata' in json_data:
        total_pages = json_data[0][1]
    else:
        total_pages = 1

    # Access data from each page
    for page_number in range(1, total_pages + 1):
        page_data = json_data[1] if page_number == 1 else read_json(f"{file[:-5]}_{page_number}.json")[1]
        print(f"Page {page_number}:")
        for record in page_data:
            print(record[0])
        print()  # Add a newline between pages

# def run():
#     json_path = 'test'

#     df = read_data(json_path)

#     test = pd.read_json(json.dumps('test.json'))
#     print("test: " + test.head())
    
#     print(df.head())
#     print(df.tail())
    