import unittest
from cards import Card, Deck

class CardsTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", "A")

    def test_card_init(self):
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")

    def test_repr(self):
        self.assertEqual(repr(self.card), "'A of Hearts'")

class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_init(self):
        self.assertTrue(isinstance(self.deck.card_deck, list))

    def test_repr(self):
        self.assertEqual(repr(self.deck), "'Deck of 52 cards'")

    def test_count(self):
        self.assertEqual(self.deck.count(), 52)
        self.deck.card_deck.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_deal_sufficient_cards(self):
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)

    def test_deal_insufficient_cards(self):
        self.deck._deal(55)
        self.assertEqual(self.deck.count(), 0)

    def test_deal_no_cards(self):
        self.deck._deal(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck._deal(55)

    def test_deal_card(self):
        card = self.deck.card_deck[-1]
        dealt_card = self.deck.deal_card()
        self.assertEqual([card], dealt_card)
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand(self):
        cards = self.deck.deal_hand(20)
        self.assertEqual(len(cards), 20)
        self.assertEqual(self.deck.count(), 32)
    
    def shuffle_full_deck(self):
        cards = self.deck.card_deck[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.card_deck)
        self.assertEqual(len(self.deck.card_deck), 52)

    def shuffle_not_full_deck(self):
        self.deck.deal_hand(20)
        with self.assertRaises(ValueError):
            self.deck.shuffle()



        

if __name__ == "__main__":
    unittest.main()