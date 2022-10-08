'''
This is a Python class representing the 'SubjectDomain' ontology profile. 
For the design and structure of this profile, check out the 'ontologies' directory.

Variables:
- subject_domain: STRING
- subject_domain_keywords: LIST
'''

class SubjectDomain:
    def __init__(self, subject_domain):
        self.subject_domain = subject_domain

    '''
    setters
    '''
    def set_subject_domain_keywords(self, keywords: list):
        self.subject_domain_keywords = keywords
    
    '''
    getters
    '''
    def get_subject_domain(self):
        return self.subject_domain
    
    def get_subject_domain_keywords(self):
        return self.subject_domain_keywords