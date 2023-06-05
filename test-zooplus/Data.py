# Page Object Model
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Data:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.zooplus.pl/')

    def click_cookies(self):
        button = self.driver.find_element('id', 'onetrust-accept-btn-handler')
        button.click()

    def make_screenshot(self):
        now = datetime.datetime.now()
        screenshot = 'screenshot' + now.strftime('_%H%M%S') + '.png'
        self.driver.get_screenshot_as_file(screenshot)

    def enter_product(self):
        field = self.driver.find_element('id', 'search_query_field_desktop')
        field.clear()
        field.send_keys('mokra karma dla kota')
        field.send_keys(Keys.ENTER)

    def enter_to_cart(self):
        overview = self.driver.find_element(By.CLASS_NAME, 'cartButton-module_cartButton__lIc-O')
        overview.click()

    def delete_product(self, productquantity):
        cart2 = self.driver.find_element(By.CSS_SELECTOR, 'button[data-zta="reduceQuantityBtn"]')
        for _ in range(productquantity):
            cart2.click()

    def choosing_product(self, productnumber):
        elements = self.driver.find_elements(By.CSS_SELECTOR, 'a[data-zta="product-link"]')
        elements[productnumber].click()

    def add_product(self, producttype, productquantity):
        addproduct = self.driver.find_elements(By.CSS_SELECTOR, 'input[data-zta="quantityStepperInput"]')
        addproduct[producttype].clear()
        addproduct[producttype].send_keys(productquantity)
        elements = self.driver.find_elements(By.CSS_SELECTOR, 'button[data-zta="add-to-cart-button"]')
        elements[producttype].click()