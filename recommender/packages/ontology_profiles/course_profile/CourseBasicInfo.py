
from hku_recommender_and_faq.recommender.packages.ontology_profiles.course_profile.SubjectDomain import *

class CourseBasicInfo:
    # def __init__(self, course_code, course_title, offering_department, teachers, prerequisites):
    #     self.course_code = course_code
    #     self.course_title = course_title
    #     self.offering_department = offering_department
    #     self.teachers = teachers
    #     self.prerequisites = prerequisites

    #     # TODO self.course_type = course_type
    #     # TODO self.course_additional_info = course_additional_info

    def __init__(self, course_code):
        self.course_code = course_code

    '''
    setters
    '''
    def set_course_code(self, course_code):
        self.course_code = course_code
    
    def set_course_title(self, course_title):
        self.course_title = course_title
    
    def set_subject_domain(self, subject_domain: SubjectDomain):
        self.subject_domain = subject_domain

    '''
    getters
    '''
    def get_course_code(self):
        return self.course_code
        
    def get_course_title(self):
        return self.course_title