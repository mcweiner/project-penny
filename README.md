# Project Penney

---

## Penney's Game

Penney's Game, also known as Penney Ante, is a two-player sequence-matching game invented by Walter Penney. It's played using a standard coin (heads and tails).

How to Play:

    1. Player 1 selects a sequence of heads and tails (length 3 or more) and shows it to Player 2.

    2. Player 2 then selects their own sequence of the same length.

    3. A coin is tossed repeatedly until either Player 1's or Player 2's sequence appears as a consecutive part of the coin toss 4. results.

    The player whose sequence appears first wins.

For any sequence of length 3 or more, Penney's Game is nontransitive. This means that for any sequence Player 1 chooses, Player 2 can always pick a different sequence that has a higher probability of appearing first.

Because Player 2 makes their selection after Player 1, they have a significant mathematical edge. The table below demonstrates this advantage, showing the optimal sequence Player 2 can choose in response to Player 1's initial pick to maximize their odds of winning.

| 1st player's choice | 2nd player's choice | Odds in favour of 2nd player |
|---|---|---|
| <u>B**B**</u>B | **R**<u>BB</u> | 7.50 to 1 |
| <u>B**B**</u>R | **R**<u>BB</u> | 3.08 to 1 |
| <u>B**R**</u>B | **B**<u>BR</u> | 1.99 to 1 |
| <u>B**R**</u>R | **B**<u>BR</u> | 2.04 to 1 |
| <u>R**B**</u>B | **R**<u>RB</u> | 2.04 to 1 |
| <u>R**B**</u>R | **R**<u>RB</u> | 1.99 to 1 |
| <u>R**R**</u>B | **B**<u>RR</u> | 3.08 to 1 |
| <u>R**R**</u>R | **B**<u>RR</u> | 7.50 to 1 |

For a game using sequences of length 3, there is a simple "rule of thumb" Player 2 can use to guarantee an advantage.

Player 2 should build their sequence as follows:

    Take the opposite of Player 1's second (middle) choice.

    Use that as their first choice.

    Append Player 1's first two choices to it.

Let's use H for Heads and T for Tails.

    Player 1 chooses: H-T-H

    Player 2 builds their sequence:

        The middle choice of Player 1 is T. The opposite is H.

        Player 1's first two choices are H-T.

        Player 2 combines them: H + H-T

    Player 2 chooses: H-H-T

In this matchup, H-H-T will appear before H-T-H 2 out of 3 times, giving Player 2 a 2:1 advantage.

    If Player 1's sequence is: 1 - 2 - 3

    Player 2's optimal sequence is: `(Not 2) - 1 - 2

---

## The Humble-Nishiyama Variant

A common variation of Penney's Game is the Humble-Nishiyama Randomness Game, which uses a standard deck of playing cards. Instead of Heads and Tails, this version uses Red and Black cards.

How to Play:

    1. Choose Sequences: At the very start of the game, both players decide on their three-color sequence (e.g., Red-Black-Red). These sequences are fixed for the entire game.

    2. Deal Cards: Cards are turned over one at a time from a shuffled deck and placed in a line.

    3. Win a "Trick": The game continues until one of the chosen three-card sequences appears. The player whose sequence appears first wins all the upturned cards, which constitute one "trick."

    4. Continue Play: The game resumes with the remaining cards in the deck, repeating steps 2 and 3. Players collect tricks as their sequences come up.

    5. End of Game: The game is over when all cards in the pack have been used.

The winner is the player who has won the most tricks by the end of the game. A typical game from a 52-card deck results in about 7 tricks being won.

The optimal strategy for Player 2 is the same "rule of thumb" from the coin version:
    If Player 1 chooses 1 - 2 - 3, Player 2 should choose (Not 2) - 1 - 2.

However, unlike a coin toss (which is independent), a deck of cards has a "dependency" (drawing a Red card makes the next card slightly less likely to be Red). This changes the odds.

The table below provides approximate probabilities for each strategy

