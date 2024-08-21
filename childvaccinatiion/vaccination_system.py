import datetime
import time

# Data storage for parents and appointments
parents_data = {}

# Predefined list of vaccines and schedules
vaccine_schedule = {
    "BCG": "At birth",
    "Hepatitis B": "At birth, 1 month, 6 months",
    "DTP": "2 months, 4 months, 6 months, 15-18 months",
    "Polio": "2 months, 4 months, 6 months, booster at 4-6 years",
    "MMR": "12-15 months, booster at 4-6 years"
}

def show_menu():
    print("\n===== Child Vaccination Management System =====")
    print("1. Book a Vaccination Appointment")
    print("2. View Vaccination Reminders")
    print("3. View Vaccine Information")
    print("4. View Vaccination History")
    print("5. Exit")
    print("===============================================")

def book_appointment():
    parent_name = input("Enter your name: ")
    child_name = input("Enter your child's name: ")
    date_str = input("Enter the desired date for the appointment (YYYY-MM-DD): ")
    vaccine_name = input("Enter the vaccine name: ")

    # Validate date input
    try:
        appointment_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format! Please enter the date in YYYY-MM-DD format.")
        return

    # Store appointment data
    if parent_name not in parents_data:
        parents_data[parent_name] = []

    parents_data[parent_name].append({
        "child_name": child_name,
        "appointment_date": appointment_date,
        "vaccine_name": vaccine_name,
        "status": "Scheduled"
    })

    print(f"Appointment for {child_name} to receive {vaccine_name} on {appointment_date} has been successfully booked!")

def view_reminders():
    parent_name = input("Enter your name: ")
    today = datetime.date.today()
    
    if parent_name in parents_data:
        print("\nUpcoming Vaccination Reminders:")
        has_reminders = False
        for record in parents_data[parent_name]:
            if record["appointment_date"] > today and record["status"] == "Scheduled":
                print(f"{record['child_name']} - {record['vaccine_name']} on {record['appointment_date']}")
                has_reminders = True
        if not has_reminders:
            print("No upcoming appointments found.")
    else:
        print("No records found.")

def show_vaccine_info():
    print("\n===== Vaccine Information =====")
    for vaccine, schedule in vaccine_schedule.items():
        print(f"{vaccine}: {schedule}")
    print("================================\n")

def view_history():
    parent_name = input("Enter your name: ")
    
    if parent_name in parents_data:
        print(f"\nVaccination history for {parent_name}:")
        for record in parents_data[parent_name]:
            status = "Completed" if record["appointment_date"] < datetime.date.today() else record["status"]
            print(f"{record['child_name']} - {record['vaccine_name']} on {record['appointment_date']} ({status})")
    else:
        print("No records found.")

def mark_appointments_as_completed():
    """Automatically marks past appointments as completed."""
    today = datetime.date.today()
    for parent, records in parents_data.items():
        for record in records:
            if record["appointment_date"] < today and record["status"] == "Scheduled":
                record["status"] = "Completed"

def smart_appointment_suggestion():
    parent_name = input("Enter your name: ")
    
    if parent_name in parents_data:
        latest_appointment = max(parents_data[parent_name], key=lambda x: x["appointment_date"])
        next_suggested_date = latest_appointment["appointment_date"] + datetime.timedelta(days=30)
        print(f"Suggested next appointment date for {latest_appointment['child_name']}: {next_suggested_date}")
    else:
        print("No records found. Please book an initial appointment first.")

def main():
    print("Welcome to the Child Vaccination Management System!")
    
    while True:
        show_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            book_appointment()
        elif choice == "2":
            view_reminders()
        elif choice == "3":
            show_vaccine_info()
        elif choice == "4":
            view_history()
        elif choice == "5":
            print("Exiting the system... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
        
        mark_appointments_as_completed()

if __name__ == "__main__":
    main()
