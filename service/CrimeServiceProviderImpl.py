import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util.db_connection import get_connection
from entity.incident import Incident
from entity.victim import Victim
from entity.suspect import Suspect
from entity.officer import Officer
from entity.report import Report
from entity.evidence import Evidence
from entity.agency import Agency
from entity.case import Case

class CrimeServiceImpl:

    def create_incident(self, incident: Incident):
        conn = get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Incidents 
                (IncidentType, IncidentDate, Area, City, Description, Status, OfficerID) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (
            incident.incident_type,
            incident.incident_date,
            incident.area,
            incident.city,
            incident.description,
            incident.status,
            incident.officer_id
        ))
        conn.commit()
        cursor.close()
        conn.close()

    def get_incidents_in_date_range(self, start_date, end_date):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM Incidents WHERE IncidentDate BETWEEN %s AND %s""",
                       (start_date, end_date))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Incident(*r) for r in results]

    def search_incidents_by_type(self, incident_type):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Incidents WHERE IncidentType = %s", (incident_type,))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Incident(*r) for r in results]

    def generate_incident_report(self, incident_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT i.IncidentID, i.IncidentType, i.Area, i.City, i.Description,
                   i.Status, r.ReportDetails, r.ReportDate, r.Status AS ReportStatus
            FROM Incidents i
            JOIN Reports r ON i.IncidentID = r.IncidentID
            WHERE i.IncidentID = %s
        """, (incident_id,))
        report = cursor.fetchone()
        cursor.close()
        conn.close()
        return report

    def get_victims_by_incident(self, incident_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Victims WHERE IncidentID = %s", (incident_id,))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Victim(*r) for r in results]

    def get_suspects_by_incident(self, incident_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Suspects WHERE IncidentID = %s", (incident_id,))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Suspect(*r) for r in results]

    def get_evidence_by_incident(self, incident_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Evidence WHERE IncidentID = %s", (incident_id,))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Evidence(*r) for r in results]

    def update_incident_status(self, incident_id, new_status):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Incidents SET Status = %s WHERE IncidentID = %s", (new_status, incident_id))
        conn.commit()
        success = cursor.rowcount > 0
        cursor.close()
        conn.close()
        return success

    def create_case(self, case_description, incident_ids):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Cases (CaseDescription) VALUES (%s)", (case_description,))
        case_id = cursor.lastrowid
        for inc_id in incident_ids:
            cursor.execute("INSERT INTO CaseIncidents (CaseID, IncidentID) VALUES (%s, %s)", (case_id, inc_id))
        conn.commit()
        cursor.close()
        conn.close()
        return Case(case_id, case_description)

    def get_case_details(self, case_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Cases WHERE CaseID = %s", (case_id,))
        case_row = cursor.fetchone()
        cursor.execute("""SELECT i.* FROM Incidents i 
                          JOIN CaseIncidents ci ON i.IncidentID = ci.IncidentID 
                          WHERE ci.CaseID = %s""", (case_id,))
        incidents = cursor.fetchall()
        cursor.close()
        conn.close()
        return Case(*case_row), [Incident(*r) for r in incidents]

    def update_case(self, case: Case):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Cases SET CaseDescription = %s WHERE CaseID = %s", (case.case_description, case.case_id))
        conn.commit()
        updated = cursor.rowcount > 0
        cursor.close()
        conn.close()
        return updated

    def get_all_cases(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Cases")
        cases = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Case(*c) for c in cases]
