#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  PySubroutines.py
 #
 #  File Description:
 #      This Python script, PySubroutines.py, contains generic Python subroutines
 #      for completing common tasks.  Here is the list:
 #
 #      DisplayPandasBarChartFromSeries
 #      DisplayMatplotlibBarChartFromSeries
 #      DisplayPandasPieChartFromSeries
 #      DisplayMatplotlibPieChartFromSeries
 #      DisplayMatplotlibBoxPlotFromSeriesList
 #      DisplayMatplotlibLineChartFromXYSeries
 #      DisplayRegressionLine
 #      DisplayMatplotlibScatterPlotFromXYSeries
 #      DisplaySummaryStatisticsBoxPlot
 #      DisplayOneLineGraphFromSeries
 #      DisplaySeriesCountAndRedundancies
 #      DisplayTwoByTwoHistograms
 #      DisplayLinearRegressionLine
 #      DisplayTwoPieChartsSideBySide
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/22/2023      Initial Development                     N. James George
 #
 #******************************************************************************************/

import PyFunctions as function
import PyLogSubRoutines as log_subroutine

import math

import matplotlib.pyplot as plt
import pandas as pd

from scipy import stats
from pathlib import Path


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'PySubroutines.py'


# In[3]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayPandasBarChartFromSeries
 #
 #  Subroutine Description:
 #      This subroutine receives a Series and formatting parameters 
 #      and plots a bar chart using the Pandas DataFrame.plot() 
 #      method.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeriesParameter
 #                          This parameter is the Series used as input.
 #  List
 #          barColorsListParameter
 #                          This parameter is the list of bar colors.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  String
 #          yLabelStringParameter
 #                          This parameter is the y-axis label.
 #  String
 #          edgeColorStringParameter
 #                          This parameter is the bar edge color.
 #  Float
 #          lineWidthFloatParameter
 #                          This parameter is the bar edge line width.
 #  Float
 #          alphaFloatParameter
 #                          This parameter is the transparency value
 #                          for the bars (0.0-1.0).
 #  Float
 #          widthFloatParameter
 #                          This parameter is the width of a bar.
 #  Float
 #          axisTickLabelRotationFloatParameter
 #                          This parameter is the rotation of the x-axis 
 #                          tick labels.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DisplayPandasBarChartFromSeries \
        (inputSeriesParameter,
         barColorsListParameter,
         captionStringParameter, 
         yLabelStringParameter,
         edgeColorStringParameter \
            = 'blue',
         lineWidthFloatParameter \
            = 1.0,
         alphaFloatParameter \
            = 1.0,
         widthFloatParameter \
            = 0.5,
         axisTickLabelRotationFloatParameter \
            = 80.0):
    
    try:
        
        inputSeries \
            = inputSeriesParameter.copy()
        
        inputSeries \
            .plot \
            .bar \
                (stacked \
                     = False,
                 align \
                     = 'center',
                 color \
                     = barColorsListParameter,
                 edgecolor \
                     = edgeColorStringParameter,
                 linewidth \
                     = lineWidthFloatParameter,
                 alpha \
                     = alphaFloatParameter,
                 width \
                     = widthFloatParameter, 
                 xlabel \
                     = inputSeries.name, 
                 ylabel \
                     = yLabelStringParameter, 
                 rot \
                     = axisTickLabelRotationFloatParameter,
                 legend \
                     = False)
    
        plt \
            .title \
                (captionStringParameter,
                 pad = 20, 
                 fontdict \
                     = {'fontsize' : 14.0, 
                        'fontstyle' : 'normal', 
                        'fontweight' : 'bold'})

        plt \
            .xlabel \
                (inputSeries.name,
                 fontdict \
                    = {'fontsize': 
                            12})

        plt \
            .ylabel \
                (yLabelStringParameter,
                 fontdict \
                    = {'fontsize': 
                            12})
        
        plt \
            .grid \
                (axis \
                    = "y")
        
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
        
        plt \
            .show()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayPandasBarChartFromSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to plot a bar chart using Pandas.')


