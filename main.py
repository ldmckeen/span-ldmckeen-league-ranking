"""
Span League Ranking Application.

~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
<main.py> Application File

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

Usage: python main.py --file=<file_name> (for use with a file input)

       python main.py <cmd input as stringed parameter one match result per line>
       (for use with a command line input as comma and newline seperated text)
===========================================================================================
"""
import logging
import os
import sys
from argparse import ArgumentParser

from distutils.util import strtobool
from dotenv import load_dotenv

from helpers.print_functions import print_cmd_art
from helpers.print_functions import print_program_end
from league_ranking import calculate_rankings


def get_options():
    """
    Parse CLI arguments for script.

    :return: CLI Arguments
    """
    parser = ArgumentParser(description='Read File')
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
        result = calculate_rankings(score_input)
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

    print_program_end()


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