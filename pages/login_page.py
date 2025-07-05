from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.inventory_list = (By.CLASS_NAME, "inventory_list")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def load(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def is_logged_in(self):
        return len(self.driver.find_elements(*self.inventory_list)) > 0

    def has_error_message(self):
        return len(self.driver.find_elements(*self.error_message)) > 0
