'''
This is where we take the student provided information (text) and generate similarity scores against the courses in our recommender database.
'''
import logging
import numpy as np
import pandas as pd

from hku_recommender_and_faq.recommender.packages.ontology_profiles.student_profile.Student import *
from hku_recommender_and_faq.recommender.packages.ontology_profiles.student_profile.PersonalInfo import *
from hku_recommender_and_faq.recommender.packages.ontology_profiles.student_profile.EducationalInfo import *

from hku_recommender_and_faq.recommender.packages.ontology_profiles.course_profile.Course import *
from hku_recommender_and_faq.recommender.packages.ontology_profiles.course_profile.CourseBasicInfo import *
from hku_recommender_and_faq.recommender.packages.ontology_profiles.course_profile.CourseContent import *

from hku_recommender_and_faq.recommender.packages.helper_functions import *

from gensim.models import KeyedVectors

'''
FUNCTION
- Generate similarity score for an individual course
Return: FLOAT representing the final course similarity between the student text and that particular course info
TODO: currently only maps CourseContent but not other attributes e.g. BasicInfo or AssessmentInfo, need to add these later
'''
def generate_individual_course_similarity(student: Student, course: Course, model, similarity_type, course_rec_type):
    # # NOTE below: can also consider looping through all class variables defined in Course class instead of directly specifying
    # # print(dir(course))

    if course_rec_type == 'course_content':
        # get Student and Course attribute values for 'course_content'
        student_interest = student.get_educational_info().get_student_interest()
        course_description = course.get_course_content().get_course_description()
        course_learning_outcomes = course.get_course_content().get_course_learning_outcomes()

        # calculate similarity scores for learning outcomes and description respectively
        course_learning_outcomes_similarity_score = calculate_similarity(student_interest, course_learning_outcomes, model, similarity_type)
        course_description_similarity_score = calculate_similarity(student_interest, course_description, model, similarity_type)

        # calculate the final similarity score based on fixed weights (0.6:0.4)
        final_course_similarity = 0.6*course_learning_outcomes_similarity_score + 0.4*course_description_similarity_score

    # # TODO
    # elif course_rec_type == 'subject_domain':
    #     print('SELECTED SUBJECT DOMAIN')
    #     # get Student and Course attribute values for 'subject_domain'
    #     course_subject_domain = course.get_course_basic_info().get_subject_domain()


    return final_course_similarity

'''
FUNCTION
- Generate similarity score for all courses in our database
Return: DATAFRAME consisting of 2 columns: 'Course Code' and 'Course XXXX Similarity'
'''
def generate_all_course_similarities(student: Student, courses: list, MODEL_PATH, similarity_type, course_rec_type):
    all_course_similarities = []

    if similarity_type == 'cosine':
        # load model from MODEL_PATH
        model = KeyedVectors.load(MODEL_PATH)

    # for each course we generate a similarity score and store it inside the greater list
    for course in courses:
        course_similarity_score = generate_individual_course_similarity(student, course, model, similarity_type, course_rec_type)
        course_code = course.get_course_basic_info().get_course_code()
        course_title = course.get_course_basic_info().get_course_title()
        all_course_similarities.append( # store both the course code and similarity score
            [course_code, course_title, course_similarity_score]
        )
    
    # convert the matrix into a dataframe and sort the rows in descending order
    df = pd.DataFrame(
        all_course_similarities, 
        columns=['Course Code', 'Course Title', 'Course '+similarity_type+' Similarity']
    ).sort_values(by='Course '+similarity_type+' Similarity', ascending=False)

    return df