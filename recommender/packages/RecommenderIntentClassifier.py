'''
This is a Python class representing the recommender intent classifier, 
which identifies whether the student user wants a recommendation on career, subject domain, or specific course.
'''
import logging, pickle, joblib

from preprocess import get_word_embeddings
from configs import *

class RecommenderIntentClassifier:
    def __init__(self):
        self.word_embedding_model = self.load_model(DEFAULT_RECOMMENDER_INTENT_EMBEDDING_MODEL_KEY, 'word_embedding')
        self.classifier = self.load_model(DEFAULT_RECOMMENDER_INTENT_CLASSIFIER_MODEL_KEY, 'classifier')
        logging.info(f'Recommender intent classifier instance initialized.')

    '''
    getters
    '''
    def get_word_embedding_model(self):
        return self.word_embedding_model

    def get_classifier(self):
        return self.classifier
    
    '''
    METHOD
    - Load the word embedding or classifier model from local
    Return: model (can be any of the supported types)
    '''
    def load_model(self, model_key: str, type: str):
        if type == 'word_embedding': model_path_dict = RECOMMENDER_INTENT_EMBEDDING_MODELS_DICT
        elif type == 'classifier': model_path_dict = RECOMMENDER_INTENT_CLASSIFIER_MODELS_DICT

        # define model path
        specific_path = model_path_dict[model_key]['specific_path']
        model_path = 'recommender/models/' + specific_path
        self.model_path = model_path
        logging.info(f'Model path: {model_path}')

        # get the model type and file type based on model path
        model_type = model_path_dict[model_key]['type']
        self.model_type = model_type
        model_file_type = model_path_dict[model_key]['model_file_type']
        self.model_file_type = model_file_type
        logging.info(f'Model type: {model_type}')

        # load the model based on the model and model file types
        if model_file_type == 'pkl':
            with open(model_path, 'rb') as f:
                model = pickle.load(f)
        elif model_file_type == 'joblib':
            model = joblib.load(model_path)
        logging.info(f'{model_type.upper()} model loaded from {model_path}.')

        return model
    
    '''
    METHOD
    - Predict the recommender intent class given a user query
    Input: STRING representing the user query
    Return: STRING representing the intent class
    '''
    def generate_classification(self, query: str):
        # get word embeddings for the student query
        try: 
            query_embeddings = get_word_embeddings(query, model=self.word_embedding_model, lemmatize=False, stem=False)
            predicted_intent = self.classifier.predict([query_embeddings])[0]
        except: 
            logging.info(f'Could not generate word embeddings for query: \'{query}\'.')
        
        return predicted_intent

if __name__ == '__main__':
    #logging.getLogger().setLevel(logging.INFO)
    recommender_intent_classifier = RecommenderIntentClassifier()
    recommender_intent_classifier.generate_classification('Can you give some course recommendations?')