import unittest
from BowlingGame import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame() 

    def testGutterGame(self): 
        self.roll_many(0, 20)
        self.assertEqual(self.game.score(), 0)

    def testAllOnes(self):
        self.roll_many(1, 20)
        self.assertEqual(self.game.score(), 20)

    def testOneSpare(self):
        self.game.roll(5)
        self.game.roll(5)      
        self.game.roll(3)
        self.roll_many(0, 17)
        self.assertEqual(self.game.score(), 16)

    def testOneStrike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.roll_many(0, 16)
        self.assertEqual(self.game.score(), 24)

    def testPerfectGame(self):
        self.roll_many(10, 12)
        self.assertEqual(self.game.score(), 300)
    
    def testOneSpare(self):
        self.roll_many(5, 21)
        self.assertEqual(self.game.score(), 150)

    def roll_many(self, pins,rolls):
        for i in range(rolls):
            self.game.roll(pins)

if __name__ == "__main___":
    unittest.main()
