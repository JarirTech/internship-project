
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
