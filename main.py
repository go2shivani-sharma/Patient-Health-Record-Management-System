from add_patient import add_patient
from view_patient import view_patient
from search_patient import search_patient
from bmi import calculate_bmi

patients = []

while True:
    print(" ")
    print(""
    "---------------MAIN MENU---------------" \
    "")
    print("1. Add a patient.")
    print("2. View patient/s.")
    print("3. Search for a patient.")
    print("4. Calculate BMI of a person.")
    print("5. End.")
    print(" ")

    chance = input("Enter choice from 1-5 here:   ")

    if chance == "1":
         add_patient(patients)
    elif chance == "2":
         view_patient(patients)
    elif chance == "3":
        search_patient(patients)
    elif chance == "4":
        calculate_bmi()
    elif chance == "5":
        print("Thank you!")
        break
    else:
        print(" ")
        print("Invalid choice! Please type a choice between 1-4.") 
        print(" ")
