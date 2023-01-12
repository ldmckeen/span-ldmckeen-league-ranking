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
import pytest


def test_calculate_rankings(sample_league_ranking_object,
                            sample_league_input, sample_league_rankings):
    """Test Calculate Ranking Function returns Expected output."""
    assert sample_league_ranking_object.calculate_rankings(sample_league_input) == \
           sample_league_rankings


def test_calculate_rankings_error(sample_league_ranking_object,
                                  sample_league_input_erroneous,
                                  sample_league_rankings_error):
    """Test Calculate Ranking Function returns Expected output."""
    with pytest.raises(Exception) as e:
        sample_league_ranking_object.calculate_rankings(sample_league_input_erroneous)
    assert sample_league_rankings_error in str(e.value)
    assert e.type == ValueError
