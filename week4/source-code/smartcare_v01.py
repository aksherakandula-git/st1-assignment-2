#task 1
#basic version
print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# First Appointment
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'

print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")

# Second Appointment
patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM'

print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")

# task1enhanced

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    if not practitioner_name:
        raise ValueError("Practitioner name cannot be empty")
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)


def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return

    for appointment in appointments:
        print(
            f"Patient: {appointment['patient']} | "
            f"Practitioner: {appointment['practitioner']} | "
            f"Time: {appointment['time']}"
        )


print("Welcome to SmartCare: The Clinical Appointment Booking System!")

book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')

display_appointments()

#Part D - AI Alternative
appointments = []

def add_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)
    print("Appointment stored successfully.")

# Part F - Verify Behaviour

print("\n--- Part F Tests ---")

# Test 1: Normal appointment
print("\nTest 1: Normal appointment")
book_appointment("Charlie Brown", "Dr. John Doe", "2024-07-20 2:00 PM")
display_appointments()

# Test 2: Blank patient name
print("\nTest 2: Blank patient name")
try:
    book_appointment("", "Dr. John Doe", "2024-07-20 3:00 PM")
except ValueError as error:
    print(error)

# Test 3: Same practitioner and same time
print("\nTest 3: Duplicate practitioner/time")
book_appointment("David Lee", "Dr. Jane Roe", "2024-07-20 4:00 PM")
book_appointment("Emma Jones", "Dr. Jane Roe", "2024-07-20 4:00 PM")
display_appointments()

# Test 4: Strange input using None
print("\nTest 4: None values")
try:
    book_appointment(None, "Dr. John Doe", None)
except ValueError as error:
    print(error)

# Part F - Verify Behaviour

print("\n--- Part F Tests ---")

# Test 1: Normal appointment
print("\nTest 1: Normal appointment")
book_appointment("Charlie Brown", "Dr. John Doe", "2024-07-20 2:00 PM")
display_appointments()

# Test 2: Blank patient name
print("\nTest 2: Blank patient name")
try:
    book_appointment("", "Dr. John Doe", "2024-07-20 3:00 PM")
except ValueError as error:
    print(error)

# Test 3: Two appointments for the same practitioner and time
print("\nTest 3: Duplicate practitioner/time")
book_appointment("David Lee", "Dr. Jane Roe", "2024-07-20 4:00 PM")
book_appointment("Emma Jones", "Dr. Jane Roe", "2024-07-20 4:00 PM")
display_appointments()

# Test 4: Strange input using None
print("\nTest 4: None values")
try:
    book_appointment(None, "Dr. John Doe", None)
except ValueError as error:
    print(error)

# Part G - Test controlled Improvement
print("\nPart G: Blank practitioner name")

try:
    book_appointment("Grace Lee", "", "2024-07-20 5:00 PM")
except ValueError as error:
    print(error)
