# SmartCare v0.2 – Requirements Specification

## 1. Problem and Scope

SmartCare Community Clinic currently relies on spreadsheets, paper records and manual processes to manage patient information and appointments. This has resulted in duplicate appointment bookings, difficulty locating patient records, inconsistent appointment status information, limited visibility of practitioner availability, manual cancellation processes, unreliable appointment history and difficulty producing basic operational reports.

The proposed system will provide a simple and maintainable solution focused on patient, practitioner and appointment management. Complex hospital information-system functionality is outside the initial scope. Features whose detailed behaviour has not yet been defined will remain provisional until clarified with the client.

---

## 2. Stakeholders

| Stakeholder | Need | Evidence |
|---|---|---|
| Receptionists / administrative staff | Efficiently locate patient information and manage appointments. | The case study identifies difficulty locating patient records and manual appointment processes. |
| Healthcare practitioners / GPs | Reliable visibility of appointments and practitioner availability. | The clinic provides consultations through GPs and has limited visibility of practitioner availability. |
| Patients | Accurate recording of patient information and appointments. | Patient information and appointment management are explicitly within the initial system scope. |
| Clinic management | Reliable operational information and a simple, manageable system. | Management requests a simple system and identifies several operational problems. |
| Software developer / system maintainer | Clear requirements and maintainable software that can be enhanced iteratively. | The case study describes iterative development and requires a manageable application. |

---

## 3. Functional Requirements

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

## 4. Non-Functional Requirements

**NFR-01 – Reliability:** The system shall reliably retain patient, practitioner and appointment information during normal operation.

**NFR-02 – Data Integrity:** The system shall maintain accurate and consistent relationships between patient, practitioner and appointment records.

**NFR-03 – Usability:** The system shall provide clear and understandable interactions for staff performing core patient, practitioner and appointment tasks.

**NFR-04 – Maintainability:** The system shall be structured so individual components can be changed without unnecessary modification to unrelated functionality.

**NFR-05 – Testability:** Core patient, practitioner and appointment functions shall be independently testable using valid and invalid inputs.

**NFR-06 – Performance:** The system shall remain responsive when operating with the expected small-clinic dataset.

---

## 5. User Stories

**US-01:** As a clinic staff member, I want to create and maintain patient records, so that patient information can be stored accurately.

**US-02:** As a clinic staff member, I want to search for patient records, so that I can quickly locate existing patient information.

**US-03:** As a clinic staff member, I want to manage practitioner records, so that practitioner information remains accurate.

**US-04:** As a clinic staff member, I want to create an appointment linking a patient and practitioner, so that consultations can be scheduled and recorded.

**US-05:** As a clinic staff member, I want to view and update appointment status, so that the current state of an appointment is clear.

**US-06:** As a clinic staff member, I want to view appointment history, so that previous appointment information can be reliably retrieved.

---

## 6. Acceptance Criteria

### AC-01 – Patient Search

**GIVEN** an existing patient record is stored in the system  
**WHEN** staff search using supported patient search information  
**THEN** the system displays the matching patient record.

### AC-02 – Appointment Status

**GIVEN** an appointment exists in the system  
**WHEN** staff update the appointment status  
**THEN** the system stores and displays the updated status.

### AC-03 – Duplicate Booking Failure Scenario

**GIVEN** an existing appointment conflicts with a proposed appointment according to the clinic's confirmed duplicate-booking rules  
**WHEN** staff attempt to create the conflicting appointment  
**THEN** the system rejects the booking and does not create the duplicate appointment.

---

## 7. Assumptions and Open Questions

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

---

## 8. AI Requirements Review Record

| AI suggestion | Evidence? | Decision | Reason | Verification |
|---|---|---|---|---|
| Define the duplicate-booking rules more precisely. | Partial | Accepted | Duplicate bookings are a confirmed problem, but the exact rule is unspecified. | Added as an open question requiring client confirmation. |
| Specify mandatory patient information. | Partial | Accepted | Patient management is confirmed, but the required patient fields are undefined. | Added as an open question. |
| Define supported appointment statuses. | Partial | Accepted | Inconsistent appointment status is a stated problem, but valid status values are not defined. | Added as an open question. |
| Define staff roles and permissions. | No confirmed detail | Unverified | Roles and permissions are not defined by the case study. | Requires stakeholder/client validation. |
| Make usability requirements measurable. | Yes – testability issue | Modified | A measurable target would improve testability, but an arbitrary target should not be invented. | Added as an open question requiring an acceptable target. |
| Add SMS appointment reminders. | No | Rejected | SMS reminders are not supported by the case study. | Checked against the client brief and case study. |
| Add facial-recognition login. | No | Rejected | Facial recognition is unsupported and outside the scope of the simple initial system. | Checked against the case-study scope. |
| Add AI treatment recommendations. | No | Rejected | Treatment recommendations are outside the requested patient, practitioner and appointment-management system. | Checked against the client brief and case-study scope. |