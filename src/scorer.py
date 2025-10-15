import numpy as np

def first_instance_p1_only(p1_choice: np.ndarray, deck: np.ndarray):
    """
    Find the index of the first occurrence of player 1's chosen sequence in the deck. Returns -1 if not found.
    """
    windows = np.lib.stride_tricks.sliding_window_view(deck, 3)
    p1_matches = np.all(windows == p1_choice, axis=1)
    p1_idx = np.argmax(p1_matches) if np.any(p1_matches) else -1
    return p1_idx

def first_instance_p2_only(p2_choice: np.ndarray, deck: np.ndarray):
    """
    Find the index of the first occurrence of player 2's chosen sequence in the deck. Returns -1 if not found.
    """
    windows = np.lib.stride_tricks.sliding_window_view(deck, 3)
    p2_matches = np.all(windows == p2_choice, axis=1)
    p2_idx = np.argmax(p2_matches) if np.any(p2_matches) else -1
    return p2_idx

def play_entire_deck_slow_cards(p1_choice: np.ndarray, p2_choice: np.ndarray, deck: np.ndarray):
    """
    Play through the entire deck, scoring each round as sequences are found.
    Returns total cards for each player and the winner.
    """
    p1_total_cards = 0
    p2_total_cards = 0
    i = 0
    winner = 'tie'
    while i <= len(deck) - 3:
        sub_deck = deck[i:]
        p1_idx = first_instance_p1_only(p1_choice, sub_deck)
        p2_idx = first_instance_p2_only(p2_choice, sub_deck)
        if p1_idx == -1 and p2_idx == -1:
            #print('Error, neither sequence found')
            break
        elif p1_idx != -1 and (p2_idx == -1 or p1_idx < p2_idx):
            win_idx = p1_idx
            p1_total_cards += win_idx + 3
        elif p2_idx != -1 and (p1_idx == -1 or p2_idx < p1_idx):
            win_idx = p2_idx
            p2_total_cards += win_idx + 3
        else:
            win_idx = p1_idx  #tie, both at same index (probably not needed)
        i += win_idx + 3
    winner = 'p1' if p1_total_cards > p2_total_cards else 'p2' if p2_total_cards > p1_total_cards else 'tie'
    return winner, p1_total_cards, p2_total_cards

def play_entire_deck_slow_tricks(p1_choice: np.ndarray, p2_choice: np.ndarray, deck: np.ndarray):
    """
    Play through the entire deck, scoring each round as sequences are found.
    Returns total tricks for each player and the winner.
    """
    p1_total_tricks = 0
    p2_total_tricks = 0
    i = 0
    winner = 'tie'
    while i <= len(deck) - 3:
        sub_deck = deck[i:]
        p1_idx = first_instance_p1_only(p1_choice, sub_deck)
        p2_idx = first_instance_p2_only(p2_choice, sub_deck)
        if p1_idx == -1 and p2_idx == -1:
            #print('Error, neither sequence found')
            break
        elif p1_idx != -1 and (p2_idx == -1 or p1_idx < p2_idx):
            win_idx = p1_idx
            p1_total_tricks += 1
        elif p2_idx != -1 and (p1_idx == -1 or p2_idx < p1_idx):
            win_idx = p2_idx
            p2_total_tricks += 1
        else:
            win_idx = p1_idx  #tie, both at same index (probably not needed)
        i += win_idx + 3
    winner = 'p1' if p1_total_tricks > p2_total_tricks else 'p2' if p2_total_tricks > p1_total_tricks else 'tie'
    return winner, p1_total_tricks, p2_total_tricks

def find_all_indices(choice, deck_windows):
    return np.flatnonzero(np.all(deck_windows == choice, axis=1))

def play_entire_deck_cards(p1_choice, p2_choice, deck):
    deck_windows = np.lib.stride_tricks.sliding_window_view(deck, 3)
    p1_idxs = find_all_indices(p1_choice, deck_windows)
    p2_idxs = find_all_indices(p2_choice, deck_windows)

    p1_total = p2_total = 0
    pos = 0
    i1 = i2 = 0
    while i1 < len(p1_idxs) or i2 < len(p2_idxs):
        next_p1 = p1_idxs[i1] if i1 < len(p1_idxs) else np.inf
        next_p2 = p2_idxs[i2] if i2 < len(p2_idxs) else np.inf

        if next_p1 == np.inf and next_p2 == np.inf:
            break

        if next_p1 < next_p2:
            p1_total += next_p1 - pos + 3
            pos = next_p1 + 3
            i1 += 1
        elif next_p2 < next_p1:
            p2_total += next_p2 - pos + 3
            pos = next_p2 + 3
            i2 += 1
        else:  # tie
            pos = next_p1 + 3
            i1 += 1
            i2 += 1

    winner = 'p1' if p1_total > p2_total else 'p2' if p2_total > p1_total else 'tie'
    return winner, p1_total, p2_total

def play_entire_deck_tricks(p1_choice, p2_choice, deck):
    deck_windows = np.lib.stride_tricks.sliding_window_view(deck, 3)
    p1_idxs = find_all_indices(p1_choice, deck_windows)
    p2_idxs = find_all_indices(p2_choice, deck_windows)

    p1_total = p2_total = 0
    pos = 0
    i1 = i2 = 0
    while i1 < len(p1_idxs) or i2 < len(p2_idxs):
        next_p1 = p1_idxs[i1] if i1 < len(p1_idxs) else np.inf
        next_p2 = p2_idxs[i2] if i2 < len(p2_idxs) else np.inf

        if next_p1 == np.inf and next_p2 == np.inf:
            break

        if next_p1 < next_p2:
            p1_total += 1
            pos = next_p1 + 3
            i1 += 1
        elif next_p2 < next_p1:
            p2_total += 1
            pos = next_p2 + 3
            i2 += 1
        else:  # tie
            pos = next_p1 + 3
            i1 += 1
            i2 += 1

    winner = 'p1' if p1_total > p2_total else 'p2' if p2_total > p1_total else 'tie'
    return winner, p1_total, p2_total

