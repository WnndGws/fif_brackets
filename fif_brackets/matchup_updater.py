#!/bin/python
'''Takes player1_vs_player2_tournament file and updates scores in it
'''

import csv

#PLAYER1 = input('Who is Player1 today?: ')
PLAYER1 = 'wg'
#PLAYER2 = input('Who is Player2 today?: ')
PLAYER2 = 'sg'

def print_matchups():
    with open(f'{PLAYER1}_vs_{PLAYER2}_tournament.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            print(row)
        csvfile.close()

def get_row_count():
    with open(f'{PLAYER1}_vs_{PLAYER2}_tournament.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        count = 0
        for row in csvreader:
            count += 1
        csvfile.close()
    return count

print_matchups()
count = get_row_count()

matchup_choice = input(f'Which MATCHUP (1-{count}) are you updating?: ')
matchup_choice = int(matchup_choice) - 1
score = input('What was the score (in format 0-0)?: ')

with open(f'{PLAYER1}_vs_{PLAYER2}_tournament.csv', 'r') as [csvfile, tmpfile]:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvwriter = csv.reader(tmpfile, delimiter=',')
    print(csvreader.readlines()[matchup_choice])
