import random
import os
import numpy as np
import sys
import time

seed(77)

start_time = time.perf_counter()

PATH_DATA = 'Project work'

def create_shuffled_list():
    """
    Creates a single list of length 52 with 26 0s and 26 1s (representing red and black) characters, then shuffles it.
    """
    return random.sample([0] * 26 + [1] * 26, k=52)

def generate_shuffled_lists_generator(num_lists=1_000_000):
    """
    Generates an iterator that yields a shuffled list one at a time.
    """
    for n in range(num_lists):
        yield create_shuffled_list()

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



# The size of the generator object is very small
print(f"Memory size of the generator object: {sys.getsizeof(data_generator)} bytes")

# To demonstrate, we can iterate through and count the items.
# No large list is ever created.
if __name__ == "__main__":
    # --- Example Usage ---
    # Using the generator to process the data without storing it all
    num_to_generate = 100_000
    data_generator = generate_shuffled_lists_generator(num_to_generate)
    count = 0
    for shuffled_list in data_generator:
        # Here, you would perform your analysis on 'shuffled_list'
        # For example, you could check for a specific pattern.
        if (count+1)%10_000==0:
            save_data(np.array(shuffled_list[count-9_999:count]), f'data_store_{(count+1)//10_000}')
            #print(count)
        count += 1

print(f"\nSuccessfully iterated through {count} lists.")
# Record the end time ⏱️
end_time = time.perf_counter()

# Calculate and print the duration
elapsed_time = end_time - start_time
print(f"The code block took {elapsed_time:.4f} seconds to run.")