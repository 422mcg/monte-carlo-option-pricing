# import modules
import math

# generate random normal values
"""
According to the Central Limit Theorem a normalised summation of independent random variables
will approach a normal distribution. The simplest demonstration of this is adding two dice together.
"""
def pseudo_norm():
    """
    Args:
        None
    Returns:
        (int): 
    Generate a value between 1-100 in a normal distribution
    """
    count = 10
    values =  sum([random.randint(1, 100) for x in range(count)])
    return round(values/count)

# function to simulate one stock path
def simulate_path(S0, r, sigma, T, steps):
    dt = T / steps
    # generate random normal values
    Z = pseudo_norm()
    S = S0*math.exp((r - 0.5*sigma**2)*dt + sigma*math.sqrt(dt)*Z)
    return S
