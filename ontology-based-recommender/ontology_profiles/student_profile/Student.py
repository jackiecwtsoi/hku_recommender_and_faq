

from PersonalInfo import PersonalInfo
from EducationalInfo import EducationalInfo
from Skill import Skill

class Student:
    def __init__(self, personal_info, educational_info, skill):
        self.personal_info = personal_info
        self.educational_info = educational_info
        self.skill = skill
    
    '''
    getters
    '''
    def get_personal_info(self):
        return self.personal_info
    
    def get_educational_info(self):
        return self.educational_info

    def get_skill(self):
        return self.skill