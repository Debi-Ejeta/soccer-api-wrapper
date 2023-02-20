import requests
import json

"""

First iteration: api wrapper for a specific api (like user provides a token)
Second iteration: allowing it to be used for football in general (I provide the token)
Third iteration: having a script running every minute with api call and updating datatbase with this file
                 getting info from the database

"""

api_token = '2860fa567cd942c3a7222e0b94a741b1'

def get_matches():
    uri = 'https://api.football-data.org/v4/matches'
    headers = { 'X-Auth-Token': api_token }
    response = requests.get(uri, headers=headers)
    return response.json()

def get_team_matches(team):
    team_mapping = {86: "Real Madrid"}
    id = get_key(team, team_mapping) # Just for real madrid now. Doesn't map team to ID
    uri = f'https://api.football-data.org/v4/teams/{id}/matches?status=SCHEDULED'
    headers = { 'X-Auth-Token': api_token }
    response = requests.get(uri, headers=headers)
    return response.json()

def get_team_standings():
    uri = 'https://api.football-data.org/v4/competitions/PL/standings'
    headers = { 'X-Auth-Token': api_token }
    response = requests.get(uri, headers=headers)
    return response.json()

def get_top_scorers():
    uri = 'https://api.football-data.org/v4/competitions/PL/scorers'
    headers = { 'X-Auth-Token': api_token }
    response = requests.get(uri, headers=headers)
    return response.json()

def get_matchday(matchday):
    uri = f'https://api.football-data.org/v4/competitions/PL/matches?matchday={matchday}'
    headers = { 'X-Auth-Token': api_token }
    response = requests.get(uri, headers=headers)
    return response.json()

def get_key(val, mapping):
    for key, value in mapping.items():
        if val == value:
            return key

if __name__ == "__main__":
    get_team_matches("Real Madrid")