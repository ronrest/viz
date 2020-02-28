from scipy import stats
from . import pd, np, plt
from .. import lineplot

def normal_distribution_plot(mean, sd, figsize=(10, 6), title="distribution plot", ax=None, color="#307EC7", label=""):
    mu = mean
    sigma = sd
    x = np.linspace(mu-3*sigma, mu+3*sigma, 100)
    y = stats.norm.pdf(x, loc=mu, scale=sigma)
    x = pd.Series(y, index=x)
    fig, ax = lineplot(x, figsize=figsize, title=title, ax=ax, color=color, label=label)
    return fig, ax
