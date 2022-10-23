from unittest import TestCase
from main.utils import Utils

class TestUtils(TestCase):
    def setUp(self):
        self.utils = Utils()

    def test_get_player_choice(self):
        pass

    def test_score_keep(self):
        pass

    def test_winner(self):
        pass

    def test_pretty_score_print(self):
        pass

    def test_valid_user_choice(self):
        self.assertEqual(self.utils.valid_user_choice("s"), True)
