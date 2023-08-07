# *******************************************************************************************
 #
 #  File Name:  PyCitySchools_starter.ipynb
 #
 #  File Description:
 #      This interactive Python notebook, PyCitySchools_starter.ipynb, reads two csv files,
 #      students_complete.csv and schools_complete.csv, in the Resources folder, which 
 #      contain data about students and schools in a single school district.  From this data, 
 #      the notebook performs the necessary calculations to create a high-level snapshot of 
 #      the district's key metrics. The analysis above reflects my conclusions about these 
 #      metrics.
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  07/30/2023      Initial Development                     Nicholas George
 #
 #******************************************************************************************/

import pandas as pd

from pathlib import Path
from enum import Enum


# This Boolean flag indicates whether the script is in debug mode or not.
CONSTANT_DEBUG_FLAG \
    = False


# This constant represents the minimum value for a passing test score
CONSTANT_MINIMUM_PASSING_TEST_SCORE \
    = 70


# This constant specifies two decimal places when rounding numerical values.
CONSTANT_NUMBER_OF_DECIMAL_PLACES \
    = 2


# These constants contain the names of the input file paths.
CONSTANT_STUDENT_DATA_INPUT_FILE_PATH \
    = './Resources/students_complete.csv'

CONSTANT_SCHOOL_DATA_OUTPUT_FILE_PATH \
    = './Resources/schools_complete.csv'


# These constants are the names of optional additional columns to the school 
# summary dataset; the script chooses one or the other but not both.
CONSTANT_SPENDING_RANGES_COLUMN_NAME \
    = 'Spending Ranges (Per Student)'

CONSTANT_SCHOOL_SIZE_COLUMN_NAME \
    = 'School Size'


# These constants represent data formats for display
CONSTANT_GENERAL_FORMAT \
    = '{:}'

CONSTANT_NUMBER_FORMAT \
    = '{:,}'

CONSTANT_SCORE_FORMAT \
    = '{:,.2f}'

CONSTANT_CURRENCY_FORMAT \
    = '${:,.2f}'

CONSTANT_PERCENT_FORMAT \
    = '{:,.2f}%'


# This enumeration contains column indices for the student data file.
class StudentDataKeysEnumeration(Enum):

    STUDENT_ID = 0

    STUDENT_NAME = 1
    
    GENDER = 2
    
    GRADE = 3
    
    SCHOOL_NAME = 4
    
    READING_SCORE = 5
    
    MATH_SCORE = 6
    
    
# This enumeration contains column indices for the school data file.
class SchoolDataKeysEnumeration(Enum):

    SCHOOL_ID = 0

    SCHOOL_NAME = 1
    
    TYPE = 2
    
    SIZE = 3
    
    BUDGET = 4
    
    
# This enumeration contains the keys for the complete school DataFrame.
class SchoolDataCompleteKeysEnumeration(Enum):

    STUDENT_ID = 0

    STUDENT_NAME = 1
    
    GENDER = 2
    
    GRADE = 3
    
    SCHOOL_NAME = 4
    
    READING_SCORE = 5
    
    MATH_SCORE = 6
    
    SCHOOL_ID = 7
    
    TYPE = 8
    
    SIZE = 9
    
    BUDGET = 10
    
    
# This enumeration contains the keys for the district summary DataFrame.
class DistrictSummaryDataKeysEnumeration(Enum):
    
    TOTAL_SCHOOLS = 0
    
    TOTAL_STUDENTS = 1
    
    TOTAL_BUDGET = 2 
    
    MATH_SCORE = 3
    
    READING_SCORE = 4
    
    PERCENT_PASSING_MATH = 5
    
    PERCENT_PASSING_READING = 6
    
    PERCENT_OVERALL_PASSING = 7
    
    
# This enumeration contains the keys for the school summary DataFrame.
class SchoolSummaryDataKeysEnumeration(Enum):
    
    SCHOOL_TYPE = 0
    
    TOTAL_STUDENTS = 1
    
    TOTAL_SCHOOL_BUDGET = 2 
    
    PER_STUDENT_BUDGET = 3
    
    MATH_SCORE = 4
    
    READING_SCORE = 5
    
    PERCENT_PASSING_MATH = 6
    
    PERCENT_PASSING_READING = 7
    
    PERCENT_OVERALL_PASSING = 8
    
    OPTIONAL_SPENDING_RANGES_PER_STUDENT = 9
    
    OPTIONAL_SCHOOL_SIZE = 9
    
    
# This enumeration contains the keys for the scores DataFrame.
class ScoresDataKeysEnumeration(Enum):
    
    MATH_SCORE = 0
    
    READING_SCORE = 1
    
    PERCENT_PASSING_MATH = 2
    
    PERCENT_PASSING_READING = 3
    
    PERCENT_OVERALL_PASSING = 4
       
    
# This enumeration contains keys for the financial summary DataFrame.
class FinancialDataFrameKeysEnumeration(Enum):
    
    TOTAL_STUDENTS = 0
    
    TOTAL_SCHOOL_BUDGET = 1 
    
    PER_STUDENT_BUDGET = 2
    
    
# This enumeration contains the possible options for adding a column 
# to the school summary DataFrame.
class SchoolsSummaryDataOptionalColumnEnumeration(Enum):
    
    NO_OPTIONAL_COLUMNS = 0
    
    OPTIONAL_SPENDING_RANGES_PER_STUDENT = 1
    
    OPTIONAL_SCHOOL_SIZE = 2


# This enumeration holds the indices for the captions Tuple below.
class captionsEnumeration(Enum):
    
    CAPTION_3 = 0
    
    CAPTION_4 = 1

    CAPTION_5 = 2

    CAPTION_6 = 3

    CAPTION_7 = 4

    CAPTION_8_2_1 = 5

    CAPTION_8_2_2 = 6

    CAPTION_8_2_3 = 7

    CAPTION_8_3_1 = 8

    CAPTION_8_3_2 = 9

    CAPTION_8_3_3 = 10

    CAPTION_9 = 11

    CAPTION_10_1 = 12

    CAPTION_10_2 = 13

    CAPTION_10_3 = 14

    CAPTION_11 = 15

    CAPTION_12_1 = 16

    CAPTION_12_2 = 17

    CAPTION_12_3 = 18

    CAPTION_13_1 = 19

    CAPTION_13_2 = 20

    CAPTION_13_3 = 21
    
    CAPTION_14_1 = 22
    
    CAPTION_14_2 = 23

    CAPTION_14_3 = 24

    CAPTION_15_1 = 25

    CAPTION_15_2 = 26

    CAPTION_15_3 = 27
    

# The tuple holds this Python script's captions.
captionsTuple \
    = ('Table 3: Complete School Data from Input File',
       'Table 4: Summary of School District Metrics',
       'Table 5: Summary of School Metrics',
       'Table 6: Highest-Performing Schools',
       'Table 7: Lowest-Performing Schools',

       'Table 8.2.1: Math Scores (Mean) by Grade',
       'Table 8.2.2: Math Scores (Median) by Grade',
       'Table 8.2.3: Math Scores (Mean/Median) by Grade',

       'Table 8.3.1: Reading Scores (Mean) by Grade',
       'Table 8.3.2: Reading Scores (Median) by Grade',
       'Table 8.3.3: Reading Scores (Mean/Median) by Grade',

       'Table 9: Summary of School Metrics Including Spending Ranges',

       'Table 10.1: Test Scores/Passing Rates (Mean) by Spending Ranges',
       'Table 10.2: Test Scores/Passing Rates (Median) by Spending Ranges',
       'Table 10.3: Test Scores/Passing Rates (Mean/Median) by Spending Ranges',

       'Table 11: Summary of School Metrics Including School Size',

       'Table 12.1: Test Scores/Passing Rates (Mean) by School Size',
       'Table 12.2: Test Scores/Passing Rates (Median) by School Size',
       'Table 12.3: Test Scores/Passing Rates (Mean/Median) by School Size',

       'Table 13.1: Test Scores/Passing Rates (Mean) by School Type',
       'Table 13.2: Test Scores/Passing Rates (Median) by School Type',
       'Table 13.3: Test Scores/Passing Rates (Mean/Median) by School Type',

       'Table 14.1: Student Population/Financial Data (Mean) by School Size',
       'Table 14.2: Student Population/Financial Data (Median) by School Size',
       'Table 14.3: Student Population/Financial Data (Mean/Median) by School Size',

       'Table 15.1: Student Population/Financial Data (Mean) by School Type',
       'Table 15.2: Student Population/Financial Data (Median) by School Type',
       'Table 15.3: Student Population/Financial Data (Mean/Median) by School Type')


#*******************************************************************************************
 #
 #  Function Name:  SchoolDataCompleteFormattedDisplayFunction
 #
 #  Function Description:
 #      This subroutine receives a school complete DataFrame as input, copies it to a new 
 #      DataFrame for processing, formats the new DataFrame, and returns it to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          summaryDataFrameParameter
 #                          The parameter is the input data frame.
 #  String
 #          captionStringParameter
 #                          The parameter is the text for the caption.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  7/31/2023           Initial Development                         Nicholas George
 #
 #******************************************************************************************/
    
