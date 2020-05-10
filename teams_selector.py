#!/bin/python
''' Reads teams.csv, presents two teams at a time, allows a choice
then saves choices into a bracket
'''

import csv
import random

with open('teams.csv', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    random_team_number = random.randint(1,120)
    for row in csvreader:
        if int(row['Index']) == random_team_number:
            print(row)
