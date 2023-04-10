# soccer-api-wrapper

soccer-api-wrapper is a library for getting information about soccer matches in the five big club competitions, with live score, fixtures, and stats of games available. 

[![](https://img.shields.io/static/v1?label=license&message=Apache-2.0&color=%3CCOLOR%3E)](./LICENSE)
[![](https://img.shields.io/github/issues/Debi-Ejeta/soccer-api-wrapper)](../../issues)
[![codecov](https://codecov.io/gh/Debi-Ejeta/soccer-api-wrapper/branch/main/graph/badge.svg?token=1MBRYEYR2J)](https://codecov.io/gh/Debi-Ejeta/soccer-api-wrapper)
[![Build Status](https://github.com/Debi-Ejeta/soccer-api-wrapper/actions/workflows/workflow.yml/badge.svg)](https://github.com/Debi-Ejeta/soccer-api-wrapper/actions/workflows/workflow.yml)
[![PyPI](https://img.shields.io/pypi/v/soccer-api-wrapper)](https://pypi.org/project/soccer-api-wrapper/)
[![Documentation Status](https://readthedocs.org/projects/soccer-api-wrapper/badge/?version=latest)](https://soccer-api-wrapper.readthedocs.io/en/latest/?badge=latest)

## Overview

As writing GET and POST requests multiple times to get data can be frustrating, the library will streamline the process of retrieving information about soccer by making the API calls under the hood as an API Wrapper. So if anyone wants to create an app or a bot on apps like Telegram, they will be able to make use of this library to easily create their apps or bots for anything related to soccer without having to make api calls every single time. 

## Getting Started

To get started using this library follow the instructions below.

### Installing

If you run into an issue please check the closed issues on the github, although feel free to re-open a new issue if you find an issue that's been closed for a few months. The codebase can and does run into similar issues as it has before, because the api this library is based on changes things up.

```sh
pip install soccer_api_wrapper
```

## Quick Start Guide

In order to use this library, you will need to first get an API token from 
https://www.football-data.org/ as this library is completely based on that 
API and you will need to provide that token every time you use the functions 
listed below

In the first verion of this library, only the premier league is supported. 
Other league functionalities will be added in future versions. 

![[Project Preview]](./docs/previews/get_epl_scorers.gif)

Similarly, there are other functions you can call on soccerapi after importing it:

```py
# returns the matches happening within the next couple of days
soccerapi.get_recent_matches("YourAPIToken")
```

```py
# returns the matches happening for the team inputted
soccerapi.get_epl_team_matches("YourAPIToken", "TeamName")
```

```py
# returns the top scorers in the premier league
soccerapi.get_epl_top_scorers("YourAPIToken")
```

```py
# returns the premier league matches on Matchday 12
soccerapi.get_epl_matchday("YourAPIToken", 12)
```

```py
# returns information about the team inputted
# You can access the team_ids down below
soccerapi.get_team_info("YourAPIToken", "team_id")
```

```py
# returns the teams that are currently in the premier league
soccerapi.get_epl_teams("YourAPIToken")
```

```py
# returns information about the player with player_id = 44
soccerpi.get_recent_matches("YourAPIToken", 44)
```
You can find the IDs of the teams in the premier league below

| Team_ID     | Team Name                  |
| ----------- | -------------------------- |
| 57          | Arsenal                    |
| 65          | Manchester City            |
| 66          | Manchester United          |
| 73          | Tottenham Hotspur          |
| 67          | Newcastle United           |
| 63          | Fulham                     |
| 64          | Liverpool                  |
| 397         | Brighton & Hove Albion     |
| 402         | Brentford                  |
| 61          | Chelsea                    |
| 58          | Aston Villa                |
| 354         | Crystal Palace             |
| 351         | Nottingham Forest          |
| 338         | Leicester City             |
| 76          | Wolverhampton Wanderers    |
| 563         | West Ham United            |
| 341         | Leeds United               |
| 62          | Everton                    |
| 1044        | Bournemouth                |
| 340         | Southampton                |