# In[4]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayMatplotlibBarChartFromSeries
 #
 #  Subroutine Description:
 #      This subroutine receives a Series and formatting parameters 
 #      and plots a bar chart using the Matplotlib pyplot method.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeriesParameter
 #                          This parameter is the Series used as input.
 #  List
 #          barColorsListParameter
 #                          This parameter is the list of bar colors.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  String
 #          yLabelStringParameter
 #                          This parameter is the y-axis label.
 #  String
 #          edgeColorStringParameter
 #                          This parameter is the bar edge color.
 #  Float
 #          lineWidthFloatParameter
 #                          This parameter is the bar edge line width.
 #  Float
 #          alphaFloatParameter
 #                          This parameter is the transparency value
 #                          for the bars (0.0-1.0).
 #  Float
 #          widthFloatParameter
 #                          This parameter is the width of a bar.
 #  Float
 #          axisTickLabelRotationFloatParameter
 #                          This parameter is the rotation of the x-axis 
 #                          tick labels.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DisplayMatplotlibBarChartFromSeries \
        (inputSeriesParameter,
         barColorsListParameter,
         captionStringParameter, 
         yLabelStringParameter,
         edgeColorStringParameter \
            = 'blue',
         lineWidthFloatParameter \
            = 1.0,
         alphaFloatParameter \
            = 1.0,
         widthFloatParameter \
            = 0.5,
         axisTickLabelRotationFloatParameter \
            = 80.0):
    
    
    try:
        
        inputSeries \
            = inputSeriesParameter.copy()
        
        
        plt \
            .bar \
                (inputSeries.keys(),
                 inputSeries,
                 align = 'center',
                 color = barColorsListParameter,
                 edgecolor = edgeColorStringParameter,
                 linewidth = lineWidthFloatParameter,
                 alpha = alphaFloatParameter,
                 width = widthFloatParameter)
        
        plt \
            .title \
                (captionStringParameter,
                 pad = 20, 
                 fontdict \
                     = {'fontsize' : 14.0, 
                        'fontstyle' : 'normal', 
                        'fontweight' : 'bold'})

        plt \
            .xlabel \
                (inputSeries.name,
                 fontdict \
                    = {'fontsize': 
                            12.0})

        plt \
            .ylabel \
                (yLabelStringParameter,
                 fontdict \
                    = {'fontsize': 
                            12.0, 
                       'fontstyle': 
                            'italic', 
                       'fontweight': 
                            'bold'})

        plt \
            .xticks \
                (rotation \
                     = axisTickLabelRotationFloatParameter) 

        plt \
            .grid \
                (axis \
                    = "y")
        
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
        
        plt \
            .show()

    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayMatplotlibBarChartFromSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to plot a bar chart using Matplotlib.')


# In[5]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayPandasPieChartFromSeries
 #
 #  Subroutine Description:
 #      This subroutine receives a Series and formatting parameters 
 #      and plots a pie chart using the Pandas DataFrame.plot() 
 #      method.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeriesParameter
 #                          This parameter is the Series used as input.
 #  List
 #          colorsListParameter
 #                          This parameter is the list of bar colors.
 #  List
 #          explodeTupleParameter
 #                          This parameter specifies the fraction of the 
 #                          radius with which to offset each wedge.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  Float
 #          startAngleFloatParameter
 #                          This parameter is the angle by which the start 
 #                          of the pie is rotated, counterclockwise from 
 #                          the x-axis.
 #  Float
 #          autoPercentStringParameter
 #                          This parameter is the format of the wedge label.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def DisplayPandasPieChartFromSeries \
        (inputSeriesParameter, 
         colorsListParameter,
         explodeTupleParameter,
         captionStringParameter,
         startAngleFloatParameter \
            = 45.0,
         autoPercentStringParameter \
            = '%1.0f%%'):
    
    try:

        inputSeries \
            = inputSeriesParameter.copy()
        
        
        inputSeries \
            .rename \
                (None, 
                 inplace \
                     = True)
        
        
        inputSeries \
            .plot \
            .pie \
                (colors \
                     = colorsListParameter, 
             explode \
                 = explodeTupleParameter, 
             shadow \
                 = True, 
             startangle \
                 = startAngleFloatParameter, 
             autopct \
                 = autoPercentStringParameter,
             legend \
                 = False,
             figsize \
                = (6, 9))

        plt \
            .title \
                (captionStringParameter,
                 pad = 5, 
                 fontdict \
                     = {'fontsize' : 14.0})
        
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
        
        plt \
            .show()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayPandasPieChartFromSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to plot a pie chart using Pandas.')


# In[6]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayMatplotlibPieChartFromSeries
 #
 #  Subroutine Description:
 #      This subroutine receives a Series and formatting parameters 
 #      and plots a pie chart using the Matplotlib pyplot method.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeriesParameter
 #                          This parameter is the Series used as input.
 #  List
 #          colorsListParameter
 #                          This parameter is the list of bar colors.
 #  List
 #          explodeTupleParameter
 #                          This parameter specifies the fraction of the 
 #                          radius with which to offset each wedge.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  Float
 #          startAngleFloatParameter
 #                          This parameter is the angle by which the start 
 #                          of the pie is rotated, counterclockwise from 
 #                          the x-axis.
 #  Float
 #          autoPercentStringParameter
 #                          This parameter is the format of the wedge label.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DisplayMatplotlibPieChartFromSeries \
        (inputSeriesParameter, 
         colorsListParameter,
         explodeTupleParameter,
         captionStringParameter,
         startAngleFloatParameter \
            = 45.0,
         autoPercentStringParameter \
            = '%1.0f%%'):
    
    try:

        inputSeries \
            = inputSeriesParameter.copy()
        
        inputSeries \
            .rename \
                (None, 
                 inplace \
                     = True)
        
        plt \
            .pie \
                (inputSeries,
                 labels \
                     = inputSeries.index, 
                 colors \
                     = colorsListParameter,        
                 explode \
                     = explodeTupleParameter, 
                 shadow \
                     = True, 
                 startangle \
                     = startAngleFloatParameter,
                 autopct \
                     = autoPercentStringParameter)

        plt \
            .title \
                (captionStringParameter,
                 pad = 5, 
                 fontdict \
                     = {'fontsize' : 14.0, 
                        'fontstyle' : 'normal', 
                        'fontweight' : 'bold'})
        
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
        
        plt \
            .show()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayMatplotlibPieChartFromSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to plot a pie chart using Matplotlib.')


