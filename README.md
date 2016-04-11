# Simulation Demo with xlwings and Flask

This demo shows how Excel with [xlwings](http://xlwings.org) can be used to create rapid prototypes for
web apps.

The code for the actual simulation (`simulation.py`) is used unaltered both by the xlwings app (`xlwings_app.py` &
`simulation.xlsm`) and the web app (`web_app.py` & the folders `static` and `templates`).

You need to have the Python packages installed as listed in `requirements.txt`.

To run the apps:

* xlwings:

  Open Excel, then click the `Run` button. If you don't want to use your default Python installation (e.g. because
  you're using a virtualenv or a conda environment), then you will need to point the Python interpreter to this
  interpreter by changing `PYTHON_WIN` or `PYTHON_MAC` in the xlwings VBA settings, respectively.
  
* Flask web app:

  Run `python web_app.py`, then open your browser at `localhost:5002`
  
  
  
![](screenshot.png)