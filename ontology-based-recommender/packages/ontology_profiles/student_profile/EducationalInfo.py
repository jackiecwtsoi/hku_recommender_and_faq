

class EducationalInfo:
    def __init__(self, declared_faculty, declared_major, high_school_info, interest, job_aspiration):
        self.declared_faculty = declared_faculty
        self.declared_major = declared_major
        self.high_school_info = high_school_info
        self.interest = interest
        self.job_aspiration = job_aspiration
    
    # TODO: delete later
    def __init__(self, interest):
        self.interest = interest
    
    '''
    setters
    '''

    '''
    getters
    '''
    def get_interest(self):
        return self.interest
    