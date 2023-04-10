
Welcome to soccer-api-wrapper's documentation!
==============================================
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

```py
from soccer_api_wrapper import soccerapi
# To check the current standings in the premier league
teams = soccerapi.get_epl_team_standings("YourAPIToken")
for team in teams:
    # prints information about the team strating from club at position 1
    print(team)
```

Similarly, there are other functions you can call on soccerapi after importing it:

```eval_rst
.. automodule:: soccerapi
    :members:
```
## Examples Of Library Usage

![[Project Preview]](./previews/get_epl_matchday.gif)

![[Project Preview]](./previews/get_epl_scorers.gif)

![[Project Preview]](./previews/get_epl_standings.gif)

![[Project Preview]](./previews/get_epl_teams.gif)

![[Project Preview]](./previews/get_player_info.gif)

![[Project Preview]](./previews/get_recent_matches.gif)

![[Project Preview]](./previews/get_team_info.gif)
