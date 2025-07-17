from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#
# @given('Open the main page https://soft.reelly.io')
# def open_main_page(context):
#     context.driver.get('https://soft.reelly.io')
#     sleep(3)
#
# @when('Login to the page.')
# def login(context):
#     context.driver.find_element(By.ID, 'email-2').send_keys('bjarir001@gmail.com')
#     context.driver.find_element(By.ID, 'field').send_keys('J@rir2007@!')
#     sleep(1)
#     context.driver.find_element(By.XPATH, '//a[@wized="loginButton"]').click()
#     sleep(3)
#
# @when('Click on “off plan” at the left side menu.')
# def off_plan_page(context):
#     context.driver.find_element(By.XPATH, '//*[@id="w-node-_99a5c496-8f77-9959-16dd-e8eb9b22b68b-9b22b68b"]/div[3]/a[2]/div[1]/div[2]').click()
#     sleep(3)
#
# @then('Verify the right page opens.')
# def verify_right_page(context):
#     context

from behave import given, when, then
from app.application import Application

EMAIL= 'bjarir001@gmail.com'
PASSWORD = 'J@rir2007@!'
@given('Open the main page')
def step_open_main_page(context):
    context.app = Application(context.driver)
    context.app.base.open("https://soft.reelly.io")

@when('Login to the login page.')
def step_login(context):
    context.app.login_page.login(EMAIL, PASSWORD)

@when('Click on “off plan” at the left side menu.')
def step_click_off_plan(context):
    context.app.off_plan_page.click_off_plan()



@then('Verify the right page opens.')
def step_verify_page(context):
    assert context.app.off_plan_page.is_off_plan_page_loaded()

@then("Verify each product on this page contains a title and picture visible.")
def step_verify_product_content(context):
    assert context.app.off_plan_page.all_products_have_title_and_image()
