'''
This is a Python class representing the overall FAQ/Q&A session.
'''
from QueryQuestionSimilarity import *
from QueryAnswerRelevance import *
import logging

class FAQ:
    def __init__(self, use_cuda: bool, cpu_count: int):
        self.qq = QueryQuestionSimlarity(cpu_count)
        self.qa = QueryAnswerRelevance(use_cuda)
        logging.info(f'FAQ instance initialized.')

    '''
    getters
    '''
    def get_query_question_similarity_class(self):
        return self.qq
    
    def get_query_answer_relevance_class(self):
        return self.qa

    '''
    METHOD
    - Get the overall FAQ score for each QA pair in our FAQ database against the student query
    Return: DATAFRAME (sorted from highest overall score to lowest)
    '''
    def get_overall_faq_scores(self, query):
        df_qq = self.qq.generate_similarity_scores(query)
        df_qa = self.qa.generate_predictions(query)

        # concatenate the useful columns into an overall dataframe
        df_overall = pd.concat([df_qq, df_qa], axis=1, join='inner')
        
        # calculate the final score based on q-Q and q-A scores
        df_overall['Final FAQ Score'] = df_overall['Predicted Cosine q-Q Similarity'] + df_overall['Predicted q-A Relevance']
        df_overall = df_overall.sort_values(by='Final FAQ Score', ascending=False)

        return df_overall

    '''
    METHOD
    - Get the top answer from our FAQ database for the student query based on the overall FAQ score generated
    Return: STRING of the best answer
    '''
    def get_top_answer(self, query):
        df_scores = self.get_overall_faq_scores(query)
        top_answer = df_scores['Answer from FAQ Database'].values[0]
        return top_answer

