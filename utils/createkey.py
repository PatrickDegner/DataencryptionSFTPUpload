import os

from cryptography.fernet import Fernet


def create_new_key():
    # Check if keyfile already exists
    if os.path.exists('utils/Key/keyfile.key'):
        print("Keyfile already exists!")
    else:
        # Generate Key
        key = Fernet.generate_key()
        # Save key to keyfile
        with open('utils/Key/keyfile.key', 'wb') as keyfile:
            keyfile.write(key)
