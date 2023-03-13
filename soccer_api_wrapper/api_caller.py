import requests

api_token = 'XXXXXXXXXXXXXXXXXXX'
team_id_mapping = {
    57: 'Arsenal',
    65: 'Manchester City',
    66: 'Manchester United',
    73: 'Tottenham Hotspur',
    67: 'Newcastle United',
    63: 'Fulham',
    64: 'Liverpool',
    397: 'Brighton & Hove Albion',
    402: 'Brentford',
    61: 'Chelsea',
    58: 'Aston Villa',
    354: 'Crystal Palace',
    351: 'Nottingham Forest',
    338: 'Leicester City',
    76: 'Wolverhampton Wanderers',
    563: 'West Ham United',
    341: 'Leeds United',
    62: 'Everton',
    1044: 'Bournemouth',
    340: 'Southampton',
}


def get_recent_matches():
    uri = 'https://api.football-data.org/v4/matches'
    headers = {'X-Auth-Token': api_token}
    response = requests.get(uri, headers=headers)
    return response.json()


def get_epl_team_matches(team):
    id = get_key(team, team_id_mapping)
    uri = f'https://api.football-data.org/v4/teams/{id}/ \
        matches?status=SCHEDULED'
    headers = {'X-Auth-Token': api_token}
    response = requests.get(uri, headers=headers)
    return response.json()


def get_epl_team_standings():
    uri = 'https://api.football-data.org/v4/competitions/PL/standings'
    headers = {'X-Auth-Token': api_token}
    response = requests.get(uri, headers=headers)
    return response.json()["standings"][0]["table"]


def get_epl_top_scorers():
    uri = 'https://api.football-data.org/v4/competitions/PL/scorers'
    headers = {'X-Auth-Token': api_token}
    response = requests.get(uri, headers=headers)
    return response.json()["scorers"]


def get_epl_matchday(matchday):
    uri = f'https://api.football-data.org/v4/competitions/PL/matches? \
        matchday={matchday}'
    headers = {'X-Auth-Token': api_token}
    response = requests.get(uri, headers=headers)
    return response.json()


def get_key(val, mapping):
    for key, value in mapping.items():
        if val == value:
            return key
