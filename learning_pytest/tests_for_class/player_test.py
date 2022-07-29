import pytest
from player_class import Player

class TestPlayer:
    def test_change_name(self):
        test_player = Player('test_name')
        test_player.change_name('new_test_name')
        assert test_player.name == 'new_test_name'

    def test_add_points(self):
        test_player = Player('test_name')
        assert test_player.add_points(30) == 30

    def test_get_points(self):
        test_player = Player('test_name')
        test_player.add_points(30)
        assert test_player.get_points() == 30
