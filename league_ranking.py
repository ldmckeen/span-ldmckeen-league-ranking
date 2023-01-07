"""
Span League Ranking Application.

~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
<league_ranking.py> Application File

Author:             Lloyd McKeen
Github Username:    ldmckeen
Email:              ldmckeen@gmail.com
Company:            Span
Date:               January 2023
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~


Problem Statement & Instructions:
--------------------------------
We want you to create a production ready, maintainable, testable command-line application
that will calculate the ranking table for a league.

Input/output:
-------------
The input and output will be text. Either using stdin/stdout or taking filenames on the
command line is fine.
The input contains results of games, one per line. See “Sample input” for details.
The output should be ordered from most to least points, following the format specified in
“Expected output”.

The rules:
----------
In this league, a draw (tie) is worth 1 point and a win is worth 3 points. A loss is worth
0 points. If two or more teams have the same number of points, they should have the same
rank and be printed in alphabetical order (as in the tie for 3rd place in the sample data).

Test cases
==========
Sample input:
~~~~~~~~~~~~~
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0

Expected output:
~~~~~~~~~~~~~~~~
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts

Usage: python league_ranking.py --file=<file_name> (for use with a file input)

       python league_ranking.py <cmd input as stringed parameter one match result per line>
       (for use with a command line input as comma and newline seperated text)
===========================================================================================
"""
import logging
import os
import re
import sys
from argparse import ArgumentParser

from distutils.util import strtobool
from dotenv import load_dotenv


def print_cmd_art():
    """Print Function for Program Terminal Graphics."""
    print()
    print('=======================================================')
    print('~~~=~=~=>>>>   SPAN League Ranking Table   <<<<=~=~=~~~')
    print('=======================================================')
    print('====      /|      o__        o__     |   |\\        ====')
    print('====     /x|     /|          /\\      |   |X\\       ====')
    print('====    /xx|     / > o        <\\     |   |XX\\      ====')
    print('====-----------------------------------------------====')
    print('=======================================================')
    print()


def calculate_ranking(scores):
    """League Ranking table solution via newline comma seperated scores input."""
    league_table = {}  # Dictionary to store Teams and their respective League Points
    scores = scores.rstrip('\n')  # Removing trailing newline
    match_results = scores.split('\n')  # Store each line in input as new match result

    # Loop through match results to store scores against team names
    for item in match_results:
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
        else:
            league_table[team_2_name] += 1

    # Sort League Table by points descending and then by Team Name alphabetically
    # if drawn on points
    rankings = sorted(league_table.items(), key=lambda t_item: (-t_item[1], t_item[0]))

    return rankings


def get_options():
    """
    Parse CLI arguments for script.

    :return: CLI Arguments
    """
    parser = ArgumentParser(description='Read .avro File')
    required = parser.add_argument_group('Required Arguments')

    # Required Arguments
    required.add_argument(
        '--file',
        dest='filename',
        help='Filename (and path) file to read',
        required=True,
    )

    return parser.parse_args()


def main():
    """Run Application."""
    print_cmd_art()
    logging.info('Starting League Ranking Process ....')
    print('Starting League Ranking Process ....')

    # Load Environment Variables
    load_dotenv()
    file_input = bool(strtobool(os.getenv('FILE_INPUT', 'False')))
    logging.info(f'Using File Input: {file_input}')
    print(f'Using File Input: {file_input}')

    # If File Input Env True, pull data from file, otherwise pull data from cmd params
    score_input = None
    if file_input:
        # Get command line args
        opts = get_options()
        file_name = opts.filename
        with open(file_name) as f:
            score_input = f.read()
        logging.info(f'Executing file input from file: {file_name}')
        print(f'Executing file input from file: {file_name}')
    else:
        logging.info('Executing input from file command line Input')
        print('Executing input from file command line Input')
        score_input = ' '.join(sys.argv[1:])

    try:
        logging.info('.... Program Executing ....')
        print('Program Executing ....')
        if score_input is None or '':
            logging.info('No Input to Process ....')
            print('No Input to Process .... program exiting.')
            return
        result = calculate_ranking(score_input)
        print('.... League Ranking Complete\n')
        print('Span League Rank Table')
        print('-----------------------')
        print('o-o-o-o-o-o-o-o-o-o-o-o\n')

        team_rank_count = 0
        for team in result:
            team_rank_count += 1
            print(f'{team_rank_count}. {team[0]} {team[1]} pts')

        print('\no-o-o-o-o-o-o-o-o-o-o-o')
        print('-----------------------')
    except Exception as e:
        logging.info(f'Failure due to error: {e}')
        raise e

    print()
    print('=======================================================')
    print('~~~=~=~=>>>>          Program END          <<<<=~=~=~~~')
    print('=======================================================')


if __name__ == '__main__':
    """
    Script Entrypoint.
    """

    try:
        main()
    except Exception as err:
        logging.info(
            f'{os.path.basename(__file__)} failed due to error: {err}'
        )
        raise err
