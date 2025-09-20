#Any pytest file should start with test_
#pytest method name should start with test
# Any code should be wrapped within a method
import pytest
from selenium import webdriver


#Run in terminal py.test -v(details) -s(with log) (to get the console details on terminal)
# pytest {Specific file_name} -v -s (Runn specific file only)
#pytest -k {keyword in method name} -v -s (Run only the keywords present in the methods
# @pytest.mark.<tagName> (mark is used to run based on tags) -> pytest -m <tagName> -k -s
# pip install pytest-html ->Install html format for reporting
# pytest --html=report.html
# skip test with @pytest.mark.skip
# run the method but do not show in the remort @pytest.mark.xfail

# Fixtures are the annotations like setup/test data under conftest file to  generalise fixture and make it available to al test case
# datadriven and parameterization can be done  with return statement in tuple format

@pytest.mark.smoke
def test_assertProgram():
    msg = "Hello Worl"
    assert msg == "Hello World", "String Matches"

@pytest.mark.xfail
def test_creditCard():
    print("Good Morning! Credit Card")

def test_crossBrowserTest(crossBrowser):
    print(crossBrowser[1])


