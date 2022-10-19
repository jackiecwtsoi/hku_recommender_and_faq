

class PersonalInfo:
    def __init__(self, email, preferred_language):
        self.email = email
        # self.first_name = first_name
        # self.last_name = last_name
        self.preferred_language = preferred_language
    
    '''
    setters
    '''
    def set_first_name(self, first_name):
        self.first_name = first_name
        
    def set_last_name(self, last_name):
        self.last_name = last_name
    
    def set_preferred_language(self, preferred_language):
        self.preferred_language = preferred_language

    '''
    getters
    '''
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email
    
    def get_preferred_language(self):
        return self.preferred_language