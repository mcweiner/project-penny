# Project Penney

---

## Penney's Game

Penney's game, AKA Penney Ante, is an example of a three-bit sequence game invented by Walter Penney. It is played by two players using standard pennies (One side is heads and the other is tails).  The 1st player selects a sequence of heads and tails (of length 3 or larger), and shows this sequence to the 2nd player. The 2nd player then determines their own sequence of the same length as the 1st player's. The coin is then tossed until the 1st or 2nd player's sequence appears as a consecutive subsequence of the coin toss outcomes. The player whose sequence appears first wins. 

It should be noted, provided sequences of 3 or more are used, the 2nd player has an innate edge over the 1st. This is because the game is nontransitive, in that for any given sequence of length three or longer one can find another sequence that has higher probability of occurring first. 

The below table demonstrates the advantage of the second player, in how they are able to pick a specific sequence in response to the 1st player's to gain an innate advantage in the game.

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

A general rule of thumb for the second player is to start with the opposite of the middle choice of the first player, then follow it with the first player's first two choices. 
    - So for the first player's choice of 1-2-3
    - the second player must choose (!2)-1-2 
(where !2 is the opposite of the 1st player's 2nd sequence choice)

---

## The Humble-Nishiyama Variant

One suggested variation on Penney's Game uses a pack of ordinary playing cards. The Humble-Nishiyama Randomness Game follows the same format using Red and Black cards, instead of Heads and Tails. The game is played as follows:
    1.  At the start of a game each player decides on their three colour sequence for the whole game. 
    2. The cards are then turned over one at a time and placed in a line, until one of the chosen triples appears. 
    3. The winning player takes the upturned cards, having won that "trick". 
    4. The game repeats steps 1 through 3 with the unused cards, both players collecting tricks as their triples come up, until all the cards in the pack have been used. 

The winner of the game is the player that has won the most tricks, and games commonly end with a total of 7 tricks.

The general rule of thumb for the second player to gain an edge in this game is the same from Penney's Game, however the probabilty of victory are different. 

Below are approximate probabilities of the outcomes for each strategy based on computer simulations.<sup>[14]</sup>

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

The goal of this code is to demonstrate the advantage of going second in the Humble-Nishiyama Randomness Game, and better identify what the optimal choice is for going second based on the choice of sequence the first player makes. This will be accomplished by first randomly generating a settable amount of 52 length lists containing 26 0s (representing black cards) and 26 1s (representing red cards) so we have something to simulate a deck of 52 playing cards. Next, we will score the different matchups between two players in the Humble-Nishiyama Randomness Game; both playing by tricks and playing by cards. After scoring the number of wins for each player (as well as their tied games) for both ways to play the game in the 'pairs_table.csv' file located in the data folder, the code should then run to create a heatmap for both playing by tricks and playing by cards.

This Heatmap will have the x-axis labeled as 'My Choice' and the y-axis labeled as 'Opponent Choice,' with the "Opponent" being the person who chooses their sequence first and the person labeled in 'My Choice' being the person who chooses their sequence second. Each cell will contain the number of wins followed by the number of ties in paranthesis [IE: Wins(ties)], with the cell that has the best 'score' being surrounded by a black border for each row. The code should allow for a user to add more to the number of tested decks, which will automatically update the .csv table and the heatmaps.

Idealy, given enough cases (decks) to test with, the results of this code will highlight the advantage of going second in the Humble-Nishiyama Randomness Game while also showing which choice is best for the second player in each scenario.

---

## Quick-Start Guide

Everyone loves one of these! Give users a quick, short and to the point way to make your code work, for example:

This project is managed using [UV](https://docs.astral.sh/uv/guides/install-python/). If you do not yet have UV installed or need help troubleshooting issues with UV, refer to [their documentation](https://docs.astral.sh/uv/guides/install-python/).

Once you have UV installed, simply download the repository, navigate to the directory and run: `uv sync` to install dependencies.

To run the program:

`uv run run_all_files.py` 
This will generate five million decks, score them, and then create a heat map of the results. The scoring process takes a few hours. If you would like to change the number of decks generated, then you can go into `yield_generator.py` and change num_to_generate from 5_000_000 to whatever number of decks you would like. 

To augment data:
1. Our augment_data function is in `win_draw_heatmap_generator.py`. To run this function you can comment out the heatmap generator functions and uncomment the augment_data function under if __name__ == “__main__”. With this function you can specify the amount of new decks you want generate and it will update the heatmaps as well. 

3. `uv run win_draw_heatmap_generator.py`

`uv run main.py`

---

## Contents

You should provide a high-level description of the contents of your repository. You do not need to go into excruciating detail here. You can also place individual README.md files in each folder that go into more depth of the contents of that folder.

`main.py`: This is the main entry point to the program. It should be named `main.py`, unless you have a good reason to deviate from that. This way the user does not need to guess about what they should be running.

`src/`: The source code. This should contain all of the code that is needed to make your project work. We place it in a separate folder so that:

- it is clear to the user that this is the source code, and they do not need to look at it unless they want to
- the root directory of the repository does not get cluttered

`data/`: As the name implies, put data in this folder. If you have a project containing raw and processed versions of the data, then you should create subdirectories such as `data/raw` and `data/processed`, for example. Use your best judgment and stay organized!

`figures/`: Similar to above, we should place figures here. If you are keeping older versions of figures, then place the older ones in a subdirectory, and keep only the current versions in the top-level `figures/` directory.