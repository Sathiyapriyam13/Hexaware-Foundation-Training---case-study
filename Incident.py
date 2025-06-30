# entity/Incident.py
class Incident:
    def __init__(self, incident_id=None, incident_type=None, incident_date=None, location_latitude=None, location_longitude=None, description=None, status=None, victim_id=None, suspect_id=None, officer_id=None):
        self.__incident_id = incident_id
        self.__incident_type = incident_type
        self.__incident_date = incident_date
        self.__location_latitude= location_latitude
        self.__location_longitude= location_longitude
        self.__description = description
        self.__status = status
        self.__victim_id = victim_id
        self.__suspect_id = suspect_id
        self.__officer_id = officer_id

    def get_incident_id(self):
        return self.__incident_id

    def get_incident_type(self):
        return self.__incident_type

    def get_incident_date(self):
        return self.__incident_date

    def get_location_latitude(self):
        return self.__location_latitude
    
    def get_location_longitude(self):
        return self.__location_longitude

    def get_description(self):
        return self.__description

    def get_status(self):
        return self.__status

    def get_victim_id(self):
        return self.__victim_id

    def get_suspect_id(self):
        return self.__suspect_id
    
    def get_officer_id(self):
        return self.__officer_id

    def set_incident_id(self, incident_id):
        self.__incident_id = incident_id

    def set_incident_type(self, incident_type):
        self.__incident_type = incident_type

    def set_incident_date(self, incident_date):
        self.__incident_date = incident_date

    def set_location_latitude(self, location_latitude):
        self.__location_latitude = location_latitude

    def set_location_longitude(self, location_longitude):
        self.__location_longitude = location_longitude

    def set_description(self, description):
        self.__description = description

    def set_status(self, status):
        self.__status = status

    def set_victim_id(self, victim_id):
        self.__victim_id = victim_id

    def set_suspect_id(self, suspect_id):
        self.__suspect_id = suspect_id

    def set_officer_id(self, officer_id):
        self.__officer_id = officer_id

    def __str__(self):
        return (f"Incident[ID={self.__incident_id}, Type={self.__incident_type}, Date={self.__incident_date}, "
            f"Lat={self.__location_latitude}, Long={self.__location_longitude}, "
            f"Status={self.__status}, VictimID={self.__victim_id}, "
            f"SuspectID={self.__suspect_id}, OfficerID={self.__officer_id}]")
