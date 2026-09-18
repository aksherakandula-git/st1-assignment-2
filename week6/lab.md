# Stage 3 Lab – SmartCare Domain Modelling

**AI OFF → AI ON → COMPARE → VERIFY**

---

## Part A – Requirements Review

The SmartCare v0.2 requirements were reviewed to identify important nouns, verbs and business rules that can inform the domain model.

### Nouns / Domain Concepts

- Patient
- Practitioner
- Appointment
- Patient information
- Practitioner information
- Appointment status
- Appointment history
- Practitioner availability

### Verbs / Behaviours

- Create patient record
- Search patient information
- Update patient information
- Create practitioner record
- View practitioner information
- Update practitioner information
- Create appointment
- View appointment status
- Update appointment status
- Cancel appointment
- View appointment history
- Prevent duplicate bookings

### Business Rules

1. An appointment links a patient with a practitioner.
2. Appointment bookings must comply with the clinic's confirmed duplicate-booking rules.
3. An appointment has a status that can be viewed and updated.
4. Appointment history must be retained and viewable.
5. Patient, practitioner and appointment information must remain accurate and consistent.

---

## Part B – Candidate Classes

| Candidate Concept | Supporting Requirement(s) | State / Attributes | Behaviour / Responsibilities |
|---|---|---|---|
| Patient | FR-01, FR-02, FR-03 | patient_id, name | Store patient information and support access to patient details |
| Practitioner | FR-04, FR-05, FR-06 | practitioner_id, name | Store and provide practitioner information |
| Appointment | FR-07, FR-08, FR-09, FR-10, FR-11, FR-12 | appointment_id, appointment_time, status | Link a patient and practitioner, maintain status and support cancellation |
| Clinic | No direct requirement establishes a separate responsibility | Not confirmed | Keep provisional unless later requirements justify a separate Clinic class |
| Status | FR-09, FR-10 | Appointment status value | Better represented as an Appointment attribute at this stage |
| Cancellation | FR-11 | No independent state confirmed | Better represented as Appointment behaviour rather than a separate class |
| Database | None | Not applicable | Technical implementation concept rather than a SmartCare domain class |

### Selected Core Classes

The final core domain classes are:

- **Patient**
- **Practitioner**
- **Appointment**

These concepts have clear state, responsibilities and direct support from the SmartCare requirements.

---

## Part C – CRC Cards

### Patient

| Responsibilities | Collaborators |
|---|---|
| Store patient information | Appointment |
| Provide patient information when required | Appointment |
| Be associated with patient appointments | Appointment |

### Practitioner

| Responsibilities | Collaborators |
|---|---|
| Store practitioner information | Appointment |
| Provide practitioner information when required | Appointment |
| Be associated with scheduled appointments | Appointment |

### Appointment

| Responsibilities | Collaborators |
|---|---|
| Store appointment date/time and status | Patient, Practitioner |
| Associate one patient with one practitioner | Patient, Practitioner |
| Maintain appointment status | Patient, Practitioner |
| Support appointment cancellation | Patient, Practitioner |

---

## Part D – UML Model

### Patient

**Attributes**
- patient_id
- name

**Operations**
- get_details()
- update_details()

### Practitioner

**Attributes**
- practitioner_id
- name

**Operations**
- get_details()
- update_details()

### Appointment

**Attributes**
- appointment_id
- appointment_time
- status
- patient
- practitioner

**Operations**
- update_status()
- cancel()

### Associations and Multiplicities

**Patient 1 —— 0..\* Appointment**

One Patient may have zero or many Appointments.  
Each Appointment is associated with one Patient.

**Practitioner 1 —— 0..\* Appointment**

One Practitioner may have zero or many Appointments.  
Each Appointment is associated with one Practitioner.

### Inheritance

No inheritance relationship is required between Patient, Practitioner and Appointment.

An Appointment is not a type of Patient or Practitioner. Instead, Appointment is a separate domain entity that associates a Patient with a Practitioner.

### UML Diagram

```text
+--------------------+
|      Patient       |
+--------------------+
| patient_id         |
| name               |
+--------------------+
| get_details()      |
| update_details()   |
+--------------------+
          1
          |
          |
         0..*
+--------------------+
|    Appointment     |
+--------------------+
| appointment_id     |
| appointment_time   |
| status             |
| patient            |
| practitioner       |
+--------------------+
| update_status()    |
| cancel()           |
+--------------------+
         0..*
          |
          |
          1
+--------------------+
|   Practitioner     |
+--------------------+
| practitioner_id    |
| name               |
+--------------------+
| get_details()      |
| update_details()   |
+--------------------+
```

