'''
This is a Python class representing the query-question (q-Q) similarity.
'''
import numpy as np
import pandas as pd
import logging, pickle

from gensim.models import KeyedVectors
from nltk import word_tokenize
from nltk.corpus import stopwords
from scipy import spatial

from configs import *

class QueryQuestionSimlarity:
    def __init__(self):
        self.model = self.load_model(DEFAULT_QUERY_QUESTION_MODEL_KEY)
        self.faq_database = pd.read_csv(FAQ_DATABASE_PATH, index_col=0)
        logging.info(f'Query-question (q-Q) similarity instance initialized.')

    '''
    getters
    '''
    def get_cpu_count(self):
        return self.cpu_count

    def get_model(self):
        return self.model
    
    def get_faq_database(self):
        return self.faq_database
    
    '''
    METHOD
    - Get word embeddings using our trained model
    Return: LIST/ARRAY of floats representing the text
    '''
    def get_word_embeddings(self, text, model):
        tokenized = self.preprocess(text)
        word_embeddings = np.mean(np.array([model[i] for i in tokenized]), axis=0)
        return word_embeddings

    '''
    METHOD
    - Preprocess the text to tokenized form
    Return: LIST of words representing the tokenized text
    '''
    def preprocess(self, text):
        text = text.lower() # convert all letters to lowercase
        words = word_tokenize(text) # tokanize each sentence
        words = [word for word in words if word.isalpha()]

        # handle stopwords
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if not word in stop_words]
        return words

    '''
    METHOD
    - Load the word embedding model from local
    Return: model (can be any of the supported types)
    '''
    def load_model(self, model_key: str):
        # define model path
        specific_path = QUERY_QUESTION_MODELS_DICT[model_key]['specific_path']
        model_path = 'faq/q-Q_similarity/models/' + specific_path
        self.model_path = model_path
        logging.info(f'Model path: {model_path}')
        
        # get the model type and file type based on model path
        model_type = QUERY_QUESTION_MODELS_DICT[model_key]['type']
        self.model_type = model_type
        model_file_type = QUERY_QUESTION_MODELS_DICT[model_key]['model_file_type']
        self.model_file_type = model_file_type
        logging.info(f'Model type: {model_type}')

        # load the model based on the model and model file types
        if model_file_type == 'pkl':
            with open(model_path, 'rb') as f:
                model = pickle.load(f)
        elif model_file_type == 'model':
            model = KeyedVectors.load(model_path)
        logging.info(f'{model_type.upper()} model loaded from {model_path}.')

        return model

    '''
    METHOD
    - Predict the q-Q similarity scores given a user query
    Return: DATAFRAME consisting of query, question from database, predicted q-Q similarity columns
    '''
    def generate_similarity_scores(self, query: str):
        # generate query-question pairs
        questions_from_database = self.faq_database['Question'].tolist()

        # get word embeddings for student query
        try: query_embeddings = self.get_word_embeddings(query, self.model)
        except: logging.info(f'Could not generate {self.model_type} word embeddings for query: {query}')

        # generate similarity score for every q-Q pair using our FAQ database
        similarities = []
        for q in questions_from_database:
            try:
                question_embeddings = self.get_word_embeddings(q, self.model)
                # get the cosine similarity score
                similarity_score = 1 - spatial.distance.cosine(query_embeddings, question_embeddings)
            except:
                similarity_score = 0
                logging.debug(f'Could not generate similarity score for:\nQuery: {query}, Question: {q}')
            similarities.append([query, q, similarity_score])
        
        # define dataframe for output
        df_similarities = pd.DataFrame(
            similarities, columns=['Student Query', 'Question from FAQ Database', 'Predicted Cosine q-Q Similarity']
        )
        logging.info(f'{len(df_similarities)} q-Q similarity predictions complete for student query: \'{query}\'.')
            
        return df_similarities
                

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    qq_similarity = QueryQuestionSimlarity()
    print(qq_similarity.generate_similarity_scores('When is the application deadline?'))
    
    
