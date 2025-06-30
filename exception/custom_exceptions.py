# Custom Exceptions for Crime Reporting System
# exception/IncidentNotFoundException.py
class IncidentNotFoundException(Exception):
    def __init__(self, message="Incident not found"):
        super().__init__(message)

class VictimNotFoundException(Exception):
    def __init__(self, message="Victim not found."):
        super().__init__(message)

class SuspectNotFoundException(Exception):
    def __init__(self, message="Suspect not found."):
        super().__init__(message)

class OfficerNotFoundException(Exception):
    def __init__(self, message="Officer not found."):
        super().__init__(message)

class AgencyNotFoundException(Exception):
    def __init__(self, message="Law Enforcement Agency not found."):
        super().__init__(message)

class ReportNotFoundException(Exception):
    def __init__(self, message="Report not found."):
        super().__init__(message)

class EvidenceNotFoundException(Exception):
    def __init__(self, message="Evidence not found."):
        super().__init__(message)

class DuplicateEntryException(Exception):
    def __init__(self, message="Duplicate entry found."):
        super().__init__(message)

class DatabaseConnectionException(Exception):
    def __init__(self, message="Failed to connect to the database."):
        super().__init__(message)
