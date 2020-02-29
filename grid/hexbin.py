from . import plt

# import matplotlib.pyplot as plt
def hexbin_plot(x, y, z=None, bins=None, vmin=None, vmax=None, gridsize=100, mincount=None, xylimits=None, xscale="linear", yscale="linear", cmap="inferno", figsize=(10, 6), title="hexbin plot", ax=None, **kwargs):
    """ Creates a Hexbin Plot
    x, y:       (iterables) the x and y arrays
    z:          (None or iterable)
                None     = each x,y point will have a weight of 1.
                iterable = assigns the value each x,y point will have.
    bins:       (None, "log", int, list of floats) Control how binning is done, and how many
                None  = No binning
                "log" = Use log scale for colormap (log10)
                int   = number of bins to use
                list  = the values are used as the lower bounds of the bins

    cmap:       (str) matplotlib colormap. (default = "inferno")
                https://matplotlib.org/tutorials/colors/colormaps.html
                Useful values: "inferno" "GnBu"
    vmin:       (None or float) Set min value for color range
    vmax:       (None or float) Set max value for color range
    xscale:     (str) ("linear" or "log") type of scaling along x axis
    yscale:     (str) ("linear" or "log") type of scaling along y axis
    mincount:   (None or int>0) Set how many points needed before displaying cell
    gridsize:   (int, or tuple of 2 ints) number of hex cells along each axis.
    xylimits:   (tuple or None) Set the x and y limit values for the region that
                will be covered by hexbins
                (left, right, bottom, top)

    figsize:    (tuple of two ints)
    title:      (str) title for plot
    ax:         (matplotlib axes object) Existing axes to embed this plot into
    **kwargs:   Aditional keyword args to pass to matplotlib.axes.Axes.hexbin()
                Some examples:
                norm=LogNorm()
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
        fig.suptitle(title, fontsize=15)
    else:
        fig = ax.get_figure()


    ax.hexbin(x, y, C=z, bins=bins, gridsize=gridsize, cmap=cmap, vmin=vmin, vmax=vmax, mincnt=mincount, extent=xylimits)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    # ax.legend(loc="lower right", title="", frameon=False,  fontsize=8)
    # ax.set_aspect('equal')
    ax.grid(True, which='both')

    plt.close()
    return fig, ax
