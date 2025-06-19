
#You are tasked with designing a simulation of a standard 52-card French playing deck for use in games like Poker, Blackjack, and Solitaire.

#Your solution must support the following operations:

#Deck Creation:

#How would you generate a full deck of 52 unique cards, where each card is a combination of:

#A rank: 2 through 10, J, Q, K, A

#A suit: ♠ (Spades), ♦ (Diamonds), ♣ (Clubs), ♥ (Hearts)?

#Card Representation:

#What data structure would you use to represent each card in an efficient and readable way?

#Shuffling:

#How would you randomly shuffle the deck?

#Drawing Cards:

#How would you implement a function to draw (remove and return) the top card from the deck?

#How do you handle cases when the deck becomes empty?

#Behavior Requirements:

#How will you ensure:

#Each card in the deck is unique (no duplicates)?

#The deck supports list-like operations (e.g. indexing, slicing)?

#The operations are efficient (preferably O(1) or O(n))?

# Constraints:
#You must use standard Python libraries (e.g., random, collections) only.

#You should aim for clean, modular, and readable code.

#Your implementation must prevent the program from crashing if someone tries to draw a card from an empty deck.




import random
from collections import namedtuple

# Define a simple immutable card using namedtuple
Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    "A standard deck of 52 French playing cards with indexing and length support."

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades♠ diamonds♦ clubs♣ hearts♥'.split()

    def __init__(self):
        # Create the full deck using a list comprehension
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def __len__(self):
        # Return the number of cards in the deck (always 52)
        return len(self._cards)

    def __getitem__(self, position):
        # Allow indexing and slicing like a list
        return self._cards[position]

    def shuffle(self):
        """Shuffles the deck in place."""
        random.shuffle(self._cards)

    def draw(self):
        """Draws and returns the top card from the deck."""
        if not self._cards:
            raise ValueError("No cards left in the decsk.")
        return self._cards.pop()

# Usage Example
if __name__ == '__main__':
    deck = FrenchDeck()
    deck.shuffle()
    card = deck.draw()
    print(f"You drew: {card}")
