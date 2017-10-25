import numpy as np


def simulate(num_timesteps, num_simulations, starting_price, mu, vol, dt, perc_selection):
    # Preallocation
    price = np.zeros((num_timesteps + 1, num_simulations))
    percentiles = np.zeros((num_timesteps + 1, 3))

    # Set initial values
    price[0, :] = starting_price
    percentiles[0, :] = starting_price

    # Simulation at each time step
    for t in range(1, num_timesteps + 1):
        rand_nums = np.random.randn(num_simulations)
        price[t, :] = price[t - 1, :] * np.exp((mu - 0.5 * vol ** 2) * dt + vol * rand_nums * np.sqrt(dt))
        # price[t, :] = price[t - 1, :] * np.exp((mu * (np.log(starting_price) - np.log(price[t - 1, :])) -
        #                                         0.5 * vol ** 2) * dt + vol * rand_nums * np.sqrt(dt))
        percentiles[t, :] = np.percentile(price[t, :], perc_selection)

    # Return percentiles and sample path
    return percentiles, price[:, :1]
