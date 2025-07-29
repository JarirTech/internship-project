# from selenium.webdriver.common.by import By
# from time import sleep
#
#
#
#
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def login(self, email, password):
#         self.driver.find_element(By.ID, 'email-2').send_keys(email)
#         self.driver.find_element(By.ID, 'field').send_keys(password)
#         sleep(1)
#         self.driver.find_element(By.XPATH, '//a[@wized="loginButton"]').click()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        wait = WebDriverWait(self.driver, 20)


        email_input = wait.until(EC.presence_of_element_located((By.ID, 'email-2')))
        email_input.send_keys(email)

        password_input = wait.until(EC.presence_of_element_located((By.ID, 'field')))
        password_input.send_keys(password)


        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@wized="loginButton"]')))
        login_button.click()
