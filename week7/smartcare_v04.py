from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "SCHEDULED"
    CANCELLED = "CANCELLED"


class InvalidStatusTransitionError(Exception):
    """Raised when an appointment status transition is not allowed."""
    pass


class Patient:
    def __init__(self, patient_id: str, name: str):
        if not isinstance(patient_id, str) or not patient_id.strip():
            raise ValueError("Patient ID cannot be empty")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Patient name cannot be empty")

        self.patient_id = patient_id.strip()
        self.name = name.strip()

    def get_details(self):
        return {
            "patient_id": self.patient_id,
            "name": self.name
        }

    def update_details(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Patient name cannot be empty")

        self.name = name.strip()


class Practitioner:
    def __init__(
        self,
        practitioner_id: str,
        name: str,
        specialty: str
    ):
        if not isinstance(practitioner_id, str) or not practitioner_id.strip():
            raise ValueError("Practitioner ID cannot be empty")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Practitioner name cannot be empty")

        if not isinstance(specialty, str) or not specialty.strip():
            raise ValueError("Practitioner specialty cannot be empty")

        self.practitioner_id = practitioner_id.strip()
        self.name = name.strip()
        self.specialty = specialty.strip()

    def get_details(self):
        return {
            "practitioner_id": self.practitioner_id,
            "name": self.name,
            "specialty": self.specialty
        }

    def update_details(self, name: str, specialty: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Practitioner name cannot be empty")

        if not isinstance(specialty, str) or not specialty.strip():
            raise ValueError("Practitioner specialty cannot be empty")

        self.name = name.strip()
        self.specialty = specialty.strip()


class Appointment:
    def __init__(
        self,
        appointment_id: str,
        appointment_time: str,
        patient: Patient,
        practitioner: Practitioner
    ):
        if not isinstance(appointment_id, str) or not appointment_id.strip():
            raise ValueError("Appointment ID cannot be empty")

        if not isinstance(appointment_time, str) or not appointment_time.strip():
            raise ValueError("Appointment time cannot be empty")

        if not isinstance(patient, Patient):
            raise TypeError("patient must be a Patient object")

        if not isinstance(practitioner, Practitioner):
            raise TypeError("practitioner must be a Practitioner object")

        self.appointment_id = appointment_id.strip()
        self.appointment_time = appointment_time.strip()
        self.patient = patient
        self.practitioner = practitioner
        self._status = AppointmentStatus.SCHEDULED

    @property
    def status(self):
        return self._status

    def cancel(self):
        if self._status != AppointmentStatus.SCHEDULED:
            raise InvalidStatusTransitionError(
                "Only a scheduled appointment can be cancelled"
            )

        self._status = AppointmentStatus.CANCELLED


# -------------------------------------------------
# Part F - Manual Behaviour Checks
# -------------------------------------------------

print("--- Test 1: Create valid objects ---")

patient = Patient("P001", "Alice Smith")

practitioner = Practitioner(
    "PR001",
    "Dr. John Doe",
    "General Practice"
)

appointment = Appointment(
    "A001",
    "2026-09-22 10:00 AM",
    patient,
    practitioner
)

print(patient.get_details())
print(practitioner.get_details())
print("Appointment status:", appointment.status.value)


print("\n--- Test 2: Invalid Patient input ---")

try:
    Patient("P002", "")
except ValueError as error:
    print(error)


print("\n--- Test 3: Invalid Practitioner input ---")

try:
    Practitioner(
        "PR002",
        "Dr. Jane Roe",
        ""
    )
except ValueError as error:
    print(error)


print("\n--- Test 4: Cancel scheduled appointment ---")

appointment.cancel()
print("Appointment status:", appointment.status.value)


print("\n--- Test 5: Illegal repeated cancellation ---")

try:
    appointment.cancel()
except InvalidStatusTransitionError as error:
    print(error)