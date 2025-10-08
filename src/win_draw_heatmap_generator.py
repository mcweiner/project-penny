import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd # Import the pandas library to work with CSV data

def create_win_draw_heatmap_cards():
    """
    Generates and saves a heatmap based on the '_cards' columns from the CSV.
    """
    
    # Step 1: Define labels and data structure
    num_labels = 8
    br_labels = [f'{i:03b}'.replace('0', 'B').replace('1', 'R') for i in range(num_labels)]

    win_draw_prob_matrix = np.zeros((num_labels, num_labels), dtype=float)
    annot_labels = np.full((num_labels, num_labels), "", dtype=object)

    # Step 2: Read data from CSV and calculate probabilities
    # --- FIX: Create a robust path that works regardless of where the script is run ---
    # Get the directory where the script is located (e.g., .../project-penny/src)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to the project root (e.g., .../project-penny)
    project_root = os.path.dirname(script_dir)
    # Construct the path to the 'Tables' folder
    tables_folder_path = os.path.join(project_root, 'Tables')
    csv_filename = os.path.join(tables_folder_path, 'pairs_table.csv')

    try:
        df = pd.read_csv(csv_filename)
    except FileNotFoundError:
        print(f"Error: '{csv_filename}' not found. Please ensure the 'Tables' directory is next to the 'src' directory.")
        return

    # --- FIX: Calculate N from the first row, as it's consistent for each pair ---
    # We assume the number of games (N) is the same for every pair.
    first_row = df.iloc[0]
    n_value = first_row['p1_wins_cards'] + first_row['p2_wins_cards'] + first_row['ties_cards']

    for index, row in df.iterrows():
        p1_choice, p2_choice = eval(row['pairs'])
        
        p1_wins = row['p1_wins_cards']
        p2_wins = row['p2_wins_cards']
        ties = row['ties_cards']
        
        total_games = p1_wins + p2_wins + ties
        
        if total_games > 0:
            p2_win_prob = p2_wins / total_games
            tie_prob = ties / total_games
            win_or_tie_prob = (p2_wins + ties) / total_games
            p2_win_percent = int(p2_win_prob * 100)
            tie_percent = int(tie_prob * 100)
            annot_labels[p1_choice, p2_choice] = f"{p2_win_percent}({tie_percent})"
        else:
            win_or_tie_prob = 0
            annot_labels[p1_choice, p2_choice] = "0(0)"
            
        win_draw_prob_matrix[p1_choice, p2_choice] = win_or_tie_prob
        
    # Step 3: Create mask and generate plot
    mask = np.identity(num_labels, dtype=bool)
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(
        win_draw_prob_matrix, xticklabels=br_labels, yticklabels=br_labels,
        annot=annot_labels, fmt='', annot_kws={"size": 8}, mask=mask,
        cmap='YlGnBu', linewidths=.5, cbar=False, square=True
    )
    ax.set_facecolor('darkgrey')

    # Step 4: Highlight max values
    for i in range(num_labels):
        row_data = win_draw_prob_matrix[i, :]
        if row_data.any():
            max_value = np.max(row_data)
            max_indices = np.where(row_data == max_value)[0]
            for j in max_indices:
                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=False, edgecolor='black', lw=3))

    # Step 5: Add titles and save
    # --- FIX: Use the corrected N value in the title ---
    plt.title(f'My Chance of Win(Draw)\nby Cards\nN={n_value}', fontsize=16, pad=20)
    plt.xlabel('My Choice', fontsize=12)
    plt.ylabel('Opponent Choice', fontsize=12)
    plt.yticks(rotation=0) 
    plt.tight_layout(rect=[0, 0, 1, 0.96]) 

    if not os.path.exists(tables_folder_path):
        os.makedirs(tables_folder_path)
    
    output_filename = os.path.join(tables_folder_path, 'win_draw_heatmap_cards.png')
    plt.savefig(output_filename)
    print(f"Heatmap saved successfully as '{output_filename}'")
    plt.close() # Close the plot to start fresh for the next one

