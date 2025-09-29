import src.scorer as scorer
import src.yield_generator as yield_shuffles
import numpy as np
import pandas as pd
import os

def create_score_table():
    """
    Create a blank table to track scores for each combination of card choices.
    """
    return pd.DataFrame(np.zeros((56, 5), dtype=int))

print(create_score_table())