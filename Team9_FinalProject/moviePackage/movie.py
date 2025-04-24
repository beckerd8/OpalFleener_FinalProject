# File Name : movie.py
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

import json
from cryptography.fernet import Fernet

def decrypt_movie_for_team():
    team_name = "Opal Fleener"
    encrypted_file = "data/TeamsAndEncryptedMessagesForDistribution.json"
    key = b'9VzqEQcMOT1M_Z_AmUsJQvmQNWZVx4gqOHm29Ch4RZU='

    try:
        with open(encrypted_file, 'r', encoding='utf-8') as f:
            encrypted_data = json.load(f)
       
        encrypted_token = encrypted_data.get(team_name)[0]
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_token.encode()).decode()
        return f'Movie: "{decrypted}"'

    except Exception as e:
        return f"Error decrypting movie: {e}"
