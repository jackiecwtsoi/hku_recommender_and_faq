'''
This is the layer where we generate career-related recommendations for a particular student.
'''

import pandas as pd
import logging
import joblib
from gensim.models.doc2vec import Doc2Vec

from hku_recommender_and_faq.recommender.packages.ontology_profiles.student_profile.Student import *
from hku_recommender_and_faq.recommender.packages.ontology_profiles.student_profile.PersonalInfo import *
from hku_recommender_and_faq.recommender.packages.ontology_profiles.student_profile.EducationalInfo import *


from hku_recommender_and_faq.recommender.packages.helper_functions import *
from hku_recommender_and_faq.recommender.packages.generate_course_similarity import *
from hku_recommender_and_faq.recommender.packages.configs import *

'''
FUNCTION
- Generate top k CAREER recommendations for the particular student
Return: DATAFRAME of top k recommendations (job title)
'''
def generate_career_recommendations(student: Student, CAREER_BASE_DATA_PATH, CAREER_MODEL_PATHS_DICT, k=5):
    # get the necessary student information text
    student_job_aspiration = student.get_educational_info().get_job_aspiration()
    student_interest = student.get_educational_info().get_student_interest()
    student_skills = student.get_skills()

    # concatenate all three attributes (student_interest, job_aspiration, skills) to form a string which is then used to generate the similarity score
    student_info = student_interest + '; ' + student_job_aspiration + '; ' + student_skills
    logging.debug(f'The student information based on historical inputs is:\n{student_info}')

    # predict the cluster number using the specified model (already trained)
    job_cluster = predict_job_cluster(student_info, CAREER_MODEL_PATHS_DICT)
    logging.info(f'Predicted job cluster number is: {job_cluster}')

    # get the list of top k job titles based on job cluster number
    recommendations = get_top_k_job_titles(CAREER_BASE_DATA_PATH, job_cluster, k)

    df_recommendations = pd.DataFrame(recommendations, columns=['Job Title Recommendation'])

    return df_recommendations['Job Title Recommendation'].values.tolist(), student_info


def predict_job_cluster(job_aspiration_text, CAREER_MODEL_PATHS_DICT):
    # load the specified models from local
    model_classifier = joblib.load(CAREER_MODEL_PATHS_DICT['classifier'])
    model_embeddings = Doc2Vec.load(CAREER_MODEL_PATHS_DICT['text_embeddings'])

    # get d2v embeddings of the student's text
    text_embeddings = get_individual_d2v_embeddings(job_aspiration_text, model_embeddings)

    # feed the text embeddings to the model 
    predicted_cluster = model_classifier.predict([text_embeddings])[0]

    return predicted_cluster



def get_top_k_job_titles(CAREER_BASE_DATA_PATH, job_cluster, k):
    # read the local dataframe with labeled job clusters
    df_job_postings = pd.read_csv(CAREER_BASE_DATA_PATH, index_col=0)

    recommendations = df_job_postings.loc[df_job_postings['cluster']==job_cluster]['Title'].value_counts().index[:k]
    recommendations = recommendations.tolist()
    
    return recommendations