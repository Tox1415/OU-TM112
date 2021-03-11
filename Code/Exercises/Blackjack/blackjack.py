from random import *
import cards

def play_players_hand():
    score = 0
    score += deal()
    score += deal()

    print(score)
    response = 'y'
    while score < 22 and response != 'n':
        response = input('deal(y) or hold(n)')
        if response == 'y':
            score += deal()
            print(score)
    return score

def play_dealers_hand():
    dealerscore = 0;
    dealerscore += deal()
    dealerscore += deal()

    print(dealerscore)

    while dealerscore < 16:
        dealerscore += deal();

    print(dealerscore)
    return dealerscore

def work_out_winner(score, dealerscore):
    if score > 21:
        print('Bust!')
    elif dealerscore > 21:
        print('Dealer bust!')
    elif score > dealerscore:
        print('player wins')
    else:
        print('dealer wins')
    

def deal():
    card = choice(cardnames)
    score = cards.cards[card];
    print(card)
    cardnames.remove(card)
    return score

def play_a_hand():
    score = play_players_hand()
    print(score)

    dealerscore = play_dealers_hand()

    work_out_winner(score, dealerscore)

playAgain = 'y'

while playAgain == 'y':
    cardnames = list(cards.cards)
    play_a_hand()
    playAgain = input('Play again? (y/n)')
