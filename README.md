# Simulation Demo with xlwings and Flask

This demo shows how Excel with [xlwings](http://xlwings.org) can be used to create rapid prototypes for
web apps.

The code for the actual simulation (`simulation.py`) is used unaltered both by the xlwings app (`xlwings_app.py` &
`simulation.xlsm`) and the web app (`web_app.py` & the folders `static` and `templates`).

You need to have the Python packages installed as listed in `requirements.txt`. You also need the xlwings Excel add-in installed and have a reference set to xlwings under VBA Editor > Tools > References...

To run the apps:

* xlwings:

  Open Excel, then click the `Run` button. It will use the settings from your xlwings Excel add-in.
  
* Flask web app:

  Run `python web_app.py`, then open your browser at `localhost:5002`
  
  
  
![](screenshot.png)