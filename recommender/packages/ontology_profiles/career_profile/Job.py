'''
This is a Python class representing the 'Job' ontology profile. For the design and structure of this profile, check out the 'ontologies' directory.

Variables:
- JobBasicInfo (another class)
    - job_title
    - job_description
    - job_requirement
- JobQualification (another class)
    - job_required_qualification
- JobApplication (another class)
    - job_application_procedure
'''

class Job:
    def __init__(self, job_basic_info, job_qualification, job_application):
        self.job_basic_info = job_basic_info
        self.job_qualification = job_qualification
        self.job_application = job_application
    
    '''
    getters
    '''
    def get_job_basic_info(self):
        return self.job_basic_info
    
    def get_job_qualification(self):
        return self.job_qualification

    def get_job_application(self):
        return self.job_application
    
