"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Fardin Abbassi
Student ID: fabbassi
File created: October 10, 2024
******************************
This file generates a password by randomly picking a password
from lowercase letters, uppercase letters, numbers and symbols
with the specified length.
"""
import random

def generate_password(length):
    # Adding all possible characters here
    ALL_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*/?-+=,.|~"
    password_to_return = ""
    
    # Build a password using a random combination of characters using the string above
    for i in range(length):
        random_char = random.choice(ALL_CHARS)
        password_to_return += random_char
    
    # Return the randomly generated password
    return password_to_return 