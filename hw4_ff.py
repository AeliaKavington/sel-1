import pytest
from time import sleep
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(executable_path='./geckodriver')
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/en/")
    driver.find_element_by_name("email").send_keys("user@email.com")
    driver.find_element_by_name("password").send_keys("test")
    driver.find_element_by_name("login").click()
    sleep(5)