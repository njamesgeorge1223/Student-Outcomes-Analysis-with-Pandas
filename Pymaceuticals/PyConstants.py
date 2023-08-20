#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#*******************************************************************************************
 #
 #  File Name:  PyConstants.py
 #
 #  File Description:
 #      This Python script, PyFunctions.py, contains generic Python constants
 #      for completing common tasks.
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/20/2023      Initial Development                     Nicholas George
 #
 #******************************************************************************************/


# In[ ]:


CONSTANT_DEBUG_FLAG \
    = False


EQUATION_COEFFICIENT_PRECISION \
    = 3


GENERAL_TEXT_FORMAT \
    = '{:}'

INTEGER_FORMAT \
    = '{:,}'

FLOAT_FORMAT \
    = '{:,.2f}'

FLOAT_AS_INTEGER_FORMAT \
    = '{:,.0f}'

CURRENCY_INTEGER_FORMAT \
    = '$' + INTEGER_FORMAT

CURRENCY_FLOAT_FORMAT \
    = '$' + FLOAT_FORMAT

CURRENCY_FLOAT_AS_INTEGER_FORMAT \
    = '$' + FLOAT_AS_INTEGER_FORMAT

PERCENT_FLOAT_FORMAT \
    = FLOAT_FORMAT + '%'