| 1st player's choice | 2nd player's choice | Probability 1st player wins | Probability 2nd player wins | Probability of a draw |
|---|---|---|---|---|
| <u>B**B**</u>B | **R**<u>BB</u> | 0.11% | 99.49% | 0.40% |
| <u>B**B**</u>R | **R**<u>BB</u> | 2.62% | 93.54% | 3.84% |
| <u>B**R**</u>B | **B**<u>BR</u> | 11.61% | 80.11% | 8.28% |
| <u>B**R**</u>R | **B**<u>BR</u> | 5.18% | 88.29% | 6.53% |
| <u>R**B**</u>B | **R**<u>RB</u> | 5.18% | 88.29% | 6.53% |
| <u>R**B**</u>R | **R**<u>RB</u> | 11.61% | 80.11% | 8.28% |
| <u>R**R**</u>B | **B**<u>RR</u> | 2.62% | 93.54% | 3.84% |
| <u>R**R**</u>R | **B**<u>RR</u> | 0.11% | 99.49% | 0.40% |

If the game is ended after the first trick, there is a negligible chance of a draw. The odds of the second player winning in such a game appear in the table below.

| 1st player's choice | 2nd player's choice | Odds in favour of 2nd player |
|---|---|---|
| <u>B**B**</u>B | **R**<u>BB</u> | 7.50 to 1 |
| <u>B**B**</u>R | **R**<u>BB</u> | 3.08 to 1 |
| <u>B**R**</u>B | **B**<u>BR</u> | 1.99 to 1 |
| <u>B**R**</u>R | **B**<u>BR</u> | 2.04 to 1 |
| <u>R**B**</u>B | **R**<u>RB</u> | 2.04 to 1 |
| <u>R**B**</u>R | **R**<u>RB</u> | 1.99 to 1 |
| <u>R**R**</u>B | **B**<u>RR</u> | 3.08 to 1 |
| <u>R**R**</u>R | **B**<u>RR</u> | 7.50 to 1 |

Another variant exists, in which instead of evaluating the victory criteria for the Humble-Nishiyama Randomness Game by tricks, it is instead evaluated by the final number of cards both players possess. This variant of the game decreases the number of ties substantially, and further skews the probability of victory in the favor of the second player.

For more information on Penney's game and Humble-Nishiyama, make use of the below resources:
https://mathwo.github.io/assets/files/penney_game/humble-nishiyama_randomness_game-a_new_variation_on_penneys_coin_game.pdf

https://en.wikipedia.org/wiki/Penney%27s_game

--- 

## Overview

The goal of this code is to demonstrate the advantage of going second in the Humble-Nishiyama Randomness Game and to precisely identify the optimal sequence for Player 2 based on Player 1's choice. This is accomplished by first generating a user-defined number of simulated 52-card decks, each represented as a 52-item list containing 26 0s (black cards) and 26 1s (red cards). Next, the code scores every possible matchup, calculating wins and ties for two different scoring methods: playing by "tricks" and playing by "cards." All results are saved in the data/pairs_table.csv file, which is then used to generate two heatmaps.

These heatmaps are labeled "Opponent Choice" (Player 1) on the y-axis and "My Choice" (Player 2) on the x-axis. Each cell displays Player 2's Wins(Ties), and the cell with the best score in each row is highlighted with a black border. The code is designed to be augmentable, allowing a user to easily increase the number of simulated decks by running the 'augment_data(int: N)' method. Using this method will add an N number of decks automatically and score them, and then update the .csv with the additional scored deck before finally recreating the heatmaps with this updated data.

Ideally, given a sufficient number of simulated decks, the resulting data will clearly highlight the innate advantage of going second in the Humble-Nishiyama Randomness Game while also providing a definitive guide for Player 2's best response to the sequence chosen by player 1.

---

## Quick-Start Guide

Everyone loves one of these! Give users a quick, short and to the point way to make your code work, for example:

This project is managed using [UV](https://docs.astral.sh/uv/guides/install-python/). If you do not yet have UV installed or need help troubleshooting issues with UV, refer to [their documentation](https://docs.astral.sh/uv/guides/install-python/).

Once you have UV installed, simply download the repository, navigate to the directory and run: `uv sync` to install dependencies.

To run the program:

`uv run run_all_files.py` 
You will first be asked if you want to recreate our results. This will generate a specified number of decks, score them, and then create a heat map of the results. The scoring process may take a few hours. You will be asked how many decks you want to create and score. To augment data, tell the input "n" and then you will be asked if you would like to augment the data. You can then specify the number of decks you want to add. 
