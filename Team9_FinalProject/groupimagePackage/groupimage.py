# File Name : groupimage.py
# Student Name: Nikki Carfora, David Becker, Richie James, Michael Slivinski
# email:   carfornc@mail.uc.edu, beckerd8@mail.uc.edu, slivinmb@mail.uc.edu, james2c4@mail.uc.edu
# Assignment Number: Final Project
# Due Date:   4/30/25
# Course #/Section:   IS4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Complete a series of tasks with .json encyrpted files to complete a data scavenger hunt. 

# Brief Description of what this module does.  
# Citations: {"Stack Overflow" is not sufficient. Provide repeatable links, book page #, etc.}
    # www.chatpgt.com

# Anything else that's relevant:


import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class ImageDisplayer:
    '''
    A class to load and display an image from the "Data" directory using matplotlib.

    Attributes:
        image_path (str): Full path to the image file.

    Methods:
        display():
            Reads the image file and displays it using matplotlib with no axis ticks and a title
    '''
    def __init__(self, filename):
        self.image_path = os.path.join("Data", filename)

    def display(self):
        img = mpimg.imread(self.image_path)
        plt.imshow(img)
        plt.axis('off')  # Hide axis ticks
        plt.title(f"Image: {os.path.basename(self.image_path)}")
        plt.show()