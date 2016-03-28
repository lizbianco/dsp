#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

football_list = []
score_difference_list=[]
class Football(object):
    def __init__(self, team, games, wins, losses, draws, goals, goals_allowed, points):
        self.team = team
        self.games = games
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.goals = goals
        self.goals_allowed = goals_allowed
        self.points = points
        self.score_difference = abs(float(self.goals) - float(self.goals_allowed))   


def read_data(data):
    with open(data, 'r') as my_file:
        reader = csv.reader(my_file)
        next(my_file)
        for row in reader:
            football_list.append(Football(row[0], row[1], row[2],row[3], row[4], row[5], row[6], row[7]))


def get_min_score_difference(parsed_data):
    for i in parsed_data:
        score_difference_list.append(i.score_difference) 
    return min(score_difference_list)
    
    
def get_team(parsed_data):
    for i in parsed_data:
        if i.score_difference == min_score_diff:
            print (i.team)
    

read_data('football.csv')
min_score_diff = get_min_score_difference(football_list)
get_team(football_list)

   

  
