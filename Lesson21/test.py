import time

import paramiko
import pytest
import requests
import ftplib

from Lesson21.MySshClient import SimpleSshClient

host = '192.168.56.103'
user = 'and'
secret = 'and'
port = 22
url = "http://" + host + "/opencart/admin/"
max_reboot_time = 300

ftpuser_name = 'testftpuser'
ftpuser_pass = '12345678'

client = SimpleSshClient(host, user, secret, port)

client.execute("sudo userdel -r " + ftpuser_name, secret)

ftpuser_pass_encoded = client.execute("openssl passwd -crypt " + ftpuser_pass)
client.execute("sudo useradd -m " + ftpuser_name + " -p " + ftpuser_pass_encoded, secret)

client = SimpleSshClient(host, ftpuser_name, ftpuser_pass, port)
print(client.execute("ls"))
session = ftplib.FTP()
session.connect(host, 21)
session.login(ftpuser_name,ftpuser_pass)

session.dir()
