from . import pd, np, sns, plt


def heatmap(x, figsize=(10,8), title="heatmap", mask=None, vmin=None, vmax=None, center=None, square=True, ax=None, cmap="Blues", annot=True, xlabel="", ylabel="", **kwargs):
    """ Plots a heatmap

    Args:
        x:      (np array or pd dataframe) values to use for heatmap
        figsize:(tuple) matplotlib figure size
        title:  (str)
        mask:   (np array) same dimensions as x, with a 1/True to mask out particular
                cells.
        vmin, vmax: (float) min and max values (for purposes of colormapping)
        center: (float) central value (for purposes of divergent colormapping)
        square: (bool) square cells?
        ax:     (matplotlib axis) optional existing axis object
        annnot: (bool) should the values be annotated on each cell?
        cmap:   (str) a matplotlib colormap name
                https://matplotlib.org/tutorials/colors/colormaps.html
                Some useful ones:
                    Greys, Blues, Purples, Reds, BuPu, YlGn, Reds, YlOrRd,
                    YlOrBr, OrRd, Blues, hot, afmhot, plasma, autumn
                    coolwarm, RdYlBu, RdBu
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
        fig.suptitle(title)
    else:
        fig = ax.get_figure()


    ax = sns.heatmap(x, mask=mask, vmin=vmin, vmax=vmax, square=square, ax=ax, annot=annot, center=center, cmap=cmap, **kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.close()
    return fig, ax


def correlation_heatmap(df, figsize=(10,6), title="Correlation heatmap", ax=None, side="both", diagonal=True, cmap="coolwarm", annot=True):
    """ Plots a correlation heatmap of all the columns in a dataframe.
        You can optionally chose if you want to
        show just the upper, or lower side. You can also optionally not show
        values along the diagonal.

    Args:
        df:     (pandas dataframe) dataframe
        ax:     (matplotlib axis) optional existing axis object
        side:   (str)
                - both
                - lower
                - upper
        diagonal: (bool) show the diagonal values?
        cmap:   (str) a matplotlib colormap name
                https://matplotlib.org/tutorials/colors/colormaps.html
    """
    corr = df.corr()
    # corr = np.corrcoef(df)
    mask = np.zeros_like(corr)

    # CREATE A MASK FOR WHICH SIDE
    if side == "lower":
        mask[np.triu_indices_from(mask)] = True
    elif side == "upper":
        mask[np.tril_indices_from(mask)] = True
    elif side == "both":
        None
    else:
        raise AssertionError("side argument must be one of [lower, upper, both]")

    # MASK FOR DIAGONAL
    if not diagonal:
        mask[np.diag_indices_from(mask)] = True


    with sns.axes_style("white"):
        if ax is None:
            fig, ax = plt.subplots(figsize=figsize)
            fig.suptitle(title)
        else:
            fig = ax.get_figure()
        ax = sns.heatmap(corr, mask=mask, vmin=-1, vmax=1., square=True, ax=ax, annot=annot, center=0, cmap=cmap)
        # fig.tight_layout(pad=1.10,  rect=[0, 0.03, 1, 0.95])
    plt.close()
    return fig, ax
