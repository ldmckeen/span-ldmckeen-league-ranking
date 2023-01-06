"""
Span League Ranking Application.

===========================================================================================
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
<test_league_ranking.py> Unit Test File for League Ranking Application Python Functions

Author:             Lloyd McKeen
Github Username:    ldmckeen
Email:              ldmckeen@gmail.com
Company:            Span
Date:               January 2023
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
===========================================================================================
"""
from league_ranking import calculate_ranking


def test_calculate_ranking():
    """Test Calulate Ranking Function returns Expected output."""
    test_input = 'Lions 3, Snakes 3 Tarantulas 1, FC Awesome 0 Lions 1, FC Awesome 1 ' \
                 'Tarantulas 3, Snakes 1 Lions 4, Grouches 0'
    assert calculate_ranking(test_input) == test_input