# In[7]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayMatplotlibBoxPlotFromSeriesList
 #
 #  Subroutine Description:
 #      This subroutine receives a Series and formatting parameters and plots 
 #      a box plot using the Matplotlib pyplot method.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  List of Series
 #          inputSeriesListParameter
 #                          This parameter holds a list of series where 
 #                          each series is the data for one box plot.
 #  List
 #          xTicksLabelListParameter
 #                          This parameter is the list of x-axis tick 
 #                          labels.
 #  String
 #          xLabelParameter
 #                          This parameter is the x-axis label. 
 #  String
 #          xLabelParameter
 #                          This parameter is the y-axis label.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  Boolean
 #          verticalFlagBooleanParameter
 #                          This parameter indicates whether the box
 #                          plots are vertical or horizontal.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/19/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
        
def DisplayMatplotlibBoxPlotFromSeriesList \
        (inputSeriesListParameter,
         xTicksLabelListParameter,
         xLabelStringParameter,
         yLabelStringParameter,
         captionStringParameter,
         verticalFlagBooleanParameter \
             = True):
    
    try:
        
        inputSeriesList \
            = inputSeriesListParameter.copy()
        
        
        fig1, ax \
            = plt \
                .subplots()

        ax \
            .boxplot \
                (inputSeriesList,
                 vert \
                     = verticalFlagBooleanParameter,
                 widths \
                     = 0.45,
                 meanline \
                     = True, 
                 showmeans \
                     = True)
        
        ax \
            .set_title \
                (captionStringParameter,
                 pad = 15, 
                 fontdict \
                     = {'fontsize': 
                            14.0, 
                        'fontstyle': 
                            'normal', 
                        'fontweight': 
                            'bold'})
        
        ax \
            .set_xlabel \
                (xLabelStringParameter,
                 fontdict \
                     = {'fontsize': 
                            12.0})

        ax \
            .set_ylabel \
                (yLabelStringParameter,
                 fontdict \
                     = {'fontsize': 
                            12.0})
        
        
        ticksIndexList \
            = []
        
        for index, regimen in enumerate(xTicksLabelListParameter):
            
                ticksIndexList \
                    .append \
                        ( index + 1 )
        
        ax \
            .set_xticks \
                (ticksIndexList, 
                 xTicksLabelListParameter)
        
        plt \
            .grid \
                (axis \
                    = "y")
        
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
        
        plt \
            .show() 
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayMatplotlibBoxPlotFromSeriesList, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to plot a box plot using Matplotlib.')


# In[8]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayMatplotlibLineChartFromXYSeries
 #
 #  Subroutine Description:
 #      This subroutine receives a Series and formatting parameters 
 #      and plots a line chart using the Matplotlib pyplot method.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          xSeriesParameter
 #                          This parameter is the Series used as x-axis 
 #                          values.
 #  Series
 #          ySeriesParameter
 #                          This parameter is the Series used as y-axis 
 #                          values.
 #  String
 #          lineColorStringParameter
 #                          This parameter is the line color.
 #  String
 #          lineTypeStringParameter
 #                          This parameter is the line style ('solid', 
 #                          'dotted', 'dashed', or 'dashdot'.
 #  String
 #          xLabelStringParameter
 #                          This parameter is the labe for the x-axis.
 #  String
 #          yLabelStringParameter
 #                          This parameter is the labe for the y-axis.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
        
def DisplayMatplotlibLineChartFromXYSeries \
        (xSeriesParameter,
         ySeriesParameter,
         lineColorStringParameter,
         lineTypeStringParameter,
         xLabelStringParameter,
         yLabelStringParameter,
         captionStringParameter):
    
    try:
        
        xSeries \
            = xSeriesParameter.copy()
        
        ySeries \
            = ySeriesParameter.copy()
    
        plt \
            .plot \
                (xSeries,
                 ySeries,
                 alpha \
                    = 1.0,
                 color \
                     = lineColorStringParameter,
                 fillstyle \
                     = 'full',
                 linewidth \
                     = 2.0,
                 marker \
                     = 'o',
                 markeredgecolor \
                     = 'black',
                 linestyle \
                     = lineTypeStringParameter)
     
        plt \
            .title \
                (captionStringParameter,
                 pad = 15, 
                 fontdict \
                     = {'fontsize' : 14.0, 
                        'fontstyle' : 'normal', 
                        'fontweight' : 'bold'})

        plt \
            .xlabel \
                (xLabelStringParameter,
                 fontdict \
                     = {'fontsize':
                            12.0})

        plt \
            .ylabel \
                (yLabelStringParameter,
                 fontdict \
                     = {'fontsize': 
                            12.0})

        plt \
            .grid()
        
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)

        plt \
            .show()

    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayMatplotlibLineChartFromXYSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to plot a line chart using Matplotlib.')


