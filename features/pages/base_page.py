class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_screenshot_as_png(self, step_name):
        self.driver.get_screenshot_as_file(f"/screenshots/{step_name}.png")