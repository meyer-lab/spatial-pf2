"""
PaCMAP of Weighted Projections based on Pf2
"""

from ..imports import import_HTAN
from .common import subplotLabel, getSetup
from .commonFuncs.plotPaCMAP import plot_wp_pacmap
from ..factorization import pf2


def makeFigure():
    ax, f = getSetup((12, 10), (5, 4))
    subplotLabel(ax)

    X = import_HTAN()

    rank = 20
    X = pf2(X, rank, doEmbedding=True)

    for i in range(1, 21):
        plot_wp_pacmap(X, i, ax[i - 1], cbarMax=0.25)

    return f