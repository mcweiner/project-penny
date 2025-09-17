from datetime import datetime as dt
import numpy as np
import pandas as pd
import sys

import src.yield_generator as yield_shuffles
import src.iterator as iter_shuffles

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
    for i in gen:
        count += 1

    end = dt.now()
    yield_times.append((end - start).total_seconds())
    storage_bytes.append(sys.getsizeof(gen))

yield_times = np.array(yield_times)
storage_bytes = np.array(storage_bytes)
results.append({
    "Implementation": "Yield",
    "Mean Runtime": yield_times.mean(),
    "Std Dev": yield_times.std(ddof=1),
    "Mean Storage": storage_bytes.mean()
})


iterator_times = []
storage_bytes = []
for i in range(N_RUNS):
    start = dt.now()

    
    iter = iter_shuffles.ShuffledListGenerator(N_DECKS)
    count = 0
    for i in iter:
        count += 1

    end = dt.now()
    iterator_times.append((end - start).total_seconds())
    storage_bytes.append(sys.getsizeof(iter)) #Want to figure out how to incorporate the size of the internal array
iterator_times = np.array(iterator_times)
storage_bytes = np.array(storage_bytes)
results.append({
    "Implementation": "Iterator",
    "Mean Runtime": iterator_times.mean(),
    "Std Dev": iterator_times.std(ddof=1),
    "Mean Storage": storage_bytes.mean()
})

# Display results as a DataFrame
df = pd.DataFrame(results)
print(df)
