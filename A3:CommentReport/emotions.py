"""
******************************
CS 1026 - Assignment 3 – Youtube Emotions
Code by: Fardin Abbassi
Student ID: fabbassi
File created: November 05, 2024
******************************
This file has five functions: 
1. Cleaning the text of a comment by replacing any 
non-alphabetical character with a space

2. Creating a keyword dictionary by reading a file and 
creating a dictionary within a dictionary using the emotions 
felt in each word

3. Creating a comment list by reading a file that contains a 
dictionary containing the ID, username, country and text 
values of each comment, then deleting any comments that aren't
from the country specified

4. Classifying each emotion by comparing the emotions in the 
text of each comment in a comment list with the emotions 
described in a keyword dictionary, then returning the highest
felt emotion

5. Creating a report that uses the comment classifier method
to add up all the comments in a comment list using a keyword
dictionary, then adding up the emotions felt in each comment
to display the most common emotion felt to the console and
writing to a file the number of comments that had each emotion
as well as the percentage of the comment list for that emotion
"""
EMOTIONS = ['anger', 'joy', 'fear', 'trust', 'sadness', 'anticipation']

def clean_text(comment):
    # Replace any non-alphabetical character with a space
    for char in comment:
        if not char.isalpha():
            comment = comment.replace(char, " ")   
    
    # Make string lower case, then return string
    comment = comment.lower()
    return comment

def make_keyword_dict(keyword_file_name):
    # Preparing dictionary and file
    keyword_dictionary = {}
    file = open(keyword_file_name)

    # Loop until all lines have been read
    while True:
        # Prepare next line if available, initialize keyword and counter variables
        current_line = file.readline()
        word_to_add = ""
        emotion_counter = 0
        if not current_line: break
        current_line = current_line.split('\t')
        
        # Loop through each character in the line
        for i in range(len(current_line)):
            # If passed the keyword, add keyword to dictionary, create dictionary for keyword's emotions
            if i == 0:
                word_to_add = current_line[i]
                emotion_dict = {}
                keyword_dictionary[word_to_add] = emotion_dict
                
            # If at a number, set the emotion in keyword's dictionary to the number
            else:
                keyword_dictionary[word_to_add][EMOTIONS[emotion_counter]] = int(current_line[i])
                emotion_counter += 1
                
    # Close file and return keyword dictionary when done
    file.close()
    return keyword_dictionary

def make_comments_list(filter_country, comments_file_name):
    # Initialize comment list, descriptors of comment and file
    comment_list = []
    file = open(comments_file_name)
    COMMENT_CATAGORIES = ['comment_id', 'username', 'country', 'text']
    comment_counter = 0
    
    # Loop until all lines are read
    while True:
        # Read and seperate current line, initialize dictionary for comments
        current_line = file.readline()        
        if not current_line: break
        current_line = current_line.split(',')
        comment_dictionary = {}
        
        # Populate dictionary with empty values
        for i in range(len(COMMENT_CATAGORIES)):
            comment_dictionary[COMMENT_CATAGORIES[i]] = ""
        
        # Loop through each element in the line to add to the comment dictionary, then add comment to list
        for i in range(len(current_line)):            
            current_line[i] = current_line[i].strip()
            # Keep Comment ID as an int
            if current_line[i].isnumeric(): current_line[i] = int(current_line[i])
            comment_dictionary[COMMENT_CATAGORIES[i]] = current_line[i]
        comment_list.append(comment_dictionary)
        
    # Pop comments not from the specified country from the list
    while comment_counter < len(comment_list):
        # Keep all comments if specified
        if filter_country == "all": break
        # Only increase the counter if the comment is from the specified country
        if comment_list[comment_counter]['country'] == filter_country: comment_counter += 1
        # If not from the specified country, pop it off the list
        else: comment_list.pop(comment_counter)   
    
    # Close the file, return the list
    file.close()
    return comment_list   

def classify_comment_emotion(comment, keywords): 
    # Preparing comment text, emotion counter and index 
    comment = clean_text(comment)
    comment = comment.split()
    comment_emotion_counter = [0, 0, 0, 0, 0, 0]
    highest_emotion_index = 0
    
    # Loop through each keyword in the dictionary and each word in the comment
    for keyword in keywords:
        for word in comment:
            # If the word is in the dictionary, then increase the emotion counter by the emotion of the keyword
            if word == keyword:
                for i in range(len(EMOTIONS)):
                    comment_emotion_counter[i] += keywords[keyword][EMOTIONS[i]]
   
    # Loop through the emotion counter to get highest felt emotion in comment
    for i in range(len(EMOTIONS)):
        if comment_emotion_counter[i] > comment_emotion_counter[highest_emotion_index]:
            highest_emotion_index = i
    
    # return strongest emotion
    return EMOTIONS[highest_emotion_index]

""" list isn't returning a runtime error when the comment list is empty"""
def make_report(comment_list, keywords, report_filename):
    # Initializing file, list that counts each emotion in each comment, total emotion count,index of highest emotion counted, list of emotion totals 
    file = open(report_filename, "w")
    emotion_count = [0, 0, 0, 0, 0, 0]
    total_emotion_count = 0
    highest_emotion_index = 0
    emotion_totals = []
    print(comment_list)
    
    # If no comments are in the list, raise RunrimeError
    if not comment_list:
        raise RuntimeError("No comments in datatset!")
       
    # Loop through each comment to add to the emotion counts
    for comment in comment_list:
        comment_emotion = classify_comment_emotion(comment["text"], keywords)
        for i in range(len(EMOTIONS)):
            if comment_emotion == EMOTIONS[i]:
                emotion_count[i] += 1
                total_emotion_count += 1
    
    # Loop through each emotion count to create a string to write to the file, add string to the list of emotion totals
    for i in range(len(emotion_count)):
        # Avoid dividing by zero via if/else
        if total_emotion_count > 0:
            emotion_percent = 100 / total_emotion_count * emotion_count[i]
        else: emotion_percent = 0
        
        # Format the percentage differently depending on if it's a whole number or not
        if emotion_percent % 1 == 0:            
            string = "%s: %d (%.1f%%)\n" % (EMOTIONS[i], emotion_count[i], emotion_percent)
        else:
            string = "%s: %d (%.2f%%)\n" % (EMOTIONS[i], emotion_count[i], emotion_percent)
        
        emotion_totals.append(string)
        if emotion_count[i] > emotion_count[highest_emotion_index]: highest_emotion_index = i
    
    # Write each line to the file, then close the file
    file.write("Most common emotion: %s\n\nEmotion Totals\n" % EMOTIONS[highest_emotion_index])
    for i in range(len(emotion_totals)): 
        file.write(emotion_totals[i])
    file.close()
    
    # Return most common emotion
    return EMOTIONS[highest_emotion_index] 