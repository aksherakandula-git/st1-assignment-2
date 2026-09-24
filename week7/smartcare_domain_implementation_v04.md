# SmartCare v0.4 – Domain Implementation Workbook

## 1. UML-to-Code Trace

| UML Element | Python Element | Implemented? | Notes |
|---|---|---|---|
| Patient class | `class Patient` | Yes | Implements the approved Patient domain class. |
| Patient identifier | `patient_id: str` | Yes | Stored as Patient state and validated as non-empty. |
| Patient name | `name: str` | Yes | Stored as Patient state and validated as non-empty. |
| Patient operations | `get_details()`, `update_details()` | Yes | Implemented as controlled public operations. |
| Practitioner class | `class Practitioner` | Yes | Implements the approved Practitioner domain class. |
| Practitioner identifier | `practitioner_id: str` | Yes | Stored and validated as non-empty. |
| Practitioner name | `name: str` | Yes | Stored and validated as non-empty. |
| Practitioner specialty | `specialty: str` | Yes | Added as required by the Stage 4 lab implementation instructions. |
| Practitioner operations | `get_details()`, `update_details()` | Yes | Implemented as controlled public operations. |
| Appointment class | `class Appointment` | Yes | Implements the approved Appointment domain class. |
| Appointment identifier | `appointment_id: str` | Yes | Stored as Appointment state. |
| Appointment time | `appointment_time: str` | Yes | Stored as Appointment state. |
| Appointment status | `_status: AppointmentStatus` | Yes | Protected through enum-based state and controlled transitions. |
| Patient–Appointment association | `patient: Patient` | Yes | Appointment stores a Patient reference. |
| Practitioner–Appointment association | `practitioner: Practitioner` | Yes | Appointment stores a Practitioner reference. |
| Appointment cancellation | `cancel()` | Yes | Enforces the legal transition from SCHEDULED to CANCELLED. |

---

## 2. Domain Invariants

| Class | Invariant / Rule | How Protected |
|---|---|---|
| Patient | `patient_id` must not be empty. | Constructor validation raises `ValueError`. |
| Patient | `name` must not be empty. | Constructor and update validation raise `ValueError`. |
| Practitioner | `practitioner_id` must not be empty. | Constructor validation raises `ValueError`. |
| Practitioner | `name` must not be empty. | Constructor and update validation raise `ValueError`. |
| Practitioner | `specialty` must not be empty. | Constructor and update validation raise `ValueError`. |
| Appointment | Appointment must reference a valid Patient. | Constructor checks that `patient` is a Patient instance. |
| Appointment | Appointment must reference a valid Practitioner. | Constructor checks that `practitioner` is a Practitioner instance. |
| Appointment | Status cannot be changed freely from outside the class. | Internal `_status` is exposed through a read-only property. |
| Appointment | Only a SCHEDULED appointment may be cancelled. | `cancel()` checks the current status and raises `InvalidStatusTransitionError` for illegal transitions. |
| Appointment | A cancelled appointment remains as an object. | `cancel()` changes status rather than deleting the object. |

---

## 3. Composition / Inheritance Decisions

| Relationship | Decision | Rationale |
|---|---|---|
| Appointment and Patient | Association | Appointment references a Patient but is not a type of Patient. |
| Appointment and Practitioner | Association | Appointment references a Practitioner but is not a type of Practitioner. |
| Doctor and Practitioner | Inheritance, if Doctor is introduced | A Doctor could be modelled as a specialised type of Practitioner because this would form an “is-a” relationship. |
| Clinic and Appointment | Association if Clinic is later introduced | An Appointment is not a type of Clinic, and the current design does not establish lifecycle ownership. |
| Appointment and PatientRecord | No inheritance | Appointment is not a specialised PatientRecord, so inheritance would be conceptually incorrect. |

### Design Decision Summary

The implemented model uses object references rather than inappropriate
inheritance. Appointment collaborates with Patient and Practitioner through
associations while preserving separate class responsibilities.

---

## 4. AI Pair-Programming Record

| AI Contribution | Conforms? | Decision | Reason | Verification |
|---|---|---|---|---|
| Add `AppointmentStatus` enum | Yes | Accepted | Provides controlled appointment status values and supports encapsulation. | Manual checks confirmed initial SCHEDULED status and successful cancellation. |
| Add `InvalidStatusTransitionError` | Yes | Accepted | Provides clear handling of illegal repeated transitions. | Cancelling an already cancelled appointment raises the exception. |
| Protect status using `_status` plus a read-only property | Yes | Accepted | Prevents uncontrolled public status mutation. | Status is read through the property and changed through domain behaviour. |
| Keep Patient and Practitioner references inside Appointment | Yes | Accepted | Matches the approved domain associations. | Valid Appointment creation uses Patient and Practitioner objects. |
| Add SQL inside `cancel()` | No | Rejected | Persistence is not an Appointment responsibility. | Final code contains no SQL or database dependency. |
| Add NotificationManager dependency | No | Rejected | Notifications are unsupported by the approved design. | Final Appointment code contains no notification dependency. |
| Make Appointment inherit from PatientRecord | No | Rejected | Appointment is not a type of PatientRecord. | Final code uses association instead of inheritance. |
| Add unrelated service/controller classes | No | Rejected | Would exceed the approved domain-layer scope. | Final implementation contains only agreed domain elements. |

---

## 5. Updated UML

**No updated UML is required.**

Implementation did not reveal a justified change to the approved Stage 3 class
relationships.

The implementation preserves:

- Patient;
- Practitioner;
- Appointment;
- the Patient–Appointment association;
- the Practitioner–Appointment association; and
- no inheritance between the three core classes.

Two implementation details were refined without changing the core class model:

1. `AppointmentStatus` was introduced as an enum to represent valid appointment
   states safely.
2. Practitioner includes `specialty`, as explicitly required by the Stage 4 lab.

These are implementation refinements rather than changes to the fundamental
domain relationships, so the approved UML does not need to be redrawn.