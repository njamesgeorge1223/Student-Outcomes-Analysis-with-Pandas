#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  PymaceuticalsFunctions.py
 #
 #  File Description:
 #      This Python script, PymaceuticalsFunctions.py, contains generic 
 #      Python functions for completing common tasks in the Pymaceuticals
 #      Challenge.  Here is the list:
 #
 #      ReturnFormattedCompleteMedicalStudyStylerObject
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/20/2023      Initial Development                     Nicholas George
 #
 #******************************************************************************************/
    
import PyConstants as constant
import PyLogSubRoutines as log_subroutine


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'PymaceuticalsFunctions.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnFormattedCompleteMedicalStudyStylerObject
 #
 #  Function Description:
 #      This function receives a complete medical study DataFrame and returns 
 #      a formatted version to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          summaryDataFrameParameter
 #                          The parameter is the input DataFrame.
 #  String
 #          captionStringParameter
 #                          The parameter is the text for the caption.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnFormattedCompleteMedicalStudyStylerObject \
        (inputStylerObjectParameter,
         captionStringParameter):
    
    try:

        return \
            inputStylerObjectParameter \
                .set_caption \
                    (captionStringParameter) \
                .format \
                    ({'Mouse ID':
                            constant.GENERAL_TEXT_FORMAT, 
                      'Drug Regimen':
                            constant.GENERAL_TEXT_FORMAT, 
                      'Sex':
                            constant.GENERAL_TEXT_FORMAT, 
                      'Age_months':
                            constant.INTEGER_FORMAT,
                      'Weight (g)':
                            constant.FLOAT_FORMAT,
                      'Timepoint':
                            constant.INTEGER_FORMAT,
                      'Tumor Volume (mm3)':
                            constant.FLOAT_FORMAT,
                      'Metastatic Sites':
                            constant.INTEGER_FORMAT}) \
                .hide()
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnCSVFileAsDataFrame, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to format a medical study DataFrame.')
    
        return \
            None
    


# In[ ]:




