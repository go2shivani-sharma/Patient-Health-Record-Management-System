# Function to view patient list.

def view_patient(patients):
    if len(patients) == 0:
        print(" ")
        print("No such patient found.")
        print(" ")
        return
    else:
        for patient in patients:
            print("\nName:", patient["name"])
            print("Age:", patient["age"])
            print("Height:", patient["height"])
            print("Weight:", patient["weight"])
            print("Blood Group:", patient["blood_group"])
