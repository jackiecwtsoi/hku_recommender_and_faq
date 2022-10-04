'''
This is where we do all the text preprocessing and word embeddings generation.
'''

import numpy as np
import pandas as pd

from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
    
'''
FUNCTION
Return: LIST of tokenized words for a text
'''
def preprocess(text, lemmatize=False, stem=False):
    text = text.lower() # convert all letters to lowercase
    words = word_tokenize(text) # tokanize each sentence
    words = [word for word in words if word.isalpha()]

    # handle stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if not word in stop_words]
    
    # handle lemmatization
    if lemmatize==True:
        lemmatizer = WordNetLemmatizer()
        words = [lemmatizer.lemmatize(word) for word in words]

    # handle stemming
    if stem==True:
        stemmer = PorterStemmer()
        words = [stemmer.stem(word) for word in words]

    return words

'''
FUNCTION
Return: MATRIX representing word embeddings of a text
'''
def get_word_embeddings(text, model, lemmatize=False, stem=False):
    word_embeddings = np.mean(np.array([model[i] for i in preprocess(text, lemmatize, stem)]), axis=0)
    return word_embeddings

def get_individual_word_embeddings(word, model, lemmatize=False, stem=False):
    word_embeddings = np.array([model[i] for i in preprocess(word, lemmatize, stem)])
    return word_embeddings

def get_individual_d2v_embeddings(text, model, lemmatize=False, stem=True):
    text_tokenized = preprocess(text, stem=stem, lemmatize=lemmatize)
    vectors = model.infer_vector(text_tokenized)
    return vectors