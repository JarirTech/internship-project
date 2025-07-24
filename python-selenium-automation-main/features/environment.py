# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.wait import WebDriverWait
#
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from webdriver_manager.chrome import ChromeDriverManager
#
# # from selenium.webdriver.firefox.service import Service as FirefoxService
# # from selenium.webdriver.firefox.options import Options as FirefoxOptions
# # from webdriver_manager.firefox import GeckoDriverManager
#
# from app.application import Application
#
#
# def browser_init(context):
#     # bs_user='bouchaibjarir_bB3DeA'
#     # bs_key='S7pTM4PDvUyW4Zjm6czp'
#     #
#     # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
#     #
#     # options = Options()
#     # bstack_options = {
#     #      "os" : "Windows",
#     #     "osVersion" : "11",
#     #     'browserName': 'Edge',
#     #     'sessionName': "User can see titles and pictures on each product inside the off plan page",
#     # }
#     # options.set_capability('bstack:options', bstack_options)
#     # context.driver = webdriver.Remote(command_executor=url, options=options)
#
#
#     # Initialize headless Firefox browser
#     # options = FirefoxOptions()
#     # options.add_argument("--headless")
#     # options.add_argument('--disable-gpu')
#     # options.add_argument("--width=1920")
#     # options.add_argument("--height=1080")
#     # #service = Service(ChromeDriverManager().install())
#     #context.driver = webdriver.Chrome(service=service, options=options)
#
#     # service = FirefoxService(GeckoDriverManager().install())
#     # context.driver = webdriver.Firefox(service=service, options=options)
#     #
#     driver_path = ChromeDriverManager().install()
#     service = Service(driver_path)
#     context.driver = webdriver.Chrome(service=service)
#
#     context.driver.maximize_window()
#     context.driver.implicitly_wait(4)
#     context.driver.wait = WebDriverWait(context.driver, timeout=10)
#     context.app = Application(context.driver)
#
#
# def before_scenario(context, scenario):
#     print('\nStarted scenario:', scenario.name)
#     browser_init(context)
#
#
# def before_step(context, step):
#     print('\nStarted step:', step)
#
#
# def after_step(context, step):
#     if step.status == 'failed':
#         print('\nStep failed:', step)
#
#
# def after_scenario(context, scenario):
#     print('\nFinished scenario:', scenario.name)
#     context.driver.quit()
#
#
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from app.application import Application
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait


def browser_init(context):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()