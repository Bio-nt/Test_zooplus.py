from selenium import webdriver
from Data import Data
import time
import pytest

# number of product in the order displayed on the page
productnumber = 1
# type of product in the order displayed on the page
producttype = 0
# quantity of the product to be added to the cart
productquantity = 3

driver = None
core = None

@pytest.fixture(scope="session", autouse=True)
def setup():
    global driver, core
    driver = webdriver.Edge()
    core = Data(driver)
    yield
    driver.quit()

def test_accept_cookies():
    core.open()
    time.sleep(2)
    core.click_cookies()
    core.make_screenshot()

def test_searching():
    core.enter_product()
    time.sleep(2)
    core.make_screenshot()

def test_adding_product_to_cart_1():
    core.choosing_product(productnumber)
    time.sleep(1)
    core.make_screenshot()
    core.add_product(producttype, productquantity)
    core.make_screenshot()

def test_deleting_product_from_cart():
    core.enter_to_cart()
    time.sleep(3)
    core.make_screenshot()
    core.delete_product(productquantity)
    time.sleep(5)
    core.make_screenshot()

if __name__ == '__main__':
    pytest.main(['-v'])
