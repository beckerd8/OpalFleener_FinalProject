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

class LocationDecryptor:
    def __init__(self, english_file_path, encrypted_file_path):
        """
        Initializes the LocationDecryptor with the paths to the English word list
        and the encrypted location data.
 
        Args:
            english_file_path (str): Path to the UC English text file.
            encrypted_file_path (str): Path to the JSON file containing encrypted location hints.
        """
        self.english_file_path = english_file_path
        self.encrypted_file_path = encrypted_file_path
        self.word_list = self._load_word_list()
 
    def _load_word_list(self):
        """
        Loads the words and symbols from the English text file into a list.
 
        Returns:
            list: A list where each element is a line from the English text file.
        """
        try:
            with open(self.english_file_path, 'r', encoding='utf-8') as f:
                return [line.strip() for line in f]
        except FileNotFoundError:
            print(f"Error: English file not found at {self.english_file_path}")
            return []
 
    def _load_encrypted_data(self):
        """
        Loads the encrypted location data from the JSON file.
 
        Returns:
            list or None: A list of strings (representing indices) from the JSON file,
                           or None if the file is not found or JSON is invalid.
        """
        try:
            with open(self.encrypted_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get("encrypted_location")  # Assuming the JSON has a key "encrypted_location"
        except FileNotFoundError:
            print(f"Error: Encrypted data file not found at {self.encrypted_file_path}")
            return None
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from {self.encrypted_file_path}")
            return None
 
    def decrypt_location(self):
        """
        Extracts and decrypts the location data.
 
        Returns:
            str or None: The decrypted location string, or None if there was an error
                         loading files or decrypting.
        """
        encrypted_data = self._load_encrypted_data()
        if encrypted_data is None or not self.word_list:
            return None
 
        decrypted_parts = []
        for index_str in encrypted_data:
            try:
                index = int(index_str)
                if 0 <= index < len(self.word_list):
                    decrypted_parts.append(self.word_list[index])
                else:
                    print(f"Warning: Index {index} is out of bounds in the English word list.")
                    return None 
            except ValueError:
                print(f"Warning: Invalid index '{index_str}' found in the encrypted data.")
                return None 
 
        return " ".join(decrypted_parts)

 
