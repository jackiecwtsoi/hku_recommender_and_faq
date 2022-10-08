'''
This is a Python class representing the 'Course/CourseInfo' ontology profile. 
For the design and structure of this profile, check out the 'ontologies' directory.

Variables:
- CourseBasicInfo (another class)
- CourseContent (another class)
- CourseAssessmentInfo (another class)
'''

from hku_recommender_and_faq.recommender.packages.ontology_profiles.course_profile.CourseContent import *

class Course:
    def __init__(self, course_basic_info, course_content, course_assessment_info):
        self.course_basic_info = course_basic_info
        self.course_content = course_content
        self.course_assessment_info = course_assessment_info
    
    # FIXME: below constructor is temporary only because we haven't implemented the database linkage API
    def __init__(self, course_content: CourseContent):
        self.course_content = course_content

    '''
    setters
    '''
    def set_course_basic_info(self, course_basic_info):
        self.course_basic_info = course_basic_info

    '''
    getters
    '''
    def get_course_basic_info(self):
        return self.course_basic_info
    
    def get_course_content(self):
        return self.course_content
    
    def get_course_assessment_info(self):
        return self.course_assessment_info
