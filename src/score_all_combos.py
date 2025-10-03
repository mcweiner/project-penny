import scorer
import numpy as np
import pandas as pd
import itertools
import random
import yield_generator as yield_shuffles
import os


random.seed(42) # For reproducibility
# Second, bigger deck, similiar to what will be the final decks
deck2 = np.array([np.random.permutation(np.concatenate([np.zeros(26, dtype=int), np.ones(26, dtype=int)])) for _ in range(2)])

def binary_tuple_to_decimal(b_tuple):
    """Converts a tuple of binary digits to its decimal integer equivalent."""
    return int("".join(map(str, b_tuple)), 2)

def create_combined_deck(size,
                         base_file='shuffled_lists_yield_part_1.npy',
                         file_pattern='data_store_{}.npy'):
    """
    Creates a 2D NumPy array by loading and concatenating multiple data files.
    """
    if not os.path.exists(base_file):
        print(f"Error: Base file not found at '{base_file}'")
        return None
    combined_deck = yield_shuffles.load_data(base_file)
    for n in range(1, size + 1):
        next_file = file_pattern.format(n)
        if os.path.exists(next_file):
            additional_data = yield_shuffles.load_data(next_file)
            combined_deck = np.concatenate((combined_deck, additional_data), axis=0)
        else:
            print(f"Warning: File '{next_file}' not found. Skipping.")
    return combined_deck

def create_choice_list():
    """
    Create a list of all possible 3-card binary choices (0s and 1s).
    """
    options = [tuple(p) for p in itertools.product([0, 1], repeat=3)]
    pairs = [(a, b) for a, b in itertools.product(options, repeat=2) if a != b]
    return pairs

def create_score_table(pairs):
    """
    Create a blank table to track scores for each combination of card choices.
    """
    matchups = [f"({binary_tuple_to_decimal(p1)}, {binary_tuple_to_decimal(p2)})" for p1, p2 in pairs]
    df = pd.DataFrame(matchups, columns=['pairs'])
    df['p1_wins_cards'] = 0
    df['p2_wins_cards'] = 0
    df['ties_cards'] = 0
    df['p1_wins_tricks'] = 0
    df['p2_wins_tricks'] = 0
    df['ties_tricks'] = 0
    return df

def run_all_combinations_big_deck(pairs, deck, score_table):
    """
    Run the scoring for all combinations of card choices over a specified number of decks.
    """
    num_decks = len(deck)
    for n in range(num_decks):
        print(f"Processing deck {n + 1}/{num_decks}...")
        for i in range(len(pairs)):
            p1_choice = np.array(pairs[i][0])
            p2_choice = np.array(pairs[i][1])

            winner, p1_cards, p2_cards = scorer.play_entire_deck_cards(p1_choice, p2_choice, deck[n])
            if winner == 'p1':
                score_table.loc[i,'p1_wins_cards'] += 1
            elif winner == 'p2':
                score_table.loc[i, 'p2_wins_cards'] += 1
            else:
                score_table.loc[i, 'ties_cards'] += 1

            winner, p1_tricks, p2_tricks = scorer.play_entire_deck_tricks(p1_choice, p2_choice, deck[n])
            if winner == 'p1':
                score_table.loc[i,'p1_wins_tricks'] += 1
            elif winner == 'p2':
                score_table.loc[i, 'p2_wins_tricks'] += 1
            else:
                score_table.loc[i, 'ties_tricks'] += 1
    print("Processing complete.")
    return score_table

def save_results_to_csv(score_df, filepath="pairs_table.csv"):
    """
    Saves the final score DataFrame to a CSV file in a specified path.
    Creates the destination folder if it does not exist.

    Args:
        score_df (pd.DataFrame): The DataFrame containing the pairs scores.
        filepath (str): The full path for the output CSV file (e.g., "Tables/results.csv").
    """
    try:
        # Get the directory part of the filepath
        folder = os.path.dirname(filepath)
        
        # If a folder is specified (i.e., the path contains a '/')
        # and it doesn't exist, create it.
        if folder and not os.path.exists(folder):
            os.makedirs(folder)
            print(f"📁 Created directory: '{folder}'")
            
        # Save the DataFrame to the specified path
        score_df.to_csv(filepath, index=False)
        print(f"✅ Results successfully saved to '{filepath}'")
        
    except Exception as e:
        print(f"❌ Error saving file: {e}")

if __name__ == "__main__":
    #print(run_all_combinations(create_choice_list(), deck1, create_score_table()))

    #print(run_all_combinations_big_deck(create_choice_list(), deck2, create_score_table()))

    #choice_pairs = create_choice_list()
    #score_df = create_score_table(choice_pairs)
    #print(run_all_combinations_big_deck(choice_pairs, deck2, score_df))

    # 1. Create the list of all possible pairs
    choice_pairs = create_choice_list()
    
    # 2. Create an empty DataFrame to hold the scores
    score_df = create_score_table(choice_pairs)
    # If you want to use a larger deck, uncomment the next line
    deck = yield_shuffles.load_data('shuffled_lists_yield_part_1.npy')  # Adjust size as needed
    
    # 3. Run the simulation and get the final scores
    final_scores = run_all_combinations_big_deck(choice_pairs, deck, score_df)

    # 4. Print the final results to the console
    print("\n--- Final Score Table ---")
    print(final_scores)
    
    # 5. Save the final score table to a CSV file inside the "Tables" folder
    #    This is the only line you need to change.
    save_results_to_csv(final_scores, filepath="Tables/pairs_table.csv")
