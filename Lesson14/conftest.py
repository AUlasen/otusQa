import os
import pkgutil
import pytest



@pytest.mark.usefixtures("environment_info")
@pytest.fixture(scope='session', autouse=True)
def configure_html_report_env(request, module_info):
    request.config._metadata.update(
        {"Env": os.environ, "Modules": module_info}
    )
    yield


@pytest.fixture(scope='session')
def module_info():
    lst = []
    for pkg in pkgutil.iter_modules():
        lst.append(pkg.name)
    return lst




