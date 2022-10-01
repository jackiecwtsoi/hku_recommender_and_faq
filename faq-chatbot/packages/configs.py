FAQ_DATABASE_PATH = 'faq-chatbot/q-Q_similarity/faq-data/df_faq.csv'


'''
CONFIG - All the models we currently support for q-Q similarity
Type: DICT
'''
QUERY_QUESTION_MODELS_DICT = {
    'glove-wiki': {
        'type': 'glove',
        'specific_path': 'glove.model',
        'model_file_type': 'model'
    },
    'glove-wiki-finetuned': {
        'type': 'glove',
        'specific_path': 'glove_wiki_finetuned.pkl',
        'model_file_type': 'pkl'
    }
}

'''
CONFIG - Default model for q-Q similarity (highest performing model)
Type: STR
'''
DEFAULT_QUERY_QUESTION_MODEL_KEY = 'glove-wiki-finetuned'

'''
CONFIG - All the models we currently support for q-A relevance
Type: DICT
'''
QUERY_ANSWER_MODELS_DICT = {
    'roberta-t2': {
        'type': 'roberta',
        'specific_path': 'checkpoint-371-epoch-7'
    },
    'roberta-t3-squad2': {
        'type': 'roberta',
        'specific_path': '',
    },
    'mpnet-t4': {
        'type': 'mpnet',
        'specific_path': ''
    },
    'bert-t5': {
        'type': 'bert',
        'specific_path': ''
    }
}

'''
CONFIG - Default model for q-A relevance (highest performing model)
Type: STR
'''
DEFAULT_QUERY_ANSWER_MODEL_KEY = 'roberta-t2'