class Patient:
    def __init__(self, patient_id, name, age, gender, contact_number):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_number = contact_number
        self.appointments = []

    def schedule_appointment(self, doctor, date_time):
        appointment = {'doctor': doctor, 'date_time': date_time}
        self.appointments.append(appointment)
        print(f"Appointment scheduled with Dr. {doctor} on {date_time}")

    def display_info(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Contact Number: {self.contact_number}")
        print("Appointments:")
        for appointment in self.appointments:
            print(f"  - Dr. {appointment['doctor']} on {appointment['date_time']}")
        print("\n")


class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty

    def display_info(self):
        print(f"Doctor ID: {self.doctor_id}")
        print(f"Name: {self.name}")
        print(f"Specialty: {self.specialty}")
        print("\n")


class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def display_patients(self):
        print("Patients in the hospital:")
        for patient in self.patients:
            patient.display_info()

    def display_doctors(self):
        print("Doctors in the hospital:")
        for doctor in self.doctors:
            doctor.display_info()


# Example usage:
if __name__ == "__main__":
    hospital = Hospital("Sample Hospital")

    doctor1 = Doctor(1, "Dr. Smith", "Cardiologist")
    doctor2 = Doctor(2, "Dr. Johnson", "Pediatrician")

    hospital.add_doctor(doctor1)
    hospital.add_doctor(doctor2)

    patient1 = Patient(101, "John Doe", 30, "Male", "123-456-7890")
    patient2 = Patient(102, "Jane Doe", 25, "Female", "987-654-3210")

    patient1.schedule_appointment("Smith", "2024-03-10 10:00 AM")
    patient2.schedule_appointment("Johnson", "2024-03-15 02:30 PM")

    hospital.add_patient(patient1)
    hospital.add_patient(patient2)

    hospital.display_doctors()
    hospital.display_patients()