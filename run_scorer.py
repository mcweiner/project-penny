import src.scorer as scorer
import src.yield_generator as yield_shuffles
import numpy as np
import pandas as pd
import itertools
import random
import os

random.seed(42) # For reproducibility
deck1 = np.array(random.sample([0] * 26 + [1] * 26, k=52), dtype=np.int8)

def create_choice_list():
    """
    Create a list of all possible 3-card binary choices (0s and 1s).
    """
    
    options = [tuple(p) for p in itertools.product([0, 1], repeat=3)]
    pairs = [(a, b) for a, b in itertools.product(options, repeat=2) if a != b]
    return pairs

def create_score_table():
    """
    Create a blank table to track scores for each combination of card choices.
    """
    df = pd.DataFrame(np.zeros((len(create_choice_list()), 3)), dtype=int)
    df.columns = ['p1_wins_cards', 'p2_wins_cards', 'ties']
    return df

def run_all_combinations(pairs, deck, score_table):
    """
    Run the scoring for all combinations of card choices over a specified number of decks.
    """
    for i in range(len(pairs)):
        p1_choice = np.array(pairs[i][0])
        p2_choice = np.array(pairs[i][1])
        winner, p1_cards, p2_cards = scorer.play_entire_deck_tricks(p1_choice, p2_choice, deck)

        if winner == 'p1':
            score_table.loc[i,'p1_wins_cards'] += 1
        elif winner == 'p2':
            score_table.loc[i, 'p2_wins_cards'] += 1
        else:
            score_table.loc[i, 'ties'] += 1

    return score_table

print(run_all_combinations(create_choice_list(), deck1, create_score_table()))

