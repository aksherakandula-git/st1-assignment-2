# Stage 4 Lab – Implementing the SmartCare Domain Layer

**DESIGN FIRST → AI PAIR PROGRAMMING → REVIEW → VERIFY**

---

## Part A – Revisit Approved UML

Before implementation, the approved Stage 3 domain model was reviewed.

### Confirmed Core Classes

- Patient
- Practitioner
- Appointment

### Patient

**Attributes**
- patient_id
- name

**Responsibilities**
- maintain valid patient information;
- provide access to patient details.

### Practitioner

**Attributes**
- practitioner_id
- name
- specialty

**Responsibilities**
- maintain valid practitioner information;
- provide access to practitioner details.

### Appointment

**Attributes**
- appointment_id
- appointment_time
- status
- patient
- practitioner

**Responsibilities**
- associate one Patient with one Practitioner;
- maintain appointment state;
- protect appointment status transitions;
- support cancellation.

### Relationships

- Patient is associated with Appointment.
- Practitioner is associated with Appointment.
- Appointment does not inherit from Patient or Practitioner.
- Domain classes should not contain database, UI or notification logic.

---

## Part B – Implement Patient: AI OFF

Patient is implemented with type hints and basic validation.

### Design Decisions

- `patient_id` must be a non-empty string.
- `name` must be a non-empty string.
- Validation is owned by the Patient class rather than the UI.
- Patient contains no database logic.
- Patient state should only be changed through controlled class behaviour.

### Intended Python Structure

```python
class Patient:
    def __init__(self, patient_id: str, name: str):
        ...
```

The completed implementation is contained in `smartcare_v04.py`.

---

## Part C – Implement Practitioner: AI OFF

Practitioner is implemented with an identifier, name and specialty.

### Design Decisions

- `practitioner_id` must be a non-empty string.
- `name` must be a non-empty string.
- `specialty` must be a non-empty string.
- Validation belongs inside Practitioner.
- Practitioner contains no database logic.

### Intended Python Structure

```python
class Practitioner:
    def __init__(
        self,
        practitioner_id: str,
        name: str,
        specialty: str
    ):
        ...
```

The completed implementation is contained in `smartcare_v04.py`.

---

## Part D – Implement Appointment: AI ON

### AI Pair-Programming Prompt

> Act as a Python pair programmer. Implement only the Appointment class from
> the approved SmartCare UML. Use type hints and an AppointmentStatus enum.
> Cancelled appointments remain as objects. Do not add database, UI,
> notification or service classes. Protect status transitions and explain any
> decision not directly visible in the UML.

### Constraints Given to AI

The implementation was required to:

- use the approved Patient–Appointment and Practitioner–Appointment associations;
- keep Appointment independent of database and UI logic;
- use an `AppointmentStatus` enum;
- protect appointment status from uncontrolled mutation;
- allow a scheduled appointment to be cancelled;
- retain cancelled Appointment objects rather than deleting them; and
- reject an illegal repeated cancellation.

### Generated Contribution

The AI-assisted Appointment implementation introduced:

- an `AppointmentStatus` enum;
- an `InvalidStatusTransitionError` exception;
- validated Patient and Practitioner references;
- protected internal appointment status;
- a read-only status property; and
- a `cancel()` method that enforces the allowed transition.

The final implementation is contained in `smartcare_v04.py`.

---

## Part E – Review Generated Code

The generated Appointment code was reviewed against the approved domain design.

| Review area | Finding | Decision |
|---|---|---|
| Model consistency | Appointment still references one Patient and one Practitioner. | Accept |
| AppointmentStatus enum | Gives status values a controlled representation. | Accept |
| Protected status | External code cannot freely assign a new status. | Accept |
| Cancellation rule | `cancel()` controls the transition from SCHEDULED to CANCELLED. | Accept |
| Repeated cancellation | Illegal repeated cancellation raises an exception. | Accept |
| Database logic | No SQL or persistence code is inside Appointment. | Accept |
| UI logic | No user-interface behaviour is included. | Accept |
| Notification dependency | No NotificationManager was added. | Accept |
| Inheritance | Appointment does not inherit from Patient or Practitioner. | Accept |
| Extra unsupported services | No service/controller classes were introduced. | Accept |

