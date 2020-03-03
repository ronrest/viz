from . import plt, sns, np
import matplotlib

# import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
# import seaborn as sns
def scatter_and_correlation_matrix(df, figsize=(8,8), category = None, cor_text_color="#333333", cor_fontsize=10, corr_cmap="coolwarm", scatter_size=None, kde=True, hist=True, bins=None, cell_spacing=(0, 0)):
    """ Create a matrix plot with of the columns in df with the following:
        1.  Lower triangle contains scatter plots of the columns against each
            other
        2.  Diagonal contains density plot and histogram of columns
        3.  Upper triangle contains correlation heatmap of each column against
            the other columns.

    Args:
        df:             (pandas dataframe)
        figsize:        (tuple of 2 numbers)(default=(8,8)) matplotlib figsize,
        category :      (str) which column to use as categorical variable for
                        splitting the data up into different colors
        cor_text_color: (str)(default="#333333") color of correlation plot labels
        cor_fontsize:   (int)(default=10) fontsize of correlation plot labels
        corr_cmap:      (str)(default="coolwarm") matplotlib colormap name for
                        heatmap
        scatter_size:   (str)(default=None) name of column to use for setting
                        scatterplot size
        kde:            (bool)(default=True) Show Density plot on diagonal?
        hist:           (bool)(default=True) Show histogram on diagonal?
        bins:           (int)(default=None) Number of bins for histogram
        cell_spacing:   (tuple of 2 numbers)(default=(0, 0))
                        How much spacing (x, y) between each subplot
    """
    # CORRELATION
    cors = df.corr()
    shape = cors.shape
    columns = df.columns

    # COLOR MAPPER
    cmapper_norm = matplotlib.colors.Normalize(vmin=-1, vmax=1, clip=True)
    cmapper = matplotlib.cm.ScalarMappable(norm=cmapper_norm, cmap=corr_cmap)

    # INITIALIZE FIGURE
    fig, axes = plt.subplots(shape[0], shape[1], figsize=figsize)
    fig.subplots_adjust(wspace=cell_spacing[0], hspace=cell_spacing[1])

    # CORRELATION HEAT PLOTS
    idxs = np.triu_indices_from(cors, 1)
    for i,j in zip(*idxs):
        ax = axes[i,j]
        cor_val = cors.iloc[i, j]
        color = cmapper.to_rgba(cor_val)

        # Set background color of correlation cell, and text
        ax.set_facecolor(color)
        ax.text(0.5, 0.5, f"{cor_val:0.2f}", horizontalalignment="center", verticalalignment="center", fontsize=cor_fontsize, color=cor_text_color, transform=ax.transAxes)

        # Set aesthetics
        ax.set_xticks([], minor=[])
        ax.set_yticks([], minor=[])


    # SCATTER PLOTS
    idxs = np.tril_indices_from(cors, -1)
    for i,j in zip(*idxs):
        ax = axes[i,j]
        # color = colors[i,j]
        sns.scatterplot(df.iloc[:,j], df.iloc[:,i], hue=category, size=scatter_size, marker=".", ax=ax, linewidth=0, edgecolor="#000000", alpha=0.3)

        # Add Grid
        ax.grid(True)
        ax.minorticks_on()
        ax.grid(b=True, which='major', color='#999999', linestyle='-', linewidth=1)
        ax.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.7, linewidth=0.5)


    # DIAGONAL HISTOGRAM AND KDE
    idxs = np.diag_indices_from(cors)
    for i,j in zip(*idxs):
        ax = axes[i,j]
        sns.distplot(df.iloc[:,i], ax=ax, hist=hist, kde=kde, bins=bins)
        ax.set_xticks([], minor=[])
        ax.set_yticks([], minor=[])
        ax.set_xlabel(None)


    # SET GLOBAL SETTINGS FOR AXES
    for ax in axes.flatten():
        # Spines
        # ax.spines['top'].set_color("#999999")
        # ax.spines['right'].set_color("#999999")
        # ax.spines['bottom'].set_color("#999999")
        # ax.spines['left'].set_color("#999999")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        # ax.set_aspect('equal')

        # Ticks and tick labels
        ax.tick_params(axis="both", which="both", length=0, width=0, pad=0)
        ax.yaxis.set_ticklabels([])
        ax.xaxis.set_ticklabels([])

        # Axis labels
        ax.set_xlabel(None)
        ax.set_ylabel(None)
        ax.margins(x=0,y=0)

        # Margins
        # ax.margins(x=0,y=0, tight=True)

    # SETTINGS FOR LEFT AND LOWER AXES LABELS
    # for col, ax in zip(df.columns, axes[-1,:]):
    for i in range(len(columns)):
        col = columns[i]
        axes[i, 0].set_ylabel(col)
        axes[len(columns)-1, i].set_xlabel(col)

    # FINALIZE
    plt.close()
    return fig, axes
