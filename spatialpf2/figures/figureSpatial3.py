"""
PaCMAP of immune exclusion signature genes
"""
from ..imports import import_HTAN
from .common import subplotLabel, getSetup
from .commonFuncs.plotPaCMAP import plot_gene_pacmap
from ..factorization import pf2

def makeFigure():
    ax, f = getSetup((15, 8), (2, 4))

    subplotLabel(ax)

    X = import_HTAN()

    rank = 20
    X = pf2(X, rank, doEmbedding=True)

    # genes originate from epithelial cells
    plot_gene_pacmap("DDR1", "Pf2", X, ax[0])
    plot_gene_pacmap("TGFBI", "Pf2",  X, ax[1])
    plot_gene_pacmap("PAK4", "Pf2",  X, ax[2])
    plot_gene_pacmap("DPEP1", "Pf2",  X, ax[3])

    



    return f    
