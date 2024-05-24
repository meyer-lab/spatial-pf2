"""
PaCMAP of Conditions
"""

from ..imports import import_HTAN
from .common import subplotLabel, getSetup
import numpy as np
from .commonFuncs.plotPaCMAP import plot_labels_pacmap
from ..factorization import pf2

def makeFigure():
    ax, f = getSetup((8, 8), (1, 1))

    subplotLabel(ax)

    X = import_HTAN()

    rank = 20
    X = pf2(X, rank, doEmbedding=True)

    plot_labels_pacmap(X, "Condition", ax[0])


    return f    
