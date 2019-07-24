import ftplib


class SimpleFtpClient:
    def __init__(self, hostname, username, password, port=21):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port
        self.session: ftplib.FTP = None

    def connect(self):
        self.session = ftplib.FTP()
        try:
            self.session.connect(self.hostname, self.port)
        except Exception as e:
            self.session = None
            raise MyFtpClientException("Cant connect. Hostname=" + self.hostname + "; port="+self.port) from e
        try:
            self.session.login(self.username, self.password)
        except Exception as e:
            self.session = None
            raise MyFtpClientException("Cant login. Username=" + self.username + "; password="+self.password) from e

    def close(self):
        if self.session is None:
            raise MyFtpClientException("Use connect method to init session first.")
        self.session.close()
        self.session = None

    def cd(self, path):
        if self.session is None:
            raise MyFtpClientException("Use connect method to init session first.")
        self.session.cwd(path)

    def md(self, dir_name):
        if self.session is None:
            raise MyFtpClientException("Use connect method to init session first.")
        self.session.mkd(dir_name)

    def rd(self, dir_name):
        if self.session is None:
            raise MyFtpClientException("Use connect method to init session first.")
        self.session.rmd(dir_name)

    def dir(self):
        if self.session is None:
            raise MyFtpClientException("Use connect method to init session first.")
        self.session.dir()

    def upload(self, from_path, to_path):
        f = open(from_path, "rb")
        resp = self.session.storbinary("STOR " + to_path, f)
        print(resp)


class MyFtpClientException(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)