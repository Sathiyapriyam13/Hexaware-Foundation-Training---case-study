class Incident:
    def __init__(self, incident_id, incident_type, incident_date, area, city, description, status, officer_id):
        self.incident_id = incident_id
        self.incident_type = incident_type
        self.incident_date = incident_date
        self.area = area
        self.city = city
        self.description = description
        self.status = status
        self.officer_id = officer_id
