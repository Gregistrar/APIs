"""
SQLite table creation for the nhl_data Database
===============================================

Creates the following tables in the nhl_data schema on SQLite:
team_info, etc...
"""

import sqlite3

conn = sqlite3.connect('/Users/Ghodgson/Databases/nhl_data.db')
c = conn.cursor()

# Create the table for NHL Team Info
c.execute('''CREATE TABLE IF NOT EXISTS team_info (
            id integer
            , team_abbreviation text
            , team_name text
            , team text
            , arena_name text
            , city text
            , location_name text
            , founding_year integer
            , division_id integer
            , division_name text
            , division_abbreviation text
            , conference_id integer
            , conference_name text
            , franchise_id integer
            , franchise_team_name text
            , official_team_website text
            , active text
            )
            ''')

conn.close()


# For testing purposes ONLY
# dropTable = "DROP TABLE team_info"
# c.execute(dropTable)
