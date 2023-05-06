import requests

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


def get_recent_matches(api_token):
    """Function that returns recent matches that happened/will happen

    Args:
        api_token (str): api token user gets after registering at \
        https://www.football-data.org/

    Returns:
        dict

    """
    uri = 'https://api.football-data.org/v4/matches'
    headers = {'X-Auth-Token': api_token}
    response = requests.get(uri, headers=headers)
    return response.json()


def get_team_matches(api_token, team):
    """Function that returns matches for a particular team

    Args:
        api_token (str): api token user gets after registering at \
        https://www.football-data.org/
        team (str): name of the football in the format laid out in the doc

    Returns:
        dict

    """
    id = get_key(team, team_id_mapping)
    uri = f'https://api.football-data.org/v4/teams/{id}/ \
        matches'
    headers = {'X-Auth-Token': api_token}
    response = requests.get(uri, headers=headers)
    return response.json()


def get_epl_team_standings(api_token):
    """Function that returns the standings of the premier league

    Args:
        api_token (str): api token user gets after registering at \
        https://www.football-data.org/

    Returns:
        dict

    Raises:
        KeyError: If the maximum threshold of api calls is reached

    """
    uri = 'https://api.football-data.org/v4/competitions/PL/standings'
    headers = {'X-Auth-Token': api_token}
    response = requests.get(uri, headers=headers)
    try:
        team_standings = response.json()["standings"][0]["table"]
        return team_standings
    except KeyError:
        print("Maximum threshold reached")
        return response


def get_epl_top_scorers(api_token):
    """Function that returns the top scorers in the premier league

    Args:
        api_token (str): api token user gets after registering at \
        https://www.football-data.org/

    Returns:
        dict

    Raises:
        KeyError: If the maximum threshold of api calls is reached

    """
    uri = 'https://api.football-data.org/v4/competitions/PL/scorers'
    headers = {'X-Auth-Token': api_token}
    response = requests.get(uri, headers=headers)
    try:
        scorers = response.json()["scorers"]
        return scorers
    except KeyError:
        print("Maximum threshold reached")
        return response


def get_epl_matchday(api_token, matchday):
    """Function that returns matches happening on a particular \
    matchday in the premier league

    Args:
        api_token (str): api token user gets after registering at \
        https://www.football-data.org/
        matchday (int): the value of the matchday

    Returns:
        dict

    """
    uri = f'https://api.football-data.org/v4/competitions/PL/matches? \
        matchday={matchday}'
    headers = {'X-Auth-Token': api_token}
    response = requests.get(uri, headers=headers)
    return response.json()


def get_competitions_for_team(api_token, team_id):
    """Function that returns the competitions a particular team is in

    Args:
        api_token (str): api token user gets after registering at \
        https://www.football-data.org/
        team_id (int): id of the team

    Returns:
        list of competitions

    """
    uri = f'http://api.football-data.org/v4/teams/{team_id}'
    headers = {'X-Auth-Token': api_token}
    response = requests.get(uri, headers=headers)
    competitions = response.json()["runningCompetitions"]
    return competitions


def get_players_of_team(api_token, team_id):
    """Function that returns the players in a team

    Args:
        api_token (str): api token user gets after registering at \
        https://www.football-data.org/
        team_id (int): id of the team

    Returns:
        list of players

    """
    uri = f'http://api.football-data.org/v4/teams/{team_id}'
    headers = {'X-Auth-Token': api_token}
    response = requests.get(uri, headers=headers)
    squad = response.json()["squad"]
    return squad


def get_player_by_position(api_token, team_id, position):
    """Function that returns the players in a team at play at \
       the position specified

    Args:
        api_token (str): api token user gets after registering at \
        https://www.football-data.org/
        team_id (int): id of the team
        position (str): position of players requested

    Returns:
        list of players

    """
    res = []
    squad = get_players_of_team(api_token, team_id)
    for player in squad:
        if player["position"][0] == position[0]:
            res.append(player)
    return res


