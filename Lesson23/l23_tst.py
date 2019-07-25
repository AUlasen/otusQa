import subprocess
import os

class HelperException(BaseException):
    pass

def get_cur_dir():
    s = subprocess.check_output(["pwd"])
    return s.decode()


def get_package_ver(name):
    s = subprocess.check_output(["dpkg", "-l", name]).decode()
    lines = s.splitlines()
    last_line = lines[lines.__len__() - 1]
    pack_info = ' '.join(last_line.split()).split(" ")
    return pack_info[2]


def get_files(dir):
    proc1 = subprocess.Popen(['ls', '-p', dir], stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(['grep', '-v', '/'], stdin=proc1.stdout,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc1.stdout.close()
    out, err = proc2.communicate()
    files = out.decode().splitlines()
    return files


def get_kernel_ver():
    s = subprocess.check_output(["uname", "-r"])
    return s.decode()


def get_os_name():
    s = subprocess.check_output(["cat", "/etc/os-release"])
    return s.decode().splitlines()[0].split("=")[1].replace("\"","")


def is_port_open(host, port, password, transport="TCP"):
    if transport == "TCP":
        port_arg = "T:" + str(port)
        nmap_cmd = ['sudo', '-S', 'nmap', '-p', port_arg, host]
    else:
        port_arg = "U:" + str(port)
        nmap_cmd = ['sudo', '-S', 'nmap', '-p', port_arg, '-sU', host]
    try:
        proc1 = subprocess.Popen(nmap_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    except FileNotFoundError as e:
        raise HelperException("nmap should be installed") from e
    #pass_str = password + '\n'
    p1_out = proc1.communicate('{}\n'.format(password))
    #print(p1_out)
    proc2 = subprocess.Popen(['grep', '^' + str(port)], stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, err = proc2.communicate(p1_out[0])
    info = out.split()[1]
    if info.lower() == "open":
        return True
    return False



#print(is_port_open("127.0.0.1", 80, "and", transport="TCP"))
