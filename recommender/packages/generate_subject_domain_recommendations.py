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
from hku_recommender_and_faq.recommender.packages.generate_subject_domain_similarity import *
from hku_recommender_and_faq.recommender.packages.configs import *
from hku_recommender_and_faq.recommender.packages.apis import subject_domain_database_api

def generate_subject_domain_recommendations(student: Student, SUBJECT_DOMAIN_KEYWORDS_DATA_PATH, SUBJECT_DOMAIN_MODEL_PATH, similarity_type='cosine', k=5, threshold=0.6):
    subject_domains = subject_domain_database_api.convert_to_subject_domains(SUBJECT_DOMAIN_KEYWORDS_DATA_PATH)
    
    df_subject_domain_similarities = generate_all_subject_domain_similarities(student, subject_domains, SUBJECT_DOMAIN_MODEL_PATH, similarity_type, threshold)

    df_recommendations = df_subject_domain_similarities.head(k)

    return df_recommendations['Subject Domain'].values
