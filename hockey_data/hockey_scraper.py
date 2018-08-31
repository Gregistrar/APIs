# Website for API documentation
# https://gitlab.com/dword4/nhlapi

import pandas as pd
import requests
import json
import pprint
import sqlite3
from pandas.io.json import json_normalize


# Connect to the website and pretty print the json in a readable format
URL = 'https://statsapi.web.nhl.com/api/v1/teams/{}'
#r = requests.get(URL)
#data = r.json()
#pprint.pprint(data)

# Loop that collects data for all teams that are both active and inactive
all_team_frames = []
for i in range(1,55):
    r = requests.get(URL.format(i))
    df = r.json()
    team_df = json_normalize(df['teams'])
    team_name = team_df.iloc[0]['name'].encode('ascii', 'ignore')
    print("Processing.........{}".format(team_name))
    all_team_frames.append(team_df)

team_concat = pd.concat(all_team_frames, ignore_index=True)
team_concat.head()
team_concat.info()

team_concat.columns = team_concat.columns.str.replace('.', '_')
team_final = team_concat.values.tolist()

conn = sqlite3.connect('/Users/Ghodgson/Databases/nhl_data.db')
c = conn.cursor()
for item in team_final:
  c.execute('''insert into nhl_team_info_all values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', item)
# Lots of time was wasted here, conn.commit() finally pushed the data into the database.
conn.commit()

c.execute("SELECT * FROM nhl_team_info_all")
c.fetchall()

conn.close()





# This was the first test run of the NHL Data API. Leaving this here for future references.

# # First level keys are 'copyright' and 'teams'
# data.keys()
# team_df = json_normalize(data['teams'])
# team_df.info()
#
# # Find the second level of keys in the json data
# a = json.dumps(data)
# b = json.loads(a)
# l = b["teams"][0].keys()
# print(l)
#
# # Subset of the data that only includes team information
# teams_data = data['teams']
#
# # Print team name and arena. Testing the different keys and values in the data.
# team_info = []
# for i in range(len(teams_data)):
#     print("The", teams_data[i]['name'], "play at", teams_data[i]['venue']['name'], "in",
#           teams_data[i]['venue']['city'] + ".")
#     list = []
#     list.append(teams_data[i]['id'])
#     list.append(teams_data[i]['abbreviation'])
#     list.append(teams_data[i]['name'])
#     list.append(teams_data[i]['teamName'])
#     list.append(teams_data[i]['venue']['name'])
#     list.append(teams_data[i]['venue']['city'])
#     list.append(teams_data[i]['locationName'])
#     try:
#         list.append(teams_data[i]['firstYearOfPlay'])
#     except:
#         list.append(None)
#     list.append(teams_data[i]['division']['id'])
#     list.append(teams_data[i]['division']['name'])
#     list.append(teams_data[i]['division']['nameShort'])
#     list.append(teams_data[i]['conference']['id'])
#     list.append(teams_data[i]['conference']['name'])
#     list.append(teams_data[i]['franchise']['franchiseId'])
#     list.append(teams_data[i]['franchise']['teamName'])
#     list.append(teams_data[i]['officialSiteUrl'])
#     list.append(teams_data[i]['active'])
#     team_info.append(list)
#
# df = pd.DataFrame(team_info)



