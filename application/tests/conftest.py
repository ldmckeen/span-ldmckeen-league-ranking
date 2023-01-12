"""
Span League Ranking Application.

~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
<conftest.py> Unit Test Fixures File for League Ranking Application Python Unit Tests

Author:             Lloyd McKeen
Github Username:    ldmckeen
Email:              ldmckeen@gmail.com
Company:            Span
Date:               January 2023
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
===========================================================================================
"""
import pytest

from application.league_ranking import LeagueRanking


@pytest.fixture
def sample_league_ranking_object():
    """League Ranking object fixture."""
    return LeagueRanking()


@pytest.fixture
def sample_league_input():
    """League Matches Sample input fixture."""
    return 'Lions 3, Snakes 3\n' \
           'Tarantulas 1, FC Awesome 0\n' \
           'Lions 1, FC Awesome 1\n' \
           'Tarantulas 3, Snakes 1\n' \
           'Lions 4, Grouches 0\n'


@pytest.fixture
def sample_league_input_erroneous():
    """League Matches Sample input erroneous fixture."""
    return 'Lions 3 Snakes 3\n' \
           'Tarantulas 1 FC Awesome 0\n' \
           'Lions 1 FC Awesome 1\n' \
           'Tarantulas 3 Snakes 1\n' \
           'Lions 4 Grouches 0\n'


@pytest.fixture
def sample_league_rankings():
    """League Ranking Sample Return fixture."""
    return [
        ('Tarantulas', 6),
        ('Lions', 5),
        ('FC Awesome', 1),
        ('Snakes', 1),
        ('Grouches', 0)
    ]


@pytest.fixture
def sample_league_rankings_error():
    """League Ranking Sample Return fixture."""
    return 'not enough values to unpack (expected 2, got 1)'
