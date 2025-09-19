import numpy as np
import random
import sys
import time
import os


start_time = time.perf_counter()

PATH_DATA = 'Data'

class ShuffledListGenerator:
    """
    An iterator that generates shuffled lists one at a time.
    """

    def __init__(self, num_lists):
        self.num_lists = num_lists
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.num_lists:
            self.count += 1
            random.seed(self.count)
            deck = random.sample([0] * 26 + [1] * 26, k=52)
            return np.array(deck, dtype=np.uint8)
        else:
            raise StopIteration

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

# --- Example Usage ---
if __name__ == "__main__":
    num_to_generate = 2_000_000
    data_iterator = ShuffledListGenerator(num_to_generate)
    lists_per_file = num_to_generate//10
    
    # Iterate over the iterator just like a list, but with low memory usage
    write_start_time = time.perf_counter()
    count = 0
    arr = np.zeros(shape=(lists_per_file, 52), dtype=np.uint8)
    for shuffled_list in data_iterator:
        if data_iterator.count%lists_per_file == 0 and count != 0:
            # print(count%10_000)
            save_data(arr, f'shuffled_lists_iter_part_{data_iterator.count//lists_per_file}')
            arr = np.zeros(shape=(lists_per_file, 52))
            count = 0
        else:
            arr[count] = shuffled_list
        count += 1

    end_time = time.perf_counter()

    # The size of the iterator object is small
    #print(f"Memory size of the iterator object: {sys.getsizeof(data_iterator)} bytes")
    #print(f"Memory size of the array: {sys.getsizeof(arr)} bytes")

    # Calculate and print the duration
    elapsed_time = end_time - start_time
    #print(f"The code block took {elapsed_time:.4f} seconds to run.")

    write_elapsed_time = end_time - start_time
    #print(f"The writing to file time took {write_elapsed_time:.4f} seconds to run.")

    loaded_data = load_data('shuffled_lists_iter_part_1.npy')
    #print(loaded_data)
