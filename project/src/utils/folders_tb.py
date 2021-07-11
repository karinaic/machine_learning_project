import pandas as pd 
import numpy as np
import sys, os
from PIL import Image
import cv2


def curr_path():
    path = os.path.dirname(os.getcwd())
    return path

def pixel_size(df,col):
    x= df.sort_values(col)
    return x.head()


   

    

