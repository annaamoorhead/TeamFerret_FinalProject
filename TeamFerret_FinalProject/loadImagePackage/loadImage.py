#loadimage.py

# Name: Anna Moorhead 
# email:moorheaa@mail.uc.edu
# Assignment Number: Final Project
# Due Date: April 23, 2024
# Course/Section: IS 4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment we used functions to decrypt two files to get location on campus and a famous movie. We took a picture at the location
# holding a quote from the movie and uploaded the image into our project

# Brief Description of what this module does: This module creates a function to display the image we took.
# Citations:
# Anything else that's relevant:

from PIL import Image

def showImage(file_name):
    '''
    This function displays the group image in front of Rieveschl Hall with our movie quote
    @param file_name: the image to load
    @return:  our group picture
    '''
    im = Image.open(file_name)
    im.show()