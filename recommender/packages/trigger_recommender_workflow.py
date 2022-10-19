import logging

from hku_recommender_and_faq.recommender.packages.ontology_profiles.student_profile.Student import *
from hku_recommender_and_faq.recommender.packages.ontology_profiles.student_profile.PersonalInfo import *
from hku_recommender_and_faq.recommender.packages.ontology_profiles.student_profile.EducationalInfo import *

from hku_recommender_and_faq.recommender.packages.ontology_profiles.course_profile.Course import *
from hku_recommender_and_faq.recommender.packages.ontology_profiles.course_profile.CourseBasicInfo import *
from hku_recommender_and_faq.recommender.packages.ontology_profiles.course_profile.CourseContent import *

from hku_recommender_and_faq.recommender.packages.helper_functions import *
from hku_recommender_and_faq.recommender.packages.generate_course_similarity import *
from hku_recommender_and_faq.recommender.packages.generate_course_recommendations import *
from hku_recommender_and_faq.recommender.packages.generate_subject_domain_recommendations import *
from hku_recommender_and_faq.recommender.packages.generate_career_recommendations import *
from hku_recommender_and_faq.recommender.packages.RecommenderIntentClassifier import *

from hku_recommender_and_faq.recommender.packages.apis import student_database_api


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
        logging.info(f'student_interest is: {student_interest}')
        if student_interest == '': further_required_info = 'student_interest'
        else: further_required_info = ''

    elif rec_type == 'subject_domain':
        '''
        For the subject domain recommender, we need to check:
        1. Student.skills
        '''
        skills = student.get_skills()
        if skills == '': further_required_info = 'skills'
        else: further_required_info = ''
    
    elif rec_type == 'career':
        '''
        For the career recommender, we need to check:
        1. Student.EducationalInfo.job_aspiration
        '''
        job_aspiration = student.get_educational_info().get_job_aspiration()
        if job_aspiration == '': further_required_info = 'job_aspiration'
        else: further_required_info = ''
            
    return further_required_info
    
'''
FUNCTION
- Generate final recommendations based on Student information
Return: TUPLE consisting of (return_type, result)
'''
def generate_final_recommendations(student: Student, rec_type: str):
    any_further_info_required = any_further_student_info_required_for_recommender(student, rec_type)
    if any_further_info_required == '':
        logging.info(f'No further information from the student required to generate {rec_type} recommendations.')
        return_type = 'recommendations'
        logging.info(f'Generating {rec_type} recommendations...')

        if rec_type == 'course':
            result, actual_string = generate_course_recommendations(student, COURSE_REC_TYPES, COURSE_BASE_DATA_PATH, COURSE_ADDITIONAL_DATA_PATH_DICT, 'cosine', K)
        elif rec_type == 'subject_domain':
            result, actual_string = generate_subject_domain_recommendations(student, SUBJECT_DOMAIN_KEYWORDS_DATA_PATH, SUBJECT_DOMAIN_MODEL_PATH, 'cosine', K, threshold=0.6)
        elif rec_type == 'career':
            result, actual_string = generate_career_recommendations(student, CAREER_BASE_DATA_PATH, CAREER_MODEL_PATHS_DICT, K)
    
    else:
        logging.info('Need further information from the student.')
        return_type = 'further_question'
        result = any_further_info_required
        actual_string = student_database_api.get_actual_string_from_email(student.get_personal_info().get_email())
        student_database_api.update_student_data(student, 'any_further_info_required', any_further_info_required)

    final_tuple = (return_type, result, actual_string)

    return final_tuple