# In[9]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayRegressionLine 
 #
 #  Subroutine Description:
 #      This subroutine receives two Series and the polynomial degree, calculates 
 #      the parameters of the regression line, and displays the results on the 
 #      scatter plot and above it.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          xSeriesParameter
 #                          This parameter is the Series used as x-axis 
 #                          values.
 #  Series
 #          ySeriesParameter
 #                          This parameter is the Series used as y-axis 
 #                          values.
 #  Integer
 #          degreeIntegerParameter
 #                          This parameter is degree of the polynomial 
 #                          regression.
 #  Float
 #          xCoordinateFloatParameter
 #                          This parameter is the x-coordinate of the text 
 #                          in the chart.
 #  Float
 #          yCoordinateFloatParameter
 #                          This parameter is the y-coordinate of the text 
 #                          in the chart.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/  
        
def DisplayRegressionLine \
                (xSeriesParameter,
                 ySeriesParameter,
                 degreeIntegerParameter,
                 xCoordinateFloatParameter,
                 yCoordinateFloatParameter):

    try:
        
        modelEquationList \
            = function \
                .ReturnRegressionModelEquationList \
                    (xSeriesParameter,
                     ySeriesParameter,
                     degreeIntegerParameter)
 
        polynomialLineSeries \
            = function \
                .ReturnPolynomialLineSeries \
                    (xSeriesParameter, 
                     ySeriesParameter)
 
        plt \
            .plot \
                (polynomialLineSeries, 
                 modelEquationList \
                    (polynomialLineSeries),
                 color \
                     = 'red',
                 linewidth \
                     = 3,
                 alpha \
                     = 1.0)

    
        equationLabelStringVariable \
            = function \
                .ReturnEquationAsString \
                    (modelEquationList)
    
        plt.annotate \
            (equationLabelStringVariable,
             (xCoordinateFloatParameter,
              yCoordinateFloatParameter),
             fontsize \
                 = 15, 
             color \
                 = 'blue')
    
    
        rSquaredFloatVariable \
            = function \
                .ReturnRSquaredValue \
                    (xSeriesParameter,
                     ySeriesParameter,
                     degreeIntegerParameter)
    
        rValueFloatVariable \
            = math.sqrt(rSquaredFloatVariable)

    
        log_subroutine \
            .PrintAndLogWriteText \
                ('r-value:     {:.4f}'.format(rValueFloatVariable))
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('r-squared:   {:.4f}'.format(rSquaredFloatVariable))
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayRegressionLine, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'was unable to calculate and display a regression line.')


# In[10]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayMatplotlibScatterPlotFromXYSeries
 #
 #  Subroutine Description:
 #      This subroutine receives two Series and formatting parameters 
 #      and plots a scatter plot using the Matplotlib pyplot method.
 #      If the polynomial degree parameter is greater than zero, it 
 #      also plots the regression line and displays the results of 
 #      the regression.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          xSeriesParameter
 #                          This parameter is the Series used as x-axis 
 #                          values.
 #  Series
 #          ySeriesParameter
 #                          This parameter is the Series used as y-axis 
 #                          values.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  Integer
 #          optionalDegreeIntegerParameter
 #                          This parameter is degree of the polynomial 
 #                          regression.
 #  Integer
 #          optionalTextXCoordinateIntegerParameter
 #                          This parameter is the x-coordinate of the text 
 #                          in the chart.
 #  Integer
 #          optionalTextYCoordinateIntegerParameter
 #                          This parameter is the y-coordinate of the text 
 #                          in the chart.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/  
    
def DisplayMatplotlibScatterPlotFromXYSeries \
        (xSeriesParameter, 
         ySeriesParameter, 
         captionStringParameter,
         optionalDegreeIntegerParameter \
             = 0,
         optionalTextXCoordinateFloatParameter \
             = 0,
         optionalTextYCoordinateFloatParameter \
             = 0):
    
    try:
        
        xSeries \
            = xSeriesParameter.copy()
    
        ySeries \
            = ySeriesParameter.copy()
    
    
        plt \
            .scatter \
                (xSeries, 
                 ySeries, 
                 marker \
                     = 'o',
                 s \
                     = 40,
                 color 
                     = 'lime', 
                 linewidth \
                     = 1.0,
                 edgecolors \
                     = 'black',
                 alpha \
                     = 0.8)

        plt \
            .title \
                (captionStringParameter, 
                 pad = 20, 
                 fontdict \
                    = {'fontsize': 
                           14.0})
    
        plt \
            .xlabel \
                (xSeries \
                     .name,
                 fontdict \
                     = {'fontsize': 
                            12.0},
                 labelpad \
                    = 10)

        plt \
            .ylabel \
                (ySeries \
                     .name,
                 fontdict \
                     = {'fontsize': 
                            12.0})
        
        plt \
            .grid()
        
        
        if optionalDegreeIntegerParameter == 1:
            
            DisplayLinearRegressionLine \
                (xSeries,
                 ySeries,
                 optionalTextXCoordinateFloatParameter,
                 optionalTextYCoordinateFloatParameter)
            
        elif optionalDegreeIntegerParameter > 1:
                
            DisplayRegressionLine \
                (xSeries,
                 ySeries,
                 optionalDegreeIntegerParameter,
                 optionalTextXCoordinateFloatParameter,
                 optionalTextYCoordinateFloatParameter)
        
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
        
        plt \
            .show()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayMatplotlibScatterPlotFromXYSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to plot a scatter plot using Matplotlib.')


