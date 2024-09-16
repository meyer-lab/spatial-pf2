"""
Spatial CC: 
"""

from .common import getSetup
from ..imports import import_HTAN
from ..factorization import pf2
from .commonFuncs.plotFactors import (
    plot_condition_factors,
    plot_eigenstate_factors,
    plot_gene_factors,
    plot_factor_weight,
)


def makeFigure():
    ax, f = getSetup((10, 12), (2, 2))
    
    rank = 2
    X = import_HTAN()

    X = pf2(X, rank, doEmbedding=False)

    plot_condition_factors(X, ax[0])
    plot_eigenstate_factors(X, ax[1])
    plot_gene_factors(X, ax[2])
    plot_factor_weight(X, ax[3])

    return f
