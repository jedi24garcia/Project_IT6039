class BowlingGame:
    """Declares the start of a new class named BowlingGame."""
    
    def __init__(self):
        """Defines the constructor method __init__ for the BowlingGame class."""
        self.rolls= []
        """Initializes an instance variable rolls as an empty list. This will store the number of pins balled down."""

    def roll(self,pins):
        self.rolls.append(pins)

    def score(self):
        result = 0
        roll_index = 0
        for frame_index in range(10):
            if self.is_Strike(roll_index):
                result += self.strikeScore(roll_index)
                roll_index += 1
            elif self.is_Spare(roll_index):
                result += self.spareScore(roll_index)
                roll_index += 2
            else:
                result += self.frameScore(roll_index)
                roll_index += 2
        return result

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
