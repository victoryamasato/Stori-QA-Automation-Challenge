import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage:
        "driver innit"
        def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(self.driver, 60)

        def wait_for_element(self, locatortype, locator):
            self.wait.until(EC.element_to_be_clickable((locatortype, locator)))

        "click elements by locator and type"
        def click_element(self, locatortype, locator):
            element = self.wait.until(EC.element_to_be_clickable((locatortype, locator)))
            element.click()

        "input text in a text field"
        def input_text_field(self, locatortype, locator, text):
            element = self.driver.find_element(locatortype, locator)
            element.send_keys(text)


        'Get the alert text'
        def switch_to_alert_get_text(self):
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            return alert_text

        'Accept alert'
        def switch_to_alert_accept(self):
            alert = self.driver.switch_to.alert
            alert.accept()
            self.driver.switch_to.default_content()
            return alert

        def get_table_rows(self):
            self.table_rows_locator = "//table[@id='product']/tbody/tr[not(th)]"
            return self.driver.find_elements(By.CSS_SELECTOR, self.table_rows_locator)


        def find_elements(self, locator):
            return self.wait.until(EC.presence_of_all_elements_located(locator))


        def switch_to_iframe(self):
            iframe = self.driver.switch_to.frame("iframe-name")
            return iframe

        def switch_to_default(self):
            self.driver.switch_to.default_content()

        def find_elements_by_tag_name(self, tag_name):
            return self.driver.find_elements(By.TAG_NAME, tag_name)

        def screenshot_evidence(self, file_path):
            return self.driver.get_screenshot_as_file(file_path)
