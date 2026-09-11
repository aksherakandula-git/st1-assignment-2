# Stage 2 Lab – SmartCare Requirements Engineering

**AI OFF → AI ON → VERIFY**

---

## Part A – Client Brief: AI OFF

SmartCare currently uses spreadsheets and paper records to manage patient
information and appointments. Staff report duplicate bookings, difficulty finding
patient information, inconsistent appointment status and limited appointment
history.

Management wants a small, maintainable system focused on patient,
practitioner and appointment management.

---

## Part B – Stakeholders and Scope: AI OFF

### Stakeholders

| Stakeholder | Need |
|---|---|
| Receptionists / administrative staff | Efficiently locate patient information and manage appointments. |
| Healthcare practitioners / GPs | Reliable visibility of appointments and practitioner availability. |
| Patients | Accurate recording of patient information and appointments. |
| Clinic management | Reliable operational information and a simple, maintainable system. |
| Software developer / system maintainer | Clear requirements and maintainable software that can be enhanced iteratively. |

### In Scope

- Patient information management
- Practitioner information management
- Appointment booking and management
- Appointment status management
- Appointment history
- Prevention of duplicate bookings
- Patient information search

### Out of Scope

- AI diagnosis or treatment recommendations
- Online payments
- Insurance processing
- Facial-recognition login
- Complex hospital information-system functionality
- Complex treatment-plan management

### Provisional / Requires Clarification

- Practitioner availability functionality
- Exact cancellation and rescheduling rules
- Exact appointment statuses
- Exact patient and practitioner information to store
- Required operational reports
- User roles and access permissions

---

## Part C – Functional Requirements: AI OFF

**FR-01:** The system shall allow staff to create a patient record.

**FR-02:** The system shall allow staff to search for and view patient information.

**FR-03:** The system shall allow staff to update existing patient information.

**FR-04:** The system shall allow staff to create a practitioner record.

**FR-05:** The system shall allow staff to view practitioner information.

**FR-06:** The system shall allow staff to update practitioner information.

**FR-07:** The system shall allow staff to create an appointment linking a patient with a practitioner.

**FR-08:** The system shall prevent appointment bookings that violate the clinic's confirmed duplicate-booking rules.

**FR-09:** The system shall allow staff to view the current status of an appointment.

**FR-10:** The system shall allow staff to update an appointment's status.

**FR-11:** The system shall support cancellation of an existing appointment.

**FR-12:** The system shall retain and allow staff to view appointment history.

---

## Part D – Non-Functional Requirements: AI OFF

**NFR-01 – Reliability:**  
The system shall reliably retain patient, practitioner and appointment information during normal operation.

**NFR-02 – Data Integrity:**  
The system shall maintain accurate and consistent relationships between patient, practitioner and appointment records.

**NFR-03 – Usability:**  
The system shall provide clear and understandable interactions for staff performing core patient, practitioner and appointment tasks.

**NFR-04 – Maintainability:**  
The system shall be structured so individual components can be changed without unnecessary modification to unrelated functionality.

**NFR-05 – Testability:**  
Core patient, practitioner and appointment functions shall be independently testable using valid and invalid inputs.

**NFR-06 – Performance:**  
The system shall remain responsive when operating with the expected small-clinic dataset.

---

## Part E – User Stories and Acceptance Criteria: AI OFF

### User Stories

**US-01:** As a clinic staff member, I want to create and maintain patient records, so that patient information can be stored accurately.

**US-02:** As a clinic staff member, I want to search for patient records, so that I can quickly locate existing patient information.

**US-03:** As a clinic staff member, I want to manage practitioner records, so that practitioner information remains accurate.

**US-04:** As a clinic staff member, I want to create an appointment linking a patient and practitioner, so that consultations can be scheduled and recorded.

**US-05:** As a clinic staff member, I want to view and update appointment status, so that the current state of an appointment is clear.

**US-06:** As a clinic staff member, I want to view appointment history, so that previous appointment information can be reliably retrieved.

### Acceptance Criteria 1 – Patient Search

**GIVEN** an existing patient record is stored in the system  
**WHEN** staff search using supported patient search information  
**THEN** the system displays the matching patient record.

### Acceptance Criteria 2 – Appointment Status

**GIVEN** an appointment exists in the system  
**WHEN** staff update the appointment status  
**THEN** the system stores and displays the updated status.

### Acceptance Criteria 3 – Duplicate Booking Failure Scenario

**GIVEN** an existing appointment conflicts with a proposed appointment according to the clinic's confirmed duplicate-booking rules  
**WHEN** staff attempt to create the conflicting appointment  
**THEN** the system rejects the booking and does not create the duplicate appointment.

---

## Part F – AI Requirements Review: AI ON

**Prompt used:**

> Act as a software requirements reviewer. Review the SmartCare requirements
> for ambiguity, inconsistency, missing clarification questions and testability.
> Do NOT invent new client requirements. For every suggestion, state whether
> it is based on evidence or is only a question/assumption requiring validation.

