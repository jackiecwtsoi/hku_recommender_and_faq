from ast import Dict, List
import logging
import numpy as np
import pandas as pd

from ontology_profiles.student_profile.Student import *
from ontology_profiles.student_profile.PersonalInfo import *
from ontology_profiles.student_profile.EducationalInfo import *

from ontology_profiles.course_profile.Course import *
from ontology_profiles.course_profile.CourseBasicInfo import *
from ontology_profiles.course_profile.CourseContent import *

from helper_functions import *
from generate_subject_domain_similarity import *
from configs import *
from apis import subject_domain_database_api

def generate_subject_domain_recommendations(student: Student, SUBJECT_DOMAIN_KEYWORDS_DATA_PATH, SUBJECT_DOMAIN_MODEL_PATH, similarity_type='cosine', k=5, threshold=0.6):
    subject_domains = subject_domain_database_api.convert_to_subject_domains(SUBJECT_DOMAIN_KEYWORDS_DATA_PATH)
    
    df_subject_domain_similarities = generate_all_subject_domain_similarities(student, subject_domains, SUBJECT_DOMAIN_MODEL_PATH, similarity_type, threshold)

    df_recommendations = df_subject_domain_similarities.head(k)

    return df_recommendations

# personal_info1 = PersonalInfo('Jackie', 'Tsoi', 'English')
# educational_info1 = EducationalInfo(STUDENT_INTEREST_TEXT)
# s1 = Student(personal_info1)
# s1.set_educational_info(educational_info1)
# s1.set_skills('computer programming, analytical skills, science, natural science, writing, speaking')
# print(s1.get_skills())

# df = generate_subject_domain_recommendations(s1, SUBJECT_DOMAIN_KEYWORDS_DATA_PATH, SUBJECT_DOMAIN_MODEL_PATH, k=K)
# print(df)