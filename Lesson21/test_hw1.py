import time

import paramiko
import pytest
import requests

host = '192.168.56.103'
user = 'user'
secret = 'password'
port = 22
url = "http://" + host + "/opencart/admin/"
max_reboot_time = 300

def test_restart_services():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=secret, port=port)

    stdin, stdout, stderr = client.exec_command('sudo systemctl stop apache2', get_pty=True)
    stdin.write(secret + '\n')
    stdin.flush()
    stdout.read()

    stdin, stdout, stderr = client.exec_command('sudo systemctl stop mysql.service', get_pty=True)
    stdin.write(secret + '\n')
    stdin.flush()
    stdout.read()


    response = None
    try:
        response = requests.get(url)
    except:
        pass
    assert response is None

    stdin, stdout, stderr = client.exec_command('sudo systemctl start mysql.service', get_pty=True)
    stdin.write(secret + '\n')
    stdin.flush()
    stdout.read()

    stdin, stdout, stderr = client.exec_command('sudo systemctl start apache2', get_pty=True)
    stdin.write(secret + '\n')
    stdin.flush()
    stdout.read()

    response = None
    try:
        response = requests.get(url)
    except:
        pass
    assert response is not None
    assert response.status_code == 200

    client.close()


def test_restart_server():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=secret, port=port)

    stdin, stdout, stderr = client.exec_command('sudo shutdown -r now', get_pty=True)
    stdin.write(secret + '\n')
    stdin.flush()
    stdout.read()
    client.close()

    i = 0
    delay = 10
    response = None
    while i < max_reboot_time:
        try:
            response = requests.get(url)
            break
        except:
            pass
        time.sleep(delay)
        i = i + delay

    assert response is not None
    assert response.status_code == 200

