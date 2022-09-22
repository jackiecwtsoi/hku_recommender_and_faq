'''
This is an API layer that:
- Converts any student from our students database to a Student instance
- Pushes additional/later information of any student to our students database

The primary key of a student's data is his/her email.
'''

import numpy as np
import pandas as pd
import logging

from ontology_profiles.student_profile.Student import *
from ontology_profiles.student_profile.PersonalInfo import *
from ontology_profiles.student_profile.EducationalInfo import *

from configs import STUDENT_DATA_PATH

'''
FUNCTION
- Read the dataframe from the STUDENT_DATA_PATH
Return: DATAFRAME
'''
def read_student_dataframe():
    df_students = pd.read_csv(STUDENT_DATA_PATH, index_col=0)
    return df_students

'''
FUNCTION
- Add a new student into our students database and subsequently saves the new database
Return: VOID
'''
# TODO
def add_new_student(student: Student):
    pass

'''
FUNCTION
- Update data for a specific student based on the additional info provided
- Save the new database to the csv file location
Return: VOID
'''
def update_student_data(student: Student, new_info_type, new_info):
    df_students = read_student_dataframe()

    # get the primary key from the Student instance
    email = student.get_personal_info().get_email()

    # update data of a particular student based on the new_info_type provided
    logging.info('Updating the newly added value for \'' + new_info_type + '\' in the students database...')
    df_students.loc[df_students['email']==email, new_info_type] = new_info

    # save the newly updated dataframe to the database csv location
    df_students.to_csv(STUDENT_DATA_PATH)