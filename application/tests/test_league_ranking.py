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
from application.league_ranking import calculate_rankings


def test_calculate_rankings(sample_league_input, sample_league_rankings):
    """Test Calculate Ranking Function returns Expected output."""
    assert calculate_rankings(sample_league_input) == sample_league_rankings
