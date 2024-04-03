import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame.BowlingGame()
    
    def testGutterGame(self):
        for i in range(0, 20):
            self.game.rolls(0)
        assert self.game.score()==0
