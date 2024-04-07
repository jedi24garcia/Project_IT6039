class BowlingGame:
    """Declares the start of a new class named BowlingGame."""
    
    def __init__(self):
        """Defines the constructor method __init__ for the BowlingGame class."""
        self.rolls= []
        """Initializes an instance variable rolls as an empty list. This will store the number of pins balled down."""

    def roll(self,pins):
        """Defines a method roll() which take a parameter pins that represents the number of pins balled down in a roll."""
        self.rolls.append(pins)
        """Adds the number of pins balled down to the list of rolls for the current game instance."""

    def score(self):
        """Details a method named 'score' which computates the total score of the game."""
        result = 0
        roll_index = 0
        """These 2 lines initialize two variables where 'result' is to store the overall score, and roll_index to retain track of the current roll being scored."""
        for frame_index in range(10):
            """This line begins a loop that iterates over 10 frames in the game."""
            if self.is_Strike(roll_index): # checks if the current roll is a strike.
                result += self.strikeScore(roll_index)
                roll_index += 1
                """This block of code add on the score for the strike to the 'result' and increase the 'roll_index' by 1 if the roll is a strike."""
            elif self.is_Spare(roll_index): # checks if the current frame is a spare by calling is_Spare() method.
                result += self.spareScore(roll_index)
                roll_index += 2
                """This block of code add on the score for the spare to the 'result' and increase the 'roll_index' by 2 if the roll is a strike."""
            else:
                result += self.frameScore(roll_index)
                roll_index += 2
                """This block of code add on the score for the orderly frame to the 'result' and increases the 'roll_index' by 2 if neither a strike or a spare happened in the current frame."""
        return result # returns the total score computated for the game.

    def is_Strike(self, roll_index):
        return self.rolls[roll_index] == 10

    def is_Spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def strikeScore(self, roll_index):
        return 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def spareScore(self, roll_index):
        return 10 + self.rolls[roll_index + 2]

    def frameScore(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]
