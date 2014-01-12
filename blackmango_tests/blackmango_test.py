"""
This is where we will add all unit tests.

The `mock` module will allow us to replace Pyglet with a fake replacement that
we can inspect to ensure that it is being called correctly, without having to
actually fire up the GUI to run tests.

The hope is to eventually start using something like TravisCI to automate tests
on every commit.
"""

import unittest

# Monkey patch any Pyglet imports to turn them into mocks
import mock_pyglet

class TestSuite(unittest.TestCase):
    pass
