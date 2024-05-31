"""
Spatial CC: 
"""

from .common import getSetup
from ..imports import import_HTAN
from ..factorization import pf2
from .commonFuncs.plotFactors import (
    plot_gene_factors_partial
)
import pandas as pd


def makeFigure():
    ax, f = getSetup((10, 12), (8, 5))

    rank = 20
    X = import_HTAN()

    X = pf2(X, rank, doEmbedding=False)

    for i in range(rank):
        plot_gene_factors_partial(i + 1, X, ax[i])
        ax[i].set(title=f"Component {i+1}")
        ax[i].set_xlabel("Gene")
        ax[i].set_ylabel("Weight")

    for i in range(rank, 2 * rank):
        plot_gene_factors_partial(i - rank + 1, X, ax[i], top=False)
        ax[i].set(title=f"Component {i - rank + 1}")
        ax[i].set_xlabel("Gene")
        ax[i].set_ylabel("Weight")

    return f
