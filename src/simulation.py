# import modules
import math
import numpy as np
import matplotlib.pyplot as plt

# =============== SINGLE PATH =================


# function to simulate one stock path
def simulate_path(S0, r, sigma, T, steps):
    """
    Function to
    Args:
        S0 (float): current stock price
        r (float): risk free interest rate
        sigma (float): volatility
        T (int): time-scale
        steps (int): number of measurements in time period
    Returns:
        stock_price (array): simulated stock prices from t = 0-T
    """
    dt = T / steps
    stock_price = [S0]

    for i in range(steps):
        # generate random normal values
        Z = np.random.normal(loc=0.0, scale=1.0, size=None)
        # apply Geometric Brownian Motion formula
        S = stock_price[-1] * math.exp(
            (r - 0.5 * sigma**2) * dt + sigma * math.sqrt(dt) * Z
        )
        # store new stock price
        stock_price.append(S)

    return stock_price


# test function
path = simulate_path(100, 0.05, 0.2, 1, 252)

print(len(path))
print(path[:5])
print(path[-1])

# plot single stock path
ys = path
xs = [x for x in range(len(ys))]

plt.plot(xs, ys)
plt.show()
# close the plt object once done
plt.close()


# ============== MULTIPLE PATHS ================
# create function to simulate multiple paths
def simulate_paths(S0, r, sigma, T, steps, simulations):
    """

    Args:
        S0 (float): current stock price
        r (float): risk free interest rate
        sigma (float): volatility
        T (int): time-scale
        steps (int): number of measurements in time period
        simulations (int): number of stock sims
    Returns:
    stock_path (list): simulated stock price paths
    """
    stock_path = []

    for i in range(simulations):
        # call simulate path function
        one_path = simulate_path(S0, r, sigma, T, steps)
        # store path in list of paths
        stock_path.append(one_path)

    return stock_path


# test function
paths = simulate_paths(100, 0.05, 0.2, 1, 252, 10)

print(len(paths))
print(len(paths[0]))

# plot 10 paths
x = np.arange(len(paths[0]))

for i in paths:
    plt.plot(x, i)

plt.ylabel("Stock Price")
plt.xlabel("Time")
plt.title("Stock price vs time for 10 simulations")

plt.savefig('./figures/10_GBM_paths.png')
plt.show()
