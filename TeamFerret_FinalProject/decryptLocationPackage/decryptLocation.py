#decryptLocation.py

import json

def decrypt_ferret_location(json_file_path, english_txt_path):
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

# Example usage:
json_file_path = r"EncryptedGroupHints Spring 2024 Section 001-1.json"  # Adjust the file path as needed
english_txt_path = 'UCEnglish.txt'  # Adjust the file path as needed
decrypted_ferret_location = decrypt_ferret_location(json_file_path, english_txt_path)
print("Decrypted Ferret Location:", decrypted_ferret_location)