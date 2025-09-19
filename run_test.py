from datetime import datetime as dt
import numpy as np
import pandas as pd
import sys
import time
import os

import yield_generator as yield_shuffles
import iterator as iter_shuffles

# Benchmark parameters
N_RUNS = 5
N_DECKS = 100_000


results = []


yield_times = []
storage_bytes = []
for i in range(N_RUNS):
    start = dt.now()
    
    gen = yield_shuffles.generate_shuffled_lists_generator(N_DECKS)
    count = 0
    size_yield = 0
    for list in gen:
        count += 1
        size_yield += sys.getsizeof(list)

    end = dt.now()
    yield_times.append((end - start).total_seconds())
    storage_bytes.append(size_yield)

yield_times = np.array(yield_times)
storage_bytes = np.array(storage_bytes)
results.append({
    "Implementation": "Yield",
    "Mean Generate Time": yield_times.mean(),
    "Std Dev": yield_times.std(ddof=1),
    "Mean Storage": storage_bytes.mean()
})


iterator_times = []
storage_bytes = []
for i in range(N_RUNS):
    start = dt.now()

    
    iter = iter_shuffles.ShuffledListGenerator(N_DECKS)
    count = 0
    size_iter = 0
    for list in iter:
        count += 1
        size_iter += sys.getsizeof(list)

    end = dt.now()
    iterator_times.append((end - start).total_seconds())
    storage_bytes.append(size_iter)
iterator_times = np.array(iterator_times)
storage_bytes = np.array(storage_bytes)
results.append({
    "Implementation": "Iterator",
    "Mean Generate Time": iterator_times.mean(),
    "Std Dev": iterator_times.std(ddof=1),
    "Mean Storage": storage_bytes.mean()
})

write_times = []
storage_bytes = []
for i in range(N_RUNS):
    start = dt.now()
    # Create a sample numpy array to save
    # May have to modify
    sample_data = np.random.rand(10_000, 52)

    # Measure write time
    start_write_time = time.perf_counter()
    yield_shuffles.save_data(sample_data, f'Yield_time_test_data{i}.npy')
    end_write_time = time.perf_counter()
    write_duration = end_write_time - start_write_time
write_times = np.array(write_times)
results.append({
    "Implementation": "Yield",
    "Mean Generate Time": write_times.mean(),
    "Std Dev": write_times.std(ddof=1),
    "Mean Storage": 'NA'
})

write_times = []
storage_bytes = []
for i in range(N_RUNS):
    start = dt.now()
    # Create a sample numpy array to save
    sample_data = np.random.rand(100_000, 52)

    # Measure write time
    start_write_time = time.perf_counter()
    iter_shuffles.save_data(sample_data, f'Iter_time_test_data{i}.npy')
    end_write_time = time.perf_counter()
    write_duration = end_write_time - start_write_time
    write_times.append(write_duration)
    # print(f"Write time: {write_duration:.4f} seconds")
write_times = np.array(write_times)
results.append({
    "Implementation": "Iterator",
    "Mean Generate Time": write_times.mean(),
    "Std Dev": write_times.std(ddof=1),
    "Mean Storage": 'NA'
})

read_times = []
storage_bytes = []
for i in range(N_RUNS):
    start = dt.now()
    # Create a sample numpy array to save
    # May have to modify
    sample_data = np.random.rand(10_000, 52)

    # Measure write time
    start_read_time = time.perf_counter()
    loaded_data = yield_shuffles.load_data(f'Yield_time_test_data{i}.npy')
    end_read_time = time.perf_counter()
    read_duration = end_read_time - start_read_time
    read_times.append(read_duration)
    #print(f"Read time: {read_duration:.4f} seconds")
    file_name = f'Yield_time_test_data{i}.npy'
    folder_name = "Data"

    # Construct the full path to the file
    file_path = os.path.join(folder_name, file_name)

    # Use a try-except block for safe deletion.
    os.remove(file_path)
    # print(f"File '{file_path}' deleted successfully.")
    read_times.append(read_duration)
    # print(f"Write time: {write_duration:.4f} seconds")
    
read_times = np.array(read_times)
results.append({
    "Implementation": "Yield",
    "Mean Read Time": read_times.mean(),
    "Std Dev": read_times.std(ddof=1),
    "Mean Storage": 'NA'
})

read_times = []
storage_bytes = []
for i in range(N_RUNS):
    start = dt.now()
    # Create a sample numpy array to save
    # May have to modify
    sample_data = np.random.rand(10_000, 52)

    # Measure write time
    start_read_time = time.perf_counter()
    loaded_data = iter_shuffles.load_data(f'Iter_time_test_data{i}.npy')
    end_read_time = time.perf_counter()
    read_duration = end_read_time - start_read_time
    read_times.append(read_duration)
    #print(f"Read time: {read_duration:.4f} seconds")
    file_name = f'Iter_time_test_data{i}.npy'
    folder_name = "Data"

    # Construct the full path to the file
    file_path = os.path.join(folder_name, file_name)

    # Use a try-except block for safe deletion.
    os.remove(file_path)
    # print(f"File '{file_path}' deleted successfully.")
    #read_times.append(read_times)
    # print(f"Write time: {write_duration:.4f} seconds")
read_times = np.array(read_times)
results.append({
    "Implementation": "Iterator",
    "Mean Generate Time": read_times.mean(),
    "Std Dev": read_times.std(ddof=1),
    "Mean Storage": 'NA'
})

# Display results as a DataFrame
df = pd.DataFrame(results)
print(df)
