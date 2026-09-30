# Project Statement & Problem Description

## Problem Statement
Medical practices and clinics need a quick, reliable way to keep track of basic patient details and health data without dealing with massive, complicated database software. 

This project solves that issue by creating a simple management information system built entirely in Python. It allows users to handle patient intakes, search the records, and calculate basic metrics like Body Mass Index (BMI).


## Scope of the Project
This application serves as a basic, local registry system for managing records during an active session. 

- The program allows users to create new patient logs, view the entire directory, look up specific profiles by name, and automatically calculate health metrics like Body Mass Index (BMI). It also filters out bad data inputs like negative numbers.


## Target Users

The system is designed for:
- Medical Receptionists / Administrative Staff
  Users who need to register incoming patients quickly during check-in.
- Clinic Nurses
  Medical staff who need to calculate a patient's BMI or quickly pull up an existing record by name before an appointment.
- Health Evaluators
  Anyone looking for a lightweight tool to run basic health data calculations.


# Project Design & Architecture

## Modular Structure
Instead of stuffing all the code into one confusing file, the project is broken down into separate files based on their specific tasks:
- `main.py` handles the core logic loop and displays the main menu choice system, acting as the database.
- `add_patient.py`, `view_patient.py`, and `search_patient.py` handle all data operations.
- `bmi.py` runs the calculation formulas separately to keep the math independent.

## Program Limitations
- Data is stored strictly in the computer's volatile runtime memory (RAM). This means closing the program will reset the patient list back to empty.
- Inputs must match the target data type rules, though validation filters out negative float inputs for BMI math.
- Lacks advanced hospital features like encryption for private data, security logins for doctors, or connections to actual medical hardware.
