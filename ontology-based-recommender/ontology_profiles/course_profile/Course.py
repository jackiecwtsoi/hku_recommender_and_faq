'''
This is a Python class representing the 'Course/CourseInfo' ontology profile. For the design and structure of this profile, check out the 'ontologies' directory.

Variables:
- CourseBasicInfo (another class)
- CourseContent (another class)
- CourseAssessmentInfo (another class)
'''

from CourseBasicInfo import CourseBasicInfo
from CourseContent import CourseContent
from CourseAssessmentInfo import CourseAssessmentInfo

class Course:
    def __init__(self, course_basic_info, course_content, course_assessment_info):
        self.course_basic_info = course_basic_info
        self.course_content = course_content
        self.course_assessment_info = course_assessment_info
        
    '''
    getters
    '''
    def get_course_basic_info(self):
        return self.course_basic_info
    
    def get_course_content(self):
        return self.course_content
    
    def get_course_assessment_info(self):
        return self.course_assessment_info