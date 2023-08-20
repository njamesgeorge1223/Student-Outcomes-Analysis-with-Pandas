#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  PyFunctions.py.ipynb
 #
 #  File Description:
 #      This Python script, PyFunctions.py, contains generic Python functions
 #      for completing common tasks.  Here is the list:
 #
 #      DebugReturnObject
 #      ReturnCSVFileAsDataFrame
 #      ReturnMergedDataFrame
 #
 #      ReturnStylerObjectStandardFormat
 #      ReturnStylerObjectBackgroundGradientFormat
 #
 #      ReturnNumberOfUniqueElementsInColumn
 #      ReturnDuplicateRowsAsDataFrame
 #      ReturnDataFrameRowsWithValue
 #      ReturnDataFrameRowsWithoutValue
 #
 #      ReturnSummaryStatisticsAsDataFrame
 #      ReturnRegressionModelEquationList
 #      ReturnPolynomialLineSeries
 #      ReturnRSquaredValue
 #      ReturnEquationAsString
 #      ReturnPearsonCorrelation
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/20/2023      Initial Development                     Nicholas George
 #
 #******************************************************************************************/

import PyConstants as constant

import numpy as np
import pandas as pd

from pathlib import Path


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'PyFunctions.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  DebugReturnObject
 #
 #  Subroutine Description:
 #      This function returns the input object if the global debug flag, 
 #      constant.CONSTANT_DEBUG_FLAG, is set to True.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Unknown
 #          objectUnknownTypeParameter
 #                          The parameter is the input object.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/11/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DebugReturnObject \
        (objectUnknownTypeParameter):
    
    # This line of code returns the variable if the global debug flag, 
    # CONSTANT_DEBUG_FLAG, is set to True.
    if constant.CONSTANT_DEBUG_FLAG == True:
        return objectUnknownTypeParameter
    else:
        return None
    

#*******************************************************************************************
 #
 #  Function Name:  ReturnCSVFileAsDataFrame
 #
 #  Function Description:
 #      This function receives a file path yo a csv file as a parameter, 
 #      reads the csv file into a DataFrame, and returns the DataFrame
 #      to the caller.  If the operation fails, the function returns
 #      None.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          filePathStringParameter
 #                          The parameter is name of the path to the csv file.
 #                          (i.e., './Resources/input.csv')
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnCSVFileAsDataFrame \
        (filePathStringParameter):
    
    try:

        return \
            pd \
                .read_csv \
                    (Path \
                        (filePathStringParameter))
        
    except:
        
        print \
            (f'The function, ReturnCSVFileAsDataFrame, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to open file path, '
             + f'{filePathStringParameter}.')
    
        return \
            None
    
    
    return \
        dataDataFrame


#*******************************************************************************************
 #
 #  Function Name:  ReturnMergedDataFrame
 #
 #  Function Description:
 #      This function receives two DataFrames, merges them into one based 
 #      on a key, index, list of keys, or list of indices and returns the 
 #      merged DataFrame.  If the operation fails, the function returns
 #      None.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          firstDataFrameParameter
 #                          This parameter is the first DataFrame
 #  DataFrame
 #          secondDataFrameParameter
 #                          This parameter is the first DataFrame
 #  String
 #          howStringParameter
 #                          This parameter specifies type of merge to be 
 #                          performed {‘left’, ‘right’, ‘outer’, ‘inner’, 
 #                          ‘cross’}. 
 # String or List
 #          onStringOrListParameter
 #                          This parameter is the column key(s) or index name(s)
 #                          to join on.  This parameter can be None, a string, 
 #                          or a list.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnMergedDataFrame \
        (firstDataFrameParameter,
         secondDataFrameParameter,
         howStringParameter,
         onStringOrListParameter):
    
    try:
        firstDataFrame \
            = firstDataFrameParameter.copy()
    
        secondDataFrame \
            = secondDataFrameParameter.copy()
    
   
        return \
            pd \
                .merge \
                    (firstDataFrame,
                     secondDataFrame,
                 how \
                     = howStringParameter,
                 on \
                     = onStringOrListParameter)
    
    except:
        
        print \
            (f'The function, returnMergedDataFrame, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to merge two Dataframes.')
        
        return \
            None
    
    
