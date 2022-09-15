'''
This is a Python class representing the 'JobBasicInfo' attribute. This class is used by the overall 'Job' class which serves as the career profile.

Variables:
- job_title
- job_description
- job_requirement
'''

class JobBasicInfo:
    def __init__(self, job_title, job_description, job_requirement):
        self.job_title = job_title
        self.job_description = job_description
        self.job_requirement = job_requirement
    
    '''
    getters
    '''
    def get_job_title(self):
        return self.get_job_title
    
    def get_job_description(self):
        return self.job_description
    
    def get_job_requirement(self):
        return self.job_requirement
    
    '''
    setters #TODO
    '''



