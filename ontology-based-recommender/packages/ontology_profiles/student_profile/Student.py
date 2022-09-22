
from ontology_profiles.student_profile.PersonalInfo import PersonalInfo
from ontology_profiles.student_profile.EducationalInfo import EducationalInfo
from preprocess import *

class Student:
    def __init__(self, personal_info, educational_info, skill):
        self.personal_info = personal_info
        self.educational_info = educational_info
        self.skill = skill

    def __init__(self, personal_info: PersonalInfo):
        self.personal_info = personal_info
    
    '''
    setters
    '''
    def set_educational_info(self, educational_info: EducationalInfo):
        self.educational_info = educational_info

    def set_skills(self, skills_text):
        skills_text_preprocessed = list(set(preprocess(skills_text, stem=True)))
        self.skills = skills_text_preprocessed
    
    def set_any_further_info_required(self, further_info):
        self.any_further_info_required = further_info

    '''
    getters
    '''
    def get_personal_info(self):
        return self.personal_info
    
    def get_educational_info(self):
        return self.educational_info

    def get_skills(self):
        return self.skills

    def get_any_further_info_required(self):
        return self.any_further_info_required