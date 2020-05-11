#!/bin/python
'''Takes two files and creates a matchup bracket from them
'''

import csv
import random

PLAYER1 = input('Who is competing today?: ')
PLAYER1_TEAMS = []
PLAYER1_FILE = f'{PLAYER1}_choices.csv'

PLAYER2 = input('Who else is competing today?: ')
PLAYER2_TEAMS = []
PLAYER2_FILE = f'{PLAYER2}_choices.csv'

with open(PLAYER1_FILE, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        PLAYER1_TEAMS.append(row[0])
with open(PLAYER2_FILE, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        PLAYER2_TEAMS.append(row[0])

random.shuffle(PLAYER1_TEAMS)
random.shuffle(PLAYER2_TEAMS)

MATCHUPS = []
for i in range(len(PLAYER1_TEAMS)):
    MATCHUPS.append([f'MATCHUP {i+1}: {PLAYER1_TEAMS[i]} vs {PLAYER2_TEAMS[i]}'])

with open(f'{PLAYER1}_vs_{PLAYER2}_tournament.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerows(MATCHUPS)
