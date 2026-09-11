# Stage 2 Tutorial – From Problems to Requirements

## Activity 1 – Stakeholder Map

| Stakeholder | Need | Potential conflict |
|---|---|---|
| Receptionists / administrative staff | Efficiently locate patient records and manage appointments, statuses and cancellations. | Need quick processes while maintaining accurate records and preventing booking conflicts. |
| Healthcare practitioners / GPs | Reliable visibility of appointments and practitioner availability. | Requested appointment times may conflict with practitioner availability. |
| Patients | Have their information and appointments recorded accurately and reliably. | Preferred appointment times may conflict with practitioner availability. |
| Clinic management | A simple, maintainable system with reliable appointment information, history and basic operational reporting. | Additional desired functionality may conflict with keeping the initial system small and manageable. |
| Software developer / system maintainer | Clear requirements and maintainable software that can be enhanced in later stages. | Increasing technical complexity may conflict with the requirement for a manageable initial system. |

## Activity 2 – Functional or Non-Functional?

| Requirement | Classification |
|---|---|
| The system shall allow staff to cancel an appointment. | Functional |
| The system should remain responsive for the course-scale dataset. | Non-functional |
| The system shall retain cancelled appointments. | Functional |
| Core business logic should be independently testable. | Non-functional |
| The system shall search for a patient by ID. | Functional |

## Activity 3 – Repair Ambiguous Requirements

### 1. The system should be easy to use.

**Problem:** "Easy to use" is subjective and cannot be measured or tested as written.

**Clarification question:** What measurable usability criteria should determine whether the system is easy to use for clinic staff?

### 2. Patient search should be fast.

**Problem:** "Fast" does not define an acceptable response time or operating conditions.

**Clarification question:** What maximum response time is acceptable for patient searches under the expected clinic workload?

### 3. The system should securely manage data.

**Problem:** "Securely" is too broad and does not specify the required security controls or access restrictions.

**Clarification question:** What security controls and access restrictions are required for patient, practitioner and appointment data?

### 4. Appointments should normally be easy to cancel.

**Problem:** "Normally" and "easy" are vague, and the cancellation process has not been defined.

**Clarification question:** Who should be allowed to cancel appointments, and what rules and steps should the cancellation process follow?

## Activity 4 – AI Requirements Audit

| AI suggestion | Classification | Evidence / reason |
|---|---|---|
| Patients receive SMS reminders. | Unsupported | SMS reminders are not mentioned in the case study. |
| Facial recognition login. | Out of scope | Facial recognition is not requested and would add unnecessary complexity to the initial system. |
| Receptionists create appointments. | Assumption requiring validation | Appointment management is required, but the case study does not explicitly assign appointment creation to receptionists. |
| Online payment. | Out of scope | Payment processing is not part of the stated system scope. |
| Practitioners view schedules. | Assumption requiring validation | Limited visibility of practitioner availability is a stated problem, but practitioner interaction with schedules is not defined. |
| AI recommends treatments. | Out of scope | Treatment recommendations are outside the requested administrative system. |
| Cancelled appointments remain in history. | Assumption requiring validation | Cancellation and appointment history are stated problems, but retention of cancelled appointments is not explicitly specified. |

## Exit Question

**Why is "AI suggested it" not sufficient evidence for a requirement?**

"AI suggested it" is not sufficient evidence because AI can make assumptions or introduce functionality that the client did not request. Requirements should be supported by the client brief, stakeholder needs, or validated evidence before they are accepted.