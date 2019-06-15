import allure
import pytest
import os




def pytest_exception_interact(node, call, report):
    if report.failed:
        dir_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(dir_path, 'sad_cat.png')
        allure.attach.file(file_path, 'Poor kitty! Test was failed.', attachment_type=allure.attachment_type.PNG)
