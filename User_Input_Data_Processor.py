# 2. User Input Data Processor
# Objective: The aim of this assignment is to process and format user input data.

# Task 1: Input Length Validato: Write a script that asks for and checks the length of the user's 
# first name and last name. Both should be at least 2 characters long. If not, print an error message.

def user_name_check():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    if len(first_name) < 2:
        print("Error! First name isn't long enough.")
    
    if len(last_name) < 2:
        print("Error! Last name isn't long enough")
    if len(first_name) >= 2 and len(last_name) >= 2:
        print(f"Welcome, {first_name} {last_name}!")

user_name_check()