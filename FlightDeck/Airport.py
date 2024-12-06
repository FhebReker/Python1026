"""
******************************
CS 1026 - Assignment 4 – Flights
Code by: Fardin Abbassi
Student ID: fabbassi
File created: November 28, 2024
******************************
Class of airports, featuring:
- Constructor using code, city and country
- String representation of the airport that outputs airport code, city and country
- Equality check that ensures that the other value being checked is both an airport instance and has the same code
- Getters for code, city and country
- Setters for city and country
"""

class Airport:
    # Constructor
    def __init__(self, code, city, country):
        self._code = code
        self._city = city
        self._country = country
    
    # String Representation
    def __str__(self):
        return "%s (%s, %s)" % (self._code, self._city, self._country)
    
    # Equality Check
    def __eq__(self, other):
        # Might be incorrect, test to ensure correctness
        # Check if airport is an Airport instance
        if not isinstance(other, Airport):
            return False
        
        # If they have the same code, they're the same
        if self._code == other._code:
            return True
        # Otherwise, they're not
        else:
            return False

    # Getters
    def get_code(self): 
        return self._code
    def get_city(self): 
        return self._city
    def get_country(self):  
        return self._country

    # Setters
    def set_city(self, value):  
        self._city = value
    def set_country(self, value):   
        self._country = value  