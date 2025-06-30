import pytest
from entity.incident import Incident
from service.CrimeServiceProviderImpl import CrimeServiceProviderImpl
from exception.custom_exceptions import IncidentNotFoundException

service = CrimeServiceProviderImpl()

def test_register_and_get_incident():
    incident = Incident(999, "Robbery", "2024-06-25", 12.9716, 77.5946, "Sector 21", "Mumbai", "Test case", "Open", 1, 1, 1)
    service.register_incident(incident)
    result = service.get_incident_by_id(999)
    assert result.incident_id == 999

def test_invalid_incident_raises_exception():
    with pytest.raises(IncidentNotFoundException):
        service.get_incident_by_id(999999)
