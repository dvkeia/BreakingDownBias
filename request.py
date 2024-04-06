from dotenv import load_dotenv
import os
import requests
import json

# Load environment variables from .env file
load_dotenv()

# Access the API key from the environment
API_KEY = os.getenv('API_KEY')


url = 'https://api.data.gov/ed/collegescorecard/v1/schools.json?fields=school.name'

page = 1

# API parameters
params = {
    'api_key': API_KEY 
}

# Make the API request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the API response
    data = response.json()

    file_path = 'test.json'
    
    # Access the specific column
    for school in data['results']:
        print(school['school.name'])

    # Write the JSON data to a file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"JSON data saved to {file_path}")

    # Read the JSON file
    with open(file_path, 'r') as json_file:
        # Load the JSON data
        data = json.load(json_file)
    
    # Print all contents of the JSON data
    print(json.dumps(data, indent=4))
else:
    print(f"Failed to fetch data: {response.status_code}")