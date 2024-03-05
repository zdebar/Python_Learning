import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # Called when print is used on an object
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"

class Deck:
    # Deck of cards generation
    def __init__(self):
        # List of all suits
        suits = ["♥", "♦", "♣", "♠"]
        # Generate list of all ranks in str format
        ranks = [str(rank) for rank in range(2, 11)] + list("JQKA")
        # Creates dictionary where key = ranks : value = value of cards in BlackJack; ex. {'J': 10}
        rank_values = {rank: 11 if rank == "A" else 10 if rank in list("JQK") else int(rank) for rank in ranks}
        # Creates deck of cards as list of all 52 cards in format [suit, {rank, value}]; ex. ['♠', {'7': 7}]
        self.cards = [[suit, {key: value}] for suit in suits for key, value in rank_values.items()]
               
    # Shuffle Cards
    def shuffle(self):
        random.shuffle(self.cards)

    # Deal(number of dealt cards) cards in a list
    def deal(self, number):
        return [self.cards.pop() for _ in range(number) if self.cards]
    
class Hand:
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True

deck = Deck()
deck.shuffle()

hand = Hand()
hand.add_card(deck.deal(3))
print(hand.cards[1])