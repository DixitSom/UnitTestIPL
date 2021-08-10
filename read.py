import csv
from os import read

# Data Files.
deliveries_csv = './data/deliveries.csv'
matches_csv = './data/matches.csv'


def get_total_runs_by_team():

    # Dictionary To Store runs by team.
    total_runs_by_team = dict()
    with open(deliveries_csv) as file:

        reader = csv.reader(file)

        # First Row Needs to avoided.
        first_row = next(reader)

        for row in reader:

            playing_team = row[2]
            total_run = row[-4]
            
            if playing_team in total_runs_by_team.keys():
                total_runs_by_team[playing_team] += total_run
            else:
                total_runs_by_team[playing_team] = total_run
        
    return total_runs_by_team