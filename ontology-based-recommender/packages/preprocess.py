'''
This is where we do all the text preprocessing and word embeddings generation.
'''

import numpy as np
import pandas as pd

import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk import word_tokenize
from nltk.corpus import stopwords
    
'''
FUNCTION
Return: LIST of tokenized words for a text
'''
def preprocess(text):
    text = text.lower()
    words = word_tokenize(text)
    words = [word for word in words if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if not word in stop_words]
    
    return words

'''
FUNCTION
Return: MATRIX representing word embeddings of a text
'''
def get_word_embeddings(text, model):
    word_embeddings = np.sum(np.array([model[i] for i in preprocess(text)]), axis=0)
    return word_embeddings

