"""
******************************
CS 1026 - Assignment 4 – Flights
Code by: Fardin Abbassi
Student ID: fabbassi
File created: November 28, 2024
******************************
Class of flights, featuring:
- Constructor that first checks if the origin and destination are airports, 
then uses flight number, original airport, destination ariport and flight duration
- String representation of the flight that outputs origin, destination and duration, 
as well as whether or not the flight is domestic
- Equality check that ensures that the other value being checked is both a flight instance and has the same origin and destination
- Adding two flights by making sure the first flight's destination is the same as the next flight's origin
- Getters for code, city and country
- Domestic check to see if both the original airport and destination airport are located in the same country
- Setters for city and country
"""

from Airport import *
class Flight:
    # Constructor
    def __init__(self, flight_no, origin, dest, dur):
        # Checking if both airports are instances of the Aiport class
        if not (isinstance(origin, Airport) and isinstance(dest, Airport)):
            raise TypeError("The origin and destination must be Airport objects")
        
        self._flight_no = flight_no
        self._origin = origin
        self._destination = dest
        self._duration = dur
        
    # String Representation
    def __str__(self):
        # Use the class' is_domestic function further down to properly format the flight's string representation
        if self.is_domestic():
            return ("%s to %s (%d h) [domestic]" % (self._origin.get_city(), self._destination.get_city(), round(self._duration)))
        else:
            return ("%s to %s (%d h) [international]" % (self._origin.get_city(), self._destination.get_city(), round(self._duration)))          
    
    # Equality Check
    def __eq__(self, other):
        # Check if the other flight is a Flight instance
        if not isinstance(other, Flight):
            return False
        
        # If they have the same origin and destination, they're the same
        if self._origin == other._origin and self._destination == other._destination:
            return True
        # Otherwise, they're not
        else:
            return False
        
    # Adding Flights
    def __add__(self, conn_flight):
        # Check if the connecting flight is a Flight instance
        if not isinstance(conn_flight, Flight):
            raise TypeError("The connecting_flight must be a Flight object")
        
        # If the flight ends where the next begins, return a flight that keeps the original airport and flight number, 
        # but replaces the destination with the next flight's and adds the duration of both flights
        if self._destination == conn_flight._origin:
            return Flight(self._flight_no, self._origin, conn_flight._destination, (self._duration + conn_flight._duration))
        
        # If they don't end, then start at the same airport, raise an error
        else:
            raise ValueError("These flights cannot be combined")
    
    # Getters
    def get_flight_no(self):
        return self._flight_no
    def get_origin(self):
        return self._origin
    def get_destination(self):
        return self._destination
    def get_duration(self):
        return self._duration

    # Domestic Flight Check
    def is_domestic(self):
        # Check if the original airport is the same as the destination's
        if self._origin.get_country() == self._destination.get_country():
            return True
        else:
            return False

    # Setters
    def set_origin(self, value):
        self.__origin = value
    def set_destination(self, value):
        self.__destination = value