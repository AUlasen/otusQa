import paramiko


class SimpleSshClient:
    def __init__(self, hostname, username, password, port):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port

    def execute(self, command, password=None):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=self.hostname, username=self.username, password=self.password, port=self.port)
        if password is None:
            stdin, stdout, stderr = client.exec_command(command)
        else:
            stdin, stdout, stderr = client.exec_command(command, get_pty=True)
            stdin.write(password + '\n')
            stdin.flush()
        stdout_cont: str = stdout.read()
        stderr_cont: str = stderr.read()
        if stderr_cont.__len__() != 0:
            raise MySshClientException(stderr_cont)
        client.close()
        return stdout_cont


class MySshClientException(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)