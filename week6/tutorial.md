# Stage 3 Tutorial – From Requirements to Domain Models

## Candidate Concepts

| Candidate | Class? | Reason |
|---|---|---|
| Patient | Yes | Patient is a key domain entity with its own information and participates in appointments. |
| Practitioner | Yes | Practitioner is a key domain entity that represents a healthcare practitioner involved in appointments. |
| Appointment | Yes | Appointment is a core domain entity that connects a patient with a practitioner and can contain information such as appointment time and status. |
| Name | No | Name is better represented as an attribute of Patient or Practitioner rather than as a separate class for the current system. |
| Clinic | Provisional | Clinic is part of the problem domain, but the current requirements do not clearly establish responsibilities that require it to be represented as a separate class. |
| Database | No | Database is an implementation or technical concept rather than a domain entity in the SmartCare problem domain. |
| Cancellation | No | Cancellation is better represented as behaviour associated with an Appointment rather than as a separate domain class at this stage. |
| Status | No | Status is better represented as an attribute of Appointment rather than as an independent class for the current requirements. |

---

## CRC Cards

### Patient

| Responsibilities | Collaborators |
|---|---|
| Store patient information | Appointment |
| Provide patient information when required | Appointment |
| Be associated with the patient's appointments | Appointment |

### Practitioner

| Responsibilities | Collaborators |
|---|---|
| Store practitioner information | Appointment |
| Provide practitioner information when required | Appointment |
| Be associated with scheduled appointments | Appointment |

### Appointment

| Responsibilities | Collaborators |
|---|---|
| Store appointment information such as date/time and status | Patient, Practitioner |
| Associate a patient with a practitioner | Patient, Practitioner |
| Maintain the appointment's current status | Patient, Practitioner |
| Support appointment cancellation behaviour | Patient, Practitioner |

---

## Relationship Reasoning

### Patient to Appointment: which relationship and why?

Patient and Appointment should have an **association** relationship.

A patient can be associated with multiple appointments over time, while each appointment is associated with one patient. Appointment is not a type of Patient, so inheritance would not correctly represent this relationship.

A suitable multiplicity is:

**Patient 1 —— 0..\* Appointment**

This means one patient may have zero or many appointments, while each appointment belongs to one patient.

### Practitioner to Appointment: what multiplicity?

Practitioner and Appointment should also have an **association** relationship.

A practitioner may have zero or many appointments, while each appointment is associated with one practitioner.

A suitable multiplicity is:

**Practitioner 1 —— 0..\* Appointment**

### Should Appointment inherit from Patient?

**No.**

Inheritance represents an "is-a" relationship. An Appointment is not a type of Patient. Instead, an Appointment is associated with a Patient and represents a scheduled consultation involving that patient.

Using inheritance here would incorrectly model the SmartCare domain.

### Does Clinic need to own every object?

**No.**

The current requirements do not provide evidence that Clinic must own every Patient, Practitioner and Appointment object. Patient, Practitioner and Appointment can be modelled as the core domain entities with relationships between them.

Clinic should only be introduced as an owning or coordinating class if later requirements provide a clear responsibility that requires it.

---

## AI Model Critique

The proposed AI model contains:

- PatientManager
- PractitionerManager
- AppointmentManager
- ClinicController
- NotificationManager
- ScheduleEngine

### Critique

| AI-proposed class | Decision | Reason |
|---|---|---|
| PatientManager | Question / likely unnecessary at this stage | Patient management is required, but the current domain model can represent this through the Patient class and its responsibilities. A separate manager class should not be introduced without a clear responsibility. |
| PractitionerManager | Question / likely unnecessary at this stage | Practitioner is already a core domain entity. The requirements do not establish a separate PractitionerManager responsibility. |
| AppointmentManager | Question / likely unnecessary at this stage | Appointment already represents the core appointment concept and behaviour. A separate manager should only be added if later design responsibilities justify it. |
| ClinicController | Unsupported at this stage | The requirements do not establish a controller responsibility for the Clinic domain concept. This appears to introduce a design/implementation concept rather than a necessary domain class. |
| NotificationManager | Reject / unsupported | Appointment notifications are not established as a SmartCare requirement, so this class introduces unsupported functionality. |
| ScheduleEngine | Question / unsupported as currently defined | Practitioner availability is a known problem, but the requirements do not define a scheduling engine or enough scheduling behaviour to justify this class. |

### Overall Critique

The AI proposal introduces several "Manager", "Controller" and "Engine" classes that are not clearly supported by the current SmartCare requirements. These names describe possible software design or implementation structures rather than clear concepts from the problem domain.

For the current Stage 3 domain model, the strongest evidence supports three core classes:

- **Patient**
- **Practitioner**
- **Appointment**

Other classes should only be introduced when there is a clear responsibility or requirement that justifies them. This keeps the model simple, evidence-based and appropriate for the small SmartCare system.