from __future__ import division
from flask import Flask, render_template, request
import json
from simulation import simulate
import numpy as np

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/run-simulation', methods=['POST'])
def run_simulation():
    data = request.get_json(force=True)

    # User Inputs
    num_simulations = int(data['num_simulations'])
    time_horizon = float(data['time_horizon'])
    num_timesteps = int(data['num_timesteps'])
    dt = time_horizon / num_timesteps  # Length of time period
    vol = float(data['vol']) / 100
    mu = np.log(1 + float(data['exp_simple_ret']) / 100)  # Drift
    starting_price = float(data['starting_price'])
    perc_selection = [5, 50, 95]

    percentiles, sample_path = simulate(num_timesteps, num_simulations, starting_price, mu, vol, dt, perc_selection)

    x = np.round(np.linspace(0, time_horizon, num_timesteps + 1), 2).tolist()

    data = [{'x': x, 'y': percentiles[:, i].tolist(),
             'name': '{0}th Percentile'.format(perc_selection[i]) if perc_selection[i] != 50 else 'Median'}
            for i in range(percentiles.shape[1])
            ]
    data.append({'x': x, 'y': sample_path.squeeze().tolist(), 'name': 'Sample Path'})

    return json.dumps(data)

if __name__ == '__main__':
    app.run(port=5002, debug=True)
