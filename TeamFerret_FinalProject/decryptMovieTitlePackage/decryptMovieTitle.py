#decryptMovieTitle.py

import json
from cryptography.fernet import Fernet

def decrypt_filename(filename_key):
    # Load the encrypted filenames from the JSON file
    with open("TeamsAndEncryptedMessagesForDistribution - 001.json", "r") as file:
        encrypted_data = json.load(file)

    # Extract the encrypted filename based on the provided key
    if filename_key in encrypted_data:
        encrypted_filename = encrypted_data[filename_key][0]

        # Define the key (replace 'your_secret_key_here' with your actual key)
        key = "t7WyuS-VCj3eb9HE0OHPhva2b30FSid88Z5nSiYUo0c="  # our secret key

        # Create a Fernet cipher instance with the key
        cipher = Fernet(key)

        # Decrypt the filename based on the provided key
        decrypted_filename = cipher.decrypt(encrypted_filename.encode()).decode()
        return decrypted_filename
    else:
        return "Filename key not found in the encrypted data."

# Usage:

