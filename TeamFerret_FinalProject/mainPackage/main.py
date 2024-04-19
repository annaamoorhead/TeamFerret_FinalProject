#main.py

# Name: Team Ferret 
# email:moorheaa@mail.uc.edu,goyalsd@mail.uc.edu,howardgy@mail.uc.edu
# Assignment Number: Final Project
# Due Date: April 23, 2024
# Course/Section: IS 4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment we used functions to decrypt two files to get location on campus and a famous movie. We took a picture at the location
# holding a quote from the movie and uploaded the image into our project

# Brief Description of what this module does: This module calls all the functions we created
# Citations:
# Anything else that's relevant:

from loadImagePackage.loadImage import *
from decryptLocationPackage.decryptLocation import *
from decryptMovieTitlePackage.decryptMovieTitle import *
from PIL import Image
import json

if __name__ == "__main__":
    showImage("../loadImagePackage/GroupPicture.jpeg")
    
    json_file_path = "EncryptedGroupHints Spring 2024 Section 001-1.json"
    english_txt_path = "UCEnglish.txt"
    decrypted_ferret_location = decrypt_ferret_location(json_file_path, english_txt_path)
    print("Decrypted Ferret Location:", decrypted_ferret_location)

    filename_key = "Ferret"
    decrypted_filename = decrypt_filename(filename_key)
    print("Decrypted Filename for", filename_key + ":", decrypted_filename)

