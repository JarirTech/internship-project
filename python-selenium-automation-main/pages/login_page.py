from selenium.webdriver.common.by import By
from time import sleep




class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        self.driver.find_element(By.ID, 'email-2').send_keys(email)
        self.driver.find_element(By.ID, 'field').send_keys(password)
        sleep(1)
        self.driver.find_element(By.XPATH, '//a[@wized="loginButton"]').click()