def SchoolDataCompleteFormattedDisplayFunction \
        (summaryDataFrameParameter,
         captionStringParameter):
    
    # This line of code creates a copy of the input DataFrame for formatting
    # and display.
    summaryDataFrame \
        = summaryDataFrameParameter \
            .copy()
    
    
    # This line of code removes the index column name from the DataFrame for 
    # display purposes.
    summaryDataFrame \
        .index \
        .name \
            = None

    
    # This line of code formats the DataFrame and returns it to the caller.
    return \
        summaryDataFrame \
            .head() \
            .style \
            .set_caption \
                (captionStringParameter) \
            .set_table_styles \
                ([{'selector': 'caption', 
                   'props': \
                        [('color', 'black'), 
                         ('font-size', '16px'),
                         ('font-style', 'bold'),
                         ('text-align', 'center')]}]) \
            .set_properties \
                (**{'text-align': 'center'}) \
            .format \
                ({summaryDataFrame.keys() \
                      [SchoolDataCompleteKeysEnumeration.STUDENT_ID.value]: \
                           CONSTANT_GENERAL_FORMAT, 
                  summaryDataFrame.keys() \
                      [SchoolDataCompleteKeysEnumeration.STUDENT_NAME.value]: \
                            CONSTANT_GENERAL_FORMAT, 
                  summaryDataFrame.keys() \
                      [SchoolDataCompleteKeysEnumeration.GENDER.value]: \
                            CONSTANT_GENERAL_FORMAT,
                  summaryDataFrame.keys() \
                      [SchoolDataCompleteKeysEnumeration.GRADE.value]: \
                            CONSTANT_GENERAL_FORMAT,
                  summaryDataFrame.keys() \
                      [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]: \
                            CONSTANT_GENERAL_FORMAT,
                  summaryDataFrame.keys() \
                      [SchoolDataCompleteKeysEnumeration.READING_SCORE.value]: \
                            CONSTANT_SCORE_FORMAT,
                  summaryDataFrame.keys() \
                      [SchoolDataCompleteKeysEnumeration.MATH_SCORE.value]: \
                            CONSTANT_SCORE_FORMAT,
                  summaryDataFrame.keys() \
                      [SchoolDataCompleteKeysEnumeration.SCHOOL_ID.value]: \
                            CONSTANT_GENERAL_FORMAT,
                  summaryDataFrame.keys() \
                      [SchoolDataCompleteKeysEnumeration.TYPE.value]: \
                             CONSTANT_GENERAL_FORMAT,
                  summaryDataFrame.keys() \
                      [SchoolDataCompleteKeysEnumeration.SIZE.value]: \
                            CONSTANT_NUMBER_FORMAT,
                  summaryDataFrame.keys() \
                      [SchoolDataCompleteKeysEnumeration.BUDGET.value]: \
                            CONSTANT_CURRENCY_FORMAT}) \
            .hide()


#*******************************************************************************************
 #
 #  Function Name:  DistrictSummaryDataFormattedDisplayFunction
 #
 #  Function Description:
 #      This subroutine receives a district summary DataFrame as input, copies it to a new 
 #      DataFrame for processing, formats the new DataFrame, and returns it to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          summaryDataFrameParameter
 #                          The parameter is the input data frame.
 #  String
 #          captionStringParameter
 #                          The parameter is the text for the caption.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  07/31/2023           Initial Development                         Nicholas George
 #
 #******************************************************************************************/

def DistrictSummaryDataFormattedDisplayFunction \
        (summaryDataFrameParameter,
         captionStringParameter):
    
    # This line of code creates a copy of the input DataFrame for formatting
    # and display.
    summaryDataFrame \
        = summaryDataFrameParameter \
            .copy()
    
    
    # This line of code removes the index column name from the DataFrame for 
    # display purposes.
    summaryDataFrame \
        .index \
        .name \
            = None

    
    # This line of code formats the DataFrame and returns it to the caller.
    return \
        summaryDataFrame \
            .style \
            .set_caption \
                (captionStringParameter) \
            .set_table_styles \
                ([{'selector': 'caption', 
                   'props': \
                        [('color', 'black'), 
                         ('font-size', '16px'),
                         ('font-style', 'bold'),
                         ('text-align', 'center')]}]) \
            .set_properties \
                (**{'text-align': 'center'}) \
            .format({summaryDataFrame.keys() \
                        [DistrictSummaryDataKeysEnumeration.TOTAL_SCHOOLS.value]: \
                             CONSTANT_GENERAL_FORMAT, 
                     summaryDataFrame.keys() \
                        [DistrictSummaryDataKeysEnumeration.TOTAL_STUDENTS.value]: \
                             CONSTANT_NUMBER_FORMAT,
                     summaryDataFrame.keys() \
                        [DistrictSummaryDataKeysEnumeration.TOTAL_BUDGET.value]: \
                             CONSTANT_CURRENCY_FORMAT,              
                     summaryDataFrame.keys() \
                        [DistrictSummaryDataKeysEnumeration.MATH_SCORE.value]: \
                             CONSTANT_SCORE_FORMAT,
                     summaryDataFrame.keys() \
                        [DistrictSummaryDataKeysEnumeration.READING_SCORE.value]: \
                             CONSTANT_SCORE_FORMAT,             
                     summaryDataFrame.keys() \
                        [DistrictSummaryDataKeysEnumeration.PERCENT_PASSING_MATH.value]: \
                             CONSTANT_PERCENT_FORMAT,
                     summaryDataFrame.keys() \
                        [DistrictSummaryDataKeysEnumeration.PERCENT_PASSING_READING.value]: \
                             CONSTANT_PERCENT_FORMAT,
                     summaryDataFrame.keys() \
                        [DistrictSummaryDataKeysEnumeration.PERCENT_OVERALL_PASSING.value]: \
                             CONSTANT_PERCENT_FORMAT}) \
            .hide()


#*******************************************************************************************
 #
 #  Function Name:  SchoolSummaryDataFormattedDisplayFunction
 #
 #  Function Description:
 #      This subroutine receives a school summary DataFrame as input, copies it to a new 
 #      DataFrame for processing, formats the new DataFrame, and returns it to the caller.
 #      This function includes options for only returning the first few lines or the entire
 #      dataset, and formatting a school summary dataset or one with an additional column.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          summaryDataFrameParameter
 #                          The parameter is the input data frame.
 #  String
 #          captionStringParameter
 #                          The parameter is the text for the caption.
 #  Boolean
 #          headFlagBooleanParameter 
 #                          The parameter is the flag that specifies 
 #                          whether the head or whole table prints.
 #  Integer
 #          columnIndicatorIntegerParameter 
 #                          The optional parameter formats the dataframe 
 #                          with the original columns only or with an 
 #                          additional column based on the parameter.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/01/2023           Initial Development                         Nicholas George
 #
 #******************************************************************************************/

def SchoolSummaryDataFormattedDisplayFunction \
        (summaryDataFrameParameter,
         captionStringParameter,
         headFlagBooleanParameter,
         columnIndicatorIntegerParameter  \
             = SchoolsSummaryDataOptionalColumnEnumeration.NO_OPTIONAL_COLUMNS.value):
    
    # This line of code creates a copy of the input DataFrame for formatting
    # and display.
    summaryDataFrame \
        = summaryDataFrameParameter \
            .copy()
    
    
    # This line of code removes the index column name from the DataFrame for 
    # display purposes.
    summaryDataFrame \
        .index \
            .name \
                = None
    
    
    # These lines of code either copy the first few rows or the whole dataset 
    # based on the function parameter, headFlagBooleanParameter.
    if headFlagBooleanParameter == True:
        
        summaryDataFrame \
            = summaryDataFrameParameter \
                .head()
        
    else:
        
        summaryDataFrame \
            = summaryDataFrameParameter
    
    
    # These lines of code return a formatted school summary DataFrame or one with 
    # an additional column depending on the value of the parameter, 
    # columnIndicatorIntegerParameter.
    if columnIndicatorIntegerParameter  \
            == SchoolsSummaryDataOptionalColumnEnumeration.NO_OPTIONAL_COLUMNS.value:
        
        # This line of code formats the school summary DataFrame and returns it for 
        # display.
        return \
            summaryDataFrame \
                .style \
                .set_caption \
                    (captionStringParameter) \
                .set_table_styles \
                    ([{'selector': 'caption', 
                       'props': \
                            [('color', 'black'), 
                             ('font-size', '16px'),
                             ('font-style', 'bold'),
                             ('text-align', 'center')]}]) \
                .set_properties \
                    (**{'text-align': 'center'}) \
                .format \
                    ({summaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.SCHOOL_TYPE.value]: \
                            CONSTANT_GENERAL_FORMAT, 
                      summaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.TOTAL_STUDENTS.value]: \
                            CONSTANT_NUMBER_FORMAT,
                      summaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.TOTAL_SCHOOL_BUDGET.value]: \
                            CONSTANT_CURRENCY_FORMAT,
                      summaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PER_STUDENT_BUDGET.value]: \
                            CONSTANT_CURRENCY_FORMAT,
                      summaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.MATH_SCORE.value]: \
                            CONSTANT_SCORE_FORMAT,
                      summaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.READING_SCORE.value]: \
                            CONSTANT_SCORE_FORMAT,
                      summaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_MATH.value]: \
                            CONSTANT_PERCENT_FORMAT,
                      summaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_READING.value]: \
                            CONSTANT_PERCENT_FORMAT,
                      summaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PERCENT_OVERALL_PASSING.value]: \
                            CONSTANT_PERCENT_FORMAT}) \
                .bar \
                    (subset \
                        =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.TOTAL_STUDENTS.value],], 
                             color='powderblue') \
                .bar \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.TOTAL_SCHOOL_BUDGET.value],],
                             color='plum') \
                .bar \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.PER_STUDENT_BUDGET.value],], 
                             color='orange') \
                .highlight_max \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.MATH_SCORE.value],],
                             color='lime') \
                .highlight_max \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.READING_SCORE.value],],
                             color='lime') \
                .highlight_max \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_MATH.value],], 
                             color='lime') \
                .highlight_max \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_READING.value],],
                             color='lime') \
                .highlight_max \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.PERCENT_OVERALL_PASSING.value],], 
                             color='lime') \
                .highlight_min \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.MATH_SCORE.value],],
                             color='yellow') \
                .highlight_min \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.READING_SCORE.value],],
                             color='yellow') \
                .highlight_min \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_MATH.value],],
                             color='yellow') \
                .highlight_min \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_READING.value],],
                             color='yellow') \
                .highlight_min \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.PERCENT_OVERALL_PASSING.value],],
                             color='yellow')
    
    else:
        
        # This if selection structure chooses which additional column to add 
        # to the school summary DataFrame based on the value of the parameter, 
        # columnIndicatorIntegerParameter.
        if columnIndicatorIntegerParameter \
                == SchoolsSummaryDataOptionalColumnEnumeration \
                        .OPTIONAL_SPENDING_RANGES_PER_STUDENT \
                            .value:
            
            columnNameStringVariable \
                = summaryDataFrame.keys() \
                    [SchoolSummaryDataKeysEnumeration \
                        .OPTIONAL_SPENDING_RANGES_PER_STUDENT \
                            .value]
            
        else:
            
            columnNameStringVariable \
                = summaryDataFrame.keys() \
                    [SchoolSummaryDataKeysEnumeration \
                        .OPTIONAL_SCHOOL_SIZE \
                            .value]
        
        # This line of code formats the school summary DataFrame with its additional
        # column and returns it for display.
        return \
            summaryDataFrame \
                .style \
                .set_caption \
                    (captionStringParameter) \
                .set_table_styles \
                    ([{'selector': 'caption', 
                       'props': \
                            [('color', 'black'), 
                             ('font-size', '16px'),
                             ('font-style', 'bold'),
                             ('text-align', 'center')]}]) \
                .set_properties \
                    (**{'text-align': 'center'}) \
                .format \
                    ({summaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.SCHOOL_TYPE.value]: \
                            CONSTANT_GENERAL_FORMAT, 
                      summaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.TOTAL_STUDENTS.value]: \
                            CONSTANT_NUMBER_FORMAT,
                      summaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.TOTAL_SCHOOL_BUDGET.value]: \
                            CONSTANT_CURRENCY_FORMAT,
                      summaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PER_STUDENT_BUDGET.value]: \
                            CONSTANT_CURRENCY_FORMAT,
                      summaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.MATH_SCORE.value]: \
                            CONSTANT_SCORE_FORMAT,
                      summaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.READING_SCORE.value]: \
                            CONSTANT_SCORE_FORMAT,
                      summaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_MATH.value]: \
                            CONSTANT_PERCENT_FORMAT,
                      summaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_READING.value]: \
                            CONSTANT_PERCENT_FORMAT,
                      summaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PERCENT_OVERALL_PASSING.value]: \
                            CONSTANT_PERCENT_FORMAT,
                      columnNameStringVariable: \
                            CONSTANT_GENERAL_FORMAT}) \
                .bar \
                    (subset \
                        =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.TOTAL_STUDENTS.value],], 
                             color='powderblue') \
                .bar \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.TOTAL_SCHOOL_BUDGET.value],],
                             color='plum') \
                .bar \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.PER_STUDENT_BUDGET.value],], 
                             color='orange') \
                .highlight_max \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.MATH_SCORE.value],],
                             color='lime') \
                .highlight_max \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.READING_SCORE.value],],
                             color='lime') \
                .highlight_max \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_MATH.value],], 
                             color='lime') \
                .highlight_max \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_READING.value],],
                             color='lime') \
                .highlight_max \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.PERCENT_OVERALL_PASSING.value],], 
                             color='lime') \
                .highlight_min \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.MATH_SCORE.value],],
                             color='yellow') \
                .highlight_min \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.READING_SCORE.value],],
                             color='yellow') \
                .highlight_min \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_MATH.value],],
                             color='yellow') \
                .highlight_min \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_READING.value],],
                             color='yellow') \
                .highlight_min \
                    (subset \
                         =[summaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.PERCENT_OVERALL_PASSING.value],],
                             color='yellow')   
    
    