# In[11]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayStackedSubplots
 #
 #  Subroutine Description:
 #      This subroutine receives a DataFrame, and formatting parameters, and creates
 #      stacked subplots.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Dictionary
 #          frameDictionaryParameter
 #                          This parameter is the input Dictionary for conversion 
 #                          to a DataFrame.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  List of Strings
 #          colorListParameter
 #                          This parameter is the list of colors for the subplots.
 #  String
 #          figureXLabelStringParameter
 #                          This parameter is the title for the figure's x-axis.
 #  String
 #          figureYLabelStringParameter
 #                          This parameter is the title for the figure's y-axis.
 #  String
 #          xLabelStringParameter
 #                          This parameter is the title for the plot's x-axis.
 #  String
 #          yLabelStringParameter
 #                          This parameter is the title for the plot's y-axis.
 #  Float
 #          figureXLabelYPositionFloatParameter
 #                          This parameter is the y-axis offset for the figure's 
 #                          x-label.
 #  Float
 #          figureYLabelYPositionFloatParameter
 #                          This parameter is the x-axis offset for the figure's 
 #                          y-label.
 #  Boolean
 #          legendFlagBooleanParameter 
 #                          This parameter indicates whether there will be a 
 #                          legend or not.
 #  Float
 #          legendXOffsetFloatParameter
 #                          This parameter is the x-axis offset for the figure's 
 #                          legend.
 #  Float
 #          legendYOffsetFloatParameter
 #                          This parameter is the y-axis offset for the figure's 
 #                          legend.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/  
        
def DisplayStackedSubplots \
        (frameDictionaryParameter,
         captionStringParameter,
         colorListParameter,
         figureXLabelStringParameter \
            = None,
         figureYLabelStringParameter \
            = None,
         xLabelStringParameter \
            = None,
         yLabelStringParameter \
            = None,
         figureXLabelYPositionFloatParameter \
            = 0.0,
         figureYLabelXPositionFloatParameter \
            = 0.0,
         legendFlagBooleanParameter \
            = False,
         legendXOffsetFloatParameter \
            = 0.0,
         legendYOffsetFloatParameter \
            = 0.0):
    
    try:

        inputDataFrame \
            = pd \
                .DataFrame \
                    (frameDictionaryParameter)
        
    
        numberOfSubPlotsIntegerVariable \
            = len(inputDataFrame.keys())
    
  
        fig, axs \
            = plt \
                .subplots \
                    (numberOfSubPlotsIntegerVariable)
   
        fig \
            .suptitle \
                (captionStringParameter, 
                 fontsize = 14)
      
        if figureXLabelStringParameter != None:
            
            fig \
                .supxlabel \
                    (figureXLabelStringParameter,
                     fontsize \
                         = 12,
                     y \
                         = figureXLabelYPositionFloatParameter)
       
        if figureYLabelStringParameter != None:
            
            fig \
                .supylabel \
                    (figureYLabelStringParameter,
                     fontsize \
                         = 12,
                     x \
                         = figureYLabelXPositionFloatParameter)
    
        legendLinePlotList \
             = []
        
        legendLineNamesList \
            = []
    
            
        for index, subPlot in enumerate(axs):
        
            lineSubPlot, \
                = subPlot \
                    .plot \
                        (inputDataFrame.iloc[:,index], 
                         color \
                             = colorListParameter[index])
            
            
            legendLinePlotList \
                .append \
                    (lineSubPlot)
            
            legendLineNamesList \
                .append \
                    (inputDataFrame.iloc[:,index].name)
            
            
            subPlot \
                .grid()
            
            if index != (numberOfSubPlotsIntegerVariable - 1):
                
                subPlot \
                    .set_xticklabels \
                        (labels = [])
                
            else:
                subPlot \
                    .tick_params \
                        (axis = 'x', 
                         rotation = 90.0)
                
                if xLabelStringParameter == None:
                
                    subPlot \
                        .set_xlabel \
                            ('')
                    
                else:
                    
                    subPlot \
                        .set_xlabel \
                            (xLabelStringParameter)
            
            if yLabelStringParameter == None:
                
                subPlot \
                    .set_ylabel \
                        (inputDataFrame.iloc[:,index].name)
            
            else:
                    
                subPlot \
                    .set_ylabel \
                        (yLabelStringParameter)
                
                
        if legendFlagBooleanParameter == True:
        
            fig \
                .legend \
                    (legendLinePlotList, 
                     legendLineNamesList, 
                     loc \
                         = 'center right',
                     bbox_to_anchor \
                         = (legendXOffsetFloatParameter, 
                            legendYOffsetFloatParameter))
        
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
        
        plt \
            .show()
            
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayStackedSubplots, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to create stacked subplots.')


