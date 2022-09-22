

class PersonalInfo:
    def __init__(self, first_name, last_name, email, preferred_language):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.preferred_language = preferred_language
    
    def __init__(self, email):
        self.email = email
        
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