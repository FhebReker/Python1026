"""
******************************
CS 1026 - Assignment 4 – Flights
Code by: Fardin Abbassi
Student ID: fabbassi
File created: November 28, 2024
******************************
The core of the program from which the Airport and Flight objects are created as their corresponding text files are loaded in; 
Using a list of airports and a dictionary of flights based on airport codes:
- Read in data from files that have information on airports and flights (assumed to be properly formatted)
- Search for aiports by their code
- Find flights to and from a city
- Find flights to and from a country
- Find either a direct flight or a set of single-hop layover airports between two airports
- Find the shortest flight to and from an airport
- Find if a flight exists that head in the opposite direction of an original flight

"""
# Imports
from Flight import *
from Airport import *

# Initializing airport list and flight dictionary
all_airports = []
all_flights = {}

# Populates the airport and flight containers
def load_data(airport_file, flight_file):
    # Calling on the global variables that represent the containers
    global all_airports
    global all_flights
    
    # Try and catch in case of any errors
    try:
        # Open the file that contains information for the airports
        with open(airport_file) as air_file:
            # Split every line into an array, strip each part of whitespace
            for line in air_file:
                splits = line.split("-")
                for i in range(len(splits)):
                    splits[i] = splits[i].strip()
                    
                # Use that array to create variables that represent each part of the airport
                code = splits[0]
                country = splits[1]
                city = splits[2]
                
                # Use the variables to create an airport instance, then add it to the list
                airport = Airport(code, city, country)
                all_airports.append(airport)
        
        # Open the file that contains information for the flights
        with open(flight_file) as fly_file:
            for line in fly_file:
                splits = line.split("-")
                for i in range(len(splits)):
                    splits[i] = splits[i].strip()
                    
                # Initialize each variable
                flight_code = ""
                origin_airport = ""
                destination_airport = ""
                duration = 0
                
                # Loop through all airports
                for airport in all_airports:
                    
                    # Use the array to assign values to the flight
                    flight_code = splits[0] + "-" + splits[1]
                    duration = float(splits[4])
                    # Check if the airport is an origin ariport or destination airport
                    if airport.get_code() == splits[2]:
                        origin_airport = airport
                    elif airport.get_code() == splits[3]:
                        destination_airport = airport
                    
                    # If the line has an origin airport and a destination airport, create a flight
                    if isinstance(origin_airport, Airport) and isinstance(destination_airport, Airport):
                        flight = Flight(flight_code, origin_airport, destination_airport, duration)
                        
                        # If the origin airport isn't already in the dictionary, make a list with that code
                        if origin_airport.get_code() not in all_flights:
                            all_flights[origin_airport.get_code()] = [flight]
                        # Otherwise add it to the existing entry
                        else:
                            all_flights[origin_airport.get_code()].append(flight)    
                        
                        # Break out the loop once the flight is added to the dictionary                    
                        break
        
        # If the code executes with out any errors, return true
        return True
    
    # In the case any error pops up, just return false
    except:        
        return False

# Searches for airports via code
def get_airport_by_code(code):
    # Calling on the global variable that represent the airports    
    global all_airports
    
    # Search through all airports in the list to find one that has the airoprt code
    for airport in all_airports:
        if airport.get_code() == code:
            return airport
    
    # If none are found, raise a value error
    raise ValueError("No airport with the given code: %s" % (code))

# Finds all flights to and from a city
def find_all_city_flights(city):
    # Calling on the global variable that represent the flights    
    global all_flights
    
    # Initialize a list that represents flights from the city
    flight_list = []
    
    # Loop through each flight to find flights to and from the city, then add them to the list
    for flight_origin in all_flights:
        for flight in all_flights[flight_origin]:
            if flight.get_origin().get_city() == city or flight.get_destination().get_city() == city:
                flight_list.append(flight)
    
    # Return whatever flights travel to or from the city
    return flight_list

# Finds all flights to and from a country
def find_all_country_flights(country):
    # Calling on the global variable that represent the flights    
    global all_flights

    # Initialize a list that represents flights from the country
    flight_list = []
    
    # Loop through each flight to find flights to and from the country, then add them to the list
    for flight_origin in all_flights:
        for flight in all_flights[flight_origin]:
            if flight.get_origin().get_country() == country or flight.get_destination().get_country() == country:
                flight_list.append(flight)
                print(flight_list)

    # Return whatever flights travel to or from the country
    return flight_list

# Find flights between two airports
def find_flight_between(orig_airport, dest_airport):
    # Calling on the global variable that represent the flights    
    global all_flights
    
    # Initialize no_flights flag, set of layover flights and codes
    no_flights = True
    starting_layover_flights = set()
    ending_layover_flights = set()
    layover_codes = set()

    # Loop through each flight in the dictionary
    for flight_origin in all_flights:
        for flight in all_flights[flight_origin]:
            # If there exists a direct flight between airports, return the string below
            if flight.get_origin() == orig_airport and flight.get_destination() == dest_airport:
                no_flights = False         
                return "Direct Flight: %s to %s" % (orig_airport.get_code(), dest_airport.get_code())
            
            # If a flight starts from the specified origin airport, add it to the corresponding set
            elif flight.get_origin().get_code() == orig_airport.get_code():
                starting_layover_flights.add(flight.get_destination().get_code())
            # If a flight ends at the specified destination airport, add it to the corresponding set
            elif flight.get_destination().get_code() == dest_airport.get_code():
                ending_layover_flights.add(flight.get_origin().get_code())
                    
    # Assuming no direct flight was found, loop through each potential layover code
    for starting_code in starting_layover_flights:
        for ending_code in ending_layover_flights:
            # If one flight to this code  comes from the origin airport and one flight from here leads to the destination airport, 
            # add to the certified list
            if starting_code == ending_code:
                layover_codes.add(starting_code)
                no_flights = False
    
    # If the flag for no flights wasn't put down, raise a value error
    if no_flights:
        raise ValueError("There are no direct or single-hop connecting flights from %s to %s" % 
                         (orig_airport.get_code(), dest_airport.get_code()))
    # If it was put down, return the list of potential layover codes
    else:
        return layover_codes

# Find the shortest flight to or from an airport
def shortest_flight_from(orig_airport):
    # Calling on the global variable that represent the flights    
    global all_flights
    
    # Initialize the shortest flight with the first flight at the airport
    shortest_flight = all_flights[orig_airport.get_code()][0]
    
    # Loop through each flight at the airport to find a flight shorter than the current shortest flight
    for flight in all_flights[orig_airport.get_code()]:
        if flight.get_duration() < shortest_flight.get_duration():
            shortest_flight = flight
    
    # Return the shortest flight
    return shortest_flight

# Find if another flight can head back to the original airport
def find_return_flight(first_flight):
    # Calling on the global variable that represent the flights    
    global all_flights
    
    # Loop through each flight at the first flight's destination to see if a flight comes back to the original airport
    for flight in all_flights[first_flight.get_destination().get_code()]:
        # If such a flight exists, return that flight
        if flight.get_destination() == first_flight.get_origin():
            return flight
    
    # If no such flight exists, return a value error
    raise ValueError("There is no flight from %s to %s" % 
                     (first_flight.get_destination().get_code(), first_flight.get_origin().get_code()))

if __name__ == "__main__":
    pass
