import random

def draw_card():
    return random.choice(deck)

def calculate_score(hand):
    score = sum(card.value for card in hand)
    if score > 21:
        for card in hand:
            if card.rank == 'Ace' and card.value == 11:
                card.value = 1
                score -= 10
                if score <= 21:
                    break
    return score

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        if rank in ['J', 'Q', 'K']:
            self.value = 10
        elif rank == 'A':
            self.value = 11
        else:
            self.value = int(rank)

class Deck:
    def __init__(self):
        ranks = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        return ', '.join(str(card.rank) + ' of ' + str(card.suit) for card in self.cards)

deck = Deck()
player_hand = Hand()
dealer_hand = Hand()

for i in range(2):
    player_hand.add_card(draw_card())
    dealer_hand.add_card(draw_card())

while True:
    print('Player has:', player_hand)
    print('Dealer has:', dealer_hand)
    choice = input('Do you want to hit or stand? ')
    if choice.lower() == 'hit':
        player_hand.add_card(draw_card())
        if calculate_score(player_hand.cards) > 21:
            print('Player busts!')
            break
    else:
        while calculate_score(dealer_hand.cards) < 17:
            dealer_hand.add_card(draw_card())
        print('Player has:', player_hand)
        print('Dealer has:', dealer_hand)
        player_score = calculate_score(player_hand.cards)
        dealer_score = calculate_score(dealer_hand.cards)
        if dealer_score > 21 or player_score > dealer_score:
            print('Player wins!')
            break
        elif player_score < dealer_score:
            print('Dealer wins!')
            break
        else:
            print('Tie!')
