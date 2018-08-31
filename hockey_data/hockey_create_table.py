"""
SQLite table creation for the nhl_data Database
===============================================

Creates the following tables in the nhl_data schema on SQLite:
team_info, etc...
"""

import sqlite3

# Local database connection
conn = sqlite3.connect('/Users/Ghodgson/Databases/nhl_data.db')
c = conn.cursor()

# Create the table for NHL Team Info
c.execute('''CREATE TABLE IF NOT EXISTS nhl_team_info_all (
            abbreviation integer
            , active text
            , conference_id integer
            , conference_link text
            , conference_name text
            , division_abbreviation text
            , division_id integer
            , division_link text
            , division_name text
            , division_nameShort text
            , firstYearOfPlay text
            , franchise_franchiseId integer
            , franchise_link text
            , franchise_teamName text
            , franchiseId integer
            , id integer
            , link text
            , locationName text
            , name text
            , officialSiteUrl text
            , shortName text
            , teamName text
            , venue_city text
            , venue_link text
            , venue_name text
            , venue_timeZone_id integer
            , venue_timeZone_offset integer
            , venue_timeZone_tz text
        )
''')

conn.close()


# For testing purposes ONLY
dropTable = "DROP TABLE team_info"
c.execute(dropTable)





# Old NHL Team Info table
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