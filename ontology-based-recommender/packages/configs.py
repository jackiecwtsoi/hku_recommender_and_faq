'''
This a file for configurations ONLY. We define any global variables to be used throughout the other files.
'''


'''
CONFIG - All the paths of our course-related datasets for our recommender
- Key: The type of course recommendation
- Value: Path of where the dataset is stored
Type: DICT
'''
COURSE_DATA_PATHS_DICT = {
    'course_content': 'ontology-based-recommender/data/df_course_content.csv'
}


'''
CONFIG - All the types of course-related recommendations we accept
Type: LIST
'''
COURSE_REC_TYPES = [
    'course_content'
]

'''
CONFIG - All the paths of the models used in our course-related recommender
- Key: The type of course recommendation
- Value: Path of where the model is stored
Type: DICT
'''
COURSE_MODEL_PATHS_DICT = {
    'course_content': 'ontology-based-recommender/models/w2v_google_news_300.model'
}


#################################################################
# Student Inputs
#################################################################
STUDENT_INTEREST_TEXT = 'I like robots and want to do something engineering related.'
K = 5
