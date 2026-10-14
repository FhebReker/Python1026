"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Fardin Abbassi
Student ID: fabbassi
File created: October 10, 2024
******************************
This file takes in a user's password - or generates a password
using a function from generate.py - and then checks the 
strength of it compared to the minimum strength required by
using the function in password.py.
"""
from password import *
from generate import *

def process_password(min_strength):
    password_to_check = ""
    
    # Keep prompting the user to enter a valid password
    while password_to_check == "":
        
        # User inputs a password or asks for a randomly generated one
        password_to_check = input("Type in a new password or type X from a randomly generated password: ")
        
        # If only entered X, randomly generate password and give unique restatement
        if password_to_check.upper() == "X":
            password_to_check = generate_password(15)
            strength = password_strength(password_to_check)        
            print("Your password: %s" % (password_to_check))
            print("Your password has a strength of %d" % (strength))
        # Otherwise, check strength and use the usual restatement
        else:
            print("Your entered: %s" % (password_to_check))
            strength = password_strength(password_to_check)       
            print("Your password has a strength of %d" % (strength))

        # Check if strength is sufficient enough
        if strength >= min_strength:
            print("Your password is strong enough! Thank you.")
            break
        # If it's still weak, user must re-enter their password or generate a new one
        else:
            print("Your password is not strong enough. Please create a new password that is stronger")
            password_to_check = ""
            print()