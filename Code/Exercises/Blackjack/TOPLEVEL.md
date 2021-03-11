# Problem decomposition.

The problem is first decomposed to a top level solution and then further refined to provide lower levels until we arrive at an algorithm we can convert to code.

## Top level decomposition

This is the high level decomposition of the overall problem and the initial sub problems.

I think there are 4 basic things we need to do. Deal the cards, player plays, dealer plays, work out who is the winner. The main actions can be defined as functions. The top level decomposition then is as follows. 

> Play a game of blackjack against the computer
>> Define a deal  
>> Define how to identify a winner  
>> Define the actions for the players hand  
>> Define the actions for the dealers hand  

There will be other steps to look at which will form the main loop of the program.

## Next levels of decomposition

Each of the problems will be dealt with individually.

### Define a deal.

We will use a dictionary for the card names and each entry will be in the form. 

Cardname : Score

Use a variable to keep score of the deal.

Heres the logic.

>> Define a deal. 
>>> Set card to a random card from the card names dictionary. 
>>> Set the return value score to the value assiciated with the card selected. 
>>> Remove the item from the card names dictionary. 
>>> Return the score. 
>>> Set the return value score to the value assiciated with the card selected
