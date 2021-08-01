import numpy as np

def squaresumerror(W, b, X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    n = len(Y) # number of files
    m = X.shape()[0] # number of channels
    w = W
    x = X.reshape((m**2, n))
    return (np.linalg.norm(np.transpose(w)*x + b - np.transpose(Y))**2)