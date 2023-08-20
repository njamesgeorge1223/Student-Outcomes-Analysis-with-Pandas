#!/usr/bin/env python
# coding: utf-8

# In[5]:


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
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/20/2023      Initial Development                     Nicholas George
 #
 #******************************************************************************************/

import PyFunctions as function

import math
import matplotlib.pyplot as plt


# In[6]:


CONSTANT_LOCAL_FILE_NAME \
    = 'PySubroutines.py'


# In[7]:


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
                            12.0, 
                       'fontstyle': 
                            'italic', 
                       'fontweight': 
                            'bold'})

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
            .grid \
                (axis \
                    = "y")
        
        plt \
            .show()
        
    except:
        
        print \
            (f'The subroutine, DisplayPandasBarChartFromSeries, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to plot a bar chart using Pandas.')
        
        
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
                            12.0, 
                       'fontstyle': 
                            'italic', 
                       'fontweight': 
                            'bold'})

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
        
        plt \
            .show()

    except:
        
        print \
            (f'The subroutine, DisplayMatplotlibBarChartFromSeries, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to plot a bar chart using Matplotlib.')
        
        
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
                 = False)

        plt \
            .title \
                (captionStringParameter,
                 pad = 5, 
                 fontdict \
                     = {'fontsize' : 14.0, 
                        'fontstyle' : 'normal', 
                        'fontweight' : 'bold'})
        
        plt \
            .show()
        
        
    except:
        
        print \
            (f'The subroutine, DisplayPandasPieChartFromSeries, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to plot a pie chart using Pandas.')
        
        
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

        plt \
            .show()
        
        
    except:
        
        print \
            (f'The subroutine, DisplayMatplotlibPieChartFromSeries, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to plot a pie chart using Matplotlib.')
     
    
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
                            12.0, 
                        'fontstyle': 
                            'italic', 
                        'fontweight': 
                            'bold'})

        ax \
            .set_ylabel \
                (yLabelStringParameter,
                 fontdict \
                     = {'fontsize': 
                            12.0, 
                        'fontstyle': 
                            'italic', 
                        'fontweight': 
                            'bold'})
        
        
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
        
        plt \
            .show() 
        
    except:
        
        print \
            (f'The subroutine, DisplayMatplotlibBoxPlotFromSeriesList, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to plot a box plot using Matplotlib.')

        
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
                            12.0, 
                        'fontstyle': 
                            'italic', 
                        'fontweight': 
                            'bold'})

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
            .grid()

        plt \
            .show()

    except:
        
        print \
            (f'The subroutine, DisplayMatplotlibLineChartFromXYSeries, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to plot a line chart using Matplotlib.')
      
    
#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayRegressionLine 
 #
 #  Subroutine Description:
 #      This subroutine receives two Series and the polynomial degree, calculates 
 #      the parameters of the regression line, and displays the results on the 
 #      scatter plot and below it.
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
    
        correlationFloatVariable \
            = xSeriesParameter \
                .corr \
                    (ySeriesParameter, 
                     method \
                         = 'pearson')

    
        print \
            ('r-value:     {:.4f}'.format(math.sqrt(rSquaredFloatVariable)))
        
        print \
            ('r-squared:   {:.4f}'.format(rSquaredFloatVariable))
        
        print \
            ('correlation: {:.4f}'.format(correlationFloatVariable))
        
    except:
        
        print \
            (f'The subroutine, DisplayRegressionLine, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to calculate and display a regression line.')

        
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
                 pad = 15, 
                 fontdict \
                    = {'fontsize': 
                           14.0, 
                       'fontstyle': 
                           'normal', 
                       'fontweight':
                           'bold'})
    
        plt \
            .xlabel \
                (xSeries \
                     .name,
                 fontdict \
                     = {'fontsize': 
                            12.0, 
                        'fontstyle': 
                            'italic', 
                        'fontweight': 
                            'bold'})

        plt \
            .ylabel \
                (ySeries \
                     .name,
                 fontdict \
                     = {'fontsize': 
                            12.0, 
                        'fontstyle': 
                            'italic', 
                        'fontweight': 
                            'bold'})
        
        plt \
            .grid()
        
        
        if optionalDegreeIntegerParameter > 0:
            
            DisplayRegressionLine \
                (xSeries,
                 ySeries,
                 optionalDegreeIntegerParameter,
                 optionalTextXCoordinateFloatParameter,
                 optionalTextYCoordinateFloatParameter)
        
        
        plt \
            .show()

        
    except:
        
        print \
            (f'The subroutine, DisplayMatplotlibScatterPlotFromXYSeries, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to plot a scatter plot using Matplotlib.')


# In[ ]:




