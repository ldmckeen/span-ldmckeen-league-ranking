"""
Span League Ranking Application.

~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
<test_league_ranking.py> Unit Test File for League Ranking Application Python Functions

Author:             Lloyd McKeen
Github Username:    ldmckeen
Email:              ldmckeen@gmail.com
Company:            Span
Date:               January 2023
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

Usage: pytest (to run all tests)
       or
       pytest tests/test_league_ranking.py (to run tests in this file)

===========================================================================================
"""
from league_ranking import calculate_rankings


def test_calculate_rankings():
    """Test Calculate Ranking Function returns Expected output."""
    test_input = 'Lions 3, Snakes 3 Tarantulas 1, FC Awesome 0 Lions 1, FC Awesome 1 ' \
                 'Tarantulas 3, Snakes 1 Lions 4, Grouches 0'
    assert calculate_rankings(test_input) == test_input
