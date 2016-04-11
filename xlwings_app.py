from __future__ import division
import os
import numpy as np
import xlwings as xw
from simulation import simulate


def run_simulation():
    wb = xw.Workbook.caller()

    # User Inputs
    num_simulations = xw.Range('E3').options(numbers=int).value
    time_horizon = xw.Range('E4').value
    num_timesteps = xw.Range('E5').options(numbers=int).value
    dt = time_horizon / num_timesteps  # Length of time period
    vol = xw.Range('E7').value
    mu = np.log(1 + xw.Range('E6').value)  # Drift
    starting_price = xw.Range('E8').value
    perc_selection = [5, 50, 95]

    # Excel: clear output, write out initial values of percentiles/sample path and set chart source and x-axis values
    xw.Range('O2').table.clear_contents()
    xw.Range('P2').value = [starting_price, starting_price, starting_price, starting_price, perc_selection]
    xw.Chart('Chart 5').set_source_data(xw.Range((1, 15), (num_timesteps + 2, 19)))
    xw.Range('O2').value = np.round(np.linspace(0, time_horizon, num_timesteps + 1).reshape(-1, 1), 2)

    percentiles, sample_path = simulate(num_timesteps, num_simulations, starting_price, mu, vol, dt, perc_selection)

    xw.Range('P2').value = percentiles
    xw.Range('S2').value = sample_path

if __name__ == '__main__':
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'simulation.xlsm'))
    xw.Workbook.set_mock_caller(path)
    run_simulation()
