import random
suit_list = ["Hearts", "Diamonds", "Clubs", "Spades"]
value_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

class Card:

    def __init__(self, suit, value):
       self.suit = suit
       self.value = value

        
    def __repr__(self):
        return repr(self.value + " of " + self.suit)




class Deck:

    def __init__(self):
        self.card_deck = []
        for x in suit_list:
            for y in value_list:
                new_card = Card(x, y)
                self.card_deck.append(new_card)
   
    def count(self):
        return len(self.card_deck)

    def __iter__(self):
        return iter(self.card_deck)

    def __repr__(self):
        return repr('Deck of ' + self.count() + ' cards')

    def _deal(self, number):
        deck_length = self.count()
        removed_cards = []
        if deck_length == 0:
            raise ValueError("All cards have been dealt")
        elif number < deck_length:
            while number > 0:
                removed = self.card_deck.pop()
                removed_cards.append(removed)
                number -= 1
            return removed_cards
        else:
            if number > deck_length:
                for _ in range(deck_length):
                    self.card_deck.pop()
                    removed = self.card_deck.pop()
                    removed_cards.append(removed)
                return removed_cards

    def shuffle(self):
        deck_length = self.count()
        if deck_length != 52:
            return ValueError("Only full decks can be shuffled")
        else:
            random.shuffle(deck1)

    def deal_card(self):
        dealt_card = self._deal(1)
        return dealt_card

    def deal_hand(self, number_cards):
        dealt_hand = self._deal(number_cards)
        return dealt_hand
cards = Deck()
for card in cards:
    print(card)