import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--base_url", default="http://192.168.100.3:8081/")
    parser.addoption("--exec", action="store", default="172.18.96.1")


@pytest.fixture
def executer(request):
    brw_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")

    driver = webdriver.Remote(
        command_executor=f"http://{exec}:4444/wd/hub",
        desired_capabilities={"browserName": brw_name, "platformName": "Windows 10"}
    )

    driver.base_url = base_url
    return driver

    def closing():
        driver.quit()

    request.addfinalizer(closing)
    return driver
