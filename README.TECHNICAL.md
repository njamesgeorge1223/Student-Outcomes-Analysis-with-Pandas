# **Student Outcomes Analysis with Pandas**

----

### **Installation:**

----

If the computer has Anaconda, Jupyter Notebook, and a recent version of Python, the IPython notebook already has the following dependencies installed: datetime, io, json, matplotlib, numpy, pandas, pathlib, os, pandas, requests, requests_html, and scipy.

In addition to those modules, the Jupyter Notebook requires the following to execute: holoviews, hvplot, geoviews, geopy, aspose-words, dataframe-image.

Here are the requisite Terminal commands for the installation of these peripheral modules:

python3 -m pip install holoviews

python3 -m pip install hvplot

python3 -m pip install geoviews

python3 -m pip install geopy

python3 -m pip install aspose-words

python3 -m pip install dataframe-image

----

### **Usage:**

----

The IPython notebook, PyCitySchools.ipynb, uses the CSV files, schoolsComplete.csv and studentsComplete.csv, as input and will not run without them.  The interactive Python notebook must have the following Python scripts in the same folder with it:

PyCitySchoolsConstants.py

PyConstants.py

PyFunctions.py

PyLogConstants.py

PyLogFunctions.py

PyLogSubRoutines.py

PySubroutines.py

If the folders, Resources, Logs, and Images are not present, the IPython notebook will create them.  The Resources folder holds input files for the IPython Notebook; the Logs folder contains debug and log files from testing the IPython Notebook; and the Images folder has the PNG image files of the IPython Notebook's tables and plots.

To place the IPython notebook in Log Mode, Debug Mode, or Image Mode set the parameter for the appropriate subroutine in coding cell #2 to True. In Debug Mode, the program displays the debug information and writes it to a debug file in the Logs folder; the same is true in Log Mode for log information sent to a log file. If the program is in Log Mode but NOT Debug Mode, it displays no debug information, but writes that information to the log file. If the program is in Image Mode, it writes all DataFrames, hvplot maps, and matplotlib plots to PNG files in the Images Folder.

----

### **Resource Summary:**

----

#### Source code

PyCitySchools.ipynb, PyCitySchoolsConstants.py, PyConstants.py, PyFunctions.py, PyLogConstants.py, PyLogFunctions.py, PyLogSubRoutines.py, PySubroutines.py

#### Input files

schoolsComplete.csv, studentsComplete.csv

#### Output files

n/a

#### SQL script

n/a

#### Software

Jupyter Notebook, Pandas, Python 3.11.4

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

----

### **GitHub Repository Branches:**

----

#### main branch

|&rarr; [./PyCitySchools.ipynb](./PyCitySchools.ipynb)

|&rarr; [./PyCitySchoolsConstants.py](./PyCitySchoolsConstants.py)

|&rarr; [./PyConstants.py](./PyConstants.py)

|&rarr; [./PyFunctions.py](./PyFunctions.py)

|&rarr; [./PyLogConstants.py](./PyLogConstants.py)

|&rarr; [./PyLogFunctions.py](./PyLogFunctions.py)

|&rarr; [./PyLogSubRoutines.py](./PyLogSubRoutines.py)

|&rarr; [./PySubRoutines.py](./PySubRoutines.py)

|&rarr; [./README.TECHNICAL.md](./README.TECHNICAL.md)

|&rarr; [./README.md](./README.md)

|&rarr; [./Table-Of-Contents-SOAWP.md](./Table-Of-Contents-SOAWP.md)

