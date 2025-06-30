# ICrimeAnalysisService.py
from database.connector import establish_link

conn = establish_link()
if conn:
    cursor = conn.cursor()
    

from abc import ABC, abstractmethod
from entity.Victim import Victim
from entity.Suspect import Suspect
from entity.Officer import Officer
from entity.Incident import Incident
from entity.Case import Case


class ICrimeAnalysisService(ABC):

    @abstractmethod
    def add_victim(self, victim: Victim) -> bool:
        pass

    @abstractmethod
    def add_suspect(self, suspect: Suspect) -> bool:
        pass

    @abstractmethod
    def add_officer(self, officer: Officer) -> bool:
        pass

    @abstractmethod
    def create_incident(self, incident: Incident) -> bool:
        pass

    @abstractmethod
    def update_incident_status(self, status, incident_id: int) -> bool:
        pass

    @abstractmethod
    def get_incident_by_id(self, incident_id: int) -> str:
        pass

    @abstractmethod
    def get_incidents_in_daterange(self, start_date: str, end_date: str):
        pass

    @abstractmethod
    def get_incidents_by_type(self, incident_type: str):
        pass

    @abstractmethod
    def create_case(self, case: Case) -> bool:
        pass

    @abstractmethod
    def get_case_details(self, case_id: int) -> Case:
        pass

    @abstractmethod
    def update_case_status(self, case_id: int, new_status: str) -> bool:
        pass

    @abstractmethod
    def get_officer_by_id(self, officer_id: int) -> Officer:
        pass

    @abstractmethod
    def get_case_by_id(self, case_id: int) -> Case:
        pass

    @abstractmethod
    def get_all_victims(self):
        pass

    @abstractmethod
    def get_all_suspects(self):
        pass

    @abstractmethod
    def get_all_officers(self):
        pass

    @abstractmethod
    def get_all_incidents(self):
        pass

    @abstractmethod
    def get_all_cases(self):
        pass

    @abstractmethod
    def get_all_reports(self):
        pass

    @abstractmethod
    def generate_incident_report(self, incident_id: int) -> str:
        pass

    @abstractmethod
    def search_incidents(self, keyword: str):
        pass
