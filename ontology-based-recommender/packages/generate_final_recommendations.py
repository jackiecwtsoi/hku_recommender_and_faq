from ast import List
import numpy as np
import pandas as pd

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

def generate_final_recommendations(student: Student):
    # TODO: implement recommendation type
    rec_type = 'subject_domain'

    if rec_type == 'course':
        return generate_course_recommendations(student, COURSE_REC_TYPES, COURSE_BASE_DATA_PATH, COURSE_ADDITIONAL_DATA_PATH_DICT, 'cosine', K)
    elif rec_type == 'subject_domain':
        return generate_subject_domain_recommendations(student, SUBJECT_DOMAIN_KEYWORDS_DATA_PATH, SUBJECT_DOMAIN_MODEL_PATH, similarity_type='cosine', k=K, threshold=0.6)

# TODO: career recommendations
def generate_career_recommendations(student: Student):
    pass

# TODO: admission recommendations
def generate_admission_recommendations(student: Student):
    pass

# NOTE: define sample Student instance
personal_info1 = PersonalInfo('Jackie', 'Tsoi', 'English')
educational_info1 = EducationalInfo(STUDENT_INTEREST_TEXT)
s1 = Student(personal_info1)
s1.set_educational_info(educational_info1)
s1.set_skills('computers and modeling')
print(s1.get_skills())
df = generate_final_recommendations(s1)
print(df)