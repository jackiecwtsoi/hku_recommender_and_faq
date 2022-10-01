'''
This file stores a series of helper functions for any score calculations.
'''

import logging
import numpy as np
import pandas as pd
from scipy import spatial

from preprocess import *

'''
FUNCTION
- Calculate a single similarity score for a specified similarity type (e.g. cosine)
- Compares two pieces of texts
Return: FLOAT
'''
def calculate_similarity(student_text, text, model, similarity_type):
    if similarity_type == 'cosine':
        # get word embeddings
        try:
            student_text_embeddings = get_word_embeddings(student_text, model)
            text_embeddings = get_word_embeddings(text, model)

            # get the cosine similarity score
            similarity_score = 1 - spatial.distance.cosine(student_text_embeddings, text_embeddings)
        except:
            similarity_score = 0
            logging.debug('Could not generate similarity score.')
    
    return similarity_score