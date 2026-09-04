# import modules
import math
import random
import numpy as np


# function to simulate one stock path
def simulate_path(S0, r, sigma, T, steps):
    """
    Function to
    Args:
        S0 (float): current stock price
        r (float): risk free interest rate
        sigma (float): volatility
        T (int): time-scale
        steps (int):
    Returns:
        S (): simulated stock prices from t = 0-T
    """
    dt = T / steps
    stock_price = [S0]

    for i in range(steps):
        # generate random normal values
        Z = np.random.normal(loc=0.0, scale=1.0, size=None)
        # apply Geometric Brownian Motion formula
        S = stock_price[-1]*math.exp((r - 0.5*sigma**2)*dt + sigma*math.sqrt(dt)*Z)
        # store new stock price
        stock_price.append(S)

    return stock_price

# test function
path = simulate_path(100, 0.05, 0.2, 1, 252)

print(len(path))
print(path[:5])
print(path[-1])
