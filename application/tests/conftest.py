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


@pytest.fixture
def sample_league_input():
    """League Match Sample input fixture."""
    return 'Lions 3, Snakes 3\n' \
           'Tarantulas 1, FC Awesome 0\n' \
           'Lions 1, FC Awesome 1\n' \
           'Tarantulas 3, Snakes 1\n' \
           'Lions 4, Grouches 0\n'


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
