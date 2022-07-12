import os

from utils.connectsftp import SftpConnection


def upload_file():
    try:
        # Pick file from Encrypted folder and upload to sftp
        with SftpConnection() as sftp:
            filename = os.listdir('Encrypted/')[0]
            sftp = sftp.open_sftp()
            sftp.put('Encrypted/'+filename, filename)
            print(f'Upload of {filename} complete....')

            # Delete encrypted file if transfer complete:
            os.remove('Encrypted/' + filename)
    except IndexError:
        print('There is no file in Encrypted folder to upload to sftp.')


def download_file():
    try:
        with SftpConnection() as sftp:
            sftp = sftp.open_sftp()
            # list files on sftp folder and pick first
            filename = sftp.listdir()[0]
            # download the file and put into Downloaded folder
            sftp.get(filename, 'Downloaded/'+filename)
            print(f'Download of {filename} complete....')
            sftp.remove(filename)
    except IndexError:
        print('There is no file on your sftp folder to download.')
