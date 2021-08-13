import read
import matplotlib.pyplot as plt

# function to plot total runs scored by team.
def plot_total_run_by_team(data):

    x = data.keys()       # x is array of teams
    y = data.values()     # y is array of count of matches for respective team

    # plotting the figure

    plt.figure(figsize=(10, 5))
    plt.bar(x, y)
    plt.xlabel('Teams')
    plt.ylabel('Total runs')
    plt.title('Total Runs By team')
    plt.show()

    # END..

# function to plot total run scored by batsman for a team
def plot_batsman_run_by_team(data, team):

    x = data.keys()       # x is array of players
    y = data.values()     # y is array of count of runs for respective player

    # plotting the figure

    plt.figure(figsize=(10, 5))
    plt.bar(x, y)
    plt.xlabel('Batsman')
    plt.ylabel(f'Total runs for {team}')
    plt.title(f'Runs scored by players for {team}')
    plt.show()

    # END..

# function to plot count of foreign umprie by origin country
def plot_foreign_umprire_analysis(data):

    x = data.keys()       # x is array of countries
    y = data.values()     # y is array of count of umpires by country

    # plotting the figure

    plt.figure(figsize=(10, 5))
    plt.bar(x, y)
    plt.xlabel('Country')
    plt.ylabel('Count')
    plt.title('Count of Umprires by Country')
    plt.show()

    # END..

# function to plot matches played by team
def plot_matches_played_by_team_by_session(data):

    # change type of set to list and get all the seasons
    seasons = list(data[1])

    x = data[0].keys()    # x is array of teams
    y = []                # y is 2d array of matches count for every team by year

    # iterate through all the seasons
    for season in seasons:
        
        # tempray array to store count for a team by season
        temp = []
        for team, info in data[0].items():
            temp.append(data[0][team][season])

        y.append(temp)

    # plot first season
    plt.bar(x, y[0], label=f"{seasons[0]}")
    last = y[0]

    for i in range(1, len(y)):
        
        plt.bar(x, y[i], bottom=last, label=f"{seasons[i]}")

        # this is utilty variable needs to be passed in ploting function.
        last = [last[j] + y[i][j] for j in range(len(last))]
    
    plt.xlabel('Teams')
    plt.ylabel('Matches Played')
    plt.title('Matches Played by team by season')
    plt.legend()
    plt.show()

    # END..

# Main function...
def main():

    # get data for total runs by team
    data = read.get_total_runs_by_team()

    # plot bar chart
    plot_total_run_by_team(data)

    # get data for player runs for a team
    data = read.get_player_runs_by_team('Royal Challengers Bangalore')

    # plot the chart
    plot_batsman_run_by_team(data, 'Royal Challengers Bangalore')

    # get data for matches count by team and by session
    data = read.played_by_team_by_season()

    # plot bar chart by team
    plot_matches_played_by_team_by_session(data)


# If this is the running file
if __name__ == '__main__':

    # Run Main
    main()