import numpy as np
import random
import time

# Player choices and deck setup
p1_choice = np.array([0, 0, 0])
p2_choice = np.array([0, 0, 1])
random.seed(42) # For reproducibility
deck1 = np.array(random.sample([0] * 26 + [1] * 26, k=52), dtype=np.int8)
random.seed(43) # For reproducibility
deck2 = np.array(random.sample([0] * 26 + [1] * 26, k=52), dtype=np.int8)

import numpy as np

def find_first_instance(sequence: np.ndarray, deck: np.ndarray) -> int:
    """
    Finds the index of the first occurrence of a chosen sequence in the deck.

    Args:
        sequence (np.ndarray): The sequence of values to search for.
        deck (np.ndarray): The array to search within.

    Returns:
        int: The starting index of the first match, or -1 if the sequence is not found.
    """
    # Get the length of the sequence to create windows of the correct size.
    sequence_len = len(sequence)

    # If the deck is shorter than the sequence, a match is impossible.
    if len(deck) < sequence_len:
        return -1

    # Create sliding windows of the same size as the sequence.
    windows = np.lib.stride_tricks.sliding_window_view(deck, window_shape=sequence_len)

    # Find all windows that perfectly match the sequence.
    matches = np.all(windows == sequence, axis=1)

    # If any matches exist, np.argmax finds the index of the first 'True' value.
    # Otherwise, return -1.
    if np.any(matches):
        return np.argmax(matches)
    else:
        return -1

def first_instance_p1_only(p1_choice: np.ndarray, deck: np.ndarray):
    """
    Find the index of the first occurrence of player 1's chosen sequence in the deck. Returns -1 if not found.
    """
    windows = np.lib.stride_tricks.sliding_window_view(deck, 3)
    # The print statement was removed to allow for accurate performance timing.
    p1_matches = np.all(windows == p1_choice, axis=1)
    p1_idx = np.argmax(p1_matches) if np.any(p1_matches) else -1
    return p1_idx

def first_instance_p2_only(p2_choice: np.ndarray, deck: np.ndarray):
    """
    Find the index of the first occurrence of player 2's chosen sequence in the deck. Returns -1 if not found.
    """
    windows = np.lib.stride_tricks.sliding_window_view(deck, 3)
    # The print statement was removed to allow for accurate performance timing.
    p2_matches = np.all(windows == p2_choice, axis=1)
    p2_idx = np.argmax(p2_matches) if np.any(p2_matches) else -1
    return p2_idx

def play_entire_deck_cards(p1_choice: np.ndarray, p2_choice: np.ndarray, deck: np.ndarray):
    """
    Play through the entire deck, scoring each round as sequences are found.
    Returns total cards for each player and the winner.
    """
    p1_total_cards = 0
    p2_total_cards = 0
    i = 0
    while i <= len(deck) - 3:
        sub_deck = deck[i:]
        p1_idx = first_instance_p1_only(p1_choice, sub_deck)
        p2_idx = first_instance_p2_only(p2_choice, sub_deck)
        
        if p1_idx == -1 and p2_idx == -1:
            break
        elif p1_idx != -1 and (p2_idx == -1 or p1_idx < p2_idx):
            win_idx = p1_idx
            p1_total_cards += win_idx + 3
        elif p2_idx != -1 and (p1_idx == -1 or p2_idx < p1_idx):
            win_idx = p2_idx
            p2_total_cards += win_idx + 3
        else: # Tie logic corrected to prevent crash
            win_idx = p1_idx
        
        i += win_idx + 3
    
    winner = 'p1' if p1_total_cards > p2_total_cards else 'p2' if p2_total_cards > p1_total_cards else 'tie'
    return winner, p1_total_cards, p2_total_cards

def play_entire_deck_tricks(p1_choice: np.ndarray, p2_choice: np.ndarray, deck: np.ndarray):
    """
    Play through the entire deck, scoring each round as sequences are found.
    Returns total tricks for each player and the winner.
    """
    p1_total_tricks = 0
    p2_total_tricks = 0
    i = 0
    while i <= len(deck) - 3:
        sub_deck = deck[i:]
        p1_idx = first_instance_p1_only(p1_choice, sub_deck)
        p2_idx = first_instance_p2_only(p2_choice, sub_deck)

        if p1_idx == -1 and p2_idx == -1:
            break
        elif p1_idx != -1 and (p2_idx == -1 or p1_idx < p2_idx):
            win_idx = p1_idx
            p1_total_tricks += 1
        elif p2_idx != -1 and (p1_idx == -1 or p2_idx < p1_idx):
            win_idx = p2_idx
            p2_total_tricks += 1
        else: # Tie logic corrected to prevent crash
            win_idx = p1_idx
            
        i += win_idx + 3

    winner = 'p1' if p1_total_tricks > p2_total_tricks else 'p2' if p2_total_tricks > p1_total_tricks else 'tie'
    return winner, p1_total_tricks, p2_total_tricks

def play_entire_deck(p1_choice: np.ndarray, p2_choice: np.ndarray, deck: np.ndarray):
    """
    Play through the entire deck, scoring each round as sequences are found.
    Returns total cards and tricks for each player.
    """
    p1_total_cards = 0
    p2_total_cards = 0
    p1_total_tricks = 0
    p2_total_tricks = 0
    i = 0
    while i <= len(deck) - 3:
        sub_deck = deck[i:]
        p1_idx = first_instance_p1_only(p1_choice, sub_deck)
        p2_idx = first_instance_p2_only(p2_choice, sub_deck)
        if p1_idx == -1 and p2_idx == -1:
            break
        elif p1_idx != -1 and (p2_idx == -1 or p1_idx < p2_idx):
            win_idx = p1_idx
            p1_total_tricks += 1
            p1_total_cards += win_idx + 3
        elif p2_idx != -1 and (p1_idx == -1 or p2_idx < p1_idx):
            win_idx = p2_idx
            p2_total_tricks += 1
            p2_total_cards += win_idx + 3
        else:
            win_idx = p1_idx  # tie, both at same index
        i += win_idx + 3
    return p1_total_cards, p2_total_cards, p1_total_tricks, p2_total_tricks

# === Efficiency Comparison ===
if __name__ == "__main__":
    num_runs = 2000

    times_cards = []
    times_tricks = []
    times_combined = []

    print(f"Comparing function performance over {num_runs} runs...")

    for _ in range(num_runs):
        # Time the 'cards' function
        start_time = time.perf_counter()
        play_entire_deck_cards(p1_choice, p2_choice, deck1)
        end_time = time.perf_counter()
        times_cards.append(end_time - start_time)

        # Time the 'tricks' function
        start_time = time.perf_counter()
        play_entire_deck_tricks(p1_choice, p2_choice, deck1)
        end_time = time.perf_counter()
        times_tricks.append(end_time - start_time)

        # Time the 'combined' function
        start_time = time.perf_counter()
        play_entire_deck(p1_choice, p2_choice, deck1)
        end_time = time.perf_counter()
        times_combined.append(end_time - start_time)

    # Calculate average times
    avg_cards = sum(times_cards) / num_runs
    avg_tricks = sum(times_tricks) / num_runs
    avg_combined = sum(times_combined) / num_runs
    
    print("\n--- Average Execution Time ---")
    print(f"play_entire_deck_cards:   {avg_cards:.6f} seconds")
    print(f"play_entire_deck_tricks:  {avg_tricks:.6f} seconds")
    print(f"play_entire_deck (combined): {avg_combined:.6f} seconds")
    print("------------------------------")