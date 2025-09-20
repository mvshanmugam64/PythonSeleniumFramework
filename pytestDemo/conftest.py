import pytest


@pytest.fixture(scope="class")
def test_setup():
    print("I will be executed first")
    yield
    print("I will be executed last")

@pytest.fixture()
def test_dataLoad():
    print("User data is created")
    return ["shan", "qa"]

@pytest.fixture(params=[("chrome","shan"), ("firefox", "Qa",), "edge"])
def crossBrowser(request):
    return request.param