# In[12]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplaySummaryStatisticsBoxPlot
 #
 #  Subroutine Description:
 #      This subroutine receives a DataFrame and column name and plots a horizontal
 #      box plot based on the information.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          boxPlotDataFrameParameter
 #                          This parameter is the input DataFrame
 #  Series
 #          columnNameStringParameter
 #                          This parameter is the input Series used as y-axis 
 #                          values.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/  
            
def DisplaySummaryStatisticsBoxPlot \
        (boxPlotDataFrameParameter, \
         columnNameStringParameter, \
         captionStringParameter):
    
    try:
        
        boxPlotAxes \
            = boxPlotDataFrameParameter.boxplot \
                (by \
                     ='Industry', \
                 column \
                     = [columnNameStringParameter], 
                 fontsize \
                     = 12,
                 rot \
                     = 0.0,
                 grid \
                     = True,
                 figsize \
                     = (9,6),
                 vert \
                     = False,
                 widths \
                     = 0.7,
                 meanline \
                     = True,
                 showmeans \
                     = True)

    
        plt \
            .suptitle \
                (captionStringParameter, 
                 fontsize \
                     = 14, 
                 y \
                    = 1.01)
    
        plt \
            .xlabel('')
    
        plt \
            .ylabel('')
    
        boxPlotAxes \
            .get_figure() \
            .gca() \
            .set_xlabel('')
    
    
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
    
        plt \
            .show()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplaySummaryStatisticsBoxPlot, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to create a horizontal box plot.')


# In[13]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayOneLineGraphFromSeries
 #
 #  Subroutine Description:
 #      This subroutine displays a one line graph based on an input Series 
 #      and formatting parameters.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeriesParameter
 #                          This parameter is the input Series
 #  String
 #          colorStringParameter
 #                          This parameter specifies the color of the line.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  String
 #          xLabelStringParameter
 #                          This parameter is the x-axis label.
 #  String
 #          yLabelStringParameter
 #                          This parameter is the y-axis label.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/22/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/ 

def DisplayOneLineGraphFromSeries \
    (inputSeriesParameter,
     colorStringParameter,
     captionStringParameter,
     xLabelStringParameter,
     yLabelStringParameter):
    
    try:
    
        inputSeries \
            = inputSeriesParameter.copy()
    
        inputSeries \
            .plot \
                (kind \
                     = 'line', 
                 color \
                     = colorStringParameter, 
                 grid \
                     = True, 
                 legend \
                     = False, 
                 fontsize \
                     = 12,
                 rot \
                    = 90.0)


        plt \
            .suptitle \
                (captionStringParameter, 
                 fontsize \
                    = 14, 
                 y \
                    = 1.0)
    
        plt \
            .xlabel \
                (xLabelStringParameter, 
                    fontsize \
                        = 12,
                 labelpad \
                    = 10)
    
        plt \
            .ylabel \
                (yLabelStringParameter, \
                    fontsize \
                        = 12)
        
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
    
        plt \
            .show()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayOneLineGraphFromSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to create a one line graph.')


# In[14]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayLinesGraph
 #
 #  Subroutine Description:
 #      This subroutine displays a multiple line graph based on an input Dictionary
 #      and formatting parameters.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Dictionary
 #          frameDictionaryParameter
 #                          This parameter is the input Series as a Dictionary.
 #  List of Strings
 #          colorListParameter
 #                          This parameter is a List of colors for the lines.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  String
 #          xLabelStringParameter
 #                          This optional parameter is the x-axis label.
 #  String
 #          yLabelStringParameter
 #                          This optional parameter is the y-axis label.
 #  Integer
 #          rotationIntegerParameter
 #                          This optional parameter is the angle of rotation
 #                          for the x-axis tick labels.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/22/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/ 

def DisplayLinesGraph \
        (frameDictionaryParameter,
         colorListParameter,
         captionStringParameter,
         xlabelStringParameter = '',
         ylabelStringParameter = '',
         rotationIntegerParameter = 0.0):
        
    try:

        lineDataFrame \
            = pd \
                .DataFrame \
                    (frameDictionaryParameter)
    

        lineDataFrame \
            .plot \
                (kind \
                     = 'line',
                 grid \
                     = True, 
                 legend \
                     = True, 
                 fontsize \
                     = 12,
                 rot \
                     = 90.0,
                 color \
                     = colorListParameter)

        plt \
            .suptitle \
                (captionStringParameter, 
                 fontsize \
                    = 14, 
                 y \
                    = 0.99)
    

        plt \
            .xlabel \
                (xlabelStringParameter, 
                 fontsize \
                    = 12,
                 labelpad \
                    = 10)

        plt \
            .ylabel \
                (ylabelStringParameter,
                    fontsize \
                        = 12)
        
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
        
        plt \
            .show()

    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayLinesGraph, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to create a line graph.')


