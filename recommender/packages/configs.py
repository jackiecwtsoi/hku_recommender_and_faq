'''
This a file for configurations ONLY. We define any global variables to be used throughout the other files.
'''


COURSE_BASE_DATA_PATH = 'hku_recommender_and_faq/recommender/data/df_course_content_with_domain.csv'

COURSE_ADDITIONAL_DATA_PATH_DICT = {
}

SUBJECT_DOMAIN_KEYWORDS_DATA_PATH = 'hku_recommender_and_faq/recommender/data/subject_domain_keywords_top_20_yake_dict.json'

'''
CONFIG - All the types of course-related recommendations we accept
Type: LIST
'''
COURSE_REC_TYPES = [
    'course_content',
]

CF_COURSE_RECOMMENDER_DATA_PATH = 'hku_recommender_and_faq/recommender/data/recommendations_feedback_preprocessed_with_individual_ratings.csv'

'''
CONFIG - All the paths of the models used in our course-related recommender
- Key: The type of course recommendation
- Value: Path of where the model is stored
Type: DICT
'''
COURSE_MODEL_PATHS_DICT = {
    'course_content': 'hku_recommender_and_faq/recommender/models/w2v_google_news_300.model',
    'user_based_collaborative_filtering': {
        'word_embedding': 'hku_recommender_and_faq/recommender/models/w2v_google_news_300.model',
        'knn': 'hku_recommender_and_faq/recommender/models/collaborative_filtering_neighbors_knn.joblib'
    }
}

SUBJECT_DOMAIN_MODEL_PATH = 'hku_recommender_and_faq/recommender/models/w2v_online_job_descriptions.model'


CAREER_BASE_DATA_PATH = 'hku_recommender_and_faq/recommender/data/job_postings_labeled.csv'
CAREER_MODEL_PATHS_DICT = {
    'text_embeddings': 'hku_recommender_and_faq/recommender/models/d2v_online_job_descriptions.model',
    'classifier': 'hku_recommender_and_faq/recommender/models/clf_d2v_lr_career.joblib'
}

RECOMMENDER_INTENT_EMBEDDING_MODELS_DICT = {
    'glove-wiki-finetuned': {
        'type': 'glove',
        'specific_path': 'recommender_intent_classification_glove_wiki_finetuned.pkl',
        'model_file_type': 'pkl'
    }
}
DEFAULT_RECOMMENDER_INTENT_EMBEDDING_MODEL_KEY = 'glove-wiki-finetuned'

RECOMMENDER_INTENT_CLASSIFIER_MODELS_DICT = {
    'linear_svm': {
        'type': 'svm',
        'specific_path': 'clf_glove_sgd_recommender_intent_classification.joblib',
        'model_file_type': 'joblib'
    }
}
DEFAULT_RECOMMENDER_INTENT_CLASSIFIER_MODEL_KEY = 'linear_svm'

STUDENT_DATA_PATH = 'hku_recommender_and_faq/recommender/data/students_database.csv'

K = 5
