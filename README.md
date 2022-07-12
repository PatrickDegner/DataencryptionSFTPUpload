# Encryption tool with SFTP possibility

Tool to encrypt/decrypt files with or without SFTP upload

# Usage

Create your Key for the symmetric encryption.
<br />
Functions found in app.py
<br />

![image](https://user-images.githubusercontent.com/108484798/178458922-018e05b5-460e-4bbe-a16f-c70b6365cdd8.png)
<br />
<br />

Ive used this nice .jpg but you can use your csv,txt,json,xlsx whatever you want.
<br />
<br />
![image](https://user-images.githubusercontent.com/108484798/178459852-f2f2c5a0-674b-4e63-a64c-e237f5100b98.png)
<br />
<br />

Use encryption() function to encrypt any file in /FilesToEncrypt/ folder.<br />
The file will be encrypted using your Key in the Keyfile.<br />
<br />
<br />
![image](https://user-images.githubusercontent.com/108484798/178460352-7e2f62ba-a921-4134-8eb1-68676fcfe7d8.png)
<br />
<br />

Now you can either just use decryption_from_file() to decrypt it again,<br />
or use the upload_file() function to put it on a sftp. Login infos in utils/connectsftp/.<br />
I have used [Rebex Tiny SFTP Server](https://www.rebex.net/tiny-sftp-server/) for a localhost sftp
<br />
<br />
![image](https://user-images.githubusercontent.com/108484798/178461404-1ec0c3f0-f9f2-4743-859b-3292c9ae9273.png)
<br />
<br />

Function decryption_from_file() will just decrypt the file in /Encrypted/ folder.<br />
While Function decryption_from_sftp() will use the downloaded (download_file()) file from the sftp and decrypt it afterwards.
<br />
<br />
![image](https://user-images.githubusercontent.com/108484798/178462916-5fd351ca-7f70-4b9a-bac5-6c8609632f72.png)
<br />
<br />
Need more information about the code? Ive commented most of it for you!
<br />
Have fun!


