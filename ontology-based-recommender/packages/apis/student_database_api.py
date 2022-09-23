'''
This is an API layer that:
- Converts any student from our students database to a Student instance
- Pushes additional/later information of any student to our students database

The primary key of a student's data is his/her email.
'''

from ast import Str
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
    df_students = df_students.replace(np.nan, '')
    return df_students

'''
FUNCTION
- Find the student data in our students database based on the provided email (primary key)
Return: STUDENT instance
'''
def get_student_from_email(email: Str):
    df_students = read_student_dataframe()

    # find the corresponding row in the database for that student
    df_selected_student = df_students.loc[df_students['email'] == email]
    
    # convert each attribute in the database to attributes inside the Student instance
    
    # personal info
    first_name = df_selected_student['first_name'].values[0]
    last_name = df_selected_student['last_name'].values[0]
    preferred_language = df_selected_student['preferred_language'].values[0]
    personal_info = PersonalInfo(email, first_name, last_name, preferred_language)

    # educational info
    declared_faculty = df_selected_student['declared_faculty'].values[0]
    declared_major = df_selected_student['declared_major'].values[0]
    high_school_info = df_selected_student['high_school_info'].values[0]
    student_interest = df_selected_student['student_interest'].values[0]
    job_aspiration = df_selected_student['job_aspiration'].values[0]
    educational_info = EducationalInfo(declared_faculty, declared_major, high_school_info, student_interest, job_aspiration)

    # skills
    skills = df_selected_student['skills'].values[0]

    # any_further_info_required
    any_further_info_required = df_selected_student['any_further_info_required'].values[0]

    # finally initialize the Student instance
    student = Student(personal_info, educational_info, skills, any_further_info_required)

    return student

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
- Save the updated database to the csv file location
Return: VOID
'''
def update_student_data(student: Student, new_info_type, new_info):
    df_students = read_student_dataframe()

    # get the primary key from the Student instance
    email = student.get_personal_info().get_email()

    # update data of a particular student based on the new_info_type provided
    logging.info('Updating the newly added value for \'' + new_info_type + '\' in the students database...')
    df_students.loc[df_students['email']==email, new_info_type] = new_info

    df_students = df_students.replace(np.nan, '')

    # save the newly updated dataframe to the database csv location
    df_students.to_csv(STUDENT_DATA_PATH)

'''
FUNCTION
- Delete column data for a specific student based on the attribute specified
- Save the updated database to the csv file location
'''
def delete_student_data(student: Student, info_type_to_delete):
    df_students = read_student_dataframe()

    # get the primary key from the Student instance 
    email = student.get_personal_info().get_email()

    # delete the value in the specified column
    logging.info('Deleting the \'' + info_type_to_delete + '\' in the students database...')
    df_students.loc[df_students['email']==email, info_type_to_delete] = ''

    # save the newly updated dataframe to the database csv location
    df_students.to_csv(STUDENT_DATA_PATH)