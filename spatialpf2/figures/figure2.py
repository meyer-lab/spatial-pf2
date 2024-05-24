"""
Spatial CC: 
"""

from .common import getSetup
from ..imports import import_HTAN
from ..factorization import pf2
from .commonFuncs.plotFactors import (
    bot_top_genes
)
import pandas as pd


def makeFigure():
    ax, f = getSetup((10, 12), (4, 5))

    rank = 20
    X = import_HTAN()

    X = pf2(X, rank, doEmbedding=False)

    for i in range(rank):
        genes = bot_top_genes(X, i+1)
        df = pd.DataFrame(
            data=X.varm["Pf2_C"][:, i], index=X.var_names, columns=["Component"]
        )
        ax[i].barh(genes, df.loc[genes, "Component"])

    return f
