import pytest


def test_firstProgram(test_setup):
    print("Good Morning")

@pytest.mark.smoke
def test_secondcreditCard():
    print("Good Morning! This is second program")