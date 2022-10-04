'''
This is a Python class representing the query-answer (q-A) relevance.
'''
import numpy as pd
import pandas as pd
import logging

import torch
from simpletransformers.classification import ClassificationModel

from configs import *

class QueryAnswerRelevance:
    def __init__(self, use_cuda: bool):
        self.use_cuda = use_cuda
        self.model = self.load_model(use_cuda=use_cuda, model_key=DEFAULT_QUERY_ANSWER_MODEL_KEY)
        self.faq_database = pd.read_csv(FAQ_DATABASE_PATH, index_col=0)
        logging.info(f'Query-answer (q-A) relevance instance initialized. GPU usage: {use_cuda}.')

    '''
    getters
    '''
    def get_use_cuda(self):
        return self.use_cuda

    def get_model(self):
        return self.model

    def get_faq_database(self):
        return self.faq_database

    '''
    METHOD
    - Load the Simple Transformers sentence-pair classification model from local outputs
    Return: SimpleTransformers model
    '''
    def load_model(self, model_key: str, use_cuda: bool):
        # define model path
        specific_path = QUERY_ANSWER_MODELS_DICT[model_key]['specific_path']
        model_path = 'faq/q-A_relevance/models/' + model_key + '/' + specific_path
        logging.info(f'Model path: {model_path}')

        # get model type (e.g. 'roberta' / 'bert' / 'mpnet') based on model path
        model_type = QUERY_ANSWER_MODELS_DICT[model_key]['type']
        logging.info(f'Model type: {model_type}')

        # load the model
        model = ClassificationModel(model_type, model_path, use_cuda=use_cuda)
        logging.info(f'{model_type.upper()} model loaded from {model_path}.')

        return model 

    '''
    METHOD
    - Predict the q-A relevance classification given a user query
    Return: DATAFRAME consisting of query, answer from database, predicted q-A relevance columns
    '''
    def generate_predictions(self, query: str):
        # generate query-answer pairs (list format) from our own database
        answers_from_database = self.faq_database['Answer'].tolist()
        pairs = list(map(lambda x: [query, x], answers_from_database))
        
        # generate binary classification for each pair
        predictions, _ = self.model.predict(pairs)

        # define dataframe for output
        df_predictions = pd.DataFrame(pairs, columns = ['Student Query', 'Answer from FAQ Database'])
        df_predictions['Predicted q-A Relevance'] = predictions

        logging.info(f'{len(df_predictions)} q-A relevance predictions complete for student query: \'{query}\'.')
        return df_predictions

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    use_cuda = torch.cuda.is_available()
    qa_relevance = QueryAnswerRelevance(use_cuda)
    print(qa_relevance.generate_predictions('When is the application deadline?'))
