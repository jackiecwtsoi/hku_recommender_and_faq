'''
This is an API layer that converts our courses database to Course instances.
'''

from ast import Dict, List, Str
import numpy as np
import pandas as pd

from ontology_profiles.student_profile.Student import *
from ontology_profiles.student_profile.PersonalInfo import *
from ontology_profiles.student_profile.EducationalInfo import *

from ontology_profiles.course_profile.Course import *
from ontology_profiles.course_profile.CourseBasicInfo import *
from ontology_profiles.course_profile.CourseContent import *

'''
FUNCTION
- To be used for pd.apply() for each row
- Convert a row of a dataframe to a Course instance
Return: COURSE instance
'''
def convert_row_to_course_class(x, COURSE_ADDITIONAL_DATA_PATH_DICT):
    # assign basic course attributes
    course_description = x['Course Description']
    course_learning_outcomes = x['Learning Outcomes']
    course_content = CourseContent(course_description, course_learning_outcomes)

    course = Course(course_content)

    course_basic_info = CourseBasicInfo(x['Course Code'])
    course_basic_info.set_course_title(x['Course Title'])

    # course_basic_info.set_subject_domain(x['Subject Domain'])
    # subject_domain = SubjectDomain(x['Subject Domain'])

    course.set_course_basic_info(course_basic_info)

    # TODO
    # add additional attributes based on COURSE_ADDITIONAL_DATA_PATH_DICT
    
    return course

'''
FUNCTION
- Read the dataframe stored in a path
- Convert the entire dataframe into a list of Course instances
Return: LIST of COURSE instances
'''
def convert_to_courses(COURSE_BASE_DATA_PATH, COURSE_ADDITIONAL_DATA_PATH_DICT):
    # read the dataset from the given data paths
    df_course_contents = pd.read_csv(COURSE_BASE_DATA_PATH, index_col=0)
    
    # convert the dataframe into a list of Course instances
    courses = list(df_course_contents.apply(lambda x: convert_row_to_course_class(x, COURSE_ADDITIONAL_DATA_PATH_DICT), axis=1))
    
    return courses
