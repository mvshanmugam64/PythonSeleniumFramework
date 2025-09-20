import pytest


@pytest.mark.usefixtures("test_dataLoad")
class TestExample:

    def test_editProfile(self, test_dataLoad):
        print(test_dataLoad)
