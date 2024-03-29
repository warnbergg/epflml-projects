import numpy as np
from helpers import standardize_numpy

def import_data(path):
    """
    Import csv files and return array of X,y and vector of the column names.
    """
    train = np.loadtxt(
        f"{path}/data/train.csv",
        delimiter = ",",
        skiprows=0,
        dtype=str
    )

    test = np.loadtxt(
        f"{path}/data/test.csv",
        delimiter = ",",
        skiprows=0,
        dtype=str
    )

    col_names = train[0,:]

    # Remove column names
    train = np.delete(train, obj=0, axis=0)
    test = np.delete(test, obj=0, axis=0)

    # Map 0 & 1 to label
    label_idx = np.where(col_names == "Prediction")[0][0]
    train[:,label_idx] = np.where(train[:,label_idx]=="s", 1, 0)

    test[:,label_idx] = 0

    # Replace -999 with nan
    train = train.astype(np.float32)
    train[train == -999] = np.nan

    test = test.astype(np.float32)
    test[test == -999] = np.nan
    return train, test, col_names

def build_poly(x, degree):
    """polynomial basis functions for each column of x, for j=1 up to j=degree, and single constant term."""
    if (degree < 0): raise ValueError("degree must be positive")

    phi = np.empty((x.shape[0], x.shape[1]*degree+1))

    # Constant term
    phi[:,-1] = 1

    # Higher order terms
    for j in range(x.shape[1]):
        phi[:,j*degree] = x[:,j]
        for d in range(1,degree):
            col = j*degree+d
            phi[:,col] = phi[:,col-1] * x[:,j]

    return phi

def prepare_feautres(tx_nan, degree, mean_nan=None, mean=None, std=None):
    # Get column means, if necessary
    if mean_nan is None: mean_nan = np.nanmean(tx_nan,axis=0)

    # Replace NaNs
    tx_val = np.where(np.isnan(tx_nan), mean_nan, tx_nan)

    # Polynomial features
    tx = build_poly(tx_val, degree)
    const_col = tx.shape[1]-1

    # Add NaN indicator columns
    nan_cols = np.flatnonzero(np.any(np.isnan(tx_nan), axis=0))

    ind_cols = np.empty((tx_nan.shape[0], nan_cols.shape[0]))
    ind_cols = np.where(np.isnan(tx_nan[:,nan_cols]), 1, 0)

    tx = np.c_[tx, ind_cols]

    # Standardize
    tx, mean, std = standardize_numpy(tx, mean, std)
    tx[:,const_col] = 1.0

    return tx, mean, std, mean_nan, nan_cols
