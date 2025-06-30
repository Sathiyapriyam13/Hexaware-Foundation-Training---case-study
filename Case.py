class Case:
    def __init__(self, case_id=None, incident_id=None, victim_id=None, suspect_id=None, officer_id=None, case_status=None, case_details=None):
        self.__case_id = case_id
        self.__incident_id = incident_id
        self.__victim_id = victim_id
        self.__suspect_id = suspect_id
        self.__officer_id = officer_id
        self.__case_status = case_status
        self.__case_details = case_details

    def get_case_id(self):
        return self.__case_id 
    
    def get_incident_id(self):
        return self.__incident_id

    def get_victim_id(self):
        return self.__victim_id

    def get_suspect_id(self):
        return self.__suspect_id

    def get_officer_id(self):
        return self.__officer_id

    def get_case_status(self):
        return self.__case_status
    
    def get_case_details(self):
        return self.__case_details

    def set_case_id(self, case_id):
        self.__case_id = case_id

    def set_incident_id(self, incident_id):
        self.__incident_id = incident_id

    def set_victim_id(self, victim_id):
        self.__victim_id = victim_id

    def set_suspect_id(self, suspect_id):
        self.__suspect_id = suspect_id

    def set_officer_id(self, officer_id):
        self.__officer_id = officer_id

    def set_case_status(self, case_status):
        self.__case_status = case_status

    def set_case_details(self, case_details):
        self.__case_details = case_details

    def __str__(self):
        return (
            f"\n--- Case #{self.__case_id} ---\n"
            f"Incident ID   : {self.__incident_id}\n"
            f"Victim ID     : {self.__victim_id}\n"
            f"Suspect ID    : {self.__suspect_id}\n"
            f"Officer ID    : {self.__officer_id}\n"
            f"Case Status   : {self.__case_status}\n"
            f"Case Details  : {self.__case_details}"
        )