#*******************************************************************************************
 #
 #  Function Name:  ReturnStylerObjectStandardFormat
 #
 #  Function Description:
 #      This function receives a DataFrame, formats it (standard), and returns 
 #      the Styler Object to the caller.  If the operation fails, the function 
 #      returns None.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          The parameter is the input DataFrame.
 #  String
 #          captionStringParameter
 #                          The parameter is the text for the caption.
 #  Integer
 #          precisionIntegerParameter
 #                          This optional parameter is the decimal place 
 #                          precision of the displayed numbers
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnStylerObjectStandardFormat \
        (inputDataFrameParameter,
         captionStringParameter,
         precisionIntegerParameter = 2):
    
    try:
        
        inputDataFrame \
            = inputDataFrameParameter \
                .copy()
        
        return \
            inputDataFrame \
                .style \
                .set_caption \
                    (captionStringParameter) \
                .set_table_styles \
                    ([dict \
                         (selector = 'caption',
                          props = [('color', 'black'),
                                 ('font-size', '20px'),
                                 ('font-style', 'bold'),
                                 ('text-align', 'center')])]) \
                .set_properties \
                    (**{'text-align':
                            'center',
                        'border':
                        '1.3px solid red',
                        'color':
                        'blue'}) \
                .format \
                    (precision \
                        = 2, 
                     thousands \
                        = ',', 
                     decimal \
                        = '.') \
                .hide()
        
    except:
            
        print \
            (f'The function, returnStylerObjectStandardFormat, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to format a DataFrame as a Styler object.')
        
        return \
            None
    
    
#*******************************************************************************************
 #
 #  Function Name:  ReturnStylerObjectBackgroundGradientFormat
 #
 #  Function Description:
 #      This function receives a DataFrame, formats it (background gtadient), and
 #      returns the Styler Object to the caller.  If the operation fails, the
 #      function returns None.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          The parameter is the input DataFrame.
 #  String
 #          captionStringParameter
 #                          The parameter is the text for the caption.
 #  Integer
 #          precisionIntegerParameter
 #                          This optional parameter is the decimal place 
 #                          precision of the displayed numbers
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnStylerObjectBackgroundGradientFormat \
        (inputDataFrameParameter,
         captionStringParameter,
         precisionIntegerParameter = 2):
    
    try:
        
        inputDataFrame \
            = inputDataFrameParameter \
                .copy()
        
        return \
            inputDataFrame \
                .style \
                .set_caption \
                    (captionStringParameter) \
                .set_table_styles \
                    ([dict \
                         (selector = 'caption',
                          props = [('color', 'black'),
                                 ('font-size', '20px'),
                                 ('font-style', 'bold'),
                                 ('text-align', 'center')])]) \
                .set_properties \
                    (**{'text-align':
                            'center'}) \
                .format \
                    (precision \
                        = 2, 
                     thousands \
                        = ',', 
                     decimal \
                        = '.') \
                .background_gradient()
        
    except:
            
        print \
            (f'The function, returnStylerObjectStandardFormat, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to format a DataFrame as a Styler object.')
        
        return \
            None
    
#*******************************************************************************************
 #
 #  Function Name:  ReturnNumberOfUniqueElementsInColumn
 #
 #  Function Description:
 #      This function calculates and returns the number of unique elements 
 #      in a DataFrame column.  If the operation fails, the function returns 
 #      None.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          The parameter is the input DataFrame.
 #  String
 #          keyNameStringParameter
 #                          The parameter is the column key's name.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnNumberOfUniqueElementsInColumn \
    (inputDataFrameParameter,
     keyNameStringParameter):
    
    try:
        
        return \
            inputDataFrameParameter \
                [keyNameStringParameter] \
            .nunique()
        
    except:
        
        print \
            (f'The function, returnNumberOfUniqueElementsInColumnFunction, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to calculate the unique number of elements '
             + f'in a DataFrame column.')
        
        return \
            None
    
    
