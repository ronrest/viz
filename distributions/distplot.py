from . import plt, sns, pd, np

def distplot(x, figsize=(10, 6), bins=None, title="title", ax=None, color="steelblue", label="KDE", xlabel="x", ylabel="density", legend_pos="lower right", **kwargs):
    # potentially embed in another figure
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
        fig.suptitle(title, fontsize=15)
    else:
        fig = ax.get_figure()

    # distplot requires that all values be non-null
    x = pd.Series(x)
    x = x[x.notnull()]


    # Settings
    kde_kws = dict({"color": color, "lw": 2, "label": label}, **(kwargs.get("kde_kws", {})))
    hist_kws=dict({"histtype": "step", "linewidth": 1, "alpha": 0.5, "color": color}, **(kwargs.get("hist_kws", {})))
    for key in ["kde_kws", "hist_kws"]:
        try:
            kwargs.pop(key)
        except:
            pass

    # plot
    sns.set_style('whitegrid')
    ax = sns.distplot(x,
        # rug=True, rug_kws={"color": color}, # Show rugplot
        bins=bins,
        kde_kws=kde_kws,
        hist_kws=hist_kws,
        ax=ax,
        **kwargs
        )

    # format
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(loc=legend_pos, title="", frameon=False,  fontsize=8)
    # ax.set_aspect('equal')
    # ax.grid(True, which='both')

    plt.close()
    return fig, ax
