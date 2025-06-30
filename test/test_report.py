# Pytest for reports
from service.CrimeServiceProviderImpl import CrimeServiceProviderImpl

crime_service = CrimeServiceProviderImpl()

def test_generate_report_by_area():
    area = "Andheri"
    result = crime_service.generate_crime_report_by_area(area)
    assert isinstance(result, list)