#*******************************************************************************************
 #
 #  Function Name:  ReturnDuplicateRowsAsDataFrame
 #
 #  Function Description:
 #      This function return duplicate rows in a DataFrame based on the
 #      particular column(s) key(s).  If the operation fails, the function 
 #      returns None.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          The parameter is the input DataFrame.
 #  String or List
 #          criteriaStringorListParameter
 #                          The parameter is the DataFrame's column name(s) 
 #                          used as criteria for the process.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnDuplicateRowsAsDataFrame \
        (inputDataFrameParameter,
         criteriaStringorListParameter):
    
    try:
        
        inputDataFrame \
            = inputDataFrameParameter.copy()
    
        return \
            inputDataFrame \
                [inputDataFrame.duplicated \
                    (subset \
                        = criteriaStringorListParameter)]
        
    except:
        
        print \
            (f'The function, returnDuplicateRowsAsDataFrame, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to return duplicate rows from a DataFrame.')
        
        return \
            None
    
#*******************************************************************************************
 #
 #  Function Name:  ReturnDataFrameRowsWithValue
 #
 #  Function Description:
 #      This function returns rows in a DataFrame with the specified value(s) in
 #      the particular column of the particular column(s).  If the operation
 #      fails, the function returns None.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          The parameter is the input DataFrame.
 #  String
 #          keyNameStringVariable
 #                          The parameter is the DataFrame column key of interest 
 #  String or List
 #          criteriaStringorListParameter
 #                          The parameter is a list of the values from the column
 #                          used as criteria in the process.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnDataFrameRowsWithValue \
        (inputDataFrameParameter,
         keyNameStringVariable,
         criteriaListParameter):
        
    try:
        
        inputDataFrame \
            = inputDataFrameParameter.copy()
    
        return \
           inputDataFrame \
                .apply \
                    (lambda row: \
                         row \
                             [inputDataFrame \
                                  [keyNameStringVariable] \
                             .isin \
                                  (criteriaListParameter)])
    
    except:
        
        print \
            (f'The function, ReturnDataFrameRowsWithValue, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to return rows with specified value(s).')
        
        return \
            None
    

#*******************************************************************************************
 #
 #  Function Name:  ReturnDataFrameRowsWithoutValue
 #
 #  Function Description:
 #      This function returns rows in a DataFrame without the specified value(s)
 #      in the particular column of the particular column(s).  If the operation
 #      fails, the function returns None.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          The parameter is the input DataFrame.
 #  String
 #          keyNameStringVariable
 #                          The parameter is the name of the DataFrame column 
 #                          of interest 
 #  String or List
 #          criteriaStringorListParameter
 #                          The parameter is a list of the values from the column
 #                          used as criteria in the process.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnDataFrameRowsWithoutValue \
        (inputDataFrameParameter,
         keyNameStringVariable,
         criteriaListParameter):
        
    try:
        
        inputDataFrame \
            = inputDataFrameParameter.copy()
    
        return \
           inputDataFrame \
                .apply \
                    (lambda row: \
                         row \
                             [~inputDataFrame \
                                  [keyNameStringVariable] \
                             .isin \
                                  (criteriaListParameter)])
    
    except:
        
        print \
            (f'The function, ReturnDataFrameRowsWithoutValue, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to return rows without specified value(s).')
        
        return \
            None
    