def get_ucl_matches(api_token):
    """Function that returns matches happening in the champions league

    Args:
        api_token (str): api token user gets after registering at \
        https://www.football-data.org/

    Returns:
        dict

    """
    uri = 'https://api.football-data.org/v4/competitions/CL/matches'
    headers = {'X-Auth-Token': api_token}
    response = requests.get(uri, headers=headers)
    return response.json()


def get_matches(api_token, competition_name):
    """Function that returns matches happening in the competition \
       requested

    Args:
        api_token (str): api token user gets after registering at \
        https://www.football-data.org/
        competition_name (str): Name of competition for which \
        matches are requested

    Returns:
        dict

    """
    uri = f'https://api.football-data.org/v4/competitions/{competition_name} \
        /matches'
    headers = {'X-Auth-Token': api_token}
    response = requests.get(uri, headers=headers)
    return response.json()


def get_head_to_head_matches(api_token, home_team_id, away_team_id):
    """Function that returns head to head matches between two given \
       teams

    Args:
        api_token (str): api token user gets after registering at \
        https://www.football-data.org/
        home_team_id (int): id of the home team
        away_team_id (int): id of the away team

    Returns:
        dict

    """
    matches_for_team = get_team_matches(api_token, home_team_id)
    match_id = -1
    for match in matches_for_team["matches"]:
        if match["homeTeam"]["id"] == home_team_id:
            if match["awayTeam"]["id"] == away_team_id:
                match_id = match["id"]
                break
    if match_id != -1:
        uri = f'http://api.football-data.org/v4/matches/{match_id}/ \
            head2head?limit=50'
        headers = {'X-Auth-Token': api_token}
        response = requests.get(uri, headers=headers)
        return response.json["matches"]
    else:
        print("Invalid ID given for one or two teams")
        return None


def get_head_to_head_stats(api_token, home_team_id, away_team_id):
    """Function that returns head to head stats between two given \
       teams including amount of wins/losses/goals

    Args:
        api_token (str): api token user gets after registering at \
        https://www.football-data.org/
        home_team_id (int): id of the home team
        away_team_id (int): id of the away team

    Returns:
        dict

    """
    matches_for_team = get_team_matches(api_token, home_team_id)
    match_id = -1
    for match in matches_for_team["matches"]:
        if match["homeTeam"]["id"] == home_team_id:
            if match["awayTeam"]["id"] == away_team_id:
                match_id = match["id"]
                break
    if match_id != -1:
        uri = f'http://api.football-data.org/v4/matches/{match_id} \
            /head2head?limit=50'
        headers = {'X-Auth-Token': api_token}
        response = requests.get(uri, headers=headers)
        return response.json["aggregates"]
    else:
        print("Invalid ID given for one or two teams")
        return None


def get_team_info(api_token, team_id):
    """Function that returns information about a particular premier league team

    Args:
        api_token (str): api token user gets after registering at \
        https://www.football-data.org/
        team_id (int): id of the team

    Returns:
        dict

    """
    uri = f'http://api.football-data.org/v4/teams/{team_id}'
    headers = {'X-Auth-Token': api_token}
    response = requests.get(uri, headers=headers)
    return response.json()


def get_epl_teams(api_token):
    """Function that returns the premier league teams in the current campaign

    Args:
        api_token (str): api token user gets after registering at \
        https://www.football-data.org/

    Returns:
        dict

    """
    uri = 'http://api.football-data.org/v4/competitions/PL/teams'
    headers = {'X-Auth-Token': api_token}
    response = requests.get(uri, headers=headers)
    return response.json()


def get_player_info(api_token, player_id):
    """Function that returns information about a player

    Args:
        api_token (str): api token user gets after registering at \
        https://www.football-data.org/
        player_id (int): id of the player

    Returns:
        dict

    """
    uri = f'http://api.football-data.org/v4/persons/{player_id}'
    headers = {'X-Auth-Token': api_token}
    response = requests.get(uri, headers=headers)
    return response.json()


def get_key(val, mapping):
    for key, value in mapping.items():
        if val == value:
            return key