def create_win_draw_heatmap_tricks():
    """
    Generates and saves a heatmap based on the '_tricks' columns from the CSV.
    """
    
    # Step 1: Define labels and data structure
    num_labels = 8
    br_labels = [f'{i:03b}'.replace('0', 'B').replace('1', 'R') for i in range(num_labels)]

    win_draw_prob_matrix = np.zeros((num_labels, num_labels), dtype=float)
    annot_labels = np.full((num_labels, num_labels), "", dtype=object)

    # Step 2: Read data from CSV and calculate probabilities
    # --- FIX: Create a robust path that works regardless of where the script is run ---
    # Get the directory where the script is located (e.g., .../project-penny/src)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to the project root (e.g., .../project-penny)
    project_root = os.path.dirname(script_dir)
    # Construct the path to the 'Tables' folder
    tables_folder_path = os.path.join(project_root, 'Tables')
    csv_filename = os.path.join(tables_folder_path, 'pairs_table.csv')

    try:
        df = pd.read_csv(csv_filename)
    except FileNotFoundError:
        print(f"Error: '{csv_filename}' not found. Please ensure the 'Tables' directory is next to the 'src' directory.")
        return

    # --- FIX: Calculate N from the first row, as it's consistent for each pair ---
    # We assume the number of games (N) is the same for every pair.
    first_row = df.iloc[0]
    n_value = first_row['p1_wins_tricks'] + first_row['p2_wins_tricks'] + first_row['ties_tricks']

    for index, row in df.iterrows():
        p1_choice, p2_choice = eval(row['pairs'])
        
        p1_wins = row['p1_wins_tricks']
        p2_wins = row['p2_wins_tricks']
        ties = row['ties_tricks']
        
        total_games = p1_wins + p2_wins + ties
        
        if total_games > 0:
            p2_win_prob = p2_wins / total_games
            tie_prob = ties / total_games
            win_or_tie_prob = (p2_wins + ties) / total_games
            p2_win_percent = int(p2_win_prob * 100)
            tie_percent = int(tie_prob * 100)
            annot_labels[p1_choice, p2_choice] = f"{p2_win_percent}({tie_percent})"
        else:
            win_or_tie_prob = 0
            annot_labels[p1_choice, p2_choice] = "0(0)"
            
        win_draw_prob_matrix[p1_choice, p2_choice] = win_or_tie_prob
        
    # Step 3: Create mask and generate plot
    mask = np.identity(num_labels, dtype=bool)
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(
        win_draw_prob_matrix, xticklabels=br_labels, yticklabels=br_labels,
        annot=annot_labels, fmt='', annot_kws={"size": 8}, mask=mask,
        cmap='YlGnBu', linewidths=.5, cbar=False, square=True
    )
    ax.set_facecolor('darkgrey')

    # Step 4: Highlight max values
    for i in range(num_labels):
        row_data = win_draw_prob_matrix[i, :]
        if row_data.any():
            max_value = np.max(row_data)
            max_indices = np.where(row_data == max_value)[0]
            for j in max_indices:
                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=False, edgecolor='black', lw=3))

    # Step 5: Add titles and save
    # --- FIX: Use the corrected N value in the title ---
    plt.title(f'My Chance of Win(Draw)\nby Tricks\nN={n_value}', fontsize=16, pad=20)
    plt.xlabel('My Choice', fontsize=12)
    plt.ylabel('Opponent Choice', fontsize=12)
    plt.yticks(rotation=0) 
    plt.tight_layout(rect=[0, 0, 1, 0.96]) 

    if not os.path.exists(tables_folder_path):
        os.makedirs(tables_folder_path)
    
    output_filename = os.path.join(tables_folder_path, 'win_draw_heatmap_tricks.png')
    plt.savefig(output_filename)
    print(f"Heatmap saved successfully as '{output_filename}'")
    plt.close() # Close the plot

def augment_data(n: int):
    """
    This function should complete the following:
    - Create n new decks
    - Automatically update scores and figures based on the new decks
    """

if __name__ == '__main__':
    create_win_draw_heatmap_cards()
    create_win_draw_heatmap_tricks()