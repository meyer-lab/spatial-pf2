import glob
from concurrent.futures import ProcessPoolExecutor
import numpy as np
import anndata
import scanpy as sc
from scipy.sparse import spmatrix
from sklearn.utils.sparsefuncs import inplace_column_scale, mean_variance_axis


def prepare_dataset(
    X: anndata.AnnData, condition_name: str, geneThreshold: float
) -> anndata.AnnData:
    assert isinstance(X.X, spmatrix)
    assert np.amin(X.X.data) >= 0.0  # type: ignore

    # Filter out genes with too few reads
    readmean, _ = mean_variance_axis(X.X, axis=0)  # type: ignore
    X = X[:, readmean > geneThreshold]

    # Normalize read depth
    sc.pp.normalize_total(X, exclude_highly_expressed=False, inplace=True)

    # Scale genes by sum
    readmean, _ = mean_variance_axis(X.X, axis=0)  # type: ignore
    readsum = X.shape[0] * readmean
    inplace_column_scale(X.X, 1.0 / readsum)

    # Transform values
    X.X.data = np.log10((1000.0 * X.X.data) + 1.0)  # type: ignore

    # Get the indices for subsetting the data
    _, sgIndex = np.unique(X.obs_vector(condition_name), return_inverse=True)
    X.obs["condition_unique_idxs"] = sgIndex

    # Pre-calculate gene means
    means, _ = mean_variance_axis(X.X, axis=0)  # type: ignore
    X.var["means"] = means

    return X


def import_HTAN() -> anndata.AnnData:
    """Imports Vanderbilt's HTAN 10X data."""
    files = glob.glob("/opt/extra-storage/HTAN/*.mtx.gz")
    futures = []
    data = {}

    with ProcessPoolExecutor(max_workers=10) as executor:
        for filename in files:
            future = executor.submit(
                sc.read_10x_mtx,
                "/opt/extra-storage/HTAN/",
                gex_only=False,
                make_unique=True,
                prefix=filename.split("/")[-1].split("matrix.")[0],
            )
            futures.append(future)

        for i, k in enumerate(files):
            result = futures[i].result()
            data[k.split("/")[-1].split("_matrix.")[0]] = result

    X = anndata.concat(data, merge="same", label="Condition")

    return prepare_dataset(X, "Condition", geneThreshold=0.1)
