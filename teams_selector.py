#!/bin/python
''' Reads teams.csv, presents two teams at a time, allows a choice
then saves choices into a bracket
'''

import csv
import random

import click

def set_options():
    with open('teams.csv', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        random_team_number_1 = random.randint(1,120)
        random_team_number_2 = random.randint(1,120)
        for row in csvreader:
            if int(row['Index']) == random_team_number_1:
                option_1 = f'{row["Name"]} ({row["League"]})({row["OverAll"]})'
                team_1 = row["Name"]
            elif int(row['Index']) == random_team_number_2:
                option_2 = f'{row["Name"]} ({row["League"]})({row["OverAll"]})'
                team_2 = row["Name"]
    return (team_1, team_2)

team_1 = set_options()[0]
team_2 = set_options()[1]

@click.command()
@click.option('--choice', prompt=True, type=click.Choice(["1", "2"]))
def choice_made(choice):
    if choice == "1":
        return(team_1)
    else:
        return(team_2)


if __name__ == "__main__":
    print(f'[1] {team_1}')
    print(f'[2] {team_2}')
    team = choice_made()
    print(team)
