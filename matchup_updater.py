#!/bin/python
'''Takes player1_vs_player2_tournament file and updates scores in it
'''

import csv

#PLAYER1 = input('Who is Player1 today?: ')
PLAYER1 = 'wg'
#PLAYER2 = input('Who is Player2 today?: ')
PLAYER2 = 'sg'

def print_matchups(p1, p2):
    with open(f'{p1}_vs_{p2}_tournament.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            print(row)
        csvfile.close()

def get_row_count(p1, p2):
    with open(f'{p1}_vs_{p2}_tournament.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        count = 0
        for row in csvreader:
            count += 1
        csvfile.close()
    return count

print_matchups(PLAYER1, PLAYER2)
count = get_row_count(PLAYER1, PLAYER2)
print(count)
#with open(f'{PLAYER1}_vs_{PLAYER2}_tournament.csv', 'w') as csvhile:
    #matchup_choice = input(f'Which MATCHUP (1-{count}) are you updating?: ')
    #matchup_choice = int(matchup_choice) - 1
    #score = input('What was the score (in format 0-0)?: ')
    #print(csvreader[matchup_choice])
