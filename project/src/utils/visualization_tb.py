import seaborn as sns
import matplotlib.pyplot as plt 
import os, sys


def frequency_class(df):
    c = df['ClassId'].nunique()
    x = df['ClassId'].value_counts()
    plt.bar(x=x.index.sort_values(), height=x, color='hotpink')
    plt.title('Numbers of sample in each class', color='black')
    plt.xlabel("Class ID", color='black')
    plt.ylabel("Samples", color='black')
    plt.tick_params(colors='black')

    





