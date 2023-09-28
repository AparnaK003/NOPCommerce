import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser =='chrome':
        driver = webdriver.Chrome()
        print("Launching ")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'InternetEx':
        driver = webdriver.Ie()
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")




# ###################   Pytest Html report               ###############################
# #
# # it is hook for adding environment info to html report
# def pytest_configure_metadata(metadata):
#     metadata['Project Name'] = 'nop Commerce'
#     metadata['Module Name'] = 'Customers'
#     metadata['Tester'] = 'Pavan'
#
#
# # It is hook for delete/Modify Environment info to HTML Report
#
# def pytest_configure_metadata_cleanup(metadata):
#     del metadata["JAVA_HOME", None]
#     del metadata["Plugins", None]
#
