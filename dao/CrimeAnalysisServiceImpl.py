from database.connector import establish_link

conn = establish_link()
if conn:
    cursor = conn.cursor()

from util.DBConnUtil import DBConnUtil

from dao.ICrimeAnalysisService import ICrimeAnalysisService

from entity.Incident import Incident
from entity.IncidentType import IncidentType
from entity.Status import Status
from entity.Report import Report
from entity.Victim import Victim
from entity.Suspect import Suspect
from entity.Officer import Officer
from entity.Case import Case

from exception.IncidentNotFound import IncidentNumberNotFoundException
from exception.OfficerNotFound import OfficerNotFoundException
from exception.CaseNotFound import CaseNotFoundException

class CrimeAnalysisServiceImpl(ICrimeAnalysisService):
    connection = DBConnUtil.get_connection()

    def __init__(self):
        if not CrimeAnalysisServiceImpl.connection:
            CrimeAnalysisServiceImpl.connection = DBConnUtil.get_connection()

    from database.connector import establish_link
from entity.Victim import Victim

class CrimeAnalysisServiceImpl:

    from database.connector import establish_link
from entity.Victim import Victim

class CrimeAnalysisServiceImpl:

    def add_victim(self, victim: Victim):
        try:
            conn = establish_link()
            cursor = conn.cursor()

            insert_query = """
            INSERT INTO Victims (FirstName, LastName, Gender, Phone, Address, Age)
            VALUES (%s, %s, %s, %s, %s, %s)
            """

            values = (
                victim.get_first_name(),
                victim.get_last_name(),
                victim.get_gender(),
                victim.get_phone(),
                victim.get_address(),
                victim.get_age()
            )

            cursor.execute(insert_query, values)
            conn.commit()

            return True

        except Exception as e:
            print(f"Error in add_victim: {e}")
            return False

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()



    def add_suspect(self, suspect: Suspect) -> bool:
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO Suspects (SuspectID, FirstName, LastName, DateOfBirth, Gender, ContactInformation)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (
                suspect.get_suspect_id(),
                suspect.get_first_name(),
                suspect.get_last_name(),
                suspect.get_date_of_birth().strftime('%Y-%m-%d'),
                suspect.get_gender(),
                suspect.get_contact_info()
            )
            cursor.execute(query, values)
            self.connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("Error adding suspect:", e)
            return False
        finally:
            if cursor:
                cursor.close()

    def add_officer(self, officer: Officer) -> bool:
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO Officers (OfficerID, FirstName, LastName, BadgeNumber, `Rank`, ContactInformation, AgencyID)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                officer.get_officer_id(),
                officer.get_first_name(),
                officer.get_last_name(),
                officer.get_badge_number(),
                officer.get_rank(),
                officer.get_contact_info(),
                officer.get_agency_id()
            )
            cursor.execute(query, values)
            self.connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("Error adding officer:", e)
            return False
        finally:
            if cursor:
                cursor.close()

    def create_incident(self, incident: Incident) -> bool:
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO Incidents (
                    IncidentID, IncidentType, IncidentDate,
                    LocationLatitude, LocationLongitude,
                    Description, Status,
                    VictimID, SuspectID, OfficerID
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            incident_date_str = incident.get_incident_date().strftime('%Y-%m-%d') if incident.get_incident_date() else None
            values = (
                incident.get_incident_id(),
                incident.get_incident_type(),
                incident_date_str,
                float(incident.get_location_latitude()),
                float(incident.get_location_longitude()),
                incident.get_description(),
                incident.get_status(),
                incident.get_victim_id(),
                incident.get_suspect_id(),
                incident.get_officer_id()
            )
            cursor.execute(query, values)
            self.connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("Error creating incident:", e)
            return False
        finally:
            if cursor:
                cursor.close()

    def update_incident_status(self, status, incident_id: int) -> bool:
        cursor = None
        try:
            cursor = self.connection.cursor()
            new_status = status.get_status_name() if hasattr(status, "get_status_name") else status
            query = "UPDATE Incidents SET Status = %s WHERE IncidentID = %s"
            cursor.execute(query, (new_status, incident_id))
            self.connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("Error updating incident status:", e)
            return False
        finally:
            if cursor:
                cursor.close()

    def get_incident_by_id(self, incident_id: int) -> str:
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Incidents WHERE IncidentID = %s"
            cursor.execute(query, (incident_id,))
            row = cursor.fetchone()
            if row:
                incident = Incident(*row)
                return (
                    f"\n---\nIncident ID: {incident.get_incident_id()}\n"
                    f"Type: {incident.get_incident_type()}\nDate: {incident.get_incident_date()}\n"
                    f"Lat: {incident.get_location_latitude()} | Long: {incident.get_location_longitude()}\n"
                    f"Status: {incident.get_status()}\nVictim ID: {incident.get_victim_id()} | "
                    f"Suspect ID: {incident.get_suspect_id()} | Officer ID: {incident.get_officer_id()}"
                )
            else:
                raise IncidentNumberNotFoundException(incident_id)
        finally:
            if cursor:
                cursor.close()

    def get_incidents_in_daterange(self, start_date: str, end_date: str):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Incidents WHERE IncidentDate BETWEEN %s AND %s"
            cursor.execute(query, (start_date, end_date))
            return [Incident(*row) for row in cursor.fetchall()]
        finally:
            if cursor:
                cursor.close()

    def get_incidents_by_type(self, incident_type: str):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Incidents WHERE IncidentType = %s"
            cursor.execute(query, (incident_type,))
            return [Incident(*row) for row in cursor.fetchall()]
        finally:
            if cursor:
                cursor.close()

    def get_incident_counts_by_type(self):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT IncidentType, COUNT(*) AS TotalIncidents
                FROM Incidents
                GROUP BY IncidentType
            """
            cursor.execute(query)
            return cursor.fetchall()
        finally:
            if cursor:
                cursor.close()

    def create_case(self, case: Case) -> bool:
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO Cases (CaseID, IncidentID, VictimID, SuspectID, OfficerID, CaseStatus, CaseDetails)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                case.get_case_id(),
                case.get_incident_id(),
                case.get_victim_id(),
                case.get_suspect_id(),
                case.get_officer_id(),
                case.get_case_status(),
                case.get_case_details()
            )
            cursor.execute(query, values)
            self.connection.commit()
            return cursor.rowcount > 0
        finally:
            if cursor:
                cursor.close()

    def get_case_details(self, case_id: int) -> Case:
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Cases WHERE CaseID = %s"
            cursor.execute(query, (case_id,))
            row = cursor.fetchone()
            if row:
                return Case(*row)
            else:
                raise CaseNotFoundException(f"Case ID {case_id} not found.")
        finally:
            if cursor:
                cursor.close()

    def update_case_status(self, case_id: int, new_status: str) -> bool:
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Cases SET CaseStatus = %s WHERE CaseID = %s"
            cursor.execute(query, (new_status, case_id))
            self.connection.commit()
            return cursor.rowcount > 0
        finally:
            if cursor:
                cursor.close()

    def get_officer_by_id(self, officer_id: int) -> Officer:
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Officers WHERE OfficerID = %s", (officer_id,))
            row = cursor.fetchone()
            if row:
                return Officer(*row)
            else:
                raise OfficerNotFoundException(officer_id)
        finally:
            if cursor:
                cursor.close()

    def get_case_by_id(self, case_id: int) -> Case:
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Cases WHERE CaseID = %s", (case_id,))
            row = cursor.fetchone()
            if row:
                return Case(*row)
            else:
                raise CaseNotFoundException(case_id)
        finally:
            if cursor:
                cursor.close()

    def get_all_victims(self):
        return self._fetch_all("SELECT * FROM Victims", Victim)

    def get_all_suspects(self):
        return self._fetch_all("SELECT * FROM Suspects", Suspect)

    def get_all_officers(self):
        return self._fetch_all("SELECT * FROM Officers", Officer)

    def get_all_incidents(self):
        return self._fetch_all("SELECT * FROM Incidents", Incident)

    def get_all_cases(self):
        return self._fetch_all("SELECT * FROM Cases", Case)

    def get_all_reports(self):
        return self._fetch_all("SELECT * FROM Reports", Report)

    def _fetch_all(self, query, entity_class):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            return [entity_class(*row) for row in cursor.fetchall()]
        finally:
            if cursor:
                cursor.close()

    def get_recent_incidents_with_officer_details(self):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT i.IncidentID, i.IncidentType, i.IncidentDate, o.FirstName
                FROM Incidents i
                INNER JOIN Officers o ON i.OfficerID = o.OfficerID
                WHERE i.IncidentDate = (
                    SELECT MAX(IncidentDate)
                    FROM Incidents sub
                    WHERE sub.OfficerID = i.OfficerID
                )
            """
            cursor.execute(query)
            return cursor.fetchall()
        finally:
            if cursor:
                cursor.close()

    def generate_incident_report(self, incident_id: int) -> str:
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Incidents WHERE IncidentID = %s"
            cursor.execute(query, (incident_id,))
            row = cursor.fetchone()
            if row:
                incident = Incident(*row)
                report = (
                    f"\n--- Incident Report ---\n"
                    f"Incident ID: {incident.get_incident_id()}\n"
                    f"Type: {incident.get_incident_type()}\n"
                    f"Date: {incident.get_incident_date()}\n"
                    f"Location: ({incident.get_location_latitude()}, {incident.get_location_longitude()})\n"
                    f"Status: {incident.get_status()}\n"
                    f"Description: {incident.get_description()}\n"
                    f"Victim ID: {incident.get_victim_id()} | Suspect ID: {incident.get_suspect_id()} | Officer ID: {incident.get_officer_id()}"
                )
                return report
            else:
                raise IncidentNumberNotFoundException(incident_id)
        finally:
            if cursor:
                cursor.close()

    def search_incidents(self, keyword: str):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT * FROM Incidents
                WHERE Description LIKE %s OR IncidentType LIKE %s
            """
            param = f"%{keyword}%"
            cursor.execute(query, (param, param))
            return [Incident(*row) for row in cursor.fetchall()]
        finally:
            if cursor:
                cursor.close()
