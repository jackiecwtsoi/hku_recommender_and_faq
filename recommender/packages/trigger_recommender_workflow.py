import logging, contextlib

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
from generate_career_recommendations import *
from RecommenderIntentClassifier import *

from apis import student_database_api

import nltk

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
        student_interest = student.get_educational_info().get_student_interest()
        if student_interest == '': further_required_info = 'student_interest'
        else: further_required_info = None

    elif rec_type == 'subject_domain':
        '''
        For the subject domain recommender, we need to check:
        1. Student.skills
        '''
        skills = student.get_skills()
        if skills == '': further_required_info = 'skills'
        else: further_required_info = None
    
    elif rec_type == 'career':
        '''
        For the career recommender, we need to check:
        1. Student.EducationalInfo.job_aspiration
        '''
        job_aspiration = student.get_educational_info().get_job_aspiration()
        if job_aspiration == '': further_required_info = 'job_aspiration'
        else: further_required_info = None
            
    return further_required_info
    
'''
FUNCTION
- Generate final recommendations based on Student information
Return: TUPLE consisting of (return_type, result)
'''
def generate_final_recommendations(student: Student, rec_type):
    any_further_info_required = any_further_student_info_required_for_recommender(student, rec_type)
    if any_further_info_required is None:
        logging.info(f'No further information from the student required to generate {rec_type} recommendations.')
        return_type = 'recommendations'
        logging.info(f'Generating {rec_type} recommendations...')

        if rec_type == 'course':
            result = generate_course_recommendations(student, COURSE_REC_TYPES, COURSE_BASE_DATA_PATH, COURSE_ADDITIONAL_DATA_PATH_DICT, 'cosine', K)
        elif rec_type == 'subject_domain':
            result = generate_subject_domain_recommendations(student, SUBJECT_DOMAIN_KEYWORDS_DATA_PATH, SUBJECT_DOMAIN_MODEL_PATH, 'cosine', K, threshold=0.6)
        elif rec_type == 'career':
            result = generate_career_recommendations(student, CAREER_BASE_DATA_PATH, CAREER_MODEL_PATHS_DICT, K)
    
    else:
        logging.info('Need further information from the student.')
        return_type = 'further_question'
        result = any_further_info_required
        student_database_api.update_student_data(student, 'any_further_info_required', any_further_info_required)

    final_tuple = (return_type, result)

    return final_tuple

def trigger_recommender_cycle():
    print(f'\n###########################################################')
    print(f'You have entered the recommender system.')
    print(f'###########################################################\n')
    email = input(f'Please input your EMAIL (or type \'quit\' to quit this program):\n')
    if email == 'quit': return
    student_input = input(f'Please input your QUERY (or type \'quit\' to quit this program):\n')
    while student_input != 'quit':
        trigger_single_recommender_cycle(email, student_input)
        student_input = input(f'Please input your query (or type \'quit\' to quit this program:)\n')


def trigger_single_recommender_cycle(email: str, student_response):
    student = student_database_api.get_student_from_email(email)
    recommender_intent_classifier = RecommenderIntentClassifier()
    rec_type = recommender_intent_classifier.generate_classification(student_response)
    return_type, result = generate_final_recommendations(student, rec_type)

    if return_type == 'recommendations':
        print(f'Our top {K} {rec_type} recommendations for you are:\n{result}')
    if return_type == 'further_question':
        # get the most updated student data from the database
        student = student_database_api.get_student_from_email(email)

        # get the attribute that we further need from the student
        new_info_type = student.get_any_further_info_required()
        if new_info_type != '': 
            student_answer = input(f'We need a bit more information from you. Please tell us your {" ".join(new_info_type.split("_"))}/interests/skills:\n')
            if student_answer == 'quit': return
            student_database_api.update_student_data(student, new_info_type, student_answer)

        # delete the entry in 'any_further_info_required' in the students database
        student_database_api.delete_student_data(student, 'any_further_info_required')

        trigger_single_recommender_cycle(email, student_response)

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    trigger_recommender_cycle()