# entity/IncidentType.py

class IncidentType:
    def __init__(self, incident_type_id=None, incident_type_name=None):
        self.__incident_type_id = incident_type_id
        self.__incident_type_name = incident_type_name

    def get_incident_type_id(self):
        return self.__incident_type_id

    def get_incident_type_name(self):
        return self.__incident_type_name

    def set_incident_type_id(self, incident_type_id):
        self.__incident_type_id = incident_type_id

    def set_incident_type_name(self, incident_type_name):
        self.__incident_type_name = incident_type_name
