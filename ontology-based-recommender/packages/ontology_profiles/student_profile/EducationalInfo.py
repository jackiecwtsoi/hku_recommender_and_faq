

class EducationalInfo:
    def __init__(self, declared_faculty, declared_major, high_school_info, student_interest, job_aspiration):
        self.declared_faculty = declared_faculty
        self.declared_major = declared_major
        self.high_school_info = high_school_info
        self.student_interest = student_interest
        self.job_aspiration = job_aspiration
    
    '''
    setters
    '''
    # TODO: set interested_subject_domain

    '''
    getters
    '''
    def get_student_interest(self):
        return self.student_interest

    def get_job_aspiration(self):
        return self.job_aspiration
    