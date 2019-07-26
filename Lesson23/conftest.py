import pytest

def pytest_addoption(parser):
    parser.addoption("--ip", action="store", default="192.168.56.103", help="Opencart host ip")
    parser.addoption("--http_port", action="store", default="80", help="Opencart http port")
    parser.addoption("--user", action="store", default="and", help="Opencart host user")
    parser.addoption("--password", action="store", default="and", help="Opencart host password")
    parser.addoption("--address", action="store", default="http://192.168.56.103/", help="Opencart web address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")
    parser.addoption("--timeouts", action="store", default="10000", help="Timeouts")