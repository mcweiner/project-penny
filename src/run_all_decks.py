import os
import numpy as np
import pandas as pd
import yield_generator as yield_shuffles
import score_all_combos as score_all_combos

def load_decks():
    ''' 
    Load pre-generated decks from a .npy file.
    '''
    decks = yield_shuffles.load_data('shuffled_lists_yield_part_1.npy')
    return decks

def score_all_decks(scoring_function: str) -> np.ndarray:
    ''' 
    Score all decks using the specified scoring function ('cards' or 'tricks').
    '''
    pairs = score_all_combos.create_choice_list()
    results = score_all_combos.create_score_table()

    all_decks = load_decks()
    for deck in all_decks:
        results = score_all_combos.run_all_combinations(pairs, deck, results, scoring_function)
    return results

if __name__ == "__main__":
    scoring_function = 'cards'  # or 'tricks'
    results = score_all_decks(scoring_function)
    df = pd.DataFrame(results, columns=['p1_wins', 'p2_wins', 'ties'])
    df['pair'] = score_all_combos.create_choice_list()
    print(df)
