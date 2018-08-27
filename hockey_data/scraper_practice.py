# Website for API documentation
# https://gitlab.com/dword4/nhlapi


import requests
import json
import pprint

# Connect to the website and pretty print the json in a readable format
URL = 'https://statsapi.web.nhl.com/api/v1/teams'
r = requests.get(URL)
data = r.json()
pprint.pprint(data)

# First level keys are 'copyright' and 'teams'
data.keys()

# Find the second level of keys in the json data
a = json.dumps(data)
b = json.loads(a)
l = b["teams"][0].keys()
print(l)

# Subset of the data that only includes team information
teams_data = data['teams']

# Print team name and arena. Testing the different keys and values in the data.
team_info = []
for i in range(len(teams_data)):
    print("The", teams_data[i]['name'], "play at", teams_data[i]['venue']['name'], "in",
          teams_data[i]['venue']['city'] + ".")
    list = []
    list.append(teams_data[i]['id'])
    list.append(teams_data[i]['name'])
    list.append(teams_data[i]['venue']['name'])
    list.append(teams_data[i]['venue']['city'])
    team_info.append(list)


