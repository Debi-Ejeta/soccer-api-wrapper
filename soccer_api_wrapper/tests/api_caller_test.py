import api_caller
import unittest
from unittest.mock import patch
import sys

sys.path.insert(1, '../soccer-api-wrapper')


class Tests(unittest.TestCase):
    def test_get_recent_matches(self):
        with patch('api_caller.requests.get') as mock_get:
            api_caller.get_recent_matches()
            self.assertEqual(mock_get.called, True)

    def test_get_epl_team_matches(self):
        with patch('api_caller.requests.get') as mock_get:
            api_caller.get_epl_team_matches("test")
            self.assertEqual(mock_get.called, True)

    def test_get_epl_team_matches_for_a_team(self):
        with patch('api_caller.requests.get') as mock_get:
            mock_get.return_value.json().text = {
                "id": "57",
                "team": "Arsenal",
                "matchday": "14",
                "opposition": "Manchester City",
            }
            response = api_caller.get_epl_team_matches("Arsenal")
            self.assertEqual(response.text["id"], "57")
            self.assertEqual(response.text["team"], "Arsenal")
            self.assertEqual(response.text["matchday"], "14")
            self.assertEqual(response.text["opposition"], "Manchester City")

    def test_get_epl_team_standings(self):
        with patch('api_caller.requests.get') as mock_get:
            api_caller.get_epl_team_standings()
            self.assertEqual(mock_get.called, True)

    def test_get_epl_top_scorers(self):
        with patch('api_caller.requests.get') as mock_get:
            api_caller.get_epl_top_scorers()
            self.assertEqual(mock_get.called, True)

    def test_get_epl_matchday(self):
        with patch('api_caller.requests.get') as mock_get:
            api_caller.get_epl_matchday(23)
            self.assertEqual(mock_get.called, True)
