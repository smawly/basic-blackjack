import random


def deal_card():
    """Returns a random card from the deck."""
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)


def calculate_score(cards):
    """Calculates the total value of a hand of cards."""
    score = 0
    num_aces = cards.count('A')

    for card in cards:
        if card == 'A':
            score += 11
        elif card in ['K', 'Q', 'J']:
            score += 10
        else:
            score += int(card)

    while score > 21 and num_aces:
        score -= 10
        num_aces -= 1

    return score


def blackjack():
    player_cards = []
    computer_cards = []

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 21 or computer_score == 21:
            game_over = True
        else:
            should_continue = input("Type 'hit' to get another card, or 'stand' to pass: ").lower()
            if should_continue == 'hit':
                player_cards.append(deal_card())
                if calculate_score(player_cards) > 21:
                    game_over = True
            else:
                game_over = True

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if player_score > 21:
        print("You went over 21. You lose.")
    elif computer_score > 21:
        print("Computer went over 21. You win!")
    elif player_score == computer_score:
        print("It's a draw!")
    elif player_score == 21:
        print("Blackjack! You win!")
    elif player_score > computer_score:
        print("You win!")
    else:
        print("You lose.")


blackjack()
