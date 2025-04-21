# File Name : location.py
# Student Name: Nikki Carfora, David Becker, Richie James, Michael Slivinski
# email:   carfornc@mail.uc.edu, beckerd8@mail.uc.edu, slivinmb@mail.uc.edu, james2c4@mail.uc.edu
# Assignment Number: Final Project
# Due Date:   4/30/25
# Course #/Section:   IS4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Complete a series of tasks with .json encyrpted files to complete a data scavenger hunt. 

# Brief Description of what this module does. Decrypts the .json files that deal with the location assinged for our group. 
# Citations: {"Stack Overflow" is not sufficient. Provide repeatable links, book page #, etc.}

# Anything else that's relevant:

from data import *

import json

def decrypt_location_for_team():
    team_name = "Opal Fleener"
    english_file = "data/UCEnglish.txt"
    encrypted_file = "data/EncryptedGroupHints Spring 2025.json"

    try:
        with open(english_file, 'r', encoding='utf-8') as f:
            word_list = [line.strip() for line in f]

        with open(encrypted_file, 'r', encoding='utf-8') as f:
            encrypted_data = json.load(f)
            indices = encrypted_data.get(team_name)

        if not indices:
            return "Team not found."

        words = [word_list[int(i)] for i in indices]
        return " ".join(words)

    except Exception as e:
        return f"Error: {e}"
