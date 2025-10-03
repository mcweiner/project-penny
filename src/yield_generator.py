import random
import os
import numpy as np
import sys
import time


start_time = time.perf_counter()

PATH_DATA = 'Data'

def create_shuffled_list(seed: int) -> np.ndarray:
    """
    Creates a single list of length 52 with 26 0s and 26 1s (representing red and black) characters, then shuffles it.
    """
    random.seed(seed)
    return np.array(random.sample([0] * 26 + [1] * 26, k=52), dtype=np.int8)

def generate_shuffled_lists_generator(num_lists=1_000_000):
    """
    Generates an iterator that yields a shuffled list one at a time.
    """
    for n in range(num_lists):
        yield create_shuffled_list(n)

def save_data(data: np.ndarray, filename: str) -> None:
    """
    Save a numpy array in the default output directory,
    ensuring that the directory exists.
    """
    full_filename = os.path.join(PATH_DATA, filename)

    if not os.path.exists(PATH_DATA):
        os.mkdir(PATH_DATA)

    if type(data) != np.ndarray:
        raise TypeError(f'data should be np.ndarray not {type(data)}')
    else:
        if os.path.exists(full_filename):
            raise FileExistsError(f'{full_filename} already exists, select a new name!')
        np.save(full_filename, data)
    return None

def load_data(filename: str) -> np.ndarray:
    """
    Loads data from an .npy file located
    in the default directory
    """
    return np.load(os.path.join(PATH_DATA, filename))


# To demonstrate, we can iterate through and count the items.
# No large list is ever created.
if __name__ == "__main__":
    # --- Example Usage ---
    # Using the generator to process the data without storing it all
    num_to_generate = 10_000
    lists_per_file = num_to_generate/10
    data_generator = generate_shuffled_lists_generator(num_to_generate)
    count = 0
    current_batch = []
    file_counter = 0

    # Iterate through the generator
    for i, shuffled_list in enumerate(generate_shuffled_lists_generator(num_to_generate)):
        current_batch.append(shuffled_list)

        # Check if the batch is full
        if len(current_batch) == lists_per_file:
            file_counter += 1
            filename = f'shuffled_lists_yield_part_{file_counter}.npy'
            
            # Convert the list to a NumPy array and save
            data_to_save = np.array(current_batch)
            save_data(data_to_save, filename)
            
            print(f'Saved {len(data_to_save)} lists to {filename}')
            
            # Reset the batch for the next file
            current_batch = []

    # The size of the generator object is very small
    #print(f"Memory size of the generator object: {sys.getsizeof(data_generator)} bytes")

    #print(f"\nSuccessfully iterated through {count} lists.")
    # Record the end time ⏱️
    #end_time = time.perf_counter()

    # Calculate and print the duration
    #elapsed_time = end_time - start_time
    #print(f"The code block took {elapsed_time:.4f} seconds to run.")

    loaded_data = load_data('shuffled_lists_yield_part_1.npy')
    print(loaded_data)