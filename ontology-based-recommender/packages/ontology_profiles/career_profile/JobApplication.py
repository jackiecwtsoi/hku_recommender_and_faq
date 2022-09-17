'''
This is a Python class representing the 'JobApplication' attribute. This class is used by the overall 'Job' class which serves as the career profile.

Variables:
- job_application_procedure
'''

class JobApplication:
    def __init__(self, job_application_procedure):
        self.job_application_procedure = job_application_procedure
    
    '''
    getters
    '''
    def get_job_application_procedure(self):
        return self.job_application_procedure