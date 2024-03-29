
#Script to check if the implementations work on random data.
#We do not give this to the teachers

import numpy as np
from helpers import *
from implementations import *
from cross_validation import *

#### 
from sklearn import datasets #Not allowed
from sklearn.linear_model import LogisticRegression, LinearRegression  #Not allowed
from sklearn.linear_model import Ridge
from sklearn.metrics import accuracy_score #Not allowed
from sklearn.metrics import r2_score #Not allowed

np.seterr(divide = 'ignore') 

# =============================================================================
# Linear Regression 
# =============================================================================

# Load LR data
X, y = datasets.load_boston(return_X_y=True)
X = normalize(X)
# Add columns of 1's for bias term 
tx = np.c_[np.ones(X.shape[0]), X]

# Initalize paramaters
initial_w = np.zeros(tx.shape[1])
max_it = 500
gamma = 0.05


print("---------------------- \n Linear Regression \n---------------------")

# #  LR w/ GD.
w, loss = least_squares_GD(y, tx, initial_w,
                            max_it, gamma, verbose=False)
y_pred = tx @ w
print(f"GD --> Our implementation r_sq: {r_squared(y, y_pred)}, loss : {mse(y, tx, w)}")

# Sklearn LR.
reg = LinearRegression().fit(X, y)
y_pred = reg.predict(X)
print(f"Sklearn implementation r_sq: {r_squared(y, y_pred)}, sklearn loss {mse(y, tx, np.r_[reg.intercept_, reg.coef_])}")


# LR w/ SGD

w, loss = least_squares_SGD(y, tx, initial_w,
                      max_it*5, gamma, verbose = False)
y_pred = tx @ w
print(f"SGD --> Our implementation r_sq: {r_squared(y, y_pred)}, loss : {mse(y, tx, w)}")

# LR w/ normal equations
w, loss = least_squares(y, tx)
y_pred = tx @ w
print(f"EQ --> r_sq: {r_squared(y, y_pred)}, loss : {mse(y, tx, w)}")


print("----------\nRidge regression\n-----------")

# Ridge regression w/ Sklearn equations
y_pred = Ridge(alpha=1.0).fit(X, y).predict(X)
print("Sklearn ridge regression r2", r_squared(y, y_pred))

# Ridge regression
lw, loss = ridge_regression(y, tx, lambda_= 1.)
y_pred = tx @ w
print("Our implementation ridge r2", r_squared(y, y_pred))


print("\n\t\t-------------------------\n")
print("\t\t-------------------------\n")
print("\t\t-------------------------\n")

print("---------------------- \n Logistic Regression \n---------------------")


# =============================================================================
# Logistic Regression
# =============================================================================

X, y = datasets.load_breast_cancer(return_X_y = True)

# Normalize data
scaled_X = normalize(X)
# Add column of 1's for bias term
tx = np.c_[np.ones(X.shape[0]), scaled_X]
# Set parameters
initial_w = np.zeros(tx.shape[1])
max_it = 100
gamma = 0.7
# Gradient descent
w, loss = logistic_regression(y, tx, initial_w, max_it, gamma)
# Predit in sample
y_pred = np.rint(sigmoid(tx @ w))

print(f"GD --> Our implementation accuracy: {accuracy(y, y_pred)}")

# Check with the sklearn implementation

clf = LogisticRegression().fit(scaled_X,y)
print("Sklearn implementation accuracy: ",accuracy_score(y, clf.predict(scaled_X)))

# Stochastic gradient descent logistic regression.
w, loss = logistic_regression(y, tx, initial_w, max_it, gamma, batch_size=1)
y_pred = np.rint(sigmoid(tx @ w))
print(f"SGD --> Our implementation accuracy: {accuracy(y, y_pred)}")


print("---------- \nRegularized\n----------")

# Logistic regression with regularization
lambda_ = 0.02
reg = 2 # -> L2 or L1 regularization.
w, loss = reg_logistic_regression(y, tx, lambda_, reg, initial_w,
                                  max_it, gamma, verbose=True)
y_pred = np.rint(sigmoid(tx @ w))
print(f"GD --> Regularized implementation accuracy: {accuracy(y, y_pred):.4f}")


# Sklearn
rlr = LogisticRegression(penalty = "l2", C = 1/lambda_, max_iter = 10000).fit(scaled_X, y)
y_pred = rlr.predict(scaled_X)
print(f"Sklearn regularized logistic regression : {accuracy(y,y_pred):.4f}")