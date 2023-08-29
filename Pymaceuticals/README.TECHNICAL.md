Pymaceuticals.ipynb uses the CSV files, MouseMetaData.csv and StudyResults.csv, as input and will not run without them.  
The interactive Python notebook requires the following Python scripts in the same folder with it:

PyConstants.py

PyFunctions.py

PyLogConstants.py

PyLogFunctions.py

PyLogSubRoutines.py

PymaceuticalsFunctions.py

PymaceuticalsSubRoutines.py

PySubroutines.py

If the computer has Anaconda and a recent version of Python, the Jupyter notebook already has the following dependencies 
installed: datetime, io, pandas, pathlib, os, pandas, requests.

In addition to those modules, the Jupyter Notebook needs the following to execute: hvplot, matplotlib, numpy, panel, requests_html, scipy.

Here are the requisite Terminal commands for installation of these peripheral modules:

python3 -m pip install hvplot

python3 -m pip install matplotlib

python3 -m pip install numpy

python3 -m pip install panel

python3 -m pip install requests_html

python3 -m pip install scipy

If the folders, Resources, Logs, and Images are not present, the Jupyter Notebook will create them.  To place the Jupyter 
Notebook in log mode, debug mode, or image mode set the parameter for the appropriate subroutine in cell #2 to True.  In 
debug mode, the program displays the debug information and writes it to a debug file in the Logs folder; the same is true 
in log mode for log information sent to a log file in the same folder.  If the program is in log mode but not debug mode, 
it displays no debug information, but writes that information to the log file. If the program is in image mode, it writes 
all the plots to png files in the Images folder.
