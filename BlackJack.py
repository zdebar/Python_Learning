import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # Called when print is used on an object
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"

class Deck:
    # Generování balíčku karet
    def __init__(self):
        suits = ["♥", "♦", "♣", "♠"]
        ranks = [str(rank) for rank in range(2, 11)] + list("JQKA")
        rank_values = {rank: 11 if rank == "A" else 10 if rank in list("JQK") else int(rank) for rank in ranks}
        self.cards = [[suit, {key: value}] for suit in suits for key, value in rank_values.items()]
        
    # Definice funkcí

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, number):
        return [self.cards.pop() for _ in range(number) if len(self.cards) > 0]

card1 = Card("♥", {"rank":'5',"value": 5})
print(card1)
