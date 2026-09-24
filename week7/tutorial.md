# Stage 4 Tutorial – Object-Oriented Design Decisions

**Week 7 – SmartCare**

---

## Activity 1 – Encapsulation Review

| Class | Protected state / invariant | Public operations |
|---|---|---|
| **Patient** | Patient identifier and name should remain valid; invalid or empty patient data should not be accepted. | `get_details()`, `update_details()` |
| **Practitioner** | Practitioner identifier, name and specialty should remain valid and consistent. | `get_details()`, `update_details()` |
| **Appointment** | Appointment status must only change through valid transitions; patient and practitioner references must remain associated with the appointment. | `update_status()`, `cancel()` |

### Encapsulation Decision

The internal state of each object should not be changed freely from outside the
class. Validation and state changes should be controlled through class methods.

For example, Appointment status should not be directly changed by another
part of the program. The Appointment class should decide whether a requested
status transition is valid.

---

## Activity 2 – Composition or Inheritance?

### Appointment and Patient

**Decision:** Composition / association

**Reason:**  
An Appointment is associated with a Patient, but an Appointment is not a type
of Patient. The relationship should therefore be represented through an object
reference rather than inheritance.

### Appointment and Practitioner

**Decision:** Composition / association

**Reason:**  
An Appointment is associated with a Practitioner, but it is not a type of
Practitioner. The Appointment should store or reference the Practitioner
involved in the consultation.

### Doctor and Practitioner – Hypothetical

**Decision:** Inheritance

**Reason:**  
If `Doctor` is defined as a specialised type of `Practitioner`, inheritance is
appropriate because Doctor has an **"is-a"** relationship with Practitioner.

A Doctor could inherit common Practitioner attributes and behaviour while
adding doctor-specific behaviour if required.

### Clinic and Appointment

**Decision:** Composition / association

**Reason:**  
A Clinic may be associated with appointments, but an Appointment is not a type
of Clinic. Inheritance would therefore be incorrect.

The current SmartCare design also does not provide enough evidence to require
Clinic to own the lifecycle of every Appointment, so a simple association would
be safer if a Clinic class is introduced.

---

## Activity 3 – Responsibility Allocation

### Who decides whether SCHEDULED can become CANCELLED?

The **Appointment class** should decide whether a `SCHEDULED` appointment can
transition to `CANCELLED`.

This rule belongs with the object whose state is changing. Keeping the rule
inside Appointment protects the appointment invariant and prevents other parts
of the program from creating illegal states.

### Who validates a patient name?

The **Patient class** should validate the patient name when a Patient object is
created or updated.

Validation of Patient state belongs with Patient rather than with the UI or
another unrelated class.

### Should Appointment execute SQL? Why?

**No.**

Appointment is part of the domain layer and should represent appointment state
and business behaviour. Database access is a separate persistence
responsibility.

Putting SQL directly inside Appointment would tightly couple the domain model
to a particular storage implementation and make the class harder to test and
maintain.

### Should the UI decide whether a status transition is legal?

**No.**

The UI may request a status change, but the **Appointment class** should decide
whether that transition is legal.

If the UI contained this business rule, another interface could bypass the rule
and put Appointment into an invalid state.

---

## Activity 4 – AI Code Critique

The proposed AI-generated Appointment design has several object-oriented design
problems.

| Design problem | Why it is a problem | Correction |
|---|---|---|
| **1. Appointment status can be changed publicly without validation.** | Any part of the program could place the appointment into an invalid state. | Protect the status and require changes through methods such as `cancel()` or controlled status-transition logic. |
| **2. SQL is executed inside `cancel()`.** | Database access is mixed with domain behaviour, creating tight coupling and making Appointment harder to test. | Keep persistence logic outside the Appointment domain class. |
| **3. Appointment depends on `NotificationManager`.** | Notifications are not part of the approved Appointment responsibility and introduce an unnecessary dependency. | Remove the notification dependency unless a confirmed requirement later justifies it. |
| **4. Appointment inherits from `PatientRecord`.** | Appointment is not a type of PatientRecord, so the inheritance relationship is conceptually incorrect. | Use an association between Appointment and Patient instead. |
| **5. The class has too many unrelated responsibilities.** | Appointment would be responsible for domain state, persistence and notifications, reducing cohesion. | Keep Appointment focused on appointment state and business rules. |
| **6. External code can bypass business rules.** | Direct state mutation means status-transition rules may not be enforced consistently. | Encapsulate state changes and validate transitions inside Appointment. |

### Corrected Design Direction

The Appointment class should:

- store appointment-related state;
- reference the relevant Patient and Practitioner;
- protect its status;
- enforce legal status transitions;
- support cancellation through domain behaviour; and
- remain independent of database, UI and notification concerns unless later
  design evidence explicitly requires them.

---

## Exit Question

### Why can code be object-oriented syntactically but still have poor object-oriented design?

Code can use classes, objects and inheritance and still have poor
object-oriented design if responsibilities are allocated badly, internal state
is exposed, unrelated concerns are mixed together, or inheritance is used where
there is no real "is-a" relationship.

Good object-oriented design requires more than class syntax. It requires clear
responsibilities, encapsulation, appropriate relationships, low coupling and
cohesive classes.