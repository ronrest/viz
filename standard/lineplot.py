from . import plt

def lineplot(x, figsize=(10, 6), title="title", ax=None, color="#307EC7", label=""):
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
        fig.suptitle(title, fontsize=15)
    else:
        fig = ax.get_figure()

    ax.plot(x, color=color,  label=label)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="lower right", title="", frameon=False,  fontsize=8)
    # ax.set_aspect('equal')
    ax.grid(True, which='both')

    plt.close()
    return fig, ax
