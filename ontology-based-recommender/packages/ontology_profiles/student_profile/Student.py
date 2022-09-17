
from ontology_profiles.student_profile.PersonalInfo import PersonalInfo
from ontology_profiles.student_profile.EducationalInfo import EducationalInfo
from ontology_profiles.student_profile.Skill import Skill

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
    
    def set_skill(self, skill: Skill):
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
