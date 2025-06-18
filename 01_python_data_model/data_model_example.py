import random
from collections import namedtuple

# Define a simple immutable card using namedtuple
Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    "A standard deck of 52 French playing cards with indexing and length support."

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

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
            raise ValueError("No cards left in the deck.")
        return self._cards.pop()

# Usage Example
if __name__ == '__main__':
    deck = FrenchDeck()
    deck.shuffle()
    card = deck.draw()
    print(f"You drew: {card}")
