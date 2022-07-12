import os
import cryptography

from cryptography.fernet import Fernet


def decryption_from_file():
    try:
        # Get Pathname / Split for new decrypted name
        file = os.listdir('Encrypted/')[0]
        filename = os.path.splitext(file)[0]

        # Read Key from Keyfile
        with open('utils/Key/keyfile.key', 'rb') as mkey:
            key = mkey.read()

        # Store Key
        f = Fernet(key)

        # Get encrypted file
        with open('Encrypted/'+file, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()

        # Decrypt file
        decrypted = f.decrypt(encrypted)

        # Save decrypted file
        with open('Decrypted/'+filename, 'wb') as decrypter:
            decrypter.write(decrypted)

        # Delete encrypted file after encrypt:
        os.remove('Encrypted/' + file)

        # Print messages on Error
    except IndexError:
        print("No file to decrypt! Please provide a file in /Encrypted/ or use function encrypt first")
    except cryptography.fernet.InvalidToken:
        print("Invalid Token for File!")


def decryption_from_sftp():
    try:
        # Get Pathname / Split for new decrypted name
        file = os.listdir('Downloaded/')[0]
        filename = os.path.splitext(file)[0]

        # Read Key from Keyfile
        with open('utils/Key/keyfile.key', 'rb') as mkey:
            key = mkey.read()

        # Store Key
        f = Fernet(key)

        # Get encrypted file
        with open('Downloaded/'+file, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()

        # Decrypt file
        decrypted = f.decrypt(encrypted)

        # Save decrypted file
        with open('Decrypted/'+filename, 'wb') as decrypter:
            decrypter.write(decrypted)

        # Delete encrypted file after encrypt:
        os.remove('Downloaded/' + file)

        # Print messages on Error
    except IndexError:
        print("No file to decrypt! Please provide a file in /Downloaded/ or download from sftp first")
    except cryptography.fernet.InvalidToken:
        print("Invalid Token for File!")