#*******************************************************************************************
 #
 #  Function Name:  ReturnSummaryStatisticsAsDataFrame
 #
 #  Function Description:
 #      This function returns summary statistics for a box plot from a Series of values.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          dataSeriesParameter
 #                          The parameter is the input Series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/19/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnSummaryStatisticsAsDataFrame \
        (dataSeriesParameter):

    try:
        
        # This line of code allocates the distribution for the quartiles.
        quartilesSeries \
            = dataSeriesParameter \
                .quantile \
                    ([0.25,
                      0.50,
                      0.75])
    

        # These lines of code establish the lower quartile and the upper quartile.
        lowerQuartileFloatVariable \
            = quartilesSeries \
                [0.25]

        upperQuartileFloatVariable \
            = quartilesSeries \
                [0.75]
    
 
        # This line of code calculates the interquartile range (IQR).
        interquartileRangeFloatVariable \
            = upperQuartileFloatVariable - lowerQuartileFloatVariable


        # These line of code calculate the lower bound and upper bound 
        # of the distribution.
        lowerBoundFloatVariable \
            = lowerQuartileFloatVariable - (1.5*interquartileRangeFloatVariable)
    
        upperBoundFloatVariable \
            = upperQuartileFloatVariable + (1.5*interquartileRangeFloatVariable)
    
   
        # This line of code establishes a list of outliers.
        outliersSeries \
            = dataSeriesParameter \
                .loc[(dataSeriesParameter < lowerBoundFloatVariable) \
                      | (dataSeriesParameter > upperBoundFloatVariable)]
        
        
        # This line of code finds the number of outliers.
        numberOfOutliersIntegerVariable \
            = len(outliersSeries)
  

        # These lines of code create a list of all the summary statistics and store
        # the data in a DataFrame.
        summaryStatisticsList \
            = [{'Lower Quartile':
                    lowerQuartileFloatVariable,
                'Upper Quartile':
                    upperQuartileFloatVariable,
                'Interquartile Range':
                    interquartileRangeFloatVariable,
                'Median':
                    quartilesSeries[0.5],
                'Lower Boundary':
                    lowerBoundFloatVariable,
                'Upper Boundary':
                    upperBoundFloatVariable,
                'Number of Outliers':
                    numberOfOutliersIntegerVariable}]
  
                
        return \
            pd \
                .DataFrame \
                    (summaryStatisticsList)
        
    except:
            
        print \
            (f'The function, ReturnSummaryStatisticsAsDataFrame, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to calculate summary statistics for '
             + f'a Series of values.')
            
        return \
            None

    
#*******************************************************************************************
 #
 #  Function Name:  ReturnRegressionModelEquationList
 #
 #  Function Description:
 #      This function receives a two Series for an x-y equation and the polynomial 
 #      degree for the regression and returns a list of equation coefficients.
 #
 #
 #  Function Parameters:
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
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnRegressionModelEquationList \
        (xSeriesParameter, 
         ySeriesParameter,
         degreeIntegerParameter):
    try:
        
        equationList \
            = np.poly1d \
                (np.polyfit \
                     (xSeriesParameter,
                      ySeriesParameter,
                      degreeIntegerParameter))

    
        return \
            equationList
    
    except:
        
        print \
            (f'The function, ReturnRegressionModelEquationList, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to return polynomial regression equation coefficients.')
        
        return \
            None

    
#*******************************************************************************************
 #
 #  Function Name:  ReturnPolynomialLineSeries
 #
 #  Function Description:
 #      This function receives a two Series for an x-y equation and returns a series 
 #      of y-ccordinates for the polynomial line.
 #
 #
 #  Function Parameters:
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
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnPolynomialLineSeries \
        (xSeriesParameter, 
         ySeriesParameter):
       
    try:
        sampleNumberIntegerVariable \
            = abs \
                (int \
                     ((xSeriesParameter.max() - ySeriesParameter.min()) \
                      / 2))

        return \
            np \
                .linspace \
                    (xSeriesParameter.min(), 
                     xSeriesParameter.max(), 
                     sampleNumberIntegerVariable)
    except:
        
        print \
            (f'The function, ReturnPolynomialLineSeries, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to return a polynomial regression line Series.')
        
        return \
            None

    
#*******************************************************************************************
 #
 #  Function Name:  ReturnRSquaredValue
 #
 #  Function Description:
 #      This function receives a two Series for an x-y equation and the polynomial 
 #      degree for the regression and returns the r-squared value.
 #
 #
 #  Function Parameters:
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
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnRSquaredValue \
        (xSeriesParameter, 
         ySeriesParameter, 
         degreeIntegerParameter):
    
    try:
        
        coefficientsFloatArray \
            = np \
                .polyfit \
                    (xSeriesParameter, 
                     ySeriesParameter, 
                     degreeIntegerParameter)

        pPoly1D \
            = np \
                .poly1d \
                    (coefficientsFloatArray)
    
    
        yhatList \
            = pPoly1D \
                (xSeriesParameter)
    
        ybarFloatVariable \
            = ySeriesParameter.sum() \
              / len(ySeriesParameter)
    
    
        ssregFloatVariable \
            = ((yhatList-ybarFloatVariable)**2) \
              .sum()
    
        sstotFloatVariable \
            = ((ySeriesParameter - ybarFloatVariable)**2) \
              .sum()
    
    
        resultsFloatVariable \
            = ssregFloatVariable \
              / sstotFloatVariable
    
    
        return \
             resultsFloatVariable
    
    except:
        
        print \
            (f'The function, ReturnRSquaredValue, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to return the r-squared value.')
        
        return \
            None


#*******************************************************************************************
 #
 #  Function Name:  ReturnEquationAsString
 #
 #  Function Description:
 #      This function receives a List of equation coefficients and returns the equation
 #      as a String.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  List of Float
 #          modelEquationListParameter
 #                          This parameter is the list of equation coefficients
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnEquationAsString \
        (modelEquationListParameter):
   
    try:
        
        tempDegreeIntegerVariable \
            = len \
                (modelEquationListParameter)

        equationStringVariable \
            = ''
    
    
        for index, term in enumerate(modelEquationListParameter):
            
            tempStringVariable \
                = str(round(float(term), constant.EQUATION_COEFFICIENT_PRECISION))
            
            
            if tempDegreeIntegerVariable > 1:
                
                tempStringVariable \
                    = tempStringVariable \
                        + 'x' \
                        + '^' \
                        + str \
                            (tempDegreeIntegerVariable)
                
            elif tempDegreeIntegerVariable == 1:
                
                tempStringVariable \
                    = tempStringVariable + 'x'
          
    
            if tempDegreeIntegerVariable == len(modelEquationListParameter):
            
                equationStringVariable \
                    = tempStringVariable
            
            else:
            
                equationStringVariable \
                    = equationStringVariable \
                      + ' + ' \
                      + tempStringVariable
                
            
            tempDegreeIntegerVariable \
                -= 1
        
        
        equationStringVariable \
            = 'y = ' \
              + equationStringVariable
        
        
        return \
            equationStringVariable
        
    except:
        
        print \
            (f'The function, ReturnEquationAsString, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to return the regression line as a String.')
    
        return \
            None
    
    
#*******************************************************************************************
 #
 #  Function Name:  ReturnPearsonCorrelation
 #
 #  Function Description:
 #      This function receives a two Series for an x-y equation returns the 
 #      Pearson correlation.
 #
 #
 #  Function Parameters:
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
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnPearsonCorrelation \
            (xSeriesParameter, 
             ySeriesParameter):
    
    try:
       
        return \
            xSeriesParameter \
                .corr \
                    (ySeriesParameter, 
                     method \
                         = 'pearson')
        
    except:
        
        print \
            (f'The function, ReturnPearsonCorrelation, '
             + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
             + f'was unable to return the Pearson correlation.')
    
        return \
            None


# In[ ]:




