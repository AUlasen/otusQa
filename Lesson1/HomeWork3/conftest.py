import pytest


@pytest.fixture(scope="session", autouse=True)
def session_fixture(request):
    print('\nSession was started')

    def session_fin():
        print('\nSesion was finished')

    request.addfinalizer(session_fin)


@pytest.fixture(scope="module", autouse=True)
def module_fixture(request):
    print('\nModule was started')

    def module_fin():
        print('\nModule was finished')

    request.addfinalizer(module_fin)


@pytest.fixture(scope="function", autouse=False)
def test_fixture(request):
    print('\nTest was started')

    def test_fin():
        print('\nTest was finished')

    request.addfinalizer(test_fin)
