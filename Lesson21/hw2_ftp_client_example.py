import os

from Lesson21.MyFtpClient import SimpleFtpClient

host = '192.168.56.103'

ftpuser_name = 'testftpuser'
ftpuser_pass = '12345678'

client = SimpleFtpClient(host, ftpuser_name, ftpuser_pass)
client.connect()
client.dir()
client.md("test")
client.dir()
client.md("test/test2")
client.cd("test")
client.dir()
client.rd("test2")
client.dir()
client.cd("/")
dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, "somefile.txt")
client.upload(file_path, "uploaded_file.txt")
client.dir()

