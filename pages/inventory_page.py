from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart_by_name(self, item_name):
        xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        self.driver.find_element(By.XPATH, xpath).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
