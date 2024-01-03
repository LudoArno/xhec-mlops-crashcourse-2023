import numpy as np
import pandas as pd
import scipy.sparse
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from typing import Optional
from prefect import task


@task
def train_model(X: scipy.sparse.csr_matrix, y: np.ndarray) -> LinearRegression:
    lr = LinearRegression()
    lr.fit(X,y)
    return lr

@task
def predict(X: scipy.sparse.csr_matrix, model: LinearRegression) -> np.ndarray:
    return model.predict(X)

@task
def evaluate_model(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return mean_squared_error(y_true, y_pred)