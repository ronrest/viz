from . import pd, np, plt


def timeline_plot(x, figsize=(10, 6), title="plot", ax=None, color="#307EC7", label="", kind="line", t1=None, t2=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
        fig.suptitle(title, fontsize=15)
    else:
        fig = ax.get_figure()

    x = x[t1:t2]

    if kind == "step":
        ax.step(x.index, x, where="post", color=color,  label=label)
    elif kind == "line":
        ax.plot(x.index, x, color=color,  label=label)
    elif kind == "scatter":
        ax.scatter(x, y, color=color)
    else:
        raise AssertionError("kind argument must be one of [step, line, scatter]")

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="lower right", title="", frameon=False,  fontsize=8)
    ax.grid(True, which='both')
    plt.close()
    return fig, ax


def timeline_stepplot(x, figsize=(10, 6), title="plot", ax=None, color="#307EC7", label=""):
    return timeline_plot(x, figsize=figsize, title=title, ax=ax, color=color, label=label, kind="step")
