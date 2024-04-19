#decryptLocation.py

# Name: Gillian Howard 
# email: howardgy@mail.uc.edu
# Assignment Number: Final Project
# Due Date: April 23, 2024
# Course/Section: IS 4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment we used functions to decrypt two files to get location on campus and a famous movie. We took a picture at the location
# holding a quote from the movie and uploaded the image into our project

# Brief Description of what this module does: This module creates a function to decrypt Team Ferret's location on campus..
# Citations:
# Anything else that's relevant:

import json

def decrypt_ferret_location(json_file_path, english_txt_path):
    '''
    Decrypts the location data for the "Ferret" team based on encrypted list of indexes.
    @parameter json_file_path: The file path to the JSON file containing the encrypted indexes.
    @parameter english_txt_path: The file path to the text file containing English words.
    @return The decrypted location data for the "Ferret" team.
    '''
    # Read encrypted indices from the JSON file
    with open(json_file_path, 'r') as json_file:
        encrypted_data = json.load(json_file)

    # Extract the encrypted indices for the "Ferret" section
    encrypted_indices = encrypted_data.get("Ferret", [])

    # Read the English words and symbols from the text file
    with open(english_txt_path, 'r', encoding='utf-8') as english_file:
        english_words = english_file.readlines()

    # Decrypt the location data
    decrypted_location = ''
    for index in encrypted_indices:
        # Convert index to int and subtract 1 to account for 0-based indexing
        try:
            index = int(index)
            if 0 <= index < len(english_words):
                decrypted_location += english_words[index].strip() + ' '
        except ValueError:
            # Skip non-integer indices
            continue

    return decrypted_location.strip()

