import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # We want all players to get their next move
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-9:)")
            #we're going to check that this is correct value by trying to cast it to 
            # integer, and if its not then we say its invalid
            # if that spot is 
