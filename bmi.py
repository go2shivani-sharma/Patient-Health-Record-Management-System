# Function to calculate Body Mass Index (BMI) of a patient.

def calculate_bmi():
    height= float(input("Enter height in cm here:  "))
    weight= float(input("Enter weight in kg here:  "))

    if height <= 0 or weight <= 0:
        print("Error: Height and weight must be positive numbers!")
        return



    height_m = height/100
    bmi= weight/(height_m ** 2)

    if bmi <= 0:
        print("Given data is invalid. Please try again with positive numbers.")

    else:
        print("BMI=", bmi)

    
