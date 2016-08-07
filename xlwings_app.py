from __future__ import division
import numpy as np
import xlwings as xw
from simulation import simulate


def run_simulation():
    sht = xw.Book.caller().sheets[0]

    # User Inputs
    num_simulations = sht.range('E3').options(numbers=int).value
    time_horizon = sht.range('E4').value
    num_timesteps = sht.range('E5').options(numbers=int).value
    dt = time_horizon / num_timesteps  # Length of time period
    vol = sht.range('E7').value
    mu = np.log(1 + sht.range('E6').value)  # Drift
    starting_price = sht.range('E8').value
    perc_selection = [5, 50, 95]

    # Excel: clear output, write out initial values of percentiles/sample path and set chart source and x-axis values
    sht.range('O2').expand().clear_contents()
    sht.range('P2').value = [starting_price, starting_price, starting_price, starting_price, perc_selection]
    sht.charts['Chart 5'].set_source_data(sht.range((1, 15), (num_timesteps + 2, 19)))
    sht.range('O2').value = np.round(np.linspace(0, time_horizon, num_timesteps + 1).reshape(-1, 1), 2)

    percentiles, sample_path = simulate(num_timesteps, num_simulations, starting_price, mu, vol, dt, perc_selection)

    sht.range('P2').value = percentiles
    sht.range('S2').value = sample_path

if __name__ == '__main__':
    xw.Book('simulation.xlsm').set_mock_caller()
    run_simulation()
