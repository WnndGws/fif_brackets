#!/bin/python
'''Scrapes a website for the top 120 teams and outputs a file
'''

import csv
import requests_html

session = requests_html.HTMLSession()

index = 1
teams_list = []

for i in range(1,5):
    # The url i want to scrape, care about 1st 4 pages
    url = f"https://www.fifaindex.com/teams/fifa20/{i}/?order_by=overallrating&order=0"

    # Get content into memory
    r = session.get(url)

    teams = r.html.find('tr')
    for team in teams:
        try:
            team_name = team.find('td')[1].full_text
            league = team.find('td')[2].full_text
            overall = team.find('td')[6].full_text
            teams_list.append({'Name': team_name, "League": league, "OverAll": overall, "Index": index})
            index += 1
        except:
            pass

with open('../data/teams.csv', 'w') as csvfile:
    fieldnames = ['Name', 'League', 'OverAll', 'Index']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(teams_list)
