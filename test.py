import unittest
from BowlingGame import BowlingGame

class TestBowlingGame(unittest.TestCase):
    """This class represents a game of Bowling."""

    def setUp(self):
        """This sets up a new instance of BowlingGame for each test cases."""
        self.game = BowlingGame() 

    def test_Gutter_Game(self):
        """The test scoring of the gutter_game - all rolls are zero.""" 
        self.roll_many(0, 20) # roll 0 pins for 20 rolls
        self.assertEqual(self.game.score(), 0) # declare or asserts that the score is 0 

    def test_All_Ones(self):
        """Test scoring a game where all rolls knock down one pin."""
        self.roll_many(1, 20) # roll 1 pins for 20 rolls
        self.assertEqual(self.game.score(), 20) # declare or asserts that the score is 20

    def test_One_Spare(self):
        """Test scoring a game with one spare."""
        self.game.roll(5) # roll 5 pins
        self.game.roll(5) # roll 5 pins
        self.game.roll(3) # roll 3 pins
        self.roll_many(0, 17) # roll 0 pins for 17 rolls
        self.assertEqual(self.game.score(), 16) # declare or asserts that the score is 16

    def test_One_Strike(self):
        """Test scoring a game with one strike."""
        self.game.roll(10) # roll 10 pins (all pins)
        self.game.roll(4) # roll 4 pins
        self.game.roll(3) # roll 3 pins
        self.roll_many(0, 16) # roll 0 pins for 16 rolls
        self.assertEqual(self.game.score(), 24) # declare or asserts that the score is 24

    def test_Perfect_Game(self):
        """Test scoring a perfect game with all strikes"""
        self.roll_many(10, 12) # roll a strike for all 12 rolls 
        self.assertEqual(self.game.score(), 300) # declare or asserts that the score is 300
    
    def test_every_five(self):
        """Test scoring a game where every roll falls down five pins."""
        self.roll_many(5, 21) # roll 5 pins for 21 rolls
        self.assertEqual(self.game.score(), 150) # declare or asserts that the score is 150

    def roll_many(self, pins,rolls):
        """Roll a specified number of pins for a specified number of rolls.
        
        Arguments:
            rolls: The number of pins to fall down in each roll.
            pins: The number of rolls to perform.
        """
        for i in range(rolls):
            self.game.roll(pins)

if __name__ == "__main__":
    unittest.main()
