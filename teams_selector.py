#!/bin/python
''' Reads teams.csv, presents two teams at a time, allows a choice
then saves choices into a bracket
'''

import csv
import random

USER = input("Who is selecting?: ")
LOOPS = ''
while LOOPS not in ['4', '8', '16']:
    LOOPS = input('How many teams will you need? [4][8][16]: ')

def team_selector():
    '''This just chooses two random teams from the csv file'''
    with open('teams.csv', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        random_team_number_1 = random.randint(1, 120)
        random_team_number_2 = random.randint(1, 120)
        for row in csvreader:
            if int(row['Index']) == random_team_number_1:
                team_1_name = row["Name"]
                team_1_info = f'{row["Name"]} ({row["League"]})({row["OverAll"]})'
            elif int(row['Index']) == random_team_number_2:
                team_2_name = row["Name"]
                team_2_info = f'{row["Name"]} ({row["League"]})({row["OverAll"]})'
    return (team_1_name, team_1_info, team_2_name, team_2_info)

team_choices = []
def team_choice():
    '''This is where the user chooses one or the other'''
    team_options = team_selector()
    print(f'Option [1]: {team_options[1]}')
    print(f'Option [2]: {team_options[3]}')
    user_choice = ''
    while user_choice not in ['1', '2']:
        user_choice = input("Choose [1] or [2]: ")
    if user_choice == "1":
        print(f'You have chosen {team_options[0]}\n')
        team_choices.append([team_options[0]])
    else:
        print(f'You have chosen {team_options[2]}\n')
        team_choices.append([team_options[2]])

def main():
    '''Selects the correct amount of teams, and saves them'''
    loops = 0
    while loops < int(LOOPS):
        team_choice()
        loops += 1

    with open(f'{USER}_choices.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerows(team_choices)

if __name__ == "__main__":
    main()
