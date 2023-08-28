import random

class deck:
    def _init_(self):
        self.deck = []
        self.ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9',
'10', 'Jack', 'Queen', 'King']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades',]
        self.reset()
        
    def rest(self):
        self.deck = [f'{rank} of {suit}' for suit in self.suits for rank in self.ranks]
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        if len(self.deck) == 0:
            return None
        return self.deck.pop()
    
    def count(self):
        return len(self.deck)
    
# Create a deck
deck = Deck()

# Shuffle the deck
deck.shuffle()

# Deal a card
card = deck.deal()
if card is not None:
    print(f"Dealt card: {card}")
else:
    print("No more cards in the deck.")
    
# Count the remaining cards
count = deck.count()
print(f"Remaining cards in the deck:{count}")
    
