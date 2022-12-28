import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", default="chrome")
    parser.addoption("--base_url", default="http://192.168.100.3:8081/")
    parser.addoption("--exec", action="store", default="http://172.25.144.1")
    parser.addoption('--browser_version', default='108.0')


@pytest.fixture
def executer(request):
    brw_name = request.config.getoption("--browser_name")
    base_url = request.config.getoption("--base_url")
    executor = request.config.getoption("--exec")
    browser_name = request.config.getoption('--browser_name')

    driver = webdriver.Remote(
        command_executor=f"http://{executor}:4444/wd/hub",
        desired_capabilities={"browserName": brw_name}
    )

    driver.base_url = base_url
   
    def closing():
        driver.quit()
        
    request.addfinalizer(closing)
        
    return driver
