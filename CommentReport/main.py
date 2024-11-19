"""
******************************
CS 1026 - Assignment 3 – Youtube Emotions
Code by: Fardin Abbassi
Student ID: fabbassi
File created: November 05, 2024
******************************
Ask user to input the names of a Tab-Seperated Values (.tsv) 
file, a Comma-Seperated Values (.csv) file, a country from the
list provided just under this header or all countries and a 
report file; call on functions from the emotions.py file to 
create a list of comments and dictionary of keywords, then 
use those two with the report filename to create a report
"""
import os.path
from emotions import *

VALID_COUNTRIES = ['bangladesh', 'brazil', 'canada', 'china', 'egypt',
                   'france', 'germany', 'india', 'iran', 'japan', 'mexico',
                   'nigeria', 'pakistan', 'russia', 'south korea', 'turkey',
                   'united kingdom',  'united states']

""" Not returning correct values in a tuple? """
def ask_user_for_input():    
    # Initializing filenames, country and tuple to always return
    keyword_file = None
    comment_file = None
    country = None
    report_file = None
    
    # Get user to input the keyword file, raise exception if it has improper file suffix or doesn't exist
    keyword_file = input("Input keyword file (ending in .tsv): ")
    if not keyword_file.endswith(".tsv"):
        raise ValueError("%s does not end in .tsv!" % (keyword_file))
    if not os.path.exists(keyword_file):
        raise IOError("%s does not exist!" % (keyword_file))
        
    # Get user to input the comment file, raise exception if it has improper file suffix or doesn't exist
    comment_file = input("Input comment file (ending in .csv): ")
    if not comment_file.endswith(".csv"):
        raise ValueError("%s does not end in .csv!" % (comment_file))
    if not os.path.exists(comment_file):
        raise IOError("%s does not exist!" % (comment_file))  
          
    # Get user to input the country name, raise exception if it isn't in the specified list
    country = input("Input a country to analyze (or \"all\" for all countries): ").lower()
    if country not in VALID_COUNTRIES and country != "all":
        raise ValueError("%s is not a valid country to search by!" % (country))
    
    # Get user to input the report file, raise exception if it has improper file suffix or already exists
    report_file = input("Input the name of the report file (ending in .txt): ")
    if not report_file.endswith(".txt"):
        raise ValueError("%s does not end in .txt!" % (report_file))
    if os.path.exists(report_file):
        raise IOError("%s already exists!" % (report_file))
       
    # Collect all inputs into a tuple, then return values
    return  keyword_file, comment_file, country, report_file


def main():
    # Initialize tuple for values, rewrite using the ask_user_for_input function if values are valid
    values = ()
    while not values:
        try:
            values = ask_user_for_input()
            print(values)
            print()
            for i in range(len(values)):
                if values[i] == None:
                    values = ()
                    break
                
        # print out any exceptions that pop up
        except Exception as e:
            print("Error: %s" %(e))             
                   
    comment_list = make_comments_list(values[2], values[1])
    keyword_dictionary = make_keyword_dict(values[0])
    try:
        reported_emotion = make_report(comment_list, keyword_dictionary, values[3])
        print("Most common emotion: %s" % reported_emotion)
    # In case of an empty comment list, display dismay at the lack of comments
    except RuntimeError as e:
        print("Error: %s" % (e))
        
if __name__ == "__main__":
    main()
