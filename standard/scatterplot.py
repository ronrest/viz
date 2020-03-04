from . import plt, pd, sns

def scatterplot(x, y, figsize=(10, 6), size=2, title="title", ax=None, color="#307EC7", label="", xlabel="x", ylabel="y", **kwargs):
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
        fig.suptitle(title, fontsize=15)
    else:
        fig = ax.get_figure()

    if y is None:
        y = pd.Series(x)
        x = y.index

    sns.scatterplot(x=x, y=y, size=size, **kwargs)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if label != "":
        ax.legend(loc="lower right", title="", frameon=False,  fontsize=8)
    # ax.set_aspect('equal')
    ax.grid(True, which='both')

    plt.close()
    return fig, ax
