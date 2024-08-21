# Child Vaccination Management System

## Overview
The Child Vaccination Management System is a console-based application developed in Python. It is designed to help parents manage their children's vaccination schedules, book appointments, and view vaccination history and reminders. The system is user-friendly and operates without the need for frontend or database storage, making it simple yet efficient for use.

## Features
- **Book Vaccination Appointments:** Easily schedule vaccination appointments for your child by entering the date and vaccine name.
- **View Vaccination Reminders:** Stay updated with upcoming vaccination appointments.
- **View Vaccine Information:** Access a predefined list of vaccines and their schedules.
- **Vaccination History:** Track your child's vaccination history, including completed and upcoming appointments.
- **Smart Appointment Suggestions:** Receive suggestions for future vaccination dates based on previous bookings.
- **Auto-Completion of Appointments:** Automatically mark past appointments as completed.

## Requirements
- **Python 3.x:** Make sure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Installation
1. **Clone the Repository or Download the Files:**
   - Clone this repository or download the `vaccination_system.py` file to your local machine.

2. **Navigate to the Project Directory:**
   - Open a terminal or command prompt and navigate to the directory where the script is saved:
     ```bash
     cd path_to_directory
     ```

3. **Run the Script:**
   - Execute the script using Python:
     ```bash
     python vaccination_system.py
     ```

## How to Use
1. **Start the Application:**
   - Upon running the script, you will be greeted with a welcome message and a menu of options.

2. **Menu Options:**
   - **1. Book a Vaccination Appointment:** Enter your name, your child's name, the desired appointment date, and the vaccine name to book an appointment.
   - **2. View Vaccination Reminders:** Displays upcoming appointments for your child.
   - **3. View Vaccine Information:** Lists predefined vaccine schedules and their recommended administration times.
   - **4. View Vaccination History:** Shows past and future vaccination records for your child.
   - **5. Exit:** Exit the system.

3. **Advanced Features:**
   - **Auto-Completion of Appointments:** Any appointments that have passed their scheduled date will automatically be marked as completed when you view your child's vaccination history.
   - **Smart Appointment Suggestions:** After booking several appointments, the system will suggest future dates for vaccination based on the last appointment.

## Example Usage

```plaintext
Welcome to the Child Vaccination Management System!

===== Child Vaccination Management System =====
1. Book a Vaccination Appointment
2. View Vaccination Reminders
3. View Vaccine Information
4. View Vaccination History
5. Exit
===============================================
Choose an option: 1
Enter your name: Suhash
Enter your child's name: Arun
Enter the desired date for the appointment (YYYY-MM-DD): 2024-09-15
Enter the vaccine name: Polio
Appointment for Arun to receive Polio on 2024-09-15 has been successfully booked!
