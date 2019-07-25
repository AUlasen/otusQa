import subprocess


def get_cur_dir():
    s = subprocess.check_output(["pwd"])
    return s.decode()


def get_package_ver(name):
    s = subprocess.check_output(["dpkg", "-l", name]).decode()
    lines = s.splitlines()
    last_line = lines[lines.__len__() - 1]
    pack_info = ' '.join(last_line.split()).split(" ")
    return pack_info[2]

#s = subprocess.check_output(["echo", "Hello World!"])
#print("s = " + str(s))

print(get_package_ver("dpkg"))
