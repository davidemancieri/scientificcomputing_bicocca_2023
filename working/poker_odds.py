import random

class Card:
    
    def __init__(self, suit=1, rank=2):
        if suit < 1 or suit > 4:
            print("invalid suit, setting to 1")
            suit = 1
            
        self.suit = suit
        self.rank = rank
        
    def value(self):
        """ we want things order primarily by rank then suit """
        return self.suit + (self.rank-1)*14
    
    # we include this to allow for comparisons with < and > between cards 
    def __lt__(self, other):
        return self.value() < other.value()

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        suits = [u"\u2660",  # spade
                 u"\u2665",  # heart
                 u"\u2666",  # diamond
                 u"\u2663"]  # club
        
        r = str(self.rank)
        if self.rank == 11:
            r = "J"
        elif self.rank == 12:
            r = "Q"
        elif self.rank == 13:
            r = "K"
        elif self.rank == 14:
            r = "A"
                
        return r +':'+suits[self.suit-1]

class Deck:
    """ the deck is a collection of cards """

    def __init__(self):

        self.nsuits = 4
        self.nranks = 13
        self.minrank = 2
        self.maxrank = self.minrank + self.nranks - 1

        self.cards = []

        for rank in range(self.minrank,self.maxrank+1):
            for suit in range(1, self.nsuits+1):
                self.cards.append(Card(rank=rank, suit=suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def get_cards(self, num=1):
        hand =[]
        for n in range(num):
            hand.append(self.cards.pop())
        for card in reversed(hand):
            self.cards.append(card)

        return hand
    
    def __str__(self):
        string = ""
        for c in self.cards:
            string += str(c) + " "
        return string
    
def one_pair(hand):
    """check for one pair in a given hand"""
    ranks = [card.rank for card in hand]
    counts = [ranks.count(rank) for rank in ranks]

    if counts.count(2) == 2:
        return True
    return False

def two_pair(hand):
    """check for two pair in a given hand"""
    ranks = [card.rank for card in hand]
    counts = [ranks.count(rank) for rank in ranks]

    if counts.count(2) == 4:
        return True
    return False

def three_of_a_kind(hand):
    """check for three-of-a-kind in a given hand"""
    ranks = [card.rank for card in hand]
    counts = [ranks.count(rank) for rank in ranks]

    if 3 in counts and 2 not in counts:
        return True
    return False

def four_of_a_kind(hand):
    """check for four-of-a-kind in a given hand"""
    ranks = [card.rank for card in hand]
    counts = [ranks.count(rank) for rank in ranks]

    if 4 in counts:
        return True
    return False

def full_house(hand):
    """check for full house in a given hand"""
    ranks = [card.rank for card in hand]
    counts = [ranks.count(rank) for rank in ranks]

    if 3 in counts and 2 in counts:
        return True
    return False

