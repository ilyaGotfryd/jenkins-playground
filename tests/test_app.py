from unittest import TestCase
from app.app import return_stars

class TestApp(TestCase):

    def test_app(self):
        actual=return_stars(5)
        assert '*****' == actual
