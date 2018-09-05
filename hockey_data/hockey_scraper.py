"""
Multiple Scrapers from the Hockey Data API
==========================================

Website for API documentation
https://gitlab.com/dword4/nhlapi

Structure:
Scrapers - Team Info, Roster Info,

Insert SQLite - Team Info,
"""

import pandas as pd
import requests
import json
import pprint
import sqlite3
from pandas.io.json import json_normalize

conn = sqlite3.connect('/Users/Ghodgson/Databases/nhl_data.db')
c = conn.cursor()

def get_team_info():
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
    return team_final



def get_current_roster_info():
    # Select team IDs of all current teams
    c.execute("SELECT id FROM nhl_team_info_all WHERE active = 1")
    a = c.fetchall()
    output = [i[0] for i in a]

    # Connect to the website and pretty print the json in a readable format
    URL = 'https://statsapi.web.nhl.com/api/v1/teams/4/?expand=team.roster'
    r = requests.get(URL)
    data = r.json()
    pprint.pprint(data)
    #team_df = json_normalize(data['teams'])
    roster_team_df = data['teams']

    current_roster = roster_team_df[0]['roster']['roster']
    len(current_roster)
    for i in range(0, len(current_roster)):
        print(current_roster[i])





"""
Functions for inserting data into SQLite database
"""

def insert_team_info():
    conn = sqlite3.connect('/Users/Ghodgson/Databases/nhl_data.db')
    c = conn.cursor()
    for item in team_final:
      c.execute('''insert into nhl_team_info_all values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', item)
    # Lots of time was wasted here, conn.commit() finally pushed the data into the database.
    conn.commit()

    c.execute("SELECT * FROM nhl_team_info_all")
    c.fetchall()

    conn.close()
    print("Finished inserting team info.")





# Run Scrapers
get_team_info()



# Run SQLite Insert Statements
insert_team_info()

