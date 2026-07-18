import numpy as np

def impute(X, method="mean"):
    """
    Returns: 2D list with NaN values replaced using the specified method
    """
    X = np.asarray(X, dtype=float)

    if X.ndim == 1:
        X = X.reshape(-1, 1)
    X[X == "nan"] = np.nan
    X = X.astype(float)

    if method == "mean":
        for col in range(X.shape[1]):
            fill_0 = np.nan_to_num(np.nanmean(X[:, col]), nan=0)
            X[:, col] = np.nan_to_num(X[:, col], nan=fill_0)
        
    else:
        for col in range(X.shape[1]):
            fill_0 = np.nan_to_num(np.nanmedian(X[:, col]), nan=0)
            X[:, col] = np.nan_to_num(X[:, col], nan=fill_0)

    return X