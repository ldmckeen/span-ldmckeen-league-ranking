"""
Span League Ranking Application.

~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
<league_ranking.py> Python Function File

Author:             Lloyd McKeen
Github Username:    ldmckeen
Email:              ldmckeen@gmail.com
Company:            Span
Date:               January 2023
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

Usage: league_ranking.py(<score_input>)

===========================================================================================
"""
import logging
import re


class LeagueRanking:
    """League Ranking Class to handle objects that calculate Rankings for a League."""

    def __init__(self):
        self.league_table = {}  # Dictionary for Teams and their respective League Points
        self.match_results = ''
        self.matches_count = 0  # Total Matches Played in League

    def calculate_rankings(self, scores):
        """League Ranking table solution via newline comma seperated scores input."""
        scores = scores.rstrip('\n')  # Removing trailing newline
        self.match_results = scores.split('\n')  # Store each line input as new result

        # Loop through match results to store scores against team names
        for item in self.match_results:
            self.matches_count += 1
            # Split match result into individual teams and team scores
            try:
                team1, team2 = item.split(', ')
            except Exception as e:
                logging.error(f'Could not split input string: {e}')
                return
            team_1_name, team_1_score = re.split(r'\s(?=\d+(?!\S))', team1)
            team_2_name, team_2_score = re.split(r'\s(?=\d+(?!\S))', team2)

            # Check if team exists in existing team's dictionary, if not add it.
            if team_1_name not in self.league_table:
                self.league_table[team_1_name] = 0
            if team_2_name not in self.league_table:
                self.league_table[team_2_name] = 0

            # Check who won, lost or if a draw
            if int(team_1_score) == int(team_2_score):
                self.league_table[team_1_name] += 1
                self.league_table[team_2_name] += 1
            elif int(team_1_score) > int(team_2_score):
                self.league_table[team_1_name] += 3
            elif int(team_2_score) > int(team_1_score):
                self.league_table[team_2_name] += 3

        # Sort League Table (points descending and Team name alphabetically if draw
        print(f'Total Matches Played: {self.matches_count}')
        rankings = sorted(
            self.league_table.items(),
            key=lambda t_item: (-t_item[1], t_item[0])
        )

        return rankings
