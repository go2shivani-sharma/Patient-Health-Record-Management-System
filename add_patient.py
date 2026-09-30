# Function to add a patient.

def add_patient(patients):
    name = input("Enter patient's name here:  ")
    age = int(input("Enter age here:  "))
    height = float(input("Enter height in cm here:  "))
    weight = float(input("Enter weight in kg here:  "))

    blood_groups = ["A+","A-","B+","B-","AB+","AB-","O+","O-"]

    blood_group = input("Enter blood group here:  ")

    while blood_group not in blood_groups:
        print("Invalid blood group. Try again. (Use capital letters.)")
        blood_group = input("Enter blood group here:  ")

    patient = {
        "name": name,
        "age": age,
        "height": height,
        "weight": weight,
        "blood_group": blood_group
    }
    patients.append(patient)
    print("Patient successfully added!")
