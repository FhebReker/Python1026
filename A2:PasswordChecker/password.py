"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Fardin Abbassi
Student ID: fabbassi
File created: October 10, 2024
******************************
This file is used to determine the amount of character 
groups and strength of a password by checking whether 
or not it has lowercase letters, uppercase letters, 
numbers or symbols. It then assigns a strength based 
on the length of that password and the groups that the
password contains.
"""

def count_groups(pwd):
    groupAmount = 0
    lower = False
    upper = False
    digits = False
    symbols = False
    
    # Check each character for the group they fit into
    for i in pwd:
        if i in "abcdefghijklmnopqrstuvwxyz": lower = True
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": upper = True
        if i in "0123456789": digits = True
        if i in "!@#$%^&*/?-+=,.|~": symbols = True
        
    # Increment group amount for each group the password has
    if lower: groupAmount += 1
    if upper: groupAmount += 1
    if digits: groupAmount += 1
    if symbols: groupAmount += 1
        
    # Return amount of groups found in the password
    return groupAmount
    
def password_strength(pwd):
    charGroups = count_groups(pwd)
    strength = 0
        
    # No password strength if less than 5 characters are entered
    if len(pwd) < 5:
        strength = 0
    # If between 5 - 8 characters, check for amount of groups, then give strength accordingly
    elif len(pwd) <= 8:
        if charGroups <= 1:
            strength = 1
        elif charGroups <= 3:
            strength = 2
        else:
            strength = 3
    # Otherwise, if between 8 - 12 characters, check for amount of groups, then give strength accordingly
    elif len(pwd) <= 12:
        if charGroups <= 1:
            strength = 2
        elif charGroups <= 3:
            strength = 3
        else:
            strength = 4
    # Otherwise (meaning more than 12 characters), check for amount of groups, then give strength accordingly
    else:
        if charGroups <= 1:
            strength = 3
        elif charGroups <= 3:
            strength = 4
        else:
            strength = 5

   # If any invalid characters are in the password, no strength (invalid password)
    if ' ' in pwd or '\\n' in pwd or '\\t' in pwd:
        strength = 0
    
    # Return password strength
    return strength