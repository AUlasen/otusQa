import time

import paramiko
import pytest
import requests

from Lesson21.MySshClient import SimpleSshClient

host = '192.168.56.103'
user = 'and'
secret = 'and'
port = 22
url = "http://" + host + "/opencart/admin/"
max_reboot_time = 300

client = SimpleSshClient(host, user, secret, port)



def install_ftp(client: SimpleSshClient, secret):

    params = ("listen = NO\n"
    "listen_ipv6 = YES\n"
    "anonymous_enable = NO\n"
    "local_enable = YES\n"
    "write_enable = YES\n"
    "local_umask = 022\n"
    "dirmessage_enable = YES\n"
    "use_localtime = YES\n"
    "xferlog_enable = YES\n"
    "connect_from_port_20 = YES\n"
    "chroot_local_user = YES\n"
    "secure_chroot_dir = / var / run / vsftpd / empty\n"
    "pam_service_name = vsftpd\n"
    "rsa_cert_file = / etc / ssl / certs / ssl - cert - snakeoil.pem\n"
    "rsa_private_key_file = / etc / ssl / private / ssl - cert - snakeoil.key\n"
    "ssl_enable = NO\n"
    "pasv_enable = Yes\n"
    "pasv_min_port = 10000\n"
    "pasv_max_port = 10100\n"
    "allow_writeable_chroot = YES\n")

    client.execute("sudo sh -c \"echo \\\"" + params + "\\\" > /etc/vsftpd.conf\"", secret)
    client.execute("sudo service vsftpd restart", secret)


install_ftp(client, secret)