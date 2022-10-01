import logging
import torch

import nltk
from FAQ import *

def trigger_faq_workflow():
    use_cuda = torch.cuda.is_available()
    faq = FAQ(use_cuda)

    student_input = input(f'Please input your query or type \'quit\' to quit this program:\n')
    while student_input != 'quit':
        print(faq.get_top_answer(student_input))
        student_input = input(f'Please input your query or type \'quit\' to quit this program:\n')
        

if __name__ == '__main__':
    #logging.getLogger().setLevel(logging.INFO)
    nltk.download('punkt')
    nltk.download('stopwords')

    trigger_faq_workflow()