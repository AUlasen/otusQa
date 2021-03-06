import subprocess
import os

import pytest


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


def get_files(dirr):
    proc1 = subprocess.Popen(['ls', '-p', dirr], stdout=subprocess.PIPE)
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
    p1_out = proc1.communicate('{}\n'.format(password))
    proc2 = subprocess.Popen(['grep', '^' + str(port)], stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, err = proc2.communicate(p1_out[0])
    info = out.split()[1]
    if info.lower() == "open":
        return True
    return False


def is_service_active(name):
    proc1 = subprocess.Popen(['service', name, 'status'], stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(['grep', 'Active'], stdin=proc1.stdout,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc1.stdout.close()
    out, err = proc2.communicate()
    str_lst = out.decode().split()
    if str_lst[1] == 'active':
        return True
    return False


def get_proc_list():
    s = subprocess.check_output(["ps", "-A", "--no-headers"])
    lines = s.decode().splitlines()
    proc = {}
    for line in lines:
        proc_info = line.split()
        pid = proc_info[0]
        cmd = proc_info[3]
        proc[pid] = cmd

    return proc


def get_proc_stat(pid):
    f_name = '/proc/' + str(pid) + '/stat'
    s = subprocess.check_output(["cat", f_name])
    fields = s.decode().split()
    d = {}
    d['pid'] = fields[0]
    d['command'] = fields[1]
    d['state'] = fields[2]
    d['parent_pid'] = fields[3]
    d['process_grp'] = fields[4]
    d['session_id'] = fields[5]
    d['tty_nr'] = fields[6]
    d['num_threads'] = fields[19]
    d['starttime'] = fields[21]
    return d


def get_processor_info():
    s = subprocess.check_output(["cat", "/proc/cpuinfo"])
    lines = s.decode().splitlines()
    d = {}
    for line in lines:
        try:
            name, val = line.split(":")
        except ValueError:
            name = line[:line.__len__()-2]
            value = ''
        d[name.strip()] = val.strip()
    return d


def get_default_route_info():
    proc1 = subprocess.Popen(['ip', 'r'], stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(['grep', 'default'], stdin=proc1.stdout,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc1.stdout.close()
    out, err = proc2.communicate()
    return out.decode()


def get_ni_info():
    s = subprocess.check_output(["ifconfig"])
    int_lines = s.decode().split("\n\n")

    def parse_int_line(line):
        d = {}
        pos = line.index(":")
        d['name'] = line[:pos]
        d['ip'] = line.splitlines()[1].split()[1]
        d['mask'] = line.splitlines()[1].split()[3]
        d['flags'] = line.splitlines()[0].split()[1]
        return d
    d = {}
    for line in int_lines:
        if line != '':
            line_d = parse_int_line(line)
            d[line_d['name']] = line_d
    return d


@pytest.mark.parametrize("name", [("enp0s8")])
def test_network_ip(request, name):
    ip = request.config.getoption("--ip")
    info = get_ni_info()
    assert info.get(name) is not None
    assert info[name]['ip'] == ip


@pytest.mark.parametrize("name", [("Ubuntu")])
def test_os_name(request, name):
    os_name = get_os_name()
    assert os_name == name


@pytest.mark.parametrize("port", [("80")])
def test_http_port_is_open(request, port):
    ip = request.config.getoption("--ip")
    port = request.config.getoption("--http_port")
    password = request.config.getoption("--password")
    assert is_port_open(ip, port, password, transport="TCP")


@pytest.mark.parametrize("name", [("apache2"),("mysql")])
def test_services(request, name):
    assert is_service_active(name)