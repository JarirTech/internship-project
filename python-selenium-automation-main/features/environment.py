from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

from app.application import Application


def browser_init(context):
    # Initialize headless Firefox browser
    options = FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    #service = Service(ChromeDriverManager().install())
    #context.driver = webdriver.Chrome(service=service, options=options)

    service = FirefoxService(GeckoDriverManager().install())
    context.driver = webdriver.Firefox(service=service, options=options)

    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario:', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step:', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed:', step)


def after_scenario(context, scenario):
    print('\nFinished scenario:', scenario.name)
    context.driver.quit()
