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
import re


def calculate_rankings(scores):
    """League Ranking table solution via newline comma seperated scores input."""
    league_table = {}  # Dictionary to store Teams and their respective League Points
    scores = scores.rstrip('\n')  # Removing trailing newline
    match_results = scores.split('\n')  # Store each line in input as new match result

    # Loop through match results to store scores against team names
    matches_count = 0
    for item in match_results:
        matches_count += 1
        # Split match result into individual teams and team scores
        team1, team2 = item.split(', ')
        team_1_name, team_1_score = re.split(r'\s(?=\d+(?!\S))', team1)
        team_2_name, team_2_score = re.split(r'\s(?=\d+(?!\S))', team2)

        # Check if team exists in existing teams dictionary, if not add it.
        if team_1_name not in league_table:
            league_table[team_1_name] = 0
        if team_2_name not in league_table:
            league_table[team_2_name] = 0

        # Check who won, lost or if a draw
        if int(team_1_score) == int(team_2_score):
            league_table[team_1_name] += 1
            league_table[team_2_name] += 1
        elif int(team_1_score) > int(team_2_score):
            league_table[team_1_name] += 3
        elif int(team_2_score) > int(team_1_score):
            league_table[team_2_name] += 3

    # Sort League Table (points descending and Team name alphabetically if draw
    print(f'Total Matches Played: {matches_count}')
    rankings = sorted(league_table.items(), key=lambda t_item: (-t_item[1], t_item[0]))

    return rankings
