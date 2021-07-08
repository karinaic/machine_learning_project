import pandas as pd 
import os


def curr_path():
    path = os.path.dirname(os.getcwd())
    return path

def pixel_size(df,col):
    x= df.sort_values(col)
    return x.head()

import sys, os

