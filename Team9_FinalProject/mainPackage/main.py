# File Name : main.py
# Student Name: Nikki Carfora, David Becker, Richie James, Michael Slivinski
# email:   carfornc@mail.uc.edu, beckerd8@mail.uc.edu, slivinmb@mail.uc.edu, james2c4@mail.uc.edu
# Assignment Number: Final Project
# Due Date:   4/30/25
# Course #/Section:   IS4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Complete a series of tasks with .json encyrpted files to complete a data scavenger hunt. 

# Brief Description of what this module does. 
# Citations: {"Stack Overflow" is not sufficient. Provide repeatable links, book page #, etc.}

# Anything else that's relevant:

from importlib.resources import Package
from locationPackage.location import *
from moviePackage.movie import *


import os

if __name__ == "__main__":
    data_folder = "data"
    english_file_name = "UCEnglish.txt"
    encrypted_file_name = "TeamsAndEncryptedMessagesForDistribution.json"

    english_file = os.path.join(data_folder, english_file_name)
    encrypted_file = os.path.join(data_folder, encrypted_file_name)

    decryptor = LocationDecryptor(english_file, encrypted_file)
    decrypted_location = decryptor.decrypt_location()
 
    if decrypted_location:
        print(f"Decrypted Location: {decrypted_location}")
    else:
        print("Could not decrypt the location.")

    print(decrypt_movie_for_team())


