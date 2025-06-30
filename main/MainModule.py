import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from service.CrimeServiceProviderImpl import CrimeServiceImpl
from entity.incident import Incident
from entity.case import Case
from tabulate import tabulate
from util.db_connection import get_connection


def register_user():
    print("\n--- Register New User ---")
    username = input("Choose a username: ")
    password = input("Choose a password: ")
    role = input("Enter role (admin/officer): ").strip().lower()

    if role not in ('admin', 'officer'):
        print("❌ Invalid role. Please enter 'admin' or 'officer'.")
        return

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Users (Username, Password, Role) VALUES (%s, %s, %s)",
                       (username, password, role))
        conn.commit()
        print("✅ User registered successfully!")
    except Exception as e:
        print("❌ Registration failed:", e)
    finally:
        cursor.close()
        conn.close()


def login():
    username = input("Username: ")
    password = input("Password: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT UserID, Role FROM Users WHERE Username = %s AND Password = %s", (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result:
        print(f"\n✅ Login successful. Role: {result[1]}")
        return result[0], result[1]
    else:
        print("❌ Invalid credentials.")
        return None, None


def main():
    print("\n--- Welcome to C.A.R.S. ---")
    print("1. Login")
    print("2. Register")
    option = input("Choose an option (1/2): ")

    if option == '2':
        register_user()
        return

    user_id, role = login()
    if not role:
        return

    service = CrimeServiceImpl()

    while True:
        print(f"\n--- C.A.R.S. MENU ({role.upper()}) ---")
        print("1. Create Incident")
        print("2. View Incidents by Date Range")
        print("3. Search Incidents by Type")
        print("4. Generate Incident Report")
        print("5. View Victims by Incident ID")
        print("6. View Suspects by Incident ID")
        print("7. View Evidence by Incident ID")
        if role == 'admin':
            print("8. Update Incident Status")
            print("9. Create Case")
            print("10. View Case Details")
            print("11. Update Case")
            print("12. View All Cases")
        print("0. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                inc = Incident(
                    None,
                    input("Type: "),
                    input("Date (YYYY-MM-DD): "),
                    input("Area: "),
                    input("City: "),
                    input("Description: "),
                    input("Status: "),
                    int(input("Officer ID: "))
                )
                service.create_incident(inc)
                print("✅ Incident created.")

            elif choice == '2':
                start = input("Start Date (YYYY-MM-DD): ")
                end = input("End Date (YYYY-MM-DD): ")
                incs = service.get_incidents_in_date_range(start, end)
                table = [[i.incident_id, i.incident_type, i.incident_date, i.city, i.status] for i in incs]
                print(tabulate(table, headers=["ID", "Type", "Date", "City", "Status"], tablefmt="fancy_grid"))

            elif choice == '3':
                itype = input("Enter Incident Type: ")
                results = service.search_incidents_by_type(itype)
                table = [[i.incident_id, i.incident_type, i.status, i.city] for i in results]
                print(tabulate(table, headers=["ID", "Type", "Status", "City"], tablefmt="fancy_grid"))

            elif choice == '4':
                inc_id = int(input("Incident ID: "))
                report = service.generate_incident_report(inc_id)
                if report:
                    print(tabulate([report.values()], headers=report.keys(), tablefmt="fancy_grid"))
                else:
                    print("❌ No report found.")

            elif choice == '5':
                inc_id = int(input("Incident ID: "))
                victims = service.get_victims_by_incident(inc_id)
                if victims:
                    table = [[v.victim_id, v.first_name, v.last_name, v.dob] for v in victims]
                    print(tabulate(table, headers=["Victim ID", "First", "Last", "DOB"], tablefmt="grid"))
                else:
                    print("❌ No victims found.")

            elif choice == '6':
                inc_id = int(input("Incident ID: "))
                suspects = service.get_suspects_by_incident(inc_id)
                if suspects:
                    table = [[s.suspect_id, s.first_name, s.last_name, s.dob] for s in suspects]
                    print(tabulate(table, headers=["Suspect ID", "First", "Last", "DOB"], tablefmt="grid"))
                else:
                    print("❌ No suspects found.")

            elif choice == '7':
                inc_id = int(input("Incident ID: "))
                evidences = service.get_evidence_by_incident(inc_id)
                if evidences:
                    table = [[e.evidence_id, e.evidence_type, e.description] for e in evidences]
                    print(tabulate(table, headers=["Evidence ID", "Type", "Description"], tablefmt="grid"))
                else:
                    print("❌ No evidence found.")

            elif choice == '8' and role == 'admin':
                inc_id = int(input("Incident ID: "))
                new_status = input("New Status: ")
                updated = service.update_incident_status(inc_id, new_status)
                print("✅ Status updated." if updated else "❌ Failed to update.")

            elif choice == '9' and role == 'admin':
                desc = input("Case Description: ")
                count = int(input("Number of Incidents: "))
                ids = [int(input(f"Incident ID #{i+1}: ")) for i in range(count)]
                case = service.create_case(desc, ids)
                print(f"✅ Case created with ID: {case.case_id}")

            elif choice == '10' and role == 'admin':
                cid = int(input("Case ID: "))
                case, incs = service.get_case_details(cid)
                print(f"\n📂 Case: {case.case_description}")
                table = [[i.incident_id, i.incident_type, i.status] for i in incs]
                print(tabulate(table, headers=["Incident ID", "Type", "Status"], tablefmt="grid"))

            elif choice == '11' and role == 'admin':
                cid = int(input("Case ID: "))
                new_desc = input("New Description: ")
                success = service.update_case(Case(cid, new_desc))
                print("✅ Case updated." if success else "❌ Failed.")

            elif choice == '12' and role == 'admin':
                cases = service.get_all_cases()
                table = [[c.case_id, c.case_description] for c in cases]
                print(tabulate(table, headers=["Case ID", "Description"], tablefmt="grid"))

            elif choice == '0':
                print("👋 Exiting...")
                break
            else:
                print("❌ Invalid or unauthorized option.")

        except Exception as e:
            print("❌ Error:", e)


if __name__ == "__main__":
    main()
