import numpy as np

def NewtonRaphson(f, df, x0, tol, max_iter):
    x_old = x0
    for _ in range(max_iter):
        x_new = x_old - f(x_old)/df(x_old)
        if abs(x_new - x_old) < tol:
            return x_new
        x_old = x_new
    print("Maximum number of iterations exceeded")
    return x_new

