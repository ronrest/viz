import pandas as pd
import numpy as np

# import matplotlib as mpl
# mpl.use('TkAgg') # graphical external window
import matplotlib.pyplot as plt
import seaborn as sns

from . standard import lineplot
from . standard import barplot
from . standard import stepplot
from . standard import scatterplot

def create_figax(grid=(1,1), figsize=(10,6), title=""):
    fig, axes = plt.subplots(grid[0],grid[1], figsize=figsize)
    axes = np.array(axes).flatten()
    fig.suptitle(title, fontsize=15)
    plt.close()
    return fig, axes
