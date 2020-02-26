from . import pd, np, plt, timeline_plot


def missing_timeline_plot(x, figsize=(10, 6), title="title", ax=None, color="#307EC7", label=""):
    """ Given a pandas timeseries, it plots a step plot of missing values """
    nulls = x.isnull()
    return timeline_plot(nulls, figsize=figsize, title=title, ax=ax, color=color, label=label, kind="step")


def missing_timeplineplot_df(df, figsize=(10, 6), title="missing timeline plots", ax=None, colors=None, overlayed=False):
    """ Given a pandas dataframe, with time index, it treats each column as a
        timeseries, and plots a step plot of missing values for each column.

        you have option of overlaying all the plots on a single cell, or
        creating a separate sub plot (one below the other) for each column.
    """
    if not overlayed:
        assert ax is None, "Can only pass an axis object if you are creating an overlayed plot"

    colors = ["red", "green", "blue", "orange", "pink", "black"] if colors is None else colors

    if overlayed:
        # OVERLAY ALL MISSING TIMELINE PLOTS ON THE SAME AXIS
        for i, column in enumerate(df.columns):
            fig, ax = missing_timeline_plot(df[column], figsize=figsize, title=title, ax=ax, color=colors[i%len(colors)], label=column)
    else:
        # SEPARATE SUBPLOTS FOR EACH MISSING TIMELINE PLOT
        columns = list(df.columns)
        fig, axes = plt.subplots(len(columns), 1, figsize=figsize)
        axes = axes.flatten()
        fig.suptitle(title, fontsize=15)

        for i, column in enumerate(df.columns):
            ax = axes[i]
            fig, ax = missing_timeline_plot(df[column], figsize=figsize, title=title, ax=ax, color=colors[i%len(colors)], label=column)
            ax.set_title(column)
            ax.set_ylim([0, 1.1])
        fig.tight_layout(pad=1.10,  rect=[0, 0.03, 1, 0.95])

    plt.close()
    return fig, ax