|&rarr; [./Images/](./Images/)

  &emsp; |&rarr; [./Images/PyCitySchoolsTable13CompleteSchoolDataSet.png](./Images/PyCitySchoolsTable13CompleteSchoolDataSet.png)
  
  &emsp; |&rarr; [./Images/PyCitySchoolsTable23SchoolDistrictMetrics.png](./Images/PyCitySchoolsTable23SchoolDistrictMetrics.png)
  
  &emsp; |&rarr; [./Images/PyCitySchoolsTable33SchoolMetrics.png](./Images/PyCitySchoolsTable33SchoolMetrics.png)
  
  &emsp; |&rarr; [./Images/PyCitySchoolsTable41HighestPerformingSchools.png](./Images/PyCitySchoolsTable41HighestPerformingSchools.png)
  
  &emsp; |&rarr; [./Images/PyCitySchoolsTable42LowestPerformingSchools.png](./Images/PyCitySchoolsTable42LowestPerformingSchools.png)
  
  &emsp; |&rarr; [./Images/PyCitySchoolsTable62SchoolMetricswithSpendingRanges.png](./Images/PyCitySchoolsTable62SchoolMetricswithSpendingRanges.png)
  
  &emsp; |&rarr; [./Images/PyCitySchoolsTable74TestScoresPassingRatesMeanbySpendingRanges.png](./Images/PyCitySchoolsTable74TestScoresPassingRatesMeanbySpendingRanges.png)
  
  &emsp; |&rarr; [./Images/PyCitySchoolsTable75TestScoresPassingRatesMedianbySpendingRanges.png](./Images/PyCitySchoolsTable75TestScoresPassingRatesMedianbySpendingRanges.png)

  &emsp; |&rarr; [./Images/PyCitySchoolsTable76TestScoresPassingRatesMeanMedianbySpendingRanges.png](./Images/PyCitySchoolsTable76TestScoresPassingRatesMeanMedianbySpendingRanges.png)
  
  &emsp; |&rarr; [./Images/PyCitySchoolsTable82SchoolMetricswithSchoolSizeCategories.png](./Images/PyCitySchoolsTable82SchoolMetricswithSchoolSizeCategories.png)
  
  &emsp; |&rarr; [./Images/PyCitySchoolsTable94FinancialMetricsbySchoolSizeMean.png](./Images/PyCitySchoolsTable94FinancialMetricsbySchoolSizeMean.png)
  
  &emsp; |&rarr; [./Images/PyCitySchoolsTable95FinancialMetricsbySchoolSizeMedian.png](./Images/PyCitySchoolsTable95FinancialMetricsbySchoolSizeMedian.png)

  &emsp; |&rarr; [./Images/PyCitySchoolsTable96FinancialMetricsbySchoolSizeMeanMedian.png](./Images/PyCitySchoolsTable96FinancialMetricsbySchoolSizeMeanMedian.png)
  
  &emsp; |&rarr; [./Images/PyCitySchoolsTable104TestScoresPassingRatesMeanbySchoolSize.png](./Images/PyCitySchoolsTable104TestScoresPassingRatesMeanbySchoolSize.png)

  &emsp; |&rarr; [./Images/PyCitySchoolsTable105TestScoresPassingRatesMedianbySchoolSize.png](./Images/PyCitySchoolsTable105TestScoresPassingRatesMedianbySchoolSize.png)
  
  &emsp; |&rarr; [./Images/PyCitySchoolsTable106TestScoresPassingRatesMeanMedianbySchoolSize.png](./Images/PyCitySchoolsTable106TestScoresPassingRatesMeanMedianbySchoolSize.png)
  
  &emsp; |&rarr; [./Images/PyCitySchoolsTable114FinancialMetricsbySchoolTypeMean.png](./Images/PyCitySchoolsTable114FinancialMetricsbySchoolTypeMean.png)
  
  &emsp; |&rarr; [./Images/PyCitySchoolsTable115FinancialMetricsbySchoolTypeMedian.png](./Images/PyCitySchoolsTable115FinancialMetricsbySchoolTypeMedian.png)
  
  &emsp; |&rarr; [./Images/PyCitySchoolsTable116FinancialMetricsbySchoolTypeMeanMedian.png](./Images/PyCitySchoolsTable116FinancialMetricsbySchoolTypeMeanMedian.png)
  
  &emsp; |&rarr; [./Images/PyCitySchoolsTable124DisplayTestScoresPassingRatesMeanbySchoolType.png](./Images/PyCitySchoolsTable124DisplayTestScoresPassingRatesMeanbySchoolType.png)

  &emsp; |&rarr; [./Images/PyCitySchoolsTable124DisplayTestScoresPassingRatesMeanbySchoolType.png](./Images/PyCitySchoolsTable124DisplayTestScoresPassingRatesMeanbySchoolType.png)
  
  &emsp; |&rarr; [./Images/PyCitySchoolsTable125DisplayTestScoresPassingRatesMedianbySchoolType.png](./Images/PyCitySchoolsTable125DisplayTestScoresPassingRatesMedianbySchoolType.png)
  
  &emsp; |&rarr; [./Images/PyCitySchoolsTable126DisplayTestScoresPassingRatesMeanMedianbySchoolType.png](./Images/PyCitySchoolsTable126DisplayTestScoresPassingRatesMeanMedianbySchoolType.png)

  &emsp; |&rarr; [./Images/PyCitySchoolsTable521MathScoresMeanbyGrade.png](./Images/PyCitySchoolsTable521MathScoresMeanbyGrade.png)

  &emsp; |&rarr; [./Images/PyCitySchoolsTable522MathScoresMedianbyGrade.png](./Images/PyCitySchoolsTable522MathScoresMedianbyGrade.png)

  &emsp; |&rarr; [./Images/PyCitySchoolsTable523MathScoresMeanMedianbyGrade.png](./Images/PyCitySchoolsTable523MathScoresMeanMedianbyGrade.png)

  &emsp; |&rarr; [./Images/PyCitySchoolsTable531ReadingScoresMeanbyGrade.png](./Images/PyCitySchoolsTable531ReadingScoresMeanbyGrade.png)

  &emsp; |&rarr; [./Images/PyCitySchoolsTable532ReadingScoresMedianbyGrade.png](./Images/PyCitySchoolsTable532ReadingScoresMedianbyGrade.png)

  &emsp; |&rarr; [./Images/PyCitySchoolsTable533ReadingScoresMeanMedianbyGrade.png](./Images/PyCitySchoolsTable533ReadingScoresMeanMedianbyGrade.png)
 
  &emsp; |&rarr; [./Images/README.md](./Images/README.md)

|&rarr; [./Logs/](./Logs/)

  &emsp; |&rarr; [./Logs/20231107PyCitySchoolsDebug.txt](./Logs/20231107PyCitySchoolsDebug.txt)

  &emsp; |&rarr; [./Logs/20231107PyCitySchoolsLog.txt](./Logs/20231107PyCitySchoolsLog.txt)

  &emsp; |&rarr; [./Logs/README.md](./Logs/README.md)

|&rarr; [./Resources/](./Resources/)

  &emsp; |&rarr; [./Resources/README.md](./Resources/README.md)

  &emsp; |&rarr; [./Resources/schoolsComplete.csv](./Resources/schoolsComplete.csv)

  &emsp; |&rarr; [./Resources/studentsComplete.csv](./Resources/studentsComplete.csv)

----

### **References:**

----

[Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/stable/)

[Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)

[Python Documentation](https://docs.python.org/3/contents.html)

----

### **Authors and Acknowledgment:**

----

### Copyright

N. James George © 2023. All Rights Reserved.
