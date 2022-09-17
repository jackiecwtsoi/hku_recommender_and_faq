'''
This is an API layer that converts our courses database to Course instances.
'''

from ast import Dict, List
from lib2to3.pytree import convert
import numpy as np
import pandas as pd

from ontology_profiles.student_profile.Student import *
from ontology_profiles.student_profile.PersonalInfo import *
from ontology_profiles.student_profile.EducationalInfo import *
from ontology_profiles.student_profile.Skill import *

from ontology_profiles.course_profile.Course import *
from ontology_profiles.course_profile.CourseBasicInfo import *
from ontology_profiles.course_profile.CourseContent import *

'''
FUNCTION
- to be used for pd.apply() for each row
- convert a row of a dataframe to a Course instance
Return: COURSE instance
'''
def convert_row_to_course_class(x, course_rec_type):
    if course_rec_type == 'course_content':
        course_description = x['Course Description']
        course_learning_outcomes = x['Learning Outcomes']
        course_content = CourseContent(course_description, course_learning_outcomes)
        
        course = Course(course_content)

        course_basic_info = CourseBasicInfo(x['Course Code'])
        course_basic_info.set_course_title(x['Course Title'])
        course.set_course_basic_info(course_basic_info)
    
    return course

'''
FUNCTION
- read the dataframe stored in a path (this function takes in a dictionary that maps out the data paths)
- convert the entire dataframe into a list of Course instances
Return: LIST of COURSE instances
'''
def convert_to_courses(COURSE_DATA_PATHS_DICT: Dict):
    # read the dataset from the given data paths
    df_course_contents = pd.read_csv(COURSE_DATA_PATHS_DICT['course_content'], index_col=0)
    
    # convert the dataframe into a list of Course instances
    courses = list(df_course_contents.apply(lambda x: convert_row_to_course_class(x, 'course_content'), axis=1))
    
    return courses



