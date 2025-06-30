from abc import ABC, abstractmethod
from entity.incident import Incident
from entity.case import Case
from entity.victim import Victim
from entity.suspect import Suspect
from entity.evidence import Evidence
from entity.report import Report
from entity.officer import Officer

class CrimeServiceProvider(ABC):

    @abstractmethod
    def register_incident(self, incident: Incident):
        pass

    @abstractmethod
    def get_all_incidents(self) -> list[Incident]:
        pass

    @abstractmethod
    def get_incidents_in_date_range(self, start_date, end_date) -> list[Incident]:
        pass

    @abstractmethod
    def search_incidents_by_type(self, incident_type: str) -> list[Incident]:
        pass

    @abstractmethod
    def generate_incident_report(self, incident_id: int) -> dict:
        pass

    @abstractmethod
    def get_victims_by_incident(self, incident_id: int) -> list[Victim]:
        pass

    @abstractmethod
    def get_suspects_by_incident(self, incident_id: int) -> list[Suspect]:
        pass

    @abstractmethod
    def get_evidence_by_incident(self, incident_id: int) -> list[Evidence]:
        pass

    @abstractmethod
    def update_incident_status(self, incident_id: int, new_status: str) -> bool:
        pass

    @abstractmethod
    def create_case(self, case_description: str, incident_ids: list[int]) -> Case:
        pass

    @abstractmethod
    def get_case_details(self, case_id: int) -> tuple[Case, list[Incident]]:
        pass

    @abstractmethod
    def update_case(self, case: Case) -> bool:
        pass

    @abstractmethod
    def get_all_cases(self) -> list[Case]:
        pass
