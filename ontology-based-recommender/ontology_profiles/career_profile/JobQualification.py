'''
This is a Python class representing the 'JobQualification' attribute. This class is used by the overall 'Job' class which serves as the career profile.

Variables:
- job_required_qualification
'''

class JobQualification:
    def __init__(self, job_required_qualification):
        self.job_required_qualification = job_required_qualification

    '''
    getters
    '''
    def get_job_required_qualification(self):
        return self.job_required_qualification