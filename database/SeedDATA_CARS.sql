use crimeReporting

-- Victims
set identity_insert Victims on;
insert into Victims (VictimID, FirstName, LastName, DateOfBirth, Gender, ContactInformation)
values
(1, 'Rahul', 'Sharma', '1990-04-15', 'Male', '12 MG Road, Delhi'),
(2, 'Priya', 'Mehra', '1985-07-20', 'Female', '54 Park Street, Kolkata'),
(3, 'Aman', 'Verma', '2000-01-01', 'Transgender', '88 Residency Road, Bengaluru'),
(4, 'Vikram', 'Reddy', '1993-09-10', 'Male', '101 Banjara Hills, Hyderabad'),
(5, 'Neha', 'Patel', '1998-02-28', 'Female', '45 C.G. Road, Ahmedabad');

-- Suspects
insert into Suspects(SuspectID, FirstName, LastName, DateOfBirth, Gender, ContactInformation)
values 
(1, 'Rohit', 'Singh', '1988-03-12', 'Male', 'Sector 14, Gurugram'),
(2, 'Kavita', 'Nair', '1992-06-15', 'Female', 'Panampilly Nagar, Kochi'),
(3, 'Suresh', 'Yadav', '1980-11-25', 'Male', 'Ashok Nagar, Chennai'),
(4, 'Sneha', 'Joshi', '1995-05-18', 'Female', 'FC Road, Pune'),
(5, 'Arjun', 'Khan', '1987-12-05', 'Transgender', 'Lalbagh Road, Lucknow');

-- LawEnforcement
insert into LawEnforcement (AgencyID, AgencyName, Jurisdiction, ContactInformation)
values 
(1, 'Delhi Police', 'Delhi', 'delhipolice@gov.in'),
(2, 'Kolkata Police', 'Kolkata', 'kolkatapolice@gov.in'),
(3, 'Bengaluru Police', 'Bengaluru', 'bcp@karnataka.in'),
(4, 'Hyderabad Police', 'Hyderabad', 'hydpolice@gov.in'),
(5, 'Ahmedabad Police', 'Ahmedabad', 'ahdpolice@gujarat.gov.in');

-- Officers
insert into Officers (OfficerID, FirstName, LastName, BadgeNumber, Rank, ContactInformation, AgencyID)
values 
(1, 'Rakesh', 'Naik', 201, 'Inspector', 'rakesh.naik@delhipolice.in', 1),
(2, 'Sunita', 'Bose', 202, 'Sub-Inspector', 'sunita.bose@kolpolice.in', 2),
(3, 'Mahesh', 'Gowda', 203, 'Head Constable', 'mahesh.gowda@bcp.in', 3),
(4, 'Sanjay', 'Shetty', 204, 'DCP', 'sanjay.shetty@hydpolice.in', 4),
(5, 'Isha', 'Desai', 205, 'ACP', 'isha.desai@ahdpolice.in', 5);

-- Incidents
insert into Incidents (IncidentID, IncidentType, IncidentDate, LocationLatitude, LocationLongitude, Description, Status, VictimID, SuspectID, OfficerID)
values 
(1, 'Robbery', '2024-03-01', 28.6139, 77.2090, 'Jewellery store robbery near Chandni Chowk.', 'Open', 1, 1, 1),
(2, 'Assault', '2024-03-05', 22.5726, 88.3639, 'Assault case outside Victoria Memorial.', 'Closed', 2, 2, 2),
(3, 'Homicide', '2024-03-10', 12.9716, 77.5946, 'Body found in Cubbon Park.', 'Under Investigation', 3, 3, 3),
(4, 'Theft', '2024-03-15', 17.3850, 78.4867, 'Bike theft near Charminar.', 'Open', 4, 4, 4),
(5, 'Cyber Fraud', '2024-03-20', 23.0225, 72.5714, 'Online scam in banking app.', 'Closed', 5, 5, 5);

-- Evidence
insert into Evidence (EvidenceID, Description, LocationFound, IncidentID)
values 
(1, 'Gold chain recovered', 'Chandni Chowk', 1),
(2, 'Medical report and witness statement', 'Park Street', 2),
(3, 'Blood-stained clothes', 'Cubbon Park', 3),
(4, 'CCTV footage', 'Charminar Circle', 4),
(5, 'IP logs and email records', 'CG Road, Ahmedabad', 5);

-- Reports
insert into Reports (ReportID, IncidentID, ReportingOfficer, ReportDate, ReportDetails, Status)
values 
(1, 1, 1, '2024-03-02', 'Filed FIR for robbery case. Initial statement recorded.', 'Draft'),
(2, 2, 2, '2024-03-06', 'Assault suspect arrested and sent to court.', 'Finalized'),
(3, 3, 3, '2024-03-11', 'Investigation in progress. Awaiting forensic report.', 'Draft'),
(4, 4, 4, '2024-03-16', 'Stolen bike recovered. Details pending.', 'Draft'),
(5, 5, 5, '2024-03-21', 'Fraudster traced through digital trail.', 'Finalized');

-- Cases
-- Cases
insert into Cases (CaseID, IncidentID, VictimID, SuspectID, OfficerID, CaseStatus, CaseDetails)
values 
(1, 1, 1, 1, 1, 'Open', 'Suspect on the run. FIR registered.'),
(2, 2, 2, 2, 2, 'Closed', 'The suspect has been arrested and the case is closed.'),
(3, 3, 3, 3, 3, 'Open', 'Evidence sent for forensic testing.'),
(4, 4, 4, 4, 4, 'Open', 'Witnesses being questioned.'),
(5, 5, 5, 5, 5, 'Closed', 'Fraud traced and resolved by cyber cell.');


select * from Victims
select * from Suspects
select * from LawEnforcement
select * from Officers
select * from Incidents
select * from Evidence
select * from Reports
select * from Cases