# In[15]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplaySeriesCountAndRedundancies
 #
 #  Subroutine Description:
 #      This subroutine displays a multiple line graph based on an input Dictionary
 #      and formatting parameters.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeriesParameter
 #                          This parameter is the input Series.
 #  String
 #          whatIsItStringParameter
 #                          This parameter is the what the Series holds.
 #  String
 #          whereIsItStringParameter
 #                          This parameter is where the values came from.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/23/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/ 

def DisplaySeriesCountAndRedundancies \
        (inputSeriesParameter,
         whatIsItStringParameter,
         whereIsItStringParameter):
    
    numberOfTickersIntegerVariable \
        = inputSeriesParameter.count()

    numberOfRedundanciesIntegerVariable \
        = function \
            .ReturnNumberOfRedundanciesInSeries \
                (inputSeriesParameter)

    log_subroutine \
        .PrintAndLogWriteText \
            (f'There are now {numberOfTickersIntegerVariable} '
             + f'{whatIsItStringParameter} '
             + f'with {numberOfRedundanciesIntegerVariable} '
             + f'redundancies in {whereIsItStringParameter}.')


# In[16]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayLinesGraph
 #
 #  Subroutine Description:
 #      This subroutine displays a two-by-two plot of four histograms from 
 #      a Frame Dictionary.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Dictionary
 #          frameDictionaryParameter
 #                          This parameter is the input Series as a Dictionary.
 #  String
 #          figureTitleStringParameter
 #                          This parameter is the figure title.
 #  String
 #          figureXLabelStringParameter
 #                          This parameter is the figure x-axis label.
 #  String
 #          figureYLabelStringParameter
 #                          This parameter is the figure y-axis label.
 #  Integer
 #          numberOfBinsIntegerParameter
 #                          This optional parameter is the number of bins
 #                          for the histogram.
 #  Float
 #          alphaFloatParameter
 #                          This parameter is the alpha value (transparency level)
 #                          of the histogram bars.
 #  List of Strings
 #          colorListParameter
 #                          This parameter is a List of colors for the four histograms.
 #  Tuple of Integers
 #          figSizeTupleOfIntegersParamete
 #                          This parameter is the length and width of the figure.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/24/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/ 

def DisplayTwoByTwoHistograms \
        (frameDictionaryParameter,
         figureTitleStringParameter \
             = '',
         figureXLabelStringParameter \
             = '',
         figureYLabelStringParameter \
             = '',
         numberOfBinsIntegerParameter \
             = 10,
         alphaFloatParameter \
             = 0.8,
         colorListOfStringsParameter \
             = ['darkgreen', 
                'darkorange', 
                'darkblue', 
                'firebrick'],
         figSizeTupleOfIntegersParameter \
             = (9,6)):

    try:

        inputDataFrame \
            = pd \
                .DataFrame \
                    (frameDictionaryParameter)

        fig, axs \
            = plt \
                .subplots \
                    (2, 2,
                     figsize \
                        = figSizeTupleOfIntegersParameter,
                     sharey \
                         = True, 
                     tight_layout \
                         = True)

        index \
            = 0

        for row in range(2):
            for column in range(2):
    
                inputDataFrame \
                    .hist \
                        (column \
                             = inputDataFrame.keys()[index], 
                         ax \
                             = axs \
                                 [row, column], 
                         bins \
                             = numberOfBinsIntegerParameter, 
                         alpha \
                             = alphaFloatParameter, 
                         color \
                             = colorListOfStringsParameter \
                                 [index])
                
                axs[row, column] \
                    .set_title \
                        (inputDataFrame.keys() \
                             [index])
                
                index \
                    += 1


        fig \
            .suptitle \
                (figureTitleStringParameter,
                 fontsize = 14)

        fig \
            .supxlabel \
                (figureXLabelStringParameter,
                 fontsize = 12)

        fig \
            .supylabel \
                (figureYLabelStringParameter,
                 fontsize = 12)

        
        log_subroutine \
            .SavePlotImage \
                (figureTitleStringParameter)

        
        plt.show()

    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayTwoByTwoHistograms, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {figureTitleStringParameter},\n'
                 + f'was unable to create a two-by-two set of four histograms.')


# In[17]:


#*******************************************************************************************
 #
 #  Subroutine Name:  WriteDataFrameToCSVFile
 #
 #  Subroutine Description:
 #      This subroutine receives a file path to a csv file as a parameter, 
 #      and write the DataFrame to the file.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          This parameter is the input DataFrame.
 #  String or IOString
 #          filePathStringOrIOStringParameter
 #                          The parameter is name of the path to the csv file.
 #                          (i.e., './Resources/input.csv') or an IOString Object.
 #  String
 #          indexNameStringParameter
 #                          This parameter is the name of the index column.
 #  Boolean
 #          stringFlagBooleanParameter
 #                          This parameter indicates whether the first parameter
 #                          is a String variable or an IOString object.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/26/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def WriteDataFrameToCSVFile \
        (inputDataFrameParameter,
         filePathStringOrIOStringParameter,
         indexNameStringParameter
              = '',
         stringFlagBooleanParameter \
            = True):
    
    try:
        
        if stringFlagBooleanParameter == True:
            
            pathObject \
                = Path \
                    (filePathStringOrIOStringParameter)
            
        else:
            
            pathObject \
                = filePathStringOrIOStringParameter
        
        
        inputDataFrameParameter \
            .to_csv \
                (pathObject,
                    index_label \
                        = indexNameStringParameter)
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, WriteDataFrameToCSVFile, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to write a DataFrame to file path, '
                 + f'{filePathStringParameter}.')


# In[18]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayLinearRegressionLine
 #
 #  Subroutine Description:
 #      This subroutine receives two Series and the polynomial degree, calculates 
 #      the parameters of the linear regression line, and displays the results on
 #      the scatter plot and above it.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          xSeriesParameter
 #                          This parameter is the Series used as x-axis 
 #                          values.
 #  Series
 #          ySeriesParameter
 #                          This parameter is the Series used as y-axis 
 #                          values.
 #  Float
 #          xCoordinateFloatParameter
 #                          This parameter is the x-coordinate of the text 
 #                          in the chart.
 #  Float
 #          yCoordinateFloatParameter
 #                          This parameter is the y-coordinate of the text 
 #                          in the chart.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DisplayLinearRegressionLine \
        (xSeriesParameter,
         ySeriesParameter,
         xCoordinateFloatParameter,
         yCoordinateFloatParameter):
    
    try:
        
        xSeries \
            = xSeriesParameter.copy()
        
        ySeries \
            = ySeriesParameter.copy()
        
        (slope, 
         intercept, 
         rvalue, 
         pvalue, 
         stderr) \
            = stats \
                .linregress \
                    (xSeries, 
                     ySeries)

        linearRegressionSeries \
            = (xSeries * slope) + intercept
        
        
        plt \
            .plot \
                (xSeries,
                 linearRegressionSeries,
                 color \
                     = 'red')
        
        
        linearEquationStringVariable \
            = 'y = ' + str( round( slope, 4 ) ) + 'x + ' + str( round( intercept, 4 ) )
        
        
        plt \
            .annotate \
                (linearEquationStringVariable,
                 (xCoordinateFloatParameter, yCoordinateFloatParameter),
                  fontsize \
                     = 15, 
                  color \
                     = 'blue')   
        
        
        rSquaredFloatVariable \
            = rvalue*rvalue
        
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('r-value:     {:.4f}'.format(rvalue))
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('r-squared:   {:.4f}'.format(rSquaredFloatVariable))
        
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayLinearRegressionLine, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'was unable to calculate and display a linear regression line.')


# In[19]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayTwoPieChartsSideBySide
 #
 #  Subroutine Description:
 #      This subroutine receives a Frame Dictionary with two Series and formatting 
 #      parameters and plots a pie chart using the Pandas DataFrame.plot() method.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Dictionary
 #          frameDictionaryParameter
 #                          This parameter is the Dictionary used as input.
 #  List
 #          colorsListParameter
 #                          This parameter is the list of bar colors.
 #  List
 #          explodeTupleParameter
 #                          This parameter specifies the fraction of the 
 #                          radius with which to offset each wedge.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  Float
 #          startAngleFloatParameter
 #                          This parameter is the angle by which the start 
 #                          of the pie is rotated, counterclockwise from 
 #                          the x-axis.
 #  Float
 #          autoPercentStringParameter
 #                          This parameter is the format of the wedge label.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/28/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DisplayTwoPieChartsSideBySide \
        (frameDictionaryParameter, 
         colorsListParameter,
         explodeTupleParameter,
         captionStringParameter,
         startAngleFloatParameter \
            = 45.0,
         autoPercentStringParameter \
            = '%1.1f%%'):

    try:
        
        inputDataFrame \
            = pd \
                .DataFrame \
                    (frameDictionaryParameter)

        fig, axs \
            = plt \
                .subplots \
                    (1, 2,
                     figsize \
                        = (10, 8))

        fig \
            .suptitle \
                (captionStringParameter, 
                 y \
                     = 0.75, 
                 fontsize \
                     = 20)
    

        for columnIndex in range(2):
    
            inputDataFrame \
                .iloc[:,columnIndex]  \
                .plot \
                .pie \
                    (ax \
                        = axs \
                            [columnIndex], 
                     colors \
                        = colorsListParameter, 
                     explode \
                        = explodeTupleParameter, 
                     shadow \
                        = True, 
                     startangle \
                        = startAngleFloatParameter, 
                     autopct \
                        = autoPercentStringParameter,
                     legend \
                        = False,
                    labeldistance \
                        = 1.2,
                    ylabel \
                        = '')
        
            axs \
                [columnIndex] \
                    .set_title \
                        (inputDataFrame \
                             .iloc \
                                 [:, columnIndex].name, 
                         fontsize=14)
                

        plt \
            .subplots_adjust \
                (wspace \
                     = 1.1, 
                 hspace \
                     = None)
         
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)

        plt \
            .show()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayTwoPieChartsSideBySide, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'was unable to calculate and display two pie charts side-by-side\n'
                 + f'for the caption, {captionStringParameter}.')


# In[ ]:




