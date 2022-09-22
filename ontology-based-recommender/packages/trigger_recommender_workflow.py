from ast import List
import numpy as np
import pandas as pd
import logging

from ontology_profiles.student_profile.Student import *
from ontology_profiles.student_profile.PersonalInfo import *
from ontology_profiles.student_profile.EducationalInfo import *

from ontology_profiles.course_profile.Course import *
from ontology_profiles.course_profile.CourseBasicInfo import *
from ontology_profiles.course_profile.CourseContent import *

from helper_functions import *
from generate_course_similarity import *
from generate_course_recommendations import *
from generate_subject_domain_recommendations import *

from apis import student_database_api

'''
FUNCTION
- Determine whether the current information is sufficient to provide any recommendations on a specific rec_type
Return: STRING
'''
def any_further_student_info_required_for_recommender(student: Student, rec_type):
    if rec_type == 'course':
        '''
        For the course recommender, we need to check:
        1. Student.EducationalInfo().student_interest
        '''
        try: student.get_educational_info().get_interest()
        except: further_required_info = 'student_interest'
    elif rec_type == 'subject_domain':
        '''
        For the subject domain recommender, we need to check:
        1. Student.skills
        '''
        try: student.get_skills()
        except: further_required_info = 'student_skills'
            
    return further_required_info
    
'''
FUNCTION
- Generate final recommendations based on Student information
Return: TUPLE consisting of (return_type, result)
'''
def generate_final_recommendations(student: Student):
    # TODO: implement recommendation type

    # FIXME: delete later
    rec_type = 'course'

    if rec_type == 'course':
        try: 
            result = generate_course_recommendations(student, COURSE_REC_TYPES, COURSE_BASE_DATA_PATH, COURSE_ADDITIONAL_DATA_PATH_DICT, 'cosine', K)
            return_type = 'recommendations'
        except: 
            return_type = 'further_question'
            result = any_further_student_info_required_for_recommender(student, rec_type)

    elif rec_type == 'subject_domain':
        try:
            result = generate_subject_domain_recommendations(student, SUBJECT_DOMAIN_KEYWORDS_DATA_PATH, SUBJECT_DOMAIN_MODEL_PATH, similarity_type='cosine', k=K, threshold=0.6)
            return_type = 'recommendations'
        except:
            return_type = 'further_question'
            result = any_further_student_info_required_for_recommender(student, rec_type)

    final_tuple = (return_type, result)

    return final_tuple

def trigger_recommender_workflow(student: Student, student_response_type, student_response):
    if student_response_type == 'recommendations':
        return_type, result = generate_final_recommendations(student)
        print(return_type)
        print(result)

    elif student_response_type == 'answer':
        logging.info('This student response is an answer to our previous question - will store this answer in our students database.')
        new_info_type = student.get_any_further_info_required()
        student_database_api.update_student_data(student, new_info_type, student_response)

    elif student_response_type == 'small_talk':
        logging.info('This student response has an intent of small talk - will now switch to our small talk engine.')

    elif student_response_type == 'quit':
        logging.info('This student response has an intent of quitting our program - will now quit.')


logging.getLogger().setLevel(logging.INFO)

# NOTE: define sample Student instance
# personal_info1 = PersonalInfo('Jackie', 'Tsoi', 'tsoic1@connect.hku.hk', 'English')
personal_info1 = PersonalInfo('jtvvip1212@gmail.com')
educational_info1 = EducationalInfo(STUDENT_INTEREST_TEXT)
s1 = Student(personal_info1)
s1.set_educational_info(educational_info1)
s1.set_skills('computers and modeling')
s1.set_any_further_info_required('skills')
# print(s1.get_skills())
trigger_recommender_workflow(s1, 'answer', 'I want to learn about programming.')