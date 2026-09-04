# import modules
import math
import random


# generate random normal values
def pseudo_norm():
    """
    According to the Central Limit Theorem a normalised summation of
    independent random variables will approach a normal distribution.
    The simplest demonstration of this is adding two dice together.
    Args:
        None
    Returns:
        (int):
    Generate a value between 1-100 in a normal distribution
    """
    count = 10
    values = sum([random.randint(1, 100) for x in range(count)])
    return round(values/count)


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
    # generate random normal values
    Z = pseudo_norm()
    # apply Geometric Brownian Motion formula
    S = S0*math.exp((r - 0.5*sigma**2)*dt + sigma*math.sqrt(dt)*Z)
    return S
