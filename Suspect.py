# entity/Suspect.py

class Suspect:
    def __init__(self, suspect_id, first_name, last_name, dob, gender, contact_info):
        self.suspect_id = suspect_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.gender = gender
        self.contact_info = contact_info

    def get_suspect_id(self):
        return self.suspect_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_date_of_birth(self):
        return self.dob

    def get_gender(self):
        return self.gender

    def get_contact_info(self):
        return self.contact_info