#*******************************************************************************************
 #
 #  Function Name:  GradesDataFormattedDisplayFunction
 #
 #  Function Description:
 #      This subroutine receives a grades DataFrame as input, copies it to a new DataFrame 
 #      for processing, formats the new DataFrame, and returns it to the caller.  This 
 #      function includes an option for whether the DataFrame contains both mean and median 
 #      data or only one of these datasets.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          summaryDataFrameParameter
 #                          The parameter is the input data frame.
 #  String
 #          captionStringParameter
 #                          The parameter is the text for the caption.
 #  Boolean
 #          combinedFlagBooleanParameter 
 #                          The optional parameter specifies whether the 
 #                          DataFrame contains both mean and median data 
 #                          or only one of these datasets.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/01/2023           Initial Development                         Nicholas George
 #
 #******************************************************************************************/

def GradesDataFormattedDisplayFunction \
        (summaryDataFrameParameter,
         captionStringParameter,
         combinedFlagBooleanParameter=False):
    
    # This line of code creates a copy of the input DataFrame for formatting
    # and display.
    summaryDataFrame \
        = summaryDataFrameParameter \
            .copy()
    
    
    # This line of code removes the index column name from the DataFrame for 
    # display purposes.
    summaryDataFrame \
        .index \
            .name \
                = None
  
 
    # These lines of code return a DataFrame containing both mean and median datasets 
    # or only one of them based on the parameter, combinedFlagBooleanParameter.
    if combinedFlagBooleanParameter == True:
        
        return \
            summaryDataFrame \
                .style \
                .set_caption \
                    (captionStringParameter) \
                .set_table_styles \
                    ([{'selector': 'caption', 
                       'props': [('color', 'black'), 
                                 ('font-size', '16px'),
                                 ('font-style', 'bold'),
                                 ('text-align', 'center')]}]) \
                .set_properties \
                    (**{'text-align': 'center',
                        'border': '1.3px solid red',
                        'color': 'blue'}) \
                .format \
                    (precision=2, 
                     thousands=',', 
                     decimal='.') \
                .highlight_max(color='lime') \
                .highlight_min(color='yellow')
        
    else:
        
        return \
            summaryDataFrame \
                .style \
                .set_caption \
                    (captionStringParameter) \
                .set_table_styles \
                    ([{'selector': 'caption', 
                       'props': [('color', 'black'), 
                                 ('font-size', '16px'),
                                 ('font-style', 'bold'),
                                 ('text-align', 'center')]}]) \
                .set_properties \
                    (**{'text-align': 'center'}) \
                .format \
                    (precision=2, 
                     thousands=',', 
                     decimal='.') \
                .background_gradient()

    
#*******************************************************************************************
 #
 #  Function Name:  ScoresDataFormattedDisplayFunction
 #
 #  Function Description:
 #      This subroutine receives a scores DataFrame as input, copies it to a new DataFrame 
 #      for processing, formats the new DataFrame, and returns it to the caller.  This 
 #      function includes an option for whether the DataFrame contains both mean and median 
 #      data or only one of these datasets.
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          summaryDataFrameParameter
 #                          The parameter is the input data frame.
 #  String
 #          captionStringParameter
 #                          The parameter is the text for the caption.
 #  Boolean
 #          combinedFlagBooleanParameter 
 #                          The optional parameter specifies whether the 
 #                          DataFrame contains both mean and median data 
 #                          or only one of these datasets.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/01/2023           Initial Development                         Nicholas George
 #
 #******************************************************************************************/

def ScoresDataFormattedDisplayFunction \
        (summaryDataFrameParameter,
         captionStringParameter,
         combinedFlagBooleanParameter=False):
         
    # This line of code creates a copy of the input DataFrame for formatting
    # and display.
    summaryDataFrame \
        = summaryDataFrameParameter \
            .copy()
    

    # This line of code removes the index column name from the DataFrame for 
    # display purposes.
    summaryDataFrame \
        .index \
            .name \
                = None
    
    
    # These lines of code return a DataFrame containing both mean and median datasets 
    # or only one of them based on the parameter, combinedFlagBooleanParameter.
    if combinedFlagBooleanParameter == True:
        
        return \
            summaryDataFrame \
                .style \
                .set_caption \
                    (captionStringParameter) \
                .set_table_styles \
                    ([{'selector': 'caption', 
                       'props': [('color', 'black'), 
                                 ('font-size', '16px'),
                                 ('font-style', 'bold'),
                                 ('text-align', 'center')]}]) \
                .set_properties \
                    (**{'text-align': 'center',
                        'border': '1.3px solid red',
                        'color': 'blue'}) \
                .format \
                    (CONSTANT_SCORE_FORMAT, 
                     subset=['Math Score']) \
                .format \
                    (CONSTANT_SCORE_FORMAT, 
                     subset=['Reading Score']) \
                .format \
                    (CONSTANT_PERCENT_FORMAT, 
                     subset=['% Passing Math']) \
                .format \
                    (CONSTANT_PERCENT_FORMAT,
                     subset=['% Passing Reading']) \
                .format \
                    (CONSTANT_PERCENT_FORMAT,
                     subset=['% Overall Passing']) \
                .highlight_max(color='lime') \
                .highlight_min(color='yellow')
         
    else:
        
        return \
            summaryDataFrame \
                .style \
                .set_caption \
                    (captionStringParameter) \
                .set_table_styles \
                    ([{'selector': 'caption', 
                       'props': [('color', 'black'), 
                                 ('font-size', '16px'),
                                 ('font-style', 'bold'),
                                 ('text-align', 'center')]}]) \
                .set_properties \
                    (**{'text-align': 'center'}) \
                .format \
                     ({summaryDataFrame.keys() \
                          [ScoresDataKeysEnumeration.MATH_SCORE.value]: \
                               CONSTANT_SCORE_FORMAT, 
                      summaryDataFrame.keys() \
                          [ScoresDataKeysEnumeration.READING_SCORE.value]: \
                                CONSTANT_SCORE_FORMAT, 
                      summaryDataFrame.keys() \
                          [ScoresDataKeysEnumeration.PERCENT_PASSING_MATH.value]: \
                                CONSTANT_PERCENT_FORMAT, 
                      summaryDataFrame.keys() \
                          [ScoresDataKeysEnumeration.PERCENT_PASSING_READING.value]: \
                                CONSTANT_PERCENT_FORMAT, 
                      summaryDataFrame.keys() \
                          [ScoresDataKeysEnumeration.PERCENT_OVERALL_PASSING.value]: \
                                CONSTANT_PERCENT_FORMAT}) \
                 .background_gradient()
   
 
#*******************************************************************************************
 #
 #  Function Name:  FinancialSummaryDataFrameFormattedDisplayFunction
 #
 #  Function Description:
 #      This subroutine receives a financial summary DataFrame as input, copies it to a 
 #      new DataFrame for processing, formats the new DataFrame, and returns it to the 
 #      caller.  This function includes an option for whether the DataFrame contains 
 #      both mean and median data or only one of these datasets.
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          summaryDataFrameParameter
 #                          The parameter is the input data frame.
 #  String
 #          captionStringParameter
 #                          The parameter is the text for the caption.
 #  Boolean
 #          combinedFlagBooleanParameter 
 #                          The optional parameter specifies whether the 
 #                          DataFrame contains both mean and median data 
 #                          or only one of these datasets.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/02/2023           Initial Development                         Nicholas George
 #
 #******************************************************************************************/

