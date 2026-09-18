class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name

    def get_details(self):
        pass

    def update_details(self):
        pass


class Practitioner:
    def __init__(self, practitioner_id, name):
        self.practitioner_id = practitioner_id
        self.name = name

    def get_details(self):
        pass

    def update_details(self):
        pass


class Appointment:
    def __init__(
        self,
        appointment_id,
        appointment_time,
        status,
        patient,
        practitioner
    ):
        self.appointment_id = appointment_id
        self.appointment_time = appointment_time
        self.status = status
        self.patient = patient
        self.practitioner = practitioner

    def update_status(self):
        pass

    def cancel(self):
        pass