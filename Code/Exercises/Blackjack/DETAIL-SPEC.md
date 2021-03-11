# Detailed Specification

This task is intended to help with decomposing a written requirement into a top level design and then to refine this progressively to a fully refined design. This design is then to be implemented using Python. The specification we will be working from is:

## Simplified Blackjack

You are to design and implement a simplified version of the card game of Blackjack. This game consists of one or more hands. At the end of each hand the player is asked if they wish to play another hand. If they answer with a ‘y’ another hand is played. Any other response ends the game

A had consists of three parts; the players turn, the dealers turn and determining a winner.
The players turn first deals two cards from a deck. They are then asked if they wish to deal another card or to hold. They are to respond with a ‘y’ – deal another card, or anything else to hold – end their turn. If they respond with a ‘y’ another card is dealt and they are asked again if they want to deal or hold. This continues until they hold.

The dealers turn is simpler. They are repeatedly dealt a card until their score is over 16.

Dealing a card selects one at random from the supplied dictionary. The keys in the dictionary are the names of the card, which is displayed and the values are the score for that card. The score is added to a running total for the current player – i.e. one score is kept for the player and another for the dealer.

To determine the winner, the scores of the two players are examined. If the player has scored over 21, they are bust and have lost. If the dealer has scored over 21, they are bust and the player has won. If the player has scored more than the dealer, but 21 or less, then they have won. If the dealer has scored 21 or less but the same or more than the player, then they have won.
