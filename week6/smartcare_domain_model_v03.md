# SmartCare v0.3 – Domain Model Workbook

## 1. Requirement-to-Concept Trace

| Requirement | Concept | State / Behaviour | Decision |
|---|---|---|---|
| FR-01 – Create patient record | Patient | patient_id, name | Include Patient as a core class because patient information must be represented by the system. |
| FR-02 – Search and view patient information | Patient | get_details() | Allocate responsibility for representing and providing patient information to Patient. |
| FR-03 – Update patient information | Patient | update_details() | Patient requires behaviour representing updates to its information. |
| FR-04 – Create practitioner record | Practitioner | practitioner_id, name | Include Practitioner as a core class because practitioner information must be represented. |
| FR-05 – View practitioner information | Practitioner | get_details() | Allocate responsibility for representing and providing practitioner information to Practitioner. |
| FR-06 – Update practitioner information | Practitioner | update_details() | Practitioner requires behaviour representing updates to its information. |
| FR-07 – Create an appointment linking a patient and practitioner | Appointment | appointment_id, appointment_time, patient, practitioner | Include Appointment as a core class associated with Patient and Practitioner. |
| FR-08 – Prevent bookings that violate confirmed duplicate-booking rules | Appointment | Appointment booking constraint | Keep as Appointment-related business behaviour; exact rule still requires client confirmation. |
| FR-09 – View appointment status | Appointment | status | Represent status as an attribute of Appointment rather than a separate class. |
| FR-10 – Update appointment status | Appointment | update_status() | Allocate status-changing behaviour to Appointment. |
| FR-11 – Cancel an appointment | Appointment | cancel() | Represent cancellation as Appointment behaviour rather than a separate Cancellation class. |
| FR-12 – Retain and view appointment history | Appointment | Appointment records/associations | Appointment remains the core concept required for appointment history. |

---

## 2. CRC Cards

### Patient

| Responsibilities | Collaborators |
|---|---|
| Store patient information | Appointment |
| Provide patient information when required | Appointment |
| Represent updates to patient information | Appointment |
| Be associated with patient appointments | Appointment |

### Practitioner

| Responsibilities | Collaborators |
|---|---|
| Store practitioner information | Appointment |
| Provide practitioner information when required | Appointment |
| Represent updates to practitioner information | Appointment |
| Be associated with scheduled appointments | Appointment |

### Appointment

| Responsibilities | Collaborators |
|---|---|
| Store appointment date/time and status | Patient, Practitioner |
| Associate one patient with one practitioner | Patient, Practitioner |
| Maintain appointment status | Patient, Practitioner |
| Support appointment cancellation | Patient, Practitioner |
| Represent appointment information required for history | Patient, Practitioner |

### Optional Class – Clinic

| Responsibilities | Collaborators |
|---|---|
| No separate responsibility is confirmed by the current requirements | Patient, Practitioner, Appointment |

**Decision:** Clinic is not included as a core class in the current model. Although
the clinic exists in the problem domain, the confirmed requirements do not give
a separate `Clinic` object a clear state or responsibility. It remains
provisional and can be reconsidered if later requirements justify it.

---

## 3. UML Class Diagram

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

### Relationships and Multiplicities

**Patient 1 —— 0..\* Appointment**

A Patient may have zero or many Appointments. Each Appointment is associated
with one Patient.

**Practitioner 1 —— 0..\* Appointment**

A Practitioner may have zero or many Appointments. Each Appointment is
associated with one Practitioner.

No inheritance relationship is required. Appointment is not a type of Patient
or Practitioner; it is a separate domain concept that associates them.

---

## 4. Design Rationale

The domain model uses **Patient, Practitioner and Appointment** as its three
core classes because these concepts have clear state, responsibilities and
direct support from the SmartCare functional requirements.

Patient is responsible for representing patient information and is supported
by FR-01 to FR-03. Practitioner represents practitioner information and is
supported by FR-04 to FR-06. Appointment represents the scheduling relationship
between a patient and practitioner and is supported by FR-07 to FR-12.

Status is represented as an attribute of Appointment because the current
requirements only require appointment status to be viewed and updated.
Cancellation is represented as behaviour of Appointment because FR-11 requires
an appointment to be cancelled but does not establish Cancellation as an
independent domain entity.

Patient and Practitioner each have an association with Appointment. A Patient
may have zero or many Appointments, while each Appointment is associated with
one Patient. Similarly, a Practitioner may have zero or many Appointments,
while each Appointment is associated with one Practitioner.

The model deliberately avoids unnecessary manager, controller and engine
classes. This keeps the design consistent with the confirmed requirements and
appropriate for SmartCare's small, manageable initial system.

---

## 5. AI Design Review Record

| AI Suggestion | Evidence | Decision | Reason | Model Change |
|---|---|---|---|---|
| Use Patient as a core class | FR-01, FR-02, FR-03 | **Accepted** | Patient has clear state and responsibilities supported by the requirements. | Patient retained as a core class. |
| Use Practitioner as a core class | FR-04, FR-05, FR-06 | **Accepted** | Practitioner has clear state and responsibilities supported by the requirements. | Practitioner retained as a core class. |
| Use Appointment to associate Patient and Practitioner | FR-07 | **Accepted** | FR-07 requires an appointment linking a patient and practitioner. | Patient–Appointment and Practitioner–Appointment associations retained. |
| Add a separate ScheduleEngine | Practitioner availability is relevant, but no requirement confirms a scheduling engine | **Modified** | Scheduling concerns may be relevant, but a separate engine would over-design the current domain model. | No ScheduleEngine added; existing Appointment relationships retained. |
| Add NotificationManager | No supporting requirement | **Rejected** | Notifications and reminders are not confirmed requirements. | No NotificationManager added. |
| Add ClinicController | No supporting requirement | **Rejected** | A controller is a software design concept rather than a confirmed SmartCare domain entity. | No ClinicController added. |
| Represent Status as a separate class | FR-09, FR-10 | **Modified** | Status is required, but the current requirements do not justify an independent class. | Status represented as an Appointment attribute. |
| Represent Cancellation as a separate class | FR-11 | **Modified** | Cancellation is required behaviour, but no independent Cancellation entity is established. | `cancel()` retained as Appointment behaviour. |

---

## Final Domain Model Decision

The final SmartCare v0.3 domain model contains three core classes:

- **Patient**
- **Practitioner**
- **Appointment**

The model is traceable to the SmartCare v0.2 requirements, avoids unsupported
classes, and is consistent with the Python class skeletons in
`smartcare_v03.py`.