import socket
import ssl
import time


class MyHttpRequest:

    def __init__(self, host="www.google.com", method="GET", path="/", ver="HTTP/1.1", use_ssl=False, port=None):
        self.host = host
        self.method = method
        self.path = path
        self.ver = ver
        self.use_ssl = use_ssl
        if use_ssl is False and port is None:
            self.port = 80
        if use_ssl is True and port is None:
            self.port = 443
        if port is not None:
            self.port = port
        self.headers = []

    def add_header(self, name, value):
        self.headers.append((name, value))
        return self

    def send(self):
        req_str = self.method + " " + self.path + " " + self.ver \
            + "\nHost: " + self.host

        for header in self.headers:
            req_str = req_str + "\n" + header[0] + ":" + header[1]

        req_str = req_str + "\n\n"

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.use_ssl is True:
            soc = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
        else:
            soc = s
        addr = (self.host, self.port)
        soc.connect(addr)
        soc.send(req_str.encode())
        resp = self.__recv_timeout(soc)
        return MyHttpResponse(resp)

    def __recv_timeout(self, the_socket, timeout=2):
        '''Thanks
        https://www.binarytides.com/receive-full-data-with-the-recv-socket-function-in-python/
        '''
        # make socket non blocking
        the_socket.setblocking(0)

        # total data partwise in an array
        total_data = [];
        data = '';

        # beginning time
        begin = time.time()
        while 1:
            # if you got some data, then break after timeout
            if total_data and time.time() - begin > timeout:
                break

            # if you got no data at all, wait a little longer, twice the timeout
            elif time.time() - begin > timeout * 2:
                break

            # recv something
            try:
                data = the_socket.recv(8192)
                if data:
                    total_data.append(data.decode())
                    # change the beginning time for measurement
                    begin = time.time()
                else:
                    # sleep for sometime to indicate a gap
                    time.sleep(0.1)
            except:
                pass

        # join all parts to make final string
        return ''.join(total_data)


class MyHttpResponse:

    def __init__(self, text: str):
        self.text = text
        self.string_list = text.splitlines()
        self.http_ver = self.string_list[0].split(" ")[0]
        self.status_code = self.string_list[0].split(" ")[1]

        self.headers = []
        i = 1
        while i < self.string_list.__len__():
            cur_str = self.string_list[i]
            if cur_str == '' or cur_str == '\n':
                break
            pos = cur_str.find(":")
            self.headers.append((cur_str[:pos].strip(), cur_str[pos+1:].strip()))
            i += 1

        self.body = ''.join(self.string_list[i:])

    def get_full_text(self):
        return self.text

    def get_starting_line(self):
        return self.string_list[0]
