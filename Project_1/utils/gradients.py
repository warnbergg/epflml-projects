
import numpy as np
from helpers import *

def mse_grad(y, tx, w):
    """
    Compute gradient for mse loss

    Parameters
    ----------
    y : Vector
        Input.
    tx : Matrix
        Output.
    w : Vector
        Weights.

    Returns
    -------
    Vector of gradients.

    """
    e = y - tx @ w
    return (-1/tx.shape[0]) * tx.T @ e

def mae_grad(y, tx, w):
    """
    Compute subgradient for mae loss

    Parameters
    ----------
    y : Vector
        Input.
    tx : Matrix
        Output.
    w : Vector
        Weights.

    Returns
    -------
    Vector of gradients.

    """
    
    e = y - tx @ w
    return (-1/tx.shape[0]) * tx.T @ np.sign(e)

def logistic_grad(y, tx, w):
    """
    Compute gradient for logistic loss function

    Parameters
    ----------
    y : Vector
        Input.
    tx : Matrix
        Output.
    w : Vector
        Weights.

    Returns
    -------
    Vector of gradients.

    """
    
    e = sigmoid(tx @ w) - y
    return (1/tx.shape[0]) * tx.T @ e
    
    
