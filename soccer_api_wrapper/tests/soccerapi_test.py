from soccer_api_wrapper import soccerapi
import unittest
from unittest.mock import patch


class Tests(unittest.TestCase):
    def test_get_recent_matches(self):
        with patch('requests.get') as mock_get:
            soccerapi.get_recent_matches("test_token")
            self.assertEqual(mock_get.called, True)

    def test_get_epl_team_matches(self):
        with patch('requests.get') as mock_get:
            soccerapi.get_epl_team_matches("test_token", "test")
            self.assertEqual(mock_get.called, True)

    def test_get_epl_team_matches_for_a_team(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.json().text = {
                "id": "57",
                "team": "Arsenal",
                "matchday": "14",
                "opposition": "Manchester City",
            }
            response = soccerapi.get_epl_team_matches("test_token", "Arsenal")
            self.assertEqual(response.text["id"], "57")
            self.assertEqual(response.text["team"], "Arsenal")
            self.assertEqual(response.text["matchday"], "14")
            self.assertEqual(response.text["opposition"], "Manchester City")

    def test_get_epl_team_standings(self):
        with patch('requests.get') as mock_get:
            soccerapi.get_epl_team_standings("test_token")
            self.assertEqual(mock_get.called, True)

    def test_get_epl_top_scorers(self):
        with patch('requests.get') as mock_get:
            soccerapi.get_epl_top_scorers("test_token")
            self.assertEqual(mock_get.called, True)

    def test_get_epl_matchday(self):
        with patch('requests.get') as mock_get:
            soccerapi.get_epl_matchday("test_token", 23)
            self.assertEqual(mock_get.called, True)

    def test_get_team_info(self):
        with patch('requests.get') as mock_get:
            soccerapi.get_team_info("test_token", 23)
            self.assertEqual(mock_get.called, True)