def FinancialSummaryDataFrameFormattedDisplayFunction\
        (summaryDataFrameParameter,
         captionStringParameter,
         combinedFlagBooleanParameter=False):
      
    # This line of code creates a copy of the input DataFrame for formatting
    # and display.
    summaryDataFrame \
        = summaryDataFrameParameter \
            .copy()
    
    summaryDataFrame.astype(float)
    
    
    # This line of code removes the index column name from the DataFrame for 
    # display purposes.
    summaryDataFrame \
        .index \
            .name \
                = None
    
    
    # These lines of code return a DataFrame containing both mean and median datasets 
    # or only one of them based on the parameter, combinedFlagBooleanParameter.
    if combinedFlagBooleanParameter == True:
        
        return \
            summaryDataFrame \
                .style \
                .set_caption \
                    (captionStringParameter) \
                .set_table_styles \
                    ([{'selector': 'caption', 
                       'props': [('color', 'black'), 
                                 ('font-size', '16px'),
                                 ('font-style', 'bold'),
                                 ('text-align', 'center')]}]) \
                .set_properties \
                    (**{'text-align': 'center',
                        'border': '1.3px solid red',
                        'color': 'blue'}) \
                .format \
                    (CONSTANT_SCORE_FORMAT,
                     subset=['Total Students']) \
                .format \
                    (CONSTANT_CURRENCY_FORMAT,
                    subset=['Total School Budget']) \
                .format \
                    (CONSTANT_CURRENCY_FORMAT,
                    subset=['Per Student Budget']) \
                .highlight_max(color='lime') \
                .highlight_min(color='yellow')
    
    else:

        return \
            summaryDataFrame \
                .style \
                .set_caption \
                    (captionStringParameter) \
                .set_table_styles \
                    ([{'selector': 'caption', 
                       'props': [('color', 'black'), 
                                 ('font-size', '16px'),
                                 ('font-style', 'bold'),
                                 ('text-align', 'center')]}]) \
                .set_properties \
                    (**{'text-align': 'center'}) \
                .format \
                    ({summaryDataFrame.keys() \
                          [FinancialDataFrameKeysEnumeration.TOTAL_STUDENTS.value]: \
                               CONSTANT_SCORE_FORMAT, 
                      summaryDataFrame.keys() \
                          [FinancialDataFrameKeysEnumeration.TOTAL_SCHOOL_BUDGET.value]: \
                                CONSTANT_CURRENCY_FORMAT, 
                      summaryDataFrame.keys() \
                          [FinancialDataFrameKeysEnumeration.PER_STUDENT_BUDGET.value]: \
                                CONSTANT_CURRENCY_FORMAT}) \
                 .background_gradient()


#*******************************************************************************************
 #
 #  Subroutine Name:  DebugDisplaySubRoutine
 #
 #  Subroutine Description:
 #      This subroutine prints the input object if the global debug flag, 
 #      CONSTANT_DEBUG_FLAG, is set to true.
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
 #  8/03/2023           Initial Development                         Nicholas George
 #
 #******************************************************************************************/

def DebugDisplaySubRoutine(objectUnknownTypeParameter):
    
    # This line of code displays the value of the variable if the script
    # sets the debug flag to true.
    if CONSTANT_DEBUG_FLAG == True:
        print(objectUnknownTypeParameter)
        
    
#*******************************************************************************************
 #
 #  Subroutine Name:  ConvertSeriesValuesFromArrayToScalarSubRoutine
 #
 #  Subroutine Description:
 #      This subroutine takes a Series and converts the its values from single value arrays 
 #      to scalars for display and processing.
 # 
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Unknown
 #          objectUnknownTypeParameter
 #                          The parameter is the input Series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/03/2023           Initial Development                         Nicholas George
 #
 #******************************************************************************************/
        
def ConvertSeriesValuesFromArrayToScalarSubRoutine(inputSeriesParameter):
    
    # This for loop converts the data type of each element in the series from an array to 
    # a string data type.
    for rowIndex, row in enumerate(inputSeriesParameter):
        inputSeriesParameter[rowIndex] \
            = inputSeriesParameter[rowIndex][0]
        

# These lines of code store the two input file paths in variables.
studentDataToLoadPath \
    = Path \
        (CONSTANT_STUDENT_DATA_INPUT_FILE_PATH)

schoolDataToLoadPath \
    = Path \
        (CONSTANT_SCHOOL_DATA_OUTPUT_FILE_PATH)


# These lines of code read datasets from the two input files and store them 
# in DataFrames.
studentDataFrame \
    = pd \
        .read_csv \
            (studentDataToLoadPath)

schoolDataFrame \
    = pd \
        .read_csv \
            (schoolDataToLoadPath)


# This line of code merges the two input DataFrames into a single DataFrame.
schoolDataCompleteDataFrame \
    = pd \
        .merge \
            (studentDataFrame,
             schoolDataFrame,
             how ='left',
             on =[studentDataFrame.keys() \
                        [StudentDataKeysEnumeration.SCHOOL_NAME.value],
                  studentDataFrame.keys() \
                        [StudentDataKeysEnumeration.SCHOOL_NAME.value]])


# This function formats and displays the first five lines of the new school complete DataFrame.
SchoolDataCompleteFormattedDisplayFunction \
    (schoolDataCompleteDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_3.value])


# This line of code calculates the number of schools in the school district.
numberOfSchoolsIntegerVariable \
    = schoolDataCompleteDataFrame \
        [schoolDataCompleteDataFrame.keys() \
            [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]] \
        .nunique()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG, 
# is set to True.
DebugDisplaySubRoutine \
    (numberOfSchoolsIntegerVariable)


# This line of code calculates the number of students in the school district.
numberOfStudentsIntegerVariable \
    = len \
        (schoolDataCompleteDataFrame.index)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG, 
# is set to True.
DebugDisplaySubRoutine \
    (numberOfStudentsIntegerVariable)


# This line of code calculates the total budget for the school district.
totalBudgetIntegerVariable \
    = int \
        (schoolDataCompleteDataFrame \
            .groupby \
                (schoolDataCompleteDataFrame.keys() \
                    [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]) \
                        [schoolDataCompleteDataFrame.keys() \
                            [SchoolDataCompleteKeysEnumeration.BUDGET.value]] \
        .unique() \
        .sum())


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG, 
# is set to True.
DebugDisplaySubRoutine \
    (totalBudgetIntegerVariable)


# This line of code calculates the average math score for all the students in the 
# school district.
averageMathScoreFloatVariable \
    = round \
        (schoolDataCompleteDataFrame \
            [schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.MATH_SCORE.value]] \
            .mean(),
         CONSTANT_NUMBER_OF_DECIMAL_PLACES)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG, 
# is set to True.
DebugDisplaySubRoutine \
    (averageMathScoreFloatVariable)


# This line of code calculates the average reading score for all the students in the 
# school district.
averageReadingScoreFloatVariable \
    = round \
        (schoolDataCompleteDataFrame \
            [schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.READING_SCORE.value]] \
            .mean(),
         CONSTANT_NUMBER_OF_DECIMAL_PLACES)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG, 
# is set to True.
DebugDisplaySubRoutine \
    (averageReadingScoreFloatVariable)


# These lines of code calculate the percentage of students in the school district who 
# passed math.
passingMathCountIntegerVariable \
    = schoolDataCompleteDataFrame \
        [(schoolDataCompleteDataFrame \
            [schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.MATH_SCORE.value]] \
           >= CONSTANT_MINIMUM_PASSING_TEST_SCORE)] \
        .count() \
            [schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.STUDENT_NAME.value]]

passingMathPercentageFloatVariable \
    = round \
        (float(passingMathCountIntegerVariable) \
         / float(numberOfStudentsIntegerVariable) \
         * 100,
        CONSTANT_NUMBER_OF_DECIMAL_PLACES)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG, 
# is set to True.
DebugDisplaySubRoutine \
    (passingMathPercentageFloatVariable)


# These lines of code calculate the percentage of students in the school district
# who passed reading.
passingReadingCountIntegerVariable \
    = schoolDataCompleteDataFrame \
        [(schoolDataCompleteDataFrame \
            [schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.READING_SCORE.value]] \
          >= CONSTANT_MINIMUM_PASSING_TEST_SCORE)] \
        .count() \
            [schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.STUDENT_NAME.value]]

passingReadingPercentageFloatVariable \
    = round \
        (float(passingReadingCountIntegerVariable) \
         / float(numberOfStudentsIntegerVariable) \
         * 100,
        CONSTANT_NUMBER_OF_DECIMAL_PLACES)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG, 
# is set to True.
DebugDisplaySubRoutine \
    (passingReadingPercentageFloatVariable)


# These lines of code calculate the percentage of students in the school district
# who passed both math and reading.
passingMathAndReadingCountIntegerVariable \
    = schoolDataCompleteDataFrame \
        [(schoolDataCompleteDataFrame \
            [schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.MATH_SCORE.value]] 
          >= CONSTANT_MINIMUM_PASSING_TEST_SCORE) \
       & (schoolDataCompleteDataFrame \
            [schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.READING_SCORE.value]] 
          >= CONSTANT_MINIMUM_PASSING_TEST_SCORE)] \
            .count() \
                [schoolDataCompleteDataFrame.keys() \
                    [SchoolDataCompleteKeysEnumeration.STUDENT_NAME.value]]

overallPassingRateFloatVariable \
    = round \
        (float \
             (passingMathAndReadingCountIntegerVariable) \
         / float \
             (numberOfStudentsIntegerVariable) \
         * 100,
        CONSTANT_NUMBER_OF_DECIMAL_PLACES)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG, 
# is set to True.
DebugDisplaySubRoutine \
    (overallPassingRateFloatVariable)


# This line of code creates a list of all the school district metrics and stores
# the data in a DataFrame.
districtSummaryList \
    = [{'Total Schools': \
            numberOfSchoolsIntegerVariable,
        'Total Students': \
            numberOfStudentsIntegerVariable,
        'Total Budget': \
            totalBudgetIntegerVariable,
        'Average Math Score': \
            averageMathScoreFloatVariable,
        'Average Reading Score': \
            averageReadingScoreFloatVariable,
        '% Passing Math': \
            passingMathPercentageFloatVariable,
        '% Passing Reading': \
            passingReadingPercentageFloatVariable,
        '% Overall Passing': \
            overallPassingRateFloatVariable}]


# This line of code creates a district summary DataFrame from the aforementioned list.
districtSummaryDataFrame \
    = pd \
        .DataFrame \
            (districtSummaryList)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG, 
# is set to True.
DebugDisplaySubRoutine \
    (districtSummaryDataFrame)


# This function formats and displays the district summary metrics.
DistrictSummaryDataFormattedDisplayFunction \
    (districtSummaryDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_4.value])


# This line of code takes the different unique school types in the school complete DataFrame 
# and assigns them to a Series.
schoolTypesSeries \
    = schoolDataCompleteDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys()
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys() \
                        [SchoolDataCompleteKeysEnumeration.TYPE.value]] \
        .unique()

ConvertSeriesValuesFromArrayToScalarSubRoutine \
    (schoolTypesSeries)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG, 
# is set to True.
DebugDisplaySubRoutine(schoolTypesSeries)


# This line of code calculates the number of students per school.
studentCountPerSchoolSeries \
    = schoolDataCompleteDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys() \
                        [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]] \
        .size()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG, 
