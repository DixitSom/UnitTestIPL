import csv
from os import read

# Data Files.
deliveries_csv = './data/deliveries.csv'
matches_csv = './data/matches.csv'


def get_total_runs_by_team():
    
    """
    return: dictionary containing team name as keys and total runs scored as value
    """

    # Dictionary To Store runs by team.
    total_runs_by_team = dict()
    with open(deliveries_csv) as file:
        reader = csv.reader(file)

        # First Row Needs to avoided.
        first_row = next(reader)

        # Iterating Through all rows
        for row in reader:

            playing_team = row[2]     # get team name
            total_run = int(row[-4])       # get total run on the ball
            
            # IF playing team is in dictionary.
            if playing_team in total_runs_by_team.keys():
                total_runs_by_team[playing_team] += total_run
            else:
                total_runs_by_team[playing_team] = total_run
        
    return total_runs_by_team


def get_player_runs_by_team(team):

    """
    return: A dictionary containing player name as key and runs scored as value.
    """

    # Dictionary to Store players Runs by a given team.
    player_runs_by_team = dict()

    with open(deliveries_csv) as file:

        reader = csv.reader(file)
        
        # First Row needs to be removed
        first_row = next(reader)
        
        #Iterating Throw All rows
        for row in reader:

            playing_team = row[2]        # Get Player Team
            player_run = int(row[-6])    # Get Run Made by Player on The Ball
            player_name = row[6]         # Get Player Name

            # if team is same as the playing team
            if playing_team == team:
                
                # Check if player name in the dictionary
                if player_name in player_runs_by_team.keys():
                    player_runs_by_team[player_name] += player_run
                else:
                    player_runs_by_team[player_name] = player_run
            else:
                pass

    return player_runs_by_team


def foreign_umprire_analysis():
    """
    return: A dictionary that contains count of umpires by country
    """
    # it will store count of umpires by country
    umpires_by_country = dict()

    # dictionary to store all umpries information.
    umpires = {'Kumar Dharmasena':'Sri Lanka',
                'Marais Erasmus':'South Africa',
                'Simon Taufel':'Australia',
                'Chris Gaffaney':'New Zealand',
                'Asad Rauf':'Pakistan',
                'Bruce Oxenford':'Australia',
                'Rod Tucker':'Australia',
                'Billy Doctrove':'West Indies',
                'Rudi Koertzen':'South Africa',
                'Billy Bowden':'New Zealand',
                'Aleem Dar':'Pakistan',
                'Nigel Llong':'England',
                'Richard Illingworth':'England',
                'Russell Tiffin':'Zimbabwe',
                'Daryl Harper':'Australia',
                'Paul Reiffel':'Australia',
                'Brian Jerling':'South Africa',
                'Johan Cloete':'South Africa',
                'Ian Howell':'South Africa',
                'Mark Benson':'England',
                'Gary Baxter':'New Zealand',
                'Steve Davis':'Australia',
                'Simon Fry':'Australia',
                'Ian Gould':'England',
                'Tony Hill':'New Zealand',
                'Tyron Wijewardene':'Sri Lanka'
                }

    # it will count umpires by origin country
    for name, country in umpires.items():

        # if country is in dictionary
        if country in umpires_by_country.keys():
            umpires_by_country[country] += 1
        else:
            umpires_by_country[country] = 1
    
    return umpires_by_country

def played_by_team_by_season():

    """
    return: nested dictionary, matches count by team and season 
    """
    
    # nested dictionary match count by team and season
    match_count_by_team_by_session = dict()

    # it will store all the seasons available in our dataset
    all_seasons = set()

    with open(matches_csv) as file:

        reader = csv.reader(file)

        # First Row needs to be removed..
        first_row = next(reader)

        for row in reader:

            season = row[1]   # get the season
            team1 = row[4]    # get the team1
            team2 = row[5]    # get the team2

            all_seasons.add(season)

            #  see if team1 already in dictionary
            if team1 in match_count_by_team_by_session.keys():
                
                # see if season already in dictionary
                if season in match_count_by_team_by_session[team1].keys():
                    match_count_by_team_by_session[team1][season] += 1
                else:
                    match_count_by_team_by_session[team1][season] = 1
            else:
                match_count_by_team_by_session[team1] = dict()
            
            #  see if team2 already in dictionary
            if team2 in match_count_by_team_by_session.keys():

                # see if season already in dictionary
                if season in match_count_by_team_by_session[team2].keys():
                    match_count_by_team_by_session[team2][season] += 1
                else:
                    match_count_by_team_by_session[team2][season] = 1
            else:
                match_count_by_team_by_session[team2] = dict()


    # It will store 0 value for all seasons that are not played by teams
    # to help in plotting 

    for key, value in match_count_by_team_by_session.items():
        for season in all_seasons:

            # if team did not played any match in season then store 0 for that season
            if not season in value.keys():
                match_count_by_team_by_session[key][season] = 0

    return match_count_by_team_by_session, all_seasons