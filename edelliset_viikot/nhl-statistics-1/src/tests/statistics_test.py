import unittest
from statistics import Statistics
from statistics import sort_by_points
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_konstruktori(self):
        self.assertAlmostEqual(len(self.statistics._players), 5)

    def test_sort(self):
        self.assertAlmostEqual(sort_by_points(self.statistics._players[0]), 16)

    def test_search(self):
        player = Player("Semenko", "EDM", 4, 12)
        self.assertAlmostEqual(self.statistics.search("Semenko").name, player.name)
        self.assertAlmostEqual(self.statistics.search("123"), None) 

    def test_team(self):
        self.assertAlmostEqual(len(self.statistics.team("EDM")), 3)

    def test_top_scores(self):
        self.assertAlmostEqual(self.statistics.top_scorers(1)[0].name, "Gretzky")

