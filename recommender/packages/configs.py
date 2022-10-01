'''
This a file for configurations ONLY. We define any global variables to be used throughout the other files.
'''


COURSE_BASE_DATA_PATH = 'recommender/data/df_course_content_with_domain.csv'

COURSE_ADDITIONAL_DATA_PATH_DICT = {
}

SUBJECT_DOMAIN_KEYWORDS_DATA_PATH = 'recommender/data/subject_domain_keywords_top_20_yake_dict.json'

'''
CONFIG - All the types of course-related recommendations we accept
Type: LIST
'''
COURSE_REC_TYPES = [
    'course_content',
    'subject_domain'
]

'''
CONFIG - All the paths of the models used in our course-related recommender
- Key: The type of course recommendation
- Value: Path of where the model is stored
Type: DICT
'''
COURSE_MODEL_PATHS_DICT = {
    'course_content': 'recommender/models/w2v_google_news_300.model'
    # TODO
}

SUBJECT_DOMAIN_MODEL_PATH = 'recommender/models/w2v_online_job_descriptions.model'


CAREER_BASE_DATA_PATH = 'recommender/data/job_postings_labeled.csv'
CAREER_MODEL_PATHS_DICT = {
    'text_embeddings': 'recommender/models/d2v_online_job_descriptions.model',
    'classifier': 'recommender/models/clf_d2v_lr_career.joblib'
}


STUDENT_DATA_PATH = 'recommender/data/students_database.csv'

#################################################################
# Student Inputs
#################################################################
# STUDENT_INTEREST_TEXT = 'I like robots and want to do something engineering related.'
STUDENT_INTEREST_TEXT = 'I do not really know...' # FIXME
K = 5
