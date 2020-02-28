def add_text_to_ax(s, ax, pos, fontsize=20, color="#333333", align="center", valign="center"):
    """ Given an axis object, it writes some text to it"""
    ax.text(pos[0], pos[1], s,
            horizontalalignment=align,
            verticalalignment=valign,
            fontsize=fontsize, color=color,
            transform=ax.transAxes)
