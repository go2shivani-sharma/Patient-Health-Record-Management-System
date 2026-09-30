# Function to search for a patient.

def search_patient(patients):
    name= input("Enter name of patient here:   ")
    
    for patient in patients:
        if patient["name"] == name:
            print("Patient found!")
            print("Name:", patient["name"])
            print("Age:", patient["age"])
            print("Height:", patient["height"], "cm")
            print("Weight:", patient["weight"], "kg")
            print("Blood Group:", patient["blood_group"])
            return
    print(" ")
    print("No such patient found.")
    print(" ")