### Review Conclusion

The generated code follows the approved design more closely after restricting
the implementation to domain responsibilities only.

Appointment remains responsible for appointment state and legal state changes,
while persistence, UI and notification concerns remain outside the domain
class.

---

## Part F – Manual Behaviour Checks

The following behaviour checks are performed against `smartcare_v04.py`.

### Test 1 – Create Valid Objects

**Input**
- valid Patient
- valid Practitioner
- valid scheduled Appointment

**Expected result**
- all objects are created successfully;
- Appointment references the correct Patient and Practitioner;
- initial status is `SCHEDULED`.

### Test 2 – Invalid Patient Input

**Input**
- empty patient name

**Expected result**
- `ValueError` is raised;
- invalid Patient object is not successfully created.

### Test 3 – Invalid Practitioner Input

**Input**
- empty specialty

**Expected result**
- `ValueError` is raised;
- invalid Practitioner object is not successfully created.

### Test 4 – Cancel Scheduled Appointment

**Given**
an Appointment has status `SCHEDULED`

**When**
`cancel()` is called

**Then**
the status becomes `CANCELLED`.

### Test 5 – Illegal Repeated Transition

**Given**
an Appointment is already `CANCELLED`

**When**
`cancel()` is called again

**Then**
`InvalidStatusTransitionError` is raised and the Appointment remains
`CANCELLED`.

### Verification Result

The behaviour checks confirm that validation occurs inside the appropriate
domain classes and that Appointment protects its status transition.

Cancelled appointments remain as objects rather than being deleted.

---

## Part G – Refactor

The implementation was reviewed for unnecessary complexity and design
inconsistency.

### Refactoring Decisions

1. Kept validation close to the state it protects.
2. Removed or rejected any database logic from the domain classes.
3. Did not introduce notification, controller or service dependencies.
4. Kept Appointment independent from Patient inheritance.
5. Used one clear `cancel()` operation rather than allowing public status
   mutation.
6. Kept the implementation limited to behaviour required for this stage.

### Refactoring Outcome

The final domain implementation remains small and consistent with the approved
SmartCare design.

The code does not attempt to implement unrelated persistence, user-interface,
notification or reporting functionality.

---

## Part H – AI Engineering Log

| Item | Record |
|---|---|
| **Prompt** | AI was asked to implement only Appointment from the approved UML using type hints and an AppointmentStatus enum, while avoiding database, UI, notification and service classes. |
| **Generated contribution** | Appointment implementation, status enum, protected status transition and transition exception. |
| **Accepted decisions** | Enum-based status, controlled `cancel()` behaviour, Patient and Practitioner references, and transition exception. |
| **Modified decisions** | The implementation was kept deliberately small and restricted to approved domain responsibilities. Unsupported extra behaviour was not added. |
| **Rejected decisions** | Database logic, notification dependencies, unnecessary inheritance, public status mutation and unrelated service/controller classes. |
| **Verification evidence** | Manual checks covered valid construction, invalid Patient input, invalid Practitioner input, cancellation of a scheduled appointment and rejection of repeated cancellation. |

---

## Reflection

The AI-generated part I reviewed most carefully was the Appointment
implementation because appointment status is a domain invariant that should not
be changed freely. I kept the enum and controlled `cancel()` behaviour because
they provide a clear way to protect the transition from `SCHEDULED` to
`CANCELLED`. I rejected design choices that would have added database logic,
notification dependencies or unrelated service classes because those
responsibilities are not part of the approved Appointment domain class.

The approved Stage 3 design constrained the AI by defining the core classes,
their relationships and their responsibilities before code generation began.
Appointment had to remain associated with Patient and Practitioner rather than
inherit from them, and it had to focus on appointment state rather than
persistence or UI concerns.

This showed why design should come before AI-generated implementation. Giving
the AI explicit UML responsibilities and constraints reduced unsupported
features and made its output easier to review. The final code still required
human verification through invalid-input checks and status-transition tests
before it could be accepted.