---

## Part E – AI Design Review

### Prompt Used

> Suggest classes and relationships for the SmartCare domain model using only confirmed requirements. For every proposed class or relationship, provide the supporting requirement ID. Do not introduce functionality that is not supported by the requirements.

### AI Design Review

| AI Suggestion | Supporting Requirement(s) | Review |
|---|---|---|
| Patient class | FR-01, FR-02, FR-03 | Supported. Patient is a core domain concept with information and responsibilities. |
| Practitioner class | FR-04, FR-05, FR-06 | Supported. Practitioner is a core domain concept with its own information and responsibilities. |
| Appointment class | FR-07 to FR-12 | Supported. Appointment has its own state and behaviour and connects patients with practitioners. |
| Patient–Appointment association | FR-07, FR-12 | Supported. An appointment links to a patient, and appointment history must be retained. |
| Practitioner–Appointment association | FR-07 | Supported. An appointment links a patient with a practitioner. |
| NotificationManager class | No supporting requirement | Unsupported. Notifications or reminders are not confirmed SmartCare requirements. |
| ClinicController class | No supporting requirement | Unsupported as a domain class. It introduces a controller/design concept without requirement evidence. |
| ScheduleEngine class | No confirmed supporting requirement | Requires validation. Practitioner availability is relevant, but a separate scheduling engine is not established by the requirements. |

---

## Part F – Compare and Decide

| AI Suggestion | Decision | Reason |
|---|---|---|
| Use Patient as a core domain class. | **Accepted** | Patient management is directly supported by FR-01 to FR-03. |
| Represent practitioner scheduling using a separate ScheduleEngine. | **Modified** | Practitioner availability is relevant, but the requirements do not justify a separate scheduling engine. The Practitioner–Appointment relationship is retained without adding the engine. |
| Add NotificationManager. | **Rejected** | No confirmed requirement supports notifications or reminders. |
| Use Appointment as the link between Patient and Practitioner. | **Accepted** | FR-07 supports an appointment linking a patient with a practitioner. |
| Add ClinicController as a domain class. | **Rejected** | ClinicController introduces a design/implementation concept without requirement evidence establishing it as a domain entity. |

This comparison contains at least one **Accepted**, one **Modified**, and one **Rejected** AI suggestion.

---

## Part G – Python Skeletons

The Python skeletons represent the three selected core domain classes without implementing the complete SmartCare behaviour.

```python
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
```

The methods intentionally use `pass` because Stage 3 requires simple class skeletons rather than full behaviour.

---

## Part H – Consistency Check

| Model Element | UML Model | Python Skeleton | Consistent? |
|---|---|---|---|
| Patient class | Present | Present | Yes |
| Patient attributes | patient_id, name | patient_id, name | Yes |
| Patient operations | get_details(), update_details() | get_details(), update_details() | Yes |
| Practitioner class | Present | Present | Yes |
| Practitioner attributes | practitioner_id, name | practitioner_id, name | Yes |
| Practitioner operations | get_details(), update_details() | get_details(), update_details() | Yes |
| Appointment class | Present | Present | Yes |
| Appointment attributes | appointment_id, appointment_time, status, patient, practitioner | Same attributes | Yes |
| Appointment operations | update_status(), cancel() | update_status(), cancel() | Yes |
| Patient–Appointment relationship | Association | Appointment stores a patient reference | Yes |
| Practitioner–Appointment relationship | Association | Appointment stores a practitioner reference | Yes |
| Inheritance | None | None | Yes |

### Consistency Result

The UML model and Python class skeletons are consistent. The three core classes, their attributes, operations and relationships are represented in both the model and code.

Full business behaviour has deliberately not been implemented because Stage 3 only requires simple class skeletons.

---

## Reflection

The hardest modelling decision was deciding which candidate concepts should become classes and which should remain attributes or behaviours. Patient, Practitioner and Appointment clearly have their own state, responsibilities and relationships, while Status and Cancellation can be represented more simply as an Appointment attribute and behaviour.

AI tended to over-design the model by suggesting additional classes such as NotificationManager, ClinicController and ScheduleEngine. Although these classes may sound reasonable in a larger system, the current SmartCare requirements do not provide enough evidence to justify them. Adding them would increase complexity without addressing a confirmed requirement.

The final modelling choices were supported by the SmartCare v0.2 requirements. Patient is supported by FR-01 to FR-03, Practitioner by FR-04 to FR-06, and Appointment by FR-07 to FR-12. FR-07 also supports the associations between Appointment, Patient and Practitioner. Using requirement evidence helped keep the final model simple, consistent and appropriate for the small SmartCare system.

