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

Usage: python main.py --file=<file_path><file_name> (for use with a file input)

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

from application.helpers.print_functions import print_cmd_art
from application.helpers.print_functions import print_program_end
from application.league_ranking import LeagueRanking


def get_score_input():
    """
    Parse CLI arguments for script.

    :return: CLI Arguments
    """
    if '--file' in sys.argv[1:]:
        parser = ArgumentParser(description='Read File')
        required = parser.add_argument_group('Required Arguments')

        # Required Arguments
        required.add_argument(
            '--file',
            dest='filename',
            help='Filename (and path) file to read',
            required=True,
        )

        args = parser.parse_args()
        file_name = args.filename
        logging.info(f'Executing file input from file: {file_name}')
        print(f'Executing file input from file: {file_name}')
        with open(file_name) as f:
            score_input = f.read()
        logging.info(f'Executing file input from file: {file_name}')
        print(f'Executing file input from file: {file_name}')

        return score_input
    elif not sys.argv[1:]:
        logging.info('Executing input from file command line Input')
        print('Executing input from file command line Input\n')

        lines = []
        print('Please input your match results here below\n'
              "(When Complete Press Enter or type 'done' ...):")
        while True:
            user_input = input()

            # 👇️ if user pressed Enter without a value, break out of loop
            if user_input == '' or user_input == 'done':
                break
            else:
                lines.append(user_input + '\n')

        # Sanitise Input to replicate File input
        score_input = ' '.join(lines).replace('\n ', '\n')
        return score_input
    else:
        logging.info('Erroneous input from console.')
        print('Erroneous input from console, please restart ...')
        return


def main():
    """Run Application."""
    print_cmd_art()
    logging.info('Starting League Ranking Process ....')
    print('Starting League Ranking Process ....')

    load_dotenv()  # Load Environment Variables
    file_input = bool(strtobool(os.getenv('FILE_INPUT', 'False')))
    logging.info(f'Using File Input: {file_input}')
    print(f'Using File Input: {file_input}')

    lr = LeagueRanking()  # Instantiate League Ranking Object
    score_input = get_score_input()  # Retrieve Score Input

    try:
        logging.info('.... Program Executing ....')
        print('Program Executing ....')
        if score_input is None or score_input == '':
            logging.info('No Input to Process ....')
            print('No Input to Process .... program exiting.')
            return
        result = lr.calculate_rankings(score_input)
        print('.... League Ranking Complete\n')
        print('Span League Rank Table')
        print('-----------------------')
        print('o-o-o-o-o-o-o-o-o-o-o-o\n')

        team_rank_count = 0
        if result:
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