### AI Review

| Review finding | Suggestion | Basis |
|---|---|---|
| The duplicate-booking rules are not defined precisely. | Clarify exactly what constitutes a duplicate booking. | Question/assumption requiring validation |
| Staff roles and permissions are not defined. | Confirm which staff roles may create, view and update information. | Question/assumption requiring validation |
| Required patient information is unspecified. | Confirm which patient fields are mandatory. | Question/assumption requiring validation |
| Required appointment statuses are unspecified. | Confirm which appointment statuses must be supported. | Question/assumption requiring validation |
| "Clear and understandable" usability is difficult to measure. | Establish a measurable usability criterion after consultation with the client. | Evidence-based testability issue; target requires validation |
| "Normal operation" in the reliability requirement is vague. | Clarify the operating conditions under which reliability will be assessed. | Evidence-based ambiguity |
| The duplicate-booking failure scenario depends on an undefined rule. | Retain the failure scenario but link it to a client-confirmed duplicate-booking rule. | Evidence-based consistency issue |
| Practitioner availability is relevant but its exact functionality is unclear. | Keep practitioner availability provisional until clarified by the client. | Evidence-based scope issue |

---

## Part G – VERIFY the AI Review

| AI Suggestion | Decision | Evidence / Reason |
|---|---|---|
| Clarify what constitutes a duplicate booking. | **Accepted** | Duplicate bookings are explicitly identified as a problem, but the exact rule is not defined. |
| Confirm staff roles and permissions. | **Unverified** | The case study does not define specific access roles or permissions. |
| Confirm mandatory patient information. | **Accepted** | Patient management is required, but mandatory patient fields are not specified. |
| Confirm supported appointment statuses. | **Accepted** | Inconsistent appointment status is a stated problem, but the required status values are not defined. |
| Make the usability requirement measurable. | **Modified** | Greater testability is appropriate, but a numerical target should not be invented without client evidence. |
| Clarify "normal operation" for reliability. | **Modified** | The wording is ambiguous, but the required operating conditions need client validation. |
| Keep the duplicate-booking failure scenario linked to a confirmed rule. | **Accepted** | The failure scenario addresses a stated problem but depends on the duplicate-booking rule being clarified. |
| Keep practitioner availability provisional. | **Accepted** | Availability is a stated problem, but the required functionality has not been defined. |

---

## Part H – Finalise SmartCare v0.2

The final SmartCare v0.2 requirements specification contains:

- stakeholder analysis and scope;
- 12 functional requirements;
- 6 non-functional requirements;
- 6 user stories;
- three Given-When-Then acceptance criteria, including a negative duplicate-booking scenario;
- assumptions and open questions; and
- selected AI review findings and verification decisions.

Following the AI review, unclear or unsupported details were not converted into
confirmed requirements. Instead, unresolved areas such as duplicate-booking
rules, required patient information, appointment statuses, staff permissions,
practitioner availability and measurable quality targets remain open for client
validation.

The final detailed requirements are documented in
`smartcare_requirements_v02.md`.

### Assumptions and Open Questions

1. What patient information must be stored, and which fields are mandatory?
2. What practitioner information must be stored?
3. What exact conditions define a duplicate appointment booking?
4. What appointment statuses must the system support?
5. Which staff roles can create, view, update or cancel records?
6. How should practitioner availability be represented and maintained?
7. Should cancelled appointments remain visible in appointment history?
8. What patient information should be searchable?
9. What basic operational reports are required?
10. What measurable usability, reliability and performance targets are acceptable?

### Selected AI Review Evidence

The AI review identified ambiguity in the duplicate-booking rules, required
patient information, appointment statuses, staff permissions and measurable
non-functional requirements. These findings were checked against the SmartCare
case study. Where the case study did not provide enough evidence, the issue was
retained as an open question rather than being treated as a confirmed
requirement.

---

## Reflection

Before the AI review, I identified SmartCare's main stakeholders, scope,
functional and non-functional requirements, user stories and acceptance
criteria. The review helped identify areas that appeared reasonable but were
still ambiguous or difficult to test. In particular, I had not fully considered
that terms such as the duplicate-booking rules, supported appointment statuses
and measurable usability expectations still required clarification.

The AI also identified areas that could become assumptions if accepted without
evidence. For example, specific staff permissions or precise performance targets
cannot be confirmed from the current client information. I therefore kept these
as open questions rather than treating them as established requirements.

One requirement that changed after review was the duplicate-booking requirement.
Instead of assuming that a duplicate always means the same practitioner at the
same date and time, the final requirement refers to the clinic's confirmed
duplicate-booking rules until those rules are validated. This makes the
requirement more defensible and avoids inventing client needs. Requirements must
have evidence because unsupported assumptions can lead to software that behaves
differently from what stakeholders actually need.