import paramiko


# Setup initial SFTP Connection
class SftpConnection:
    def __init__(self):
        self.client = None

    def __enter__(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname='0.0.0.0', port=2222, username='tester', password='password',
                            allow_agent=False, look_for_keys=False)
        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.client.close()
