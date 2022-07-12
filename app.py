from utils.encrypt import encryption
from utils.decrypt import decryption_from_file, decryption_from_sftp
from utils.createkey import create_new_key
from utils.sftpusage import upload_file, download_file


'''
On first usage please uncomment the create_new_key function.
After usage comment it back else it will throw an file already exists message. 
'''
# create_new_key()
'''
Take care with this function!
Create new Key. Delete old keyfile in utils/Key if you need a new Key.
Better save it somewhere if u ever want to Decrypt old files later!
Its not possible to decrypt with a different key!
'''

# encrypt the first file in FilesToEncrypt folder
encryption()

# uploads file to sftp (Connection in utils/connectsftp.py)
upload_file()

# downloads file from sftp and deletes it on sftp
download_file()

# decrypt from file if only used encrypt without usage of sftp
# decryption_from_file()

# decrypts the file in Downloaded folder after getting from sftp
decryption_from_sftp()

