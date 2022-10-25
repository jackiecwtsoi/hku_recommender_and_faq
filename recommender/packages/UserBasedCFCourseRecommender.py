'''
This is a Python class reprsenting the additional User-based Collaborative Filtering (CF) Course Recommender.

Apart from our standard course recommender which maps the student query with the course description / learning objectives of 
courses from our database, we also implement a collaborative filtering based course recommender based on the actual student 
feedback we acquired, so that our course recommender's performance can be further improved.

The dataset we are using here is the feedback dataset we acquired by asking HKU students to test our program for two days.

For our new CF recommender, we implement the following steps, which follow the user-based CF method:
1. For each user, we find similar other users (i.e. neighbors) based on the query/user profile.
2. Suggest other highly rated courses based on the preferences of these similar users.

Note: Step 1 is different from conventional user-based CF recommenders. Here instead of using the ratings to find the most
similar users/neighbors for the target user, we use NLP and the kNN algorithm to find the neighbors.
'''

import logging, joblib
import pandas as pd
import numpy as np
from gensim.models import KeyedVectors

from hku_recommender_and_faq.recommender.packages.preprocess import preprocess, get_word_embeddings
from hku_recommender_and_faq.recommender.packages.configs import COURSE_MODEL_PATHS_DICT, CF_COURSE_RECOMMENDER_DATA_PATH

class UserBasedCFCourseRecommender:
    def __init__(self, student_info: str):
        self.word_embedding_model = self.load_model(COURSE_MODEL_PATHS_DICT['user_based_collaborative_filtering'], 'word_embedding')
        self.knn_model = self.load_model(COURSE_MODEL_PATHS_DICT['user_based_collaborative_filtering'], 'knn')
        self.feedback_database = self.load_feedback_database()
        
        self.student_info = student_info
        self.df_student_info = self.preprocess_student_info()
        self.student_info_embeddings = np.array(self.df_student_info['embeddings'].apply(lambda x: list(x)).tolist())
        
        self.get_top_n_neighbors()
        self.set_user_course_matrix()
        self.df_cf_scores = self.generate_cf_scores()

    '''
    getters
    '''
    def get_df_cf_scores(self):
        return self.df_cf_scores

    '''
    METHOD
    - Load the word embedding model from local
    Return: model (can be any of the supported types)
    '''
    def load_model(self, model_key: str, type: str):
        model_path = model_key[type]
        
        # load the model
        if type == 'word_embedding': 
            model = KeyedVectors.load(model_path)
            logging.info(f'Word embedding model loaded from path: {model_path}')
        elif type == 'knn': 
            model = joblib.load(model_path)
            logging.info(f'kNN model loaded from path: {model_path}')

        return model

    '''
    METHOD
    - Load the feedback database from local
    - Add 2 new columns to the dataframe: 'tokenized' and 'embeddings'
    Return: Dataframe
    '''
    def load_feedback_database(self):
        # load the database from local
        df = pd.read_csv(CF_COURSE_RECOMMENDER_DATA_PATH, index_col=0)

        # for each row, preprocess into tokenized words and then get word embeddings
        df['tokenized'] = df['actual_string'].apply(lambda x: preprocess(x))
        df['embeddings'] = df['actual_string'].apply(lambda x: get_word_embeddings(x, self.word_embedding_model))

        logging.info(f'Feedback database loaded for the CF recommender. There are {len(df)} rows.')

        return df

    '''
    METHOD
    - Preprocess the student query ('student_info') into word embeddings
    Return: Dataframe consisting of 3 columns: 'student_info', 'tokenized', 'embeddings'
    '''
    def preprocess_student_info(self):
        # initialize a dataframe to store necessary information about the student info
        df = pd.DataFrame([self.student_info], columns=['student_info'])
        df['tokenized'] = df['student_info'].apply(lambda x: preprocess(x))
        df['embeddings'] = df['student_info'].apply(lambda x: get_word_embeddings(x, self.word_embedding_model))
        logging.info(f'Dataframe to store necessary info about the student query/info is created.')
        return df
    
    '''
    METHOD
    - Find top 10 neighbors for the user input ('student_info')
    - Update the 'self.df_student_info' dataframe by adding three more columns containing info from neighbors generation
    '''
    def get_top_n_neighbors(self):
        df_neighbors_distances, df_neighbors = self.knn_model.kneighbors(
            self.student_info_embeddings, return_distance=True
        )
        # add 2 new columns ('neighbors' and 'neighbor_distances') to the 'df_student_info' database
        self.df_student_info['neighbors'] = df_neighbors.tolist()
        self.df_student_info['neighbors_distances'] = df_neighbors_distances.tolist()

        # find the corresponding 10 neighbor user emails for the student query/info
        df_neighbors_users = [self.feedback_database.loc[neighbors]['user_email'].values.tolist() for neighbors in df_neighbors]
        # add a new column called 'neighbors_users' to the 'df_student_info' database
        self.df_student_info['neighbors_users'] = df_neighbors_users

    '''
    METHOD
    - Generate user-course matrix and its normalized form and store them inside 2 new class variables
    '''
    def set_user_course_matrix(self):
        # create user-course matrix
        self.feedback_database_matrix = self.feedback_database.pivot_table(
            index='user_email', columns='result', values='rating'
        )
        # normalize the user-course matrix
        self.feedback_database_matrix_normalized = self.feedback_database_matrix.subtract(
            self.feedback_database_matrix.mean(axis=1), axis='rows'
        )

    '''
    METHOD
    - Generate all available collaborative filtering (CF) scores for the target user
    - Score is determined by the weighted average of the user similarity score ('neighbors_distances') AND the neighbors' historical course rating
    Return: Dataframe with 'Course' and 'CF Score' as columns
    '''
    def generate_cf_scores(self):
        # filter the big normalized matrix down
        similar_users = self.df_student_info['neighbors_users'].iloc[0]
        similar_user_distances = self.df_student_info['neighbors_distances'].iloc[0]
        similar_user_courses = self.feedback_database_matrix_normalized[
            self.feedback_database_matrix_normalized.index.isin(similar_users)
        ].dropna(axis=1, how='all')

        # initialize a dictionary to store course scores
        course_scores = {}
        for i in similar_user_courses.columns:
            # get the raitings for course i
            course_rating = similar_user_courses[i]
            total = 0
            count = 0

            for j, u in enumerate(similar_users):
                if pd.isna(course_rating[u]) == False: # if the course has rating by neighbor u
                    # score is the sum of user similarity score multiplied by the course rating
                    score = similar_user_distances[j] * course_rating[u]
                    total += score
                    count += 1
            # get the average score or the course
            course_scores[i] = total / count
        
        # convert the dictionary to dataframe format
        df_scores = pd.DataFrame(course_scores.items(), columns=['Course', 'CF Score'])
        df_scores = df_scores.sort_values(by='CF Score', ascending=False)

        logging.info(f'User-based collaborative filtering (CF) scores generated for the target user.')
        return df_scores

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    cf_recommender = UserBasedCFCourseRecommender()