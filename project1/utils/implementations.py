import numpy as np

from gd import *
from sgd import *
from costs import *


def least_squares_GD(y, tx, initial_w,
                     max_it, gamma, verbose=False):
    """Linear Regression with Gradient Descent

    Uses Mean Squared Error as the loss function.
    """
    losses, ws = gradient_descent(
        y=y,
        tx=tx,
        initial_w=initial_w,
        max_iters=max_it,
        gamma=gamma,
        verbose=verbose
    )
    
    return ws[-1], losses[-1]


def least_squares_SGD(y, tx, initial_w,
                      max_iters, gamma, verbose=False):
    """Linear regression with Stochastic Gradient Descent (SGD)

    Current implementation uses Mean Squared Error as the loss.
    """
    # Use batch_size = 1 as per the project instructions.
    losses, ws = stochastic_gradient_descent(
        y=y,
        tx=tx,
        initial_w=initial_w,
        max_iters=max_iters,
        gamma=gamma,
        batch_size=1,
        verbose=verbose
    )

    return ws[-1], mse(y, tx, ws[-1])

def least_squares(y, tx):
    """Linear regression fit using normal equations."""
    a = tx.T @ tx
    b = tx.T @ y
    w = np.linalg.solve(a, b)
    loss = mse(y, tx, w)
    return w, loss

def ridge_regression(y, tx, lambda_):
    """ Ridge regression fit using normal equations """
    a = (tx.T @ tx) + lambda_*2*tx.shape[0] * np.eye(tx.shape[1])
    b = tx.T @ y
    w = np.linalg.solve(a, b)
    return w, mse(y, tx, w)


def logistic_regression(y, tx, initial_w, max_iters, 
                        gamma, batch_size=None, verbose=False):
    """ Logistic regression with gradient descent or stochastic gradient descent"""

    
    if batch_size:
        losses, ws = stochastic_gradient_descent_logistic(
            y=y,
            tx=tx,
            initial_w=initial_w,
            batch_size=batch_size,
            max_iters=max_iters,
            gamma=gamma,
            verbose=verbose
        )
    else:
        losses, ws = gradient_descent_logistic(
            y=y,
            tx=tx,
            initial_w=initial_w,
            max_iters=max_iters,
            gamma=gamma,
            verbose=verbose
        )
        
    return ws[-1], logistic_error(y, tx, ws[-1])


def reg_logistic_regression(y, tx, lambda_, reg, initial_w,
                            max_iters, gamma, verbose=False, 
                            early_stopping=True, tol = 0.0001, 
                            patience = 5):
    """ Regularized logistic regression with gradient descent"""

    losses, ws = reg_gradient_descent_logistic(
        y=y,
        tx=tx,
        initial_w=initial_w,
        max_iters=max_iters,
        gamma=gamma,
        lambda_=lambda_,
        reg=reg,
        verbose=verbose,
        early_stopping=early_stopping,
        tol=tol,
        patience=patience
    )
    
    return ws[-1], losses[-1]
