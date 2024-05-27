
user_preferences = {}
def add_user(user_id, preferred_categories):
    user_preferences[user_id] = preferred_categories
def get_recommendations(user_id):
    preferred_categories = user_preferences.get(user_id, [])
    if not preferred_categories:
        return []
    return ["Recommendation1", "Recommendation2", "Recommendation3"]

def get_recommendations(user_id):
    preferred_categories = user_preferences.get(user_id, [])
    if not preferred_categories:
        return []
    # Placeholder for recommendation generation logic
    return ["Recommendation1", "Recommendation2", "Recommendation3"]

class Student:
    school = "AkiraChix"
    def __init__ (self, first_name , last_name, age, code):
       self.first_name = first_name
       self.last_name = last_name
       self.age = age
       self.code =code
    def greet_student(self):
        greeting = (f"Hello {self.first_name}, Welcome to {self.school}. Your code is {self.code}")
        return greeting
    def year_of_birth(self):
        birth_year = (f"{self.first_name}, Was born in {2024- self.age}")
        return birth_year
    def full_names(self):
        full_names= (f"{self.first_name} {self.last_name}")
        return full_names
    def initials(self):
        initials= (f"{self.first_name[0]}.{self.last_name[0]}")
        return initials






