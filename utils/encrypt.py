import shutil
import os

from cryptography.fernet import Fernet


def encryption():
    try:
        # Get first file in ToEncrypt folder
        file = os.listdir('FilesToEncrypt/')[0]

        # Read Key from created Keyfile
        with open('utils/Key/keyfile.key', 'rb') as mkey:
            key = mkey.read()

        # Store Key
        f = Fernet(key)

        # Get Originalfile
        with open('FilesToEncrypt/'+file, 'rb') as original_file:
            original = original_file.read()

        # Move Originalfile after reading to Original/filename
        shutil.move('FilesToEncrypt/'+file, 'Original/'+file)

        # Encrypt File
        encrypted = f.encrypt(original)

        # Save encrypted file to Encrypted/filename-encrypted
        with open('Encrypted/'+file+'.encrypted', 'wb') as encrypt:
            encrypt.write(encrypted)
    except IndexError:
        print("No file to encrypt! Please provide a file in /FilesToEncrypt/")
