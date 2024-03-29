
import numpy as np
from helpers import *
from gradients import *
from costs import *

def stochastic_gradient_descent(y, tx, initial_w,
                                batch_size, max_iters, gamma,
                                verbose = False):
    """
    Stochastic gradient descent for linear regression with mse loss.

    Parameters
    ----------
    y : Vector
        DESCRIPTION.
    tx : Array
        DESCRIPTION.
    initial_w : Vector
        DESCRIPTION.
    batch_size : Scalar
        DESCRIPTION.
    max_iters : Scalar
        DESCRIPTION.
    gamma : Scalar
        DESCRIPTION.
    verbose : Boolean, optional
        DESCRIPTION. The default is False.

    Returns
    -------
    losses : Vector
        Losses.
    ws : Vector
        Weights.

    """
    # Define parameters to store w and loss
    ws = [initial_w]
    losses = []
    w = initial_w
    for n_iter in range(max_iters):
        for minibatch_y, minibatch_tx in batch_iter(y, tx, batch_size):
            # Compute gradient and loss
            g = mse_grad(minibatch_y, minibatch_tx, w)
            loss = mse(minibatch_y, minibatch_tx, w)
            # Update the weights
            w = w - gamma * g
            w = w.ravel()
            # store w and loss
            ws.append(w)
            losses.append(loss)
            if verbose:
                print("Stochastic gradient descent({bi}/{ti}): loss={l}, w0={w0}, w1={w1}".format(
                    bi=n_iter, ti=max_iters - 1, l=loss, w0=w[0], w1=w[1]))

    return losses, ws

def stochastic_gradient_descent_logistic(y, tx, initial_w,
                                         batch_size, max_iters, gamma,
                                         verbose = False):
    """
    Stochastic gradient descent for logistic regression with logistic loss

    Parameters
    ----------
    y : Vector
        Output.
    tx : Array
        Input.
    initial_w : Vector
        Weights.
    batch_size : Scalar
        Batch size for SGD.
    max_iters : Scalar
        Max iterations.
    gamma : Scalar
        Learning rate.
    verbose : Boolean, optional
        Print each step or not. The default is False.

    Returns
    -------
    losses : Vector
        Loss at each iteration.
    ws : Vector
        Weight vector for each iteration.

    """
    # Define parameters to store w and loss

    ws = [initial_w]
    w = initial_w
    losses = []

    for n_iter in range(max_iters):
        for batch_y, batch_tx in batch_iter(y, tx, batch_size):
            # Compute gradient & loss
            g = logistic_grad(batch_y, batch_tx, w)
            loss = logistic_error(batch_y, batch_tx, w)
            # Update weights
            w = w - gamma * g
            w.ravel()
            # Store loss & weights
            ws.append(w)
            losses.append(loss)
            if verbose:
                print("Stochastic gradient descent({bi}/{ti}): loss={l}, w0={w0}, w1={w1}".format(
                    bi=n_iter, ti=max_iters - 1, l=loss, w0=w[0], w1=w[1]))
    return losses, ws
