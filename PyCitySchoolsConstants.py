#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  PyCitySchoolsConstants.py
 #
 #  File Description:
 #      This Python script, PyCitySchoolsConstants.py, contains generic Python constants
 #      for completing common tasks in the IPython file, PyCitySchools.ipynb.
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  07/30/2023      Initial Development                     N. James George
 #
 #******************************************************************************************/

from enum import Enum


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'PyCitySchoolsConstants.py'


# In[3]:


STUDENT_DATA_INPUT_FILE_PATH \
    = './Resources/studentsComplete.csv'

SCHOOL_DATA_INPUT_FILE_PATH \
    = './Resources/schoolsComplete.csv'

NUMBER_OF_DECIMAL_PLACES \
    = 2

MINIMUM_PASSING_TEST_SCORE \
    = 70


# In[4]:


# This enumeration contains column indices for the student data file.
class StudentKeysEnumeration(Enum):

    STUDENT_ID = 0

    STUDENT_NAME = 1
    
    GENDER = 2
    
    GRADE = 3
    
    SCHOOL_NAME = 4
    
    READING_SCORE = 5
    
    MATH_SCORE = 6
    

# This enumeration contains the keys for the complete school DataFrame.
class SchoolCompleteKeysEnumeration(Enum):

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
    
# This enumeration contains the keys for the school summary DataFrame.
class SchoolSummaryKeysEnumeration(Enum):
    
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


# In[ ]:




