-- creating a database
create database crimeReporting
use crimeReporting

-- Victims
/*VictimID (Primary Key) 
FirstName 
LastName 
DateOfBirth 
Gender 
Contact Information (e.g., Address, Phone Number)*/
create table Victims(
VictimID int primary key,
FirstName varchar(25),
LastName varchar(25),
DateOfBirth date,
Gender varchar(15) check(Gender in ('Male', 'Female', 'Transgender')),
ContactInformation text
);

--Suspects
/* SuspectID (Primary Key) 
FirstName 
LastName 
DateOfBirth 
Gender 
Contact Information*/
create table Suspects(
SuspectID int primary key,
FirstName varchar(25),
LastName varchar(25),
DateOfBirth date,
Gender varchar(15) check(Gender in ('Male', 'Female', 'Transgender')),
ContactInformation text
);

--Law Enforcement Agencies: 
/*AgencyID (Primary Key) 
AgencyName 
Jurisdiction 
Contact Information 
Officer(s) (Link to Officers within the agency)*/
create table LawEnforcement(
AgencyID int primary key, 
AgencyName varchar(100),
Jurisdiction varchar(50),
ContactInformation text,
);

--Officers: 
/*OfficerID (Primary Key) 
FirstName 
LastName 
BadgeNumber 
Rank 
Contact Information 
AgencyID (Foreign Key, linking to Law Enforcement Agencies)*/
create table Officers(
OfficerID int primary key, 
FirstName varchar(25),
LastName varchar(25),
BadgeNumber int,
Rank varchar(50),
ContactInformation text,
AgencyID int foreign key references LawEnforcement(AgencyID)
);

-- Incidents 
/*IncidentID (Primary Key) 
IncidentType (e.g., Robbery, Homicide, Theft) 
IncidentDate 
Location (Geospatial Data: Latitude and Longitude) 
Description 
Status (e.g., Open, Closed, Under Investigation) 
VictimID (Foreign Key, linking to Victims) 
SuspectId(Foreign Key, Linking to Suspect) 
OfficerId(Foreign key Linking to Officer)*/
create table Incidents(
IncidentID int primary key,
IncidentType varchar(20),
IncidentDate date,
LocationLatitude float,
LocationLongitude float,
Description text,
Status varchar(25) check(Status in ('Open', 'Closed', 'Under Investigation')),
VictimID int foreign key references Victims(VictimID),
SuspectID int foreign key references Suspects(SuspectID),
OfficerID int foreign key references Officers(OfficerID)
);

--Evidence: 
/*EvidenceID (Primary Key) 
Description 
Location Found 
IncidentID (Foreign Key, linking to Incidents) */
create table Evidence(
EvidenceID int primary key, 
Description text,
LocationFound varchar(100),
IncidentID int foreign Key references Incidents(IncidentID)
);

--Reports: 
/*ReportID (Primary Key) 
IncidentID (Foreign Key, linking to Incidents) 
ReportingOfficer (Foreign Key, linking to Officers) 
ReportDate 
ReportDetails 
Status (e.g., Draft, Finalized)*/
create table Reports(
ReportID int primary key, 
IncidentID int foreign key references Incidents(IncidentID),
ReportingOfficer int foreign key references Officers(OfficerID),
ReportDate date,
ReportDetails text,
Status varchar(25) check(Status in ('Draft', 'Finalized'))
);

create table Cases (
CaseID int primary key,
IncidentID int foreign key references Incidents(IncidentID),
VictimID int foreign key references Victims(VictimID),
SuspectID int foreign key references Suspects(SuspectID),
OfficerID int foreign key references Officers(OfficerID),
CaseStatus varchar(25) check (CaseStatus in ('Open', 'Closed')),
CaseDetails text
);

select * from Victims
select * from Suspects
select * from LawEnforcement
select * from Officers
select * from Incidents
select * from Evidence
select * from Reports
select * from Cases
