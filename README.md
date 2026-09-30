# Patient Health Record Management System

## Overview

This project is a python program for managing basic patient records. It uses separate python files for different functions, and allows the user to add patient details, view the saved records, search for a patient and calculate BMI.

## Features

- Add a new patient.
Store patient name, age, height, weight and blood group.
- View patient details.
- To calculate BMI using height and weight.
- Search for a specific patient.
- Display an error message for invalid inputs.

## Technologies / Tools Usee

Visual Studio Code

## Project Structure

Patient Health Reocrd Management System
- main.py
- add_patient.py
- view_patient.py
- search_patient.py
- bmi.py
- READ.md
- statement.md

## How it works?

- One main list
  An empty called `patients = []` is created inside `main.py` acting as the database.
- Sharing the list
  When selecting a menu option, `main.py` passes `patients` list into the other files (like `add_patient(patients)`). This makes sure every file alters the exact same list.
- Patient Dictionary
  New patients are saved as a Python Dictionary (grouping name, age, height, weight and blood group together) before being added to the main list.
- Separate File for BMI
  The BMI math is kept independent in `bmi.py`. Because it is separate,it can test the math independently.


## How to run the program?

- Check Your Version 
  Open your terminal window and type `python3-version` to verify it is installed.
- Open the Project
  Launch your code editor (like Visual Studio Code or PyCharm) and choose "Open Folder" to load the main project directory.
- Launch `main.py` in your code editor to open the patient system.
- Select options 1-5 from the menu to add, search, or view patient files.
