import pytest
# @pytest.mark.usefixtures use to execute within class level methods

@pytest.mark.usefixtures("test_setup")
class TestSample:

    def test_fixtureTest(self):
        print("I will be executed steps in fixtureTest method")

    def test_fixtureTest1(self):
        print("I will be executed steps in fixtureTest 1 method")

    def test_fixtureTest2(self):
        print("I will be executed steps in fixtureTest 2 method")