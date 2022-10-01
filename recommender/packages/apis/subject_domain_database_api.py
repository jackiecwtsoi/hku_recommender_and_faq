'''
This is an API layer that converts our subject domains database to SubjectDomain instances.
'''

import json

from ontology_profiles.course_profile.SubjectDomain import *

'''
FUNCTION
- Convert a key, value item of a dictionary to a SubjectDomain instance
Return: COURSE instance
'''
def convert_row_to_subject_domain_class(subject: str, keywords: list):
    subject_domain = SubjectDomain(subject)
    subject_domain.set_subject_domain_keywords(keywords)

    return subject_domain

'''
FUNCTION
- Read the JSON file stored in a path
- Convert the entire JSON into a dictionary
Return: LIST of SUBJECTDOMAIN instances
'''
def convert_to_subject_domains(SUBJECT_DOMAIN_KEYWORDS_DATA_PATH):
    with open(SUBJECT_DOMAIN_KEYWORDS_DATA_PATH, 'r') as fp:
        subject_domain_keywords_dict = json.load(fp)
        
    # convert all rows into a list of SubjectDomain instances
    subject_domains = [convert_row_to_subject_domain_class(subject, keywords) for subject, keywords in subject_domain_keywords_dict.items()]

    return subject_domains