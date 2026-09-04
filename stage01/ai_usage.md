# AI Usage

## Part C – AI as Tutor

I asked AI to act as a Python tutor and explain the SmartCare appointment-booking function. I asked it to:

1. Explain what the code does.
2. Identify three limitations.
3. Suggest improvements.
4. Not rewrite the whole application.
5. Ask me two questions to test my understanding.

The AI explained how the function creates an appointment dictionary and adds it to the appointments list. It identified limitations including incomplete validation, no appointment-time validation, and no prevention of duplicate bookings.

I answered the two understanding questions myself. This helped me check that I understood why `append()` is used and what happens when an empty patient name is provided.

## Part D – AI Alternative

I asked AI to create a simple beginner-friendly Python function that stores a patient name, practitioner name and appointment time, without using a database or GUI.

The generated version used a list, dictionary and function. I ran the code to verify that it worked for a normal appointment.

## Evaluation and Verification

I did not automatically accept the AI output as correct. I compared it with the human-written version and tested normal and unusual inputs. Testing showed that the AI alternative did not provide the same patient-name validation as the enhanced human version.

I kept the solution simple and made one controlled improvement to the human version by adding validation for an empty practitioner name. I tested this change to confirm that it produced the expected `ValueError`.