# is set to True.
DebugDisplaySubRoutine \
    (studentCountPerSchoolSeries)


# This line of code calculates the budget per school.
budgetPerSchoolSeries \
    = schoolDataCompleteDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys() \
                        [SchoolDataCompleteKeysEnumeration.BUDGET.value]] \
        .unique()

ConvertSeriesValuesFromArrayToScalarSubRoutine \
    (budgetPerSchoolSeries)
        
    
# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (budgetPerSchoolSeries)


# This line of code calculates the per capita spending per school.
perCapitaSpendingPerSchoolSeries \
    = budgetPerSchoolSeries \
      / studentCountPerSchoolSeries


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG, 
# is set to True.
DebugDisplaySubRoutine \
    (perCapitaSpendingPerSchoolSeries)


# This line of code calculates the average math test score per school.
averageMathTestScorePerSchoolSeries \
    = schoolDataCompleteDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys() \
                        [SchoolDataCompleteKeysEnumeration.MATH_SCORE.value]] \
        .sum() \
      / studentCountPerSchoolSeries \
            .astype(float)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (averageMathTestScorePerSchoolSeries)


# This line of code calculates the average reading test score per school.
averageReadingScorePerSchoolSeries \
    = schoolDataCompleteDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys() \
                        [SchoolDataCompleteKeysEnumeration.READING_SCORE.value]] \
        .sum() \
      / studentCountPerSchoolSeries \
            .astype(float)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (averageReadingScorePerSchoolSeries)


# These lines of code calculate the number of students who passed math per school.
studentsPassingMathDataFrame \
    = schoolDataCompleteDataFrame \
        [(schoolDataCompleteDataFrame \
            [schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.MATH_SCORE.value]] \
          >= CONSTANT_MINIMUM_PASSING_TEST_SCORE)]

studentsPassingMathPerSchoolSeries \
    = studentsPassingMathDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame \
                [schoolDataCompleteDataFrame.keys() \
                    [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]]) \
        .size()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (studentsPassingMathPerSchoolSeries)


# These lines of code calculate the number of students who passed reading per school.
studentsPassingReadingDataFrame \
    = schoolDataCompleteDataFrame \
        [(schoolDataCompleteDataFrame \
            [schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.READING_SCORE.value]] \
          >= CONSTANT_MINIMUM_PASSING_TEST_SCORE)]

studentsPassingReadingPerSchoolSeries \
    = studentsPassingReadingDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame \
                [schoolDataCompleteDataFrame.keys() \
                    [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]]) \
        .size()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (studentsPassingReadingPerSchoolSeries)


# These lines of code calculate the number of students who passed both math and 
# reading per school.
studentsPassingMathAndReadingDataFrame \
    = schoolDataCompleteDataFrame \
        [(schoolDataCompleteDataFrame \
            [schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.MATH_SCORE.value]] \
           >= CONSTANT_MINIMUM_PASSING_TEST_SCORE) 
          & (schoolDataCompleteDataFrame \
                [schoolDataCompleteDataFrame.keys() \
                    [SchoolDataCompleteKeysEnumeration.READING_SCORE.value]] 
             >= CONSTANT_MINIMUM_PASSING_TEST_SCORE) ]

studentsPassingMathAndReadingPerSchoolSeries \
    = studentsPassingMathAndReadingDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame \
                [schoolDataCompleteDataFrame.keys() \
                    [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]]) \
        .size()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (studentsPassingMathAndReadingPerSchoolSeries)


# This line of code calculates the math passing rate per school.
mathPassingRatePerSchoolSeries \
    = (studentsPassingMathPerSchoolSeries.astype(float) \
       / studentCountPerSchoolSeries.astype(float)) \
      * 100


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (mathPassingRatePerSchoolSeries)


# This line of code calculates the reading passing rate per school.
readingPassingRatePerSchoolSeries \
    = (studentsPassingReadingPerSchoolSeries.astype(float) \
       / studentCountPerSchoolSeries.astype(float)) \
      * 100


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (readingPassingRatePerSchoolSeries)


# This line of code calculates the overall passing rate per school.
overallPassingRatePerSchoolSeries \
    = (studentsPassingMathAndReadingPerSchoolSeries.astype(float) \
       / studentCountPerSchoolSeries.astype(float)) \
      * 100


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (overallPassingRatePerSchoolSeries)


# This line of code creates a school summary DataFrame from the above calculations.
schoolSummaryDataFrame \
    = pd \
        .concat({'School Type': \
                     schoolTypesSeries,
                 'Total Students': \
                     studentCountPerSchoolSeries,
                 'Total School Budget': \
                     budgetPerSchoolSeries,
                 'Per Student Budget': \
                     perCapitaSpendingPerSchoolSeries,
                 'Average Math Score': \
                     averageMathTestScorePerSchoolSeries,
                 'Average Reading Score': \
                     averageReadingScorePerSchoolSeries,
                 '% Passing Math': \
                     mathPassingRatePerSchoolSeries,
                 '% Passing Reading': \
                     readingPassingRatePerSchoolSeries,
                 '% Overall Passing': \
                     overallPassingRatePerSchoolSeries},
                axis=1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (schoolSummaryDataFrame)


# This function formats and displays the school summary DataFrame.
SchoolSummaryDataFormattedDisplayFunction \
    (schoolSummaryDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_5.value],
     False)


# This line of code sorts the schools in descending order by the values in the column, 
# `% Overall Passing`.
topSchoolsDataFrame \
    = schoolSummaryDataFrame.sort_values \
        (by=[schoolSummaryDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.PERCENT_OVERALL_PASSING.value]],
         ascending=False)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (topSchoolsDataFrame)


# This function formats and displays the sorted school summary DataFrame.
SchoolSummaryDataFormattedDisplayFunction \
    (topSchoolsDataFrame,
     captionsTuple[captionsEnumeration.CAPTION_6.value],
     True)


# This line of code sorts the schools by the values in the column, `% Overall Passing`,
# in descending order.
lowestSchoolsDataFrame \
    = schoolSummaryDataFrame.sort_values \
        (by=[schoolSummaryDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.PERCENT_OVERALL_PASSING.value]],
         ascending=True)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (lowestSchoolsDataFrame)


# This function formats and displays the sorted school summary DataFrame.
SchoolSummaryDataFormattedDisplayFunction \
    (lowestSchoolsDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_7.value],
     True)


# These lines of code sort the school summary DataFrame into four separate DataFrames
# by grade.
ninthGraderDataFrame \
    = schoolDataCompleteDataFrame \
        [(schoolDataCompleteDataFrame \
            [schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.GRADE.value]] \
          == '9th')]

tenthGraderDataFrame \
    = schoolDataCompleteDataFrame \
        [(schoolDataCompleteDataFrame \
            [schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.GRADE.value]] \
          == '10th')]

eleventhGraderDataFrame \
    = schoolDataCompleteDataFrame \
        [(schoolDataCompleteDataFrame \
            [schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.GRADE.value]] \
          == '11th')]

twelfthGraderDataFrame \
    = schoolDataCompleteDataFrame \
        [(schoolDataCompleteDataFrame \
            [schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.GRADE.value]] \
          == '12th')]


# For each grade, these lines of code calculate the average math scores per school.
ninthGraderAverageMathScoresSeries \
    = ninthGraderDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys() \
                        [SchoolDataCompleteKeysEnumeration.MATH_SCORE.value]] \
        .mean()

tenthGraderAverageMathScoresSeries \
    = tenthGraderDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys() \
                        [SchoolDataCompleteKeysEnumeration.MATH_SCORE.value]] \
        .mean()

eleventhGraderAverageMathScoresSeries \
    = eleventhGraderDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys() \
                        [SchoolDataCompleteKeysEnumeration.MATH_SCORE.value]] \
        .mean()

twelfthGraderAverageMathScoresSeries \
    = twelfthGraderDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys() \
                        [SchoolDataCompleteKeysEnumeration.MATH_SCORE.value]] \
        .mean()


# For each grade, these lines of code calculate the median math scores per school.
ninthGraderMedianMathScoresSeries \
    = ninthGraderDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys() \
                        [SchoolDataCompleteKeysEnumeration.MATH_SCORE.value]] \
        .median()

tenthGraderMedianMathScoresSeries \
    = tenthGraderDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys() \
                        [SchoolDataCompleteKeysEnumeration.MATH_SCORE.value]] \
        .median()

eleventhGraderMedianMathScoresSeries \
    = eleventhGraderDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys() \
                        [SchoolDataCompleteKeysEnumeration.MATH_SCORE.value]] \
        .median()

twelfthGraderMedianMathScoresSeries \
    = twelfthGraderDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys() \
                        [SchoolDataCompleteKeysEnumeration.MATH_SCORE.value]] \
        .median()


# This line of code creates a DataFrame from the average math score calculations.
averageMathScoresByGradeDataFrame \
    = pd \
        .concat \
            ({'9th': \
                  ninthGraderAverageMathScoresSeries,
              '10th': \
                  tenthGraderAverageMathScoresSeries,
              '11th': \
                  eleventhGraderAverageMathScoresSeries,
              '12th': \
                  twelfthGraderAverageMathScoresSeries },
              axis=1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (averageMathScoresByGradeDataFrame)


# This line of code creates a DataFrame from the median math score calculations.
medianMathScoresByGradeDataFrame \
    = pd \
        .concat \
            ({'9th': \
                    ninthGraderMedianMathScoresSeries,
              '10th': \
                    tenthGraderMedianMathScoresSeries,
              '11th': \
                    eleventhGraderMedianMathScoresSeries,
              '12th': \
                    twelfthGraderMedianMathScoresSeries },
             axis=1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (medianMathScoresByGradeDataFrame)


# This line of code creates a DataFrame from the average math score and median math score DataFrames.
comparisonMeanAndMedianMathScoresByGradeDataFrame \
    = averageMathScoresByGradeDataFrame \
        .compare \
            (medianMathScoresByGradeDataFrame,
             align_axis=1,
             keep_shape=True,
             keep_equal=True) \
        .rename \
            (columns={'self': 'Mean',
                      'other': 'Median'},
             level=-1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (comparisonMeanAndMedianMathScoresByGradeDataFrame)


# For each grade, this function formats and displays the average math score DataFrame.
GradesDataFormattedDisplayFunction \
    (averageMathScoresByGradeDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_8_2_1.value])


# For each grade, this function formats and displays the median math score DataFrame.
GradesDataFormattedDisplayFunction \
    (medianMathScoresByGradeDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_8_2_2.value])


# For each grade, this function formats and displays a comparison of the average 
# math score and median math score DataFrames.
GradesDataFormattedDisplayFunction \
    (comparisonMeanAndMedianMathScoresByGradeDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_8_2_3.value],
     True)


# For each grade, these lines of code calculate the average reading scores per school.
ninthGraderAverageReadingScoresSeries \
    = ninthGraderDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys() \
                        [SchoolDataCompleteKeysEnumeration.READING_SCORE.value]] \
        .mean()

tenthGraderAverageReadingScoresSeries \
    = tenthGraderDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys()
                        [SchoolDataCompleteKeysEnumeration.READING_SCORE.value]] \
        .mean()

eleventhGraderAverageReadingScoresSeries \
    = eleventhGraderDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys() \
                        [SchoolDataCompleteKeysEnumeration.READING_SCORE.value]] \
        .mean()

twelfthGraderAverageReadingScoresSeries \
    = twelfthGraderDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys() \
                        [SchoolDataCompleteKeysEnumeration.READING_SCORE.value]] \
        .mean()


# For each grade, these lines of code calculate the median reading scores per school.
ninthGraderMedianReadingScoresSeries \
    = ninthGraderDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys() \
                        [SchoolDataCompleteKeysEnumeration.READING_SCORE.value]] \
        .median()

tenthGraderMedianReadingScoresSeries \
    = tenthGraderDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys() \
                        [SchoolDataCompleteKeysEnumeration.READING_SCORE.value]] \
        .median()

eleventhGraderMedianReadingScoresSeries \
    = eleventhGraderDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys() \
                        [SchoolDataCompleteKeysEnumeration.READING_SCORE.value]] \
        .median()

twelfthGraderMedianReadingScoresSeries \
    = twelfthGraderDataFrame \
        .groupby \
            ([schoolDataCompleteDataFrame.keys() \
                [SchoolDataCompleteKeysEnumeration.SCHOOL_NAME.value]]) \
                    [schoolDataCompleteDataFrame.keys() \
                        [SchoolDataCompleteKeysEnumeration.READING_SCORE.value]] \
        .median()


# This line of code creates a DataFrame from the average reading score calculations.
averageReadingScoresByGradeDataFrame \
    = pd \
        .concat \
            ({'9th': \
                    ninthGraderAverageReadingScoresSeries,
              '10th': \
                    tenthGraderAverageReadingScoresSeries,
              '11th': \
                    eleventhGraderAverageReadingScoresSeries,
              '12th': \
                    twelfthGraderAverageReadingScoresSeries },
             axis=1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (averageReadingScoresByGradeDataFrame)


# This line of code creates a DataFrame from the median reading score calculations.
medianReadingScoresByGradeDataFrame \
    = pd \
        .concat \
            ({'9th': \
                    ninthGraderMedianReadingScoresSeries,
              '10th': \
                    tenthGraderMedianReadingScoresSeries,
              '11th': \
                    eleventhGraderMedianReadingScoresSeries,
              '12th': \
                    twelfthGraderMedianReadingScoresSeries },
             axis=1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (medianReadingScoresByGradeDataFrame)


# This line of code creates a DataFrame from the average math score and median math 
# score DataFrames.
comparisonMeanAndMedianReadingScoresByGradeDataFrame \
    = averageReadingScoresByGradeDataFrame \
        .compare \
            (medianReadingScoresByGradeDataFrame,
             align_axis=1,
             keep_shape=True,
             keep_equal=True) \
        .rename \
            (columns={'self': 'Mean',
                      'other': 'Median'},
            level=-1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (comparisonMeanAndMedianReadingScoresByGradeDataFrame)


# For each grade, this function formats and displays the average reading score DataFrame.
GradesDataFormattedDisplayFunction \
    (averageReadingScoresByGradeDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_8_3_1.value])


# For each grade, this function formats and displays the median reading score DataFrame.
GradesDataFormattedDisplayFunction \
    (averageReadingScoresByGradeDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_8_3_2.value])


# For each grade, this function formats and displays a comparison of the average reading 
# score and median reading score DataFrames.
GradesDataFormattedDisplayFunction \
    (comparisonMeanAndMedianReadingScoresByGradeDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_8_3_3.value],
     True)


# This line of code establishes the bins for the spending ranges. 
schoolSpendingBinsList \
    = [0, 585, 630, 645, 680]

# This line of code establishes the labels for the spending ranges.
schoolSpendingLabelsList \
    = ['<$585', '$585-630', '$630-645', '$645-680']


# This line of code creates a copy of the school summary DataFrame 
# and assigns it to the scores by school spending DataFrame.
scoresBySchoolSpendingDataFrame \
    = schoolSummaryDataFrame \
        .copy()

# This line of code creates a new column in the scores by school spending DataFrame
# for spending ranges: the Pandas subroutine, `pd.cut`, creates the spending ranges 
# based on the predefined bins and labels and assigns them to the new column.
scoresBySchoolSpendingDataFrame \
    [CONSTANT_SPENDING_RANGES_COLUMN_NAME] \
        = pd \
            .cut \
                (x=scoresBySchoolSpendingDataFrame \
                     [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PER_STUDENT_BUDGET.value]],
                 bins=schoolSpendingBinsList,
                 labels=schoolSpendingLabelsList)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (scoresBySchoolSpendingDataFrame)


# This function formats and displays the school summary DataFrame with the new spending
# ranges column.
SchoolSummaryDataFormattedDisplayFunction \
        (scoresBySchoolSpendingDataFrame,
         captionsTuple \
             [captionsEnumeration.CAPTION_9.value],
         False,
         SchoolsSummaryDataOptionalColumnEnumeration.OPTIONAL_SPENDING_RANGES_PER_STUDENT.value)


# This line of code calculates the average math score per spending range.
scoresAverageMathScoresSeries \
    = scoresBySchoolSpendingDataFrame \
        .groupby \
            ([scoresBySchoolSpendingDataFrame.keys() \
                  [SchoolSummaryDataKeysEnumeration.OPTIONAL_SPENDING_RANGES_PER_STUDENT.value]]) \
                        [schoolSummaryDataFrame.keys() \
                            [SchoolSummaryDataKeysEnumeration.MATH_SCORE.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (scoresAverageMathScoresSeries)


# This line of code calculates the average reading score per spending range.
scoresAverageReadingScoresSeries \
    = scoresBySchoolSpendingDataFrame \
        .groupby \
            ([scoresBySchoolSpendingDataFrame.keys() \
                  [SchoolSummaryDataKeysEnumeration.OPTIONAL_SPENDING_RANGES_PER_STUDENT.value]]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.READING_SCORE.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (scoresAverageReadingScoresSeries)


# This line of code calculates the average math passing rate per spending range.
scoresAveragePassingMathSeries \
    = scoresBySchoolSpendingDataFrame \
        .groupby \
            ([scoresBySchoolSpendingDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.OPTIONAL_SPENDING_RANGES_PER_STUDENT.value]]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_MATH.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (scoresAveragePassingMathSeries)


# This line of code calculates the average reading passing rate per spending range.
scoresAveragePassingReadingSeries \
    = scoresBySchoolSpendingDataFrame \
        .groupby \
            ([scoresBySchoolSpendingDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.OPTIONAL_SPENDING_RANGES_PER_STUDENT.value]]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_READING.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (scoresAveragePassingReadingSeries)


# This line of code calculates the average overall passing rate per spending range.
scoresAveragePassingOverallSeries \
    = scoresBySchoolSpendingDataFrame \
        .groupby \
            ([scoresBySchoolSpendingDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.OPTIONAL_SPENDING_RANGES_PER_STUDENT.value]]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PERCENT_OVERALL_PASSING.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (scoresAveragePassingOverallSeries)


# This line of code calculates the median math score per spending range.
scoresMedianMathScoresSeries \
    = scoresBySchoolSpendingDataFrame \
        .groupby \
            ([scoresBySchoolSpendingDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.OPTIONAL_SPENDING_RANGES_PER_STUDENT.value]]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.MATH_SCORE.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (scoresMedianMathScoresSeries)


# This line of code calculates the median reading score per spending range.
scoresMedianReadingScoresSeries \
    = scoresBySchoolSpendingDataFrame \
        .groupby \
            ([scoresBySchoolSpendingDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.OPTIONAL_SPENDING_RANGES_PER_STUDENT.value]]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.READING_SCORE.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (scoresMedianReadingScoresSeries)

# This line of code calculates the median math passing rate per spending range.
scoresMedianPassingMathSeries \
    = scoresBySchoolSpendingDataFrame \
        .groupby \
            ([scoresBySchoolSpendingDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.OPTIONAL_SPENDING_RANGES_PER_STUDENT.value]]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_MATH.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (scoresMedianPassingMathSeries)


# This line of code calculates the median reading passing rate per spending range.
scoresMedianPassingReadingSeries \
    = scoresBySchoolSpendingDataFrame \
        .groupby \
            ([scoresBySchoolSpendingDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.OPTIONAL_SPENDING_RANGES_PER_STUDENT.value]]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_READING.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (scoresMedianPassingReadingSeries)


# This line of code calculates the median overall passing rate per spending range.
scoresMedianPassingOverallSeries \
    = scoresBySchoolSpendingDataFrame \
        .groupby \
            ([scoresBySchoolSpendingDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.OPTIONAL_SPENDING_RANGES_PER_STUDENT.value]]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PERCENT_OVERALL_PASSING.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (scoresMedianPassingOverallSeries)


# This line of code creates a DataFrame from the average score and passing rate 
# per spending range calculations.
scoresAverageSummaryDataFrame \
    = pd \
        .concat \
            ({'Math Score': \
                    scoresAverageMathScoresSeries,
              'Reading Score': \
                    scoresAverageReadingScoresSeries,
              '% Passing Math': \
                    scoresAveragePassingMathSeries,
              '% Passing Reading': \
                    scoresAveragePassingReadingSeries,
              '% Overall Passing': \
                    scoresAveragePassingOverallSeries},
             axis=1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (scoresAverageSummaryDataFrame)


# This line of code creates a DataFrame from the median score and passing rate
# per spending range calculations.
scoresMedianSummaryDataFrame \
    = pd \
        .concat \
            ({'Math Score': \
                    scoresMedianMathScoresSeries,
              'Reading Score': \
                    scoresMedianReadingScoresSeries,
              '% Passing Math': \
                    scoresMedianPassingMathSeries,
              '% Passing Reading': \
                    scoresMedianPassingReadingSeries,
              '% Overall Passing': \
                    scoresMedianPassingOverallSeries},
             axis=1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (scoresMedianSummaryDataFrame)


# This line of code creates a DataFrame from the average and median score and passing 
# rate per spending range DataFrames.
scoresComparisonMeanAndMedianSummaryDataFrame \
    = scoresAverageSummaryDataFrame \
        .compare \
            (scoresMedianSummaryDataFrame,
             align_axis=1,
             keep_shape=True,
             keep_equal=True) \
        .rename \
            (columns={'self': 'Mean',
                      'other': 'Median'},
             level=-1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (scoresComparisonMeanAndMedianSummaryDataFrame)


# This function formats and displays the average scores and passing rates per spending 
# range DataFrame.
ScoresDataFormattedDisplayFunction \
    (scoresAverageSummaryDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_10_1.value])


# This function formats and displays the median scores and passing rates per spending 
# range DataFrame.
ScoresDataFormattedDisplayFunction \
    (scoresMedianSummaryDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_10_2.value])


# This function formats and displays a comparison of the average and median scores 
# per spending range and passing rates DataFrames.njg
ScoresDataFormattedDisplayFunction \
    (scoresComparisonMeanAndMedianSummaryDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_10_3.value],
     True)


# This line of code establishes the bins for the school size column. 
schoolSizeBinsList \
    = [0, 1000, 2000, 5000]

# This line of code establishes the labels for the school size column.
schoolSizeLabelsList \
    = ['Small (<1000)', 'Medium (1000-2000)', 'Large (2000-5000)']


# This line of code creates a copy of the school summary DataFrame and assigns 
# it the the scores by school size DataFrame.
scoresBySchoolSizeDataFrame \
    = schoolSummaryDataFrame.copy()


# This line of code creates a new column in the scores by school size DataFrame
# for school size: the Pandas subroutine, `pd.cut`, creates the school sizes 
# based on the predefined bins and labels and assigns them to the new column.
scoresBySchoolSizeDataFrame[CONSTANT_SCHOOL_SIZE_COLUMN_NAME] \
    = pd \
        .cut \
            (x=scoresBySchoolSizeDataFrame \
                [schoolSummaryDataFrame.keys() \
                    [SchoolSummaryDataKeysEnumeration.TOTAL_STUDENTS.value]],
             bins=schoolSizeBinsList,
             labels=schoolSizeLabelsList)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (scoresBySchoolSizeDataFrame)


# This function formats and displays the scores by school size DataFrame with the 
# new school sizes column.
SchoolSummaryDataFormattedDisplayFunction \
        (scoresBySchoolSizeDataFrame,
         captionsTuple \
             [captionsEnumeration.CAPTION_11.value],
         False,
         SchoolsSummaryDataOptionalColumnEnumeration \
             .OPTIONAL_SCHOOL_SIZE \
                 .value)


# This line of code calculates the average math scores per school size.
sizeAverageMathScoresSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (CONSTANT_SCHOOL_SIZE_COLUMN_NAME) \
                [schoolSummaryDataFrame.keys() \
                    [SchoolSummaryDataKeysEnumeration.MATH_SCORE.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG, 
# is set to True.
DebugDisplaySubRoutine \
    (sizeAverageMathScoresSeries)


# This line of code calculates the average reading scores per school size.
sizeAverageReadingScoresSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (CONSTANT_SCHOOL_SIZE_COLUMN_NAME) \
                [schoolSummaryDataFrame.keys() \
                    [SchoolSummaryDataKeysEnumeration.READING_SCORE.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeAverageReadingScoresSeries)


# This line of code calculates the average passing math rate per school size.
sizeAveragePassingMathSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (CONSTANT_SCHOOL_SIZE_COLUMN_NAME) \
                [schoolSummaryDataFrame.keys() \
                    [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_MATH.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeAveragePassingMathSeries)


# This line of code calculates the average passing reading rate per school size.
sizeAveragePassingReadingSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (CONSTANT_SCHOOL_SIZE_COLUMN_NAME) \
                [schoolSummaryDataFrame.keys() \
                    [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_READING.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeAveragePassingReadingSeries)


# This line of code calculates the average overall passing rate per school size.
sizeAveragePassingOverallSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (CONSTANT_SCHOOL_SIZE_COLUMN_NAME) \
                [schoolSummaryDataFrame.keys() \
                    [SchoolSummaryDataKeysEnumeration.PERCENT_OVERALL_PASSING.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeAveragePassingOverallSeries)


# This line of code calculates the median math scores per school size.
sizeMedianMathScoresSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (CONSTANT_SCHOOL_SIZE_COLUMN_NAME) \
                [schoolSummaryDataFrame.keys() \
                    [SchoolSummaryDataKeysEnumeration.MATH_SCORE.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeMedianMathScoresSeries)


# This line of code calculates the median reading scores per school size.
sizeMedianReadingScoresSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (CONSTANT_SCHOOL_SIZE_COLUMN_NAME) \
                [schoolSummaryDataFrame.keys() \
                    [SchoolSummaryDataKeysEnumeration.READING_SCORE.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeMedianReadingScoresSeries)


# This line of code calculates the median passing math rate per school size.
sizeMedianPassingMathSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (CONSTANT_SCHOOL_SIZE_COLUMN_NAME) \
                [schoolSummaryDataFrame.keys() \
                    [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_MATH.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeMedianPassingMathSeries)


# This line of code calculates the median passing reading rate per school size.
sizeMedianPassingReadingSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (CONSTANT_SCHOOL_SIZE_COLUMN_NAME) \
                [schoolSummaryDataFrame.keys() \
                    [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_READING.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeMedianPassingReadingSeries)


# This line of code calculates the median overall passing rate per school size.
sizeMedianPassingOverallSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (CONSTANT_SCHOOL_SIZE_COLUMN_NAME) \
                [schoolSummaryDataFrame.keys() \
                    [SchoolSummaryDataKeysEnumeration.PERCENT_OVERALL_PASSING.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeMedianPassingOverallSeries)


# This line of code creates a DataFrame from the average score and passing rate 
# per school size calculations.
sizeAverageSummaryDataFrame \
    = pd. \
        concat \
            ({'Math Score': \
                  sizeAverageMathScoresSeries,
              'Reading Score': \
                  sizeAverageReadingScoresSeries,
              '% Passing Math': \
                  sizeAveragePassingMathSeries,
              '% Passing Reading': \
                  sizeAveragePassingReadingSeries,
              '% Overall Passing': \
                  sizeAveragePassingOverallSeries},
             axis=1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeAverageSummaryDataFrame)


# This line of code creates a DataFrame from the median score and passing rate 
# per school size calculations.
sizeMedianSummaryDataFrame \
    = pd \
        .concat \
            ({'Math Score': \
                    sizeMedianMathScoresSeries,
              'Reading Score': \
                    sizeMedianReadingScoresSeries,
              '% Passing Math': \
                    sizeMedianPassingMathSeries,
              '% Passing Reading': \
                    sizeMedianPassingReadingSeries,
              '% Overall Passing': \
                    sizeMedianPassingOverallSeries},
             axis=1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeMedianSummaryDataFrame)


# This line of code creates a DataFrame from the median and average score and 
# passing rate per school size DataFrames.
sizeComparisonMeanAndMedianSummaryDataFrame \
    = sizeAverageSummaryDataFrame \
        .compare \
            (sizeMedianSummaryDataFrame,
             align_axis=1,
             keep_shape=True,
             keep_equal=True) \
        .rename \
            (columns={'self': 'Mean', 
                      'other': 'Median'}, 
             level=-1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeComparisonMeanAndMedianSummaryDataFrame)


# This function formats and displays the average scores and passing rates per 
# school size DataFrame.
ScoresDataFormattedDisplayFunction \
    (sizeAverageSummaryDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_12_1.value])


# This function formats and displays the median scores and passing rates per 
# school size DataFrame.
ScoresDataFormattedDisplayFunction \
    (sizeMedianSummaryDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_12_2.value])


# This function formats and displays the average and median scores and passing 
# rates per school size DataFrames.
ScoresDataFormattedDisplayFunction \
    (sizeComparisonMeanAndMedianSummaryDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_12_3.value],
     True)


# This line of code calculates the average math scores per school type.
typeAverageMathScoresSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (schoolSummaryDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.SCHOOL_TYPE.value]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.MATH_SCORE.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeAverageMathScoresSeries)


# This line of code calculates the average reading scores per school type.
typeAverageReadingScoresSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (schoolSummaryDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.SCHOOL_TYPE.value]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.READING_SCORE.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeAverageReadingScoresSeries)


# This line of code calculates the average passing math rate per school type.
typeAveragePassingMathSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (schoolSummaryDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.SCHOOL_TYPE.value]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_MATH.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeAveragePassingMathSeries)


# This line of code calculates the average passing reading rate per school type.
typeAveragePassingReadingSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (schoolSummaryDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.SCHOOL_TYPE.value]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_READING.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeAveragePassingReadingSeries)


# This line of code calculates the average overall passing rate per school type.
typeAverageOverallPassingSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (schoolSummaryDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.SCHOOL_TYPE.value]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PERCENT_OVERALL_PASSING.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeAverageOverallPassingSeries)


# This line of code calculates the median math scores per school type.
typeMedianMathScoresSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (schoolSummaryDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.SCHOOL_TYPE.value]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.MATH_SCORE.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeMedianMathScoresSeries)


# This line of code calculates the median reading scores per school type.
typeMedianReadingScoresSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (schoolSummaryDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.SCHOOL_TYPE.value]) \
                    [schoolSummaryDataFrame.keys() \
                         [SchoolSummaryDataKeysEnumeration.READING_SCORE.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeMedianReadingScoresSeries)


# This line of code calculates the median passing math rate per school type.
typeMedianPassingMathSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (schoolSummaryDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.SCHOOL_TYPE.value]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_MATH.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeMedianPassingMathSeries)


# This line of code calculates the median passing reading rate per school type.
typeMedianPassingReadingSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (schoolSummaryDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.SCHOOL_TYPE.value]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PERCENT_PASSING_READING.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeMedianPassingReadingSeries)


# This line of code calculates the median overall passing rate per school type.
typeMedianOverallPassingSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (schoolSummaryDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.SCHOOL_TYPE.value]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PERCENT_OVERALL_PASSING.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeMedianOverallPassingSeries)


# This line of code creates a DataFrame from the average score and passing rate 
# per school type calculations.
typeAverageSummaryDataFrame \
    = pd \
        .concat \
            ({'Math Score': \
                    typeAverageMathScoresSeries,
              'Reading Score': \
                    typeAverageReadingScoresSeries,
              '% Passing Math': \
                    typeAveragePassingMathSeries,
              '% Passing Reading': \
                    typeAveragePassingReadingSeries,
              '% Overall Passing': \
                    typeAverageOverallPassingSeries},
             axis=1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeAverageSummaryDataFrame)


# This line of code creates a DataFrame from the median score and passing rate 
# per school type calculations.
typeMedianSummaryDataFrame \
    = pd \
        .concat \
            ({'Math Score': \
                    typeMedianMathScoresSeries,
              'Reading Score': \
                    typeMedianReadingScoresSeries,
              '% Passing Math': \
                    typeMedianPassingMathSeries,
              '% Passing Reading': \
                    typeMedianPassingReadingSeries,
              '% Overall Passing': \
                    typeMedianOverallPassingSeries},
             axis=1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeMedianSummaryDataFrame)


# This line of code creates a DataFrame from the average and median score and passing rate 
# per school type DataFrames.
typeComparisonMeanAndMedianSummaryDataFrame \
    = typeAverageSummaryDataFrame \
        .compare \
            (typeMedianSummaryDataFrame,
             align_axis=1,
             keep_shape=True,
             keep_equal=True) \
        .rename \
            (columns={'self': 'Mean',
                      'other': 'Median'},
             level=-1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeComparisonMeanAndMedianSummaryDataFrame)


# This function formats and displays the average scores and passing rates per 
# school type DataFrame.
ScoresDataFormattedDisplayFunction \
    (typeAverageSummaryDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_13_1.value])


# This function formats and displays the median scores and passing rates per 
# school type DataFrame.
ScoresDataFormattedDisplayFunction \
    (typeMedianSummaryDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_13_2.value])

# This function formats and displays a comparison of the average scores and 
# passing rates per school type DataFrames.
ScoresDataFormattedDisplayFunction \
    (typeComparisonMeanAndMedianSummaryDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_13_3.value],
     True)


# This line of code calculates the average number of students per school size.
sizeAverageTotalStudentsSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (CONSTANT_SCHOOL_SIZE_COLUMN_NAME) \
                [schoolSummaryDataFrame.keys() \
                    [SchoolSummaryDataKeysEnumeration.TOTAL_STUDENTS.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeAverageTotalStudentsSeries)

# This line of code calculates the average school budget per school size.
sizeAverageTotalSchoolBudgetSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (CONSTANT_SCHOOL_SIZE_COLUMN_NAME) \
                [schoolSummaryDataFrame.keys() \
                    [SchoolSummaryDataKeysEnumeration.TOTAL_SCHOOL_BUDGET.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeAverageTotalSchoolBudgetSeries)


# This line of code calculates the average per student budget per school size.
sizeAveragePerStudentBudgetSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (CONSTANT_SCHOOL_SIZE_COLUMN_NAME) \
                [schoolSummaryDataFrame.keys() \
                    [SchoolSummaryDataKeysEnumeration.PER_STUDENT_BUDGET.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeAveragePerStudentBudgetSeries)


# This line of code calculates the median number of students per school per school size.
sizeMedianTotalStudentsSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (CONSTANT_SCHOOL_SIZE_COLUMN_NAME) \
                [schoolSummaryDataFrame.keys() \
                     [SchoolSummaryDataKeysEnumeration.TOTAL_STUDENTS.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeMedianTotalStudentsSeries)

# This line of code calculates the median school budget per school size.
sizeMedianTotalSchoolBudgetSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (CONSTANT_SCHOOL_SIZE_COLUMN_NAME) \
                [schoolSummaryDataFrame.keys() \
                    [SchoolSummaryDataKeysEnumeration.TOTAL_SCHOOL_BUDGET.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeMedianTotalSchoolBudgetSeries)


# This line of code calculates the median per student budget per school size.
sizeMedianPerStudentBudgetSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (CONSTANT_SCHOOL_SIZE_COLUMN_NAME) \
                [schoolSummaryDataFrame.keys() \
                    [SchoolSummaryDataKeysEnumeration.PER_STUDENT_BUDGET.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeMedianPerStudentBudgetSeries)


# This line of code creates a DataFrame from the median financial summary calculations 
# per school size.
sizeAverageFinancialSummaryDataFrame \
    = pd \
        .concat \
            ({'Total Students': \
                  sizeAverageTotalStudentsSeries,
              'Total School Budget': 
                  sizeAverageTotalSchoolBudgetSeries,
              'Per Student Budget': \
                  sizeAveragePerStudentBudgetSeries},
             axis=1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeAverageFinancialSummaryDataFrame)


# This line of code creates a DataFrame from the median financial summary calculations 
# per school size.
sizeMedianFinancialSummaryDataFrame \
    = pd.concat( \
        {'Total Students': \
             sizeMedianTotalStudentsSeries,
         'Total School Budget': \
             sizeMedianTotalSchoolBudgetSeries,
         'Per Student Budget': \
             sizeMedianPerStudentBudgetSeries},
        axis=1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeMedianFinancialSummaryDataFrame)


# This line of code creates a DataFrame from the average and median financial summary 
# per school size DataFrames.
sizeComparisonMeanAndMedianFinancialSummaryDataFrame \
    = sizeAverageFinancialSummaryDataFrame \
        .compare \
            (sizeMedianFinancialSummaryDataFrame,
             align_axis=1,
             keep_shape=True,
             keep_equal=True) \
        .rename \
            (columns={'self': 'Mean', 
                      'other': 'Median'}, 
             level=-1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (sizeComparisonMeanAndMedianFinancialSummaryDataFrame)


# This function formats and displays the average financial summary per school size 
# DataFrame.
FinancialSummaryDataFrameFormattedDisplayFunction \
    (sizeAverageFinancialSummaryDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_14_1.value])


# This function formats and displays the median financial summary per school size 
# DataFrame.
FinancialSummaryDataFrameFormattedDisplayFunction \
    (sizeMedianFinancialSummaryDataFrame,
     captionsTuple \
         [captionsEnumeration.CAPTION_14_2.value])


# This function formats and displays a comparison of the average and median financial 
# summary per school size DataFrames.
FinancialSummaryDataFrameFormattedDisplayFunction \
    (sizeComparisonMeanAndMedianFinancialSummaryDataFrame,
     captionsTuple \
        [captionsEnumeration.CAPTION_14_3.value],
     True)


# This line of code calculates the average number of students per school type.
typeAverageTotalStudentsSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (schoolSummaryDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.SCHOOL_TYPE.value]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.TOTAL_STUDENTS.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeAverageTotalStudentsSeries)


# This line of code calculates the average school budget per school type.
typeAverageTotalSchoolBudgetSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (schoolSummaryDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.SCHOOL_TYPE.value]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.TOTAL_SCHOOL_BUDGET.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeAverageTotalSchoolBudgetSeries)


# This line of code calculates the average per student budget per school type.
typeAveragePerStudentBudgetSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (schoolSummaryDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.SCHOOL_TYPE.value]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PER_STUDENT_BUDGET.value]] \
        .mean()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeAveragePerStudentBudgetSeries)


# This line of code calculates the median number of students per school type.
typeMedianTotalStudentsSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (schoolSummaryDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.SCHOOL_TYPE.value]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.TOTAL_STUDENTS.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeMedianTotalStudentsSeries)


# This line of code calculates the median school budget per school type.
typeMedianTotalSchoolBudgetSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (schoolSummaryDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.SCHOOL_TYPE.value]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.TOTAL_SCHOOL_BUDGET.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeMedianTotalSchoolBudgetSeries)


# This line of code calculates the median per student budget per school type.
typeMedianPerStudentBudgetSeries \
    = scoresBySchoolSizeDataFrame \
        .groupby \
            (schoolSummaryDataFrame.keys() \
                [SchoolSummaryDataKeysEnumeration.SCHOOL_TYPE.value]) \
                    [schoolSummaryDataFrame.keys() \
                        [SchoolSummaryDataKeysEnumeration.PER_STUDENT_BUDGET.value]] \
        .median()


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeMedianPerStudentBudgetSeries)


# This line of code creates a DataFrame from the average financial summary calculations 
# per school type.
typeAverageFinancialSummaryDataFrame \
    = pd \
        .concat \
            ({'Total Students': \
                  typeAverageTotalStudentsSeries,
              'Total School Budget': \
                  typeAverageTotalSchoolBudgetSeries,
              'Per Student Budget': \
                  typeAveragePerStudentBudgetSeries},
             axis=1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine( \
    typeAverageFinancialSummaryDataFrame)


# This line of code creates a DataFrame from the median financial summary calculations 
# per school type.
typeMedianFinancialSummaryDataFrame \
    = pd \
        .concat \
            ({'Total Students': \
                  typeMedianTotalStudentsSeries,
              'Total School Budget': \
                  typeMedianTotalSchoolBudgetSeries,
              'Per Student Budget': \
                  typeMedianPerStudentBudgetSeries},
             axis=1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeMedianFinancialSummaryDataFrame)


# This line of code creates a DataFrame from the average and median financial summary 
# calculations per school type.
typeComparisonMeanAndMedianFinancialSummaryDataFrame \
    = typeAverageFinancialSummaryDataFrame \
        .compare \
            (typeMedianFinancialSummaryDataFrame,
             align_axis=1,
             keep_shape=True,
             keep_equal=True) \
        .rename \
            (columns={'self': 'Mean',
                      'other': 'Median'},
             level=-1)


# This function prints the object if the global Boolean debug flag, CONSTANT_DEBUG_FLAG,
# is set to True.
DebugDisplaySubRoutine \
    (typeComparisonMeanAndMedianFinancialSummaryDataFrame)


# This function formats and displays the average financial summary per school type 
# DataFrame.
FinancialSummaryDataFrameFormattedDisplayFunction \
    (typeAverageFinancialSummaryDataFrame,
     captionsTuple[captionsEnumeration.CAPTION_15_1.value])


# This function formats and displays the median financial summary per school type 
# DataFrame.
FinancialSummaryDataFrameFormattedDisplayFunction \
    (typeMedianFinancialSummaryDataFrame,
     captionsTuple[captionsEnumeration.CAPTION_15_2.value])


# This function formats and displays a comparison of the average and median financial 
# summary per school type DataFrames.
FinancialSummaryDataFrameFormattedDisplayFunction \
    (typeComparisonMeanAndMedianFinancialSummaryDataFrame,
     captionsTuple[captionsEnumeration.CAPTION_15_3.value],
     True)
