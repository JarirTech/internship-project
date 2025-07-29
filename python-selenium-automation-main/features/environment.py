from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application

def browser_init(context):
    """
    Set up WebDriver to run on BrowserStack with iPhone 12 Pro
    """
    BROWSERSTACK_USERNAME = 'bouchaibjarir_bB3DeA'
    BROWSERSTACK_ACCESS_KEY = 'S7pTM4PDvUyW4Zjm6czp'

    bs_url = f'https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub'

    options = webdriver.ChromeOptions()
    options.set_capability('browserName', 'iPhone')
    options.set_capability('device', 'iPhone 12 Pro')
    options.set_capability('realMobile', 'true')
    options.set_capability('os_version', '14')
    options.set_capability('name', 'Behave Off-Plan Test')
    options.set_capability('build', 'BrowserStack iPhone Run')

    context.driver = webdriver.Remote(
        command_executor=bs_url,
        options=options
    )

    # Avoid using implicit wait on real mobile devices (MJSONWP protocol error)
    # context.driver.implicitly_wait(10)

    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)

def before_step(context, step):
    print('\nStarted step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
