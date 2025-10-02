import scorer
import numpy as np
import pandas as pd
import itertools
import random


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
    num_pairs = len(create_choice_list())  # 56
    results = np.zeros((num_pairs, 3), dtype=np.int32)
    return results

def run_all_combinations(pairs, deck, results, scoring_function):
    """
    Run the scoring for all combinations of card choices over a specified number of decks.
    """
    for i in range(len(pairs)):
        p1_choice = np.array(pairs[i][0])
        p2_choice = np.array(pairs[i][1])
        if scoring_function == 'tricks':
            winner, p1_cards, p2_cards = scorer.play_entire_deck_tricks(p1_choice, p2_choice, deck)
        else:
            winner, p1_cards, p2_cards = scorer.play_entire_deck_cards(p1_choice, p2_choice, deck)

        if winner == 'p1':
            results[i, 0] += 1
        elif winner == 'p2':
            results[i, 1] += 1
        else:
            results[i, 2] += 1

    return results

#results = run_all_combinations(create_choice_list(), deck1, create_score_table(), "cards")
#df = pd.DataFrame(results, columns=['p1_wins', 'p2_wins', 'ties'])
#df['pair'] = create_choice_list()
#print(df)
