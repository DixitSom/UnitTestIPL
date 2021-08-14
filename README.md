# IPL

## Introduction
This is a python project to do data analysis on IPL data of all years. In this project I majorly focused on following problems.
* Plot a chart of the total runs scored by each teams over the history of IPL
* Consider only games played by Royal Challengers Bangalore. Now plot the total runs scored by every batsman playing for Royal Challengers Bangalore over the history of IPL
* Obtain a source for country of origin of umpires. Plot a chart of number of umpires by in IPL by country. Indian umpires should be ignored as this would dominate the graph
* Plot a stacked bar chart of ...
  * number of games played
  * by team
  * by season
  
***
## Data
For our project we have to comma saprated files.
1. deliveries.csv
2. matches.csv

where *deliveries.csv* contains data for every ball of entire IPL history. it has 21 columns as following.
```
match_id,inning,batting_team,bowling_team,over,ball,batsman,non_striker,bowler,is_super_over,wide_runs,bye_runs,legbye_runs,noball_runs,penalty_runs,batsman_runs,extra_runs,total_runs,player_dismissed,dismissal_kind,fielder
```

and *matches.csv* contains information about every match for entire IPL history. it has 18 columns as following.
```
id,season,city,date,team1,team2,toss_winner,toss_decision,result,dl_applied,winner,win_by_runs,win_by_wickets,player_of_match,venue,umpire1,umpire2,umpire3
```

You can download these files from this [link](https://www.kaggle.com/manasgarg/ipl/version/5).
***
## Requirements

First [download](https://www.python.org/downloads/) and [install](https://www.javatpoint.com/how-to-install-python) __python__.

Setup pip as described [here](https://pip.pypa.io/en/stable/installation/).

Install following dependecies using ```pip install package-name```
```
cycler==0.10.0
kiwisolver==1.3.1
matplotlib==3.4.2
numpy==1.21.1
Pillow==8.3.1
pyparsing==2.4.7
python-dateutil==2.8.2
six==1.16.0
```

Or you can hit *pip install -r requirement.txt*

***
## Setup and Run
Make sure you installed are the dependecies as discussed above.

Then run __main.py__ file using ``` python main.py ```

***
## References

* https://www.python.org/downloads/
* https://pip.pypa.io/en/stable/installation/
* https://www.javatpoint.com/how-to-install-python

