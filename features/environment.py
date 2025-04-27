import allure
from selenium import webdriver

from features.pages.PageFactory import PageFactory
from utility.ConfigReader import ConfigReader

def before_scenario(context, scenario):
    config = ConfigReader()
    context.data = config.read()['Browser']
    browser_name = context.data['browserName']
    if browser_name == 'chrome':
        context.driver = webdriver.Chrome()
    elif browser_name == 'firefox':
        context.driver = webdriver.Firefox()
    else:
        context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(context.data['timeout'])
    context.page_factory = PageFactory(context.driver)

def after_scenario(context, scenario):
    context.driver.quit()

def after_step(context, step):
    if step.status == 'failed':
        context.driver.save_screenshot(f"./screenshots/{step.name}.png")
        with open(f"./screenshots/{step.name}.png", 'rb') as image_file:
            png_bytes = image_file.read()
        allure.attach(png_bytes, name="img", attachment_type=allure.attachment_type.PNG)