from selenium.webdriver.common.by import By
from src.Pages.BasePage import BasePage
from src.Resources.PracticePageElements import PracticePageElements

class PracticePage (BasePage):


    @property
    def suggestion_class(self):
        BasePage.wait_for_element(self, By.XPATH, PracticePageElements.suggestion_class_xpath)
        return self.driver.find_element(By.XPATH, PracticePageElements.suggestion_class_xpath)


    @property
    def dropdown_class(self):
        BasePage.wait_for_element(self, By.ID, PracticePageElements.dropdown_example_xpath)
        return self.driver.find_element(By.ID, PracticePageElements.dropdown_example_xpath)
    @property
    def dropdown_class_id(self):
        BasePage.wait_for_element(self, By.ID, PracticePageElements.dropdown_example_id)
        return self.driver.find_element(By.ID, PracticePageElements.dropdown_example_id)
    @property
    def mexico_country(self):
        BasePage.wait_for_element(self, By.XPATH, PracticePageElements.mexico_country_xpath)
        return self.driver.find_element(By.XPATH, PracticePageElements.mexico_country_xpath)

    @property
    def dropdown_option2(self):
        BasePage.wait_for_element(self, By.XPATH, PracticePageElements.dropdown_option2_xpath)
        return self.driver.find_element(By.XPATH, PracticePageElements.dropdown_option2_xpath)

    @property
    def dropdown_option3(self):
        BasePage.wait_for_element(self, By.XPATH, PracticePageElements.dropdown_option3_xpath)
        return self.driver.find_element(By.XPATH, PracticePageElements.dropdown_option3_xpath)

    @property
    def switch_window_btn(self):
        BasePage.wait_for_element(self, By.XPATH, PracticePageElements.switch_window_button_xpath)
        return self.driver.find_element(By.XPATH, PracticePageElements.switch_window_button_xpath)

    @property
    def switch_alert_field(self):
        BasePage.wait_for_element(self, By.XPATH, PracticePageElements.switch_alert_field_xpath)
        return self.driver.find_element(By.XPATH, PracticePageElements.switch_alert_field_xpath)

    @property
    def switch_alert_btn(self):
        BasePage.wait_for_element(self, By.XPATH, PracticePageElements.switch_alert_btn_xpath)
        return self.driver.find_element(By.XPATH, PracticePageElements.switch_alert_btn_xpath)

    @property
    def confirm_alert_btn(self):
        BasePage.wait_for_element(self, By.CSS_SELECTOR, PracticePageElements.confirm_alert_btn_css)
        return self.driver.find_element(By.CSS_SELECTOR, PracticePageElements.confirm_alert_btn_css)

    @property
    def web_table_example(self):
        BasePage.wait_for_element(self, By.XPATH, PracticePageElements.table_xpath)
        return self.driver.find_element(By.XPATH, PracticePageElements.table_xpath)

    @property
    def web_table_rows(self):
        BasePage.wait_for_element(self, By.XPATH, PracticePageElements.table_row_xpath)
        return self.driver.find_elements(By.XPATH, PracticePageElements.table_row_xpath)

    @property
    def web_table_course_name_column(self):
        BasePage.wait_for_element(self, By.XPATH, PracticePageElements.table_name_column_xpath)
        return self.driver.find_elements(By.XPATH, PracticePageElements.table_name_column_xpath)

    @property
    def web_table_course_price_column(self):
        BasePage.wait_for_element(self, By.XPATH, PracticePageElements.table_price_column_xpath)
        return self.driver.find_elements(By.XPATH, PracticePageElements.table_price_column_xpath)

    @property
    def table_fixed_header(self):
        BasePage.wait_for_element(self, By.XPATH, PracticePageElements.table_fixed_header_xpath)
        return self.driver.find_elements(By.XPATH, PracticePageElements.table_fixed_header_xpath)

    @property
    def table_fixed_header_row(self):
        BasePage.wait_for_element(self, By.XPATH, PracticePageElements.table_fixed_header_row_xpath)
        return self.driver.find_elements(By.XPATH, PracticePageElements.table_fixed_header_row_xpath)

    @property
    def table_fixed_header_names(self):
        BasePage.wait_for_element(self, By.XPATH, PracticePageElements.table_fixed_header_names_xpath)
        return self.driver.find_elements(By.XPATH, PracticePageElements.table_fixed_header_names_xpath)

    @property
    def table_fixed_header_position(self):
        BasePage.wait_for_element(self, By.XPATH, PracticePageElements.table_fixed_header_position_xpath)
        return self.driver.find_elements(By.XPATH, PracticePageElements.table_fixed_header_position_xpath)

    @property
    def iframe_example(self):
        BasePage.wait_for_element(self, By.ID, PracticePageElements.iframe_example_id)
        return self.driver.find_elements(By.ID, PracticePageElements.iframe_example_id)

    @property
    def iframe_text_mentorship(self):
        BasePage.wait_for_element(self, By.XPATH, PracticePageElements.iframe_text_mentorship_xpath)
        return self.driver.find_elements(By.XPATH, PracticePageElements.iframe_text_mentorship_xpath)

    @property
    def iframe_list(self):
        BasePage.wait_for_element(self, By.XPATH, PracticePageElements.iframe_list_xpath)
        return self.driver.find_elements(By.XPATH, PracticePageElements.iframe_list_xpath)

    def enter_text_in_alert_field(self, text):
        self.switch_alert_field.clear()
        self.switch_alert_field.send_keys(text)

    def print_alert_text(self):
        alert_text = self.switch_to_alert_get_text()
        print("Alert text:", alert_text)
        return alert_text

    def get_courses_with_price(self, price):
        courses = []
        # Find the table element
        table_element = self.web_table_example
        # Find all the rows in the table
        rows = self.web_table_rows
        row_amount = len(rows)
        price_element = self.web_table_course_price_column
        # Find the course name element in the row
        course_name_element = self.web_table_course_name_column
        # Iterate over each row
        for r in range(1, row_amount):
            # Find the price element in the row
            course_price = price_element
            course_name = course_name_element
            # Check if the price matches
            if course_price[r-1].text == str(price):
                # Add the course name to the list
                courses.append(course_name[r-1].text)
        return courses

    def get_people_table(self, position):
        engineers = []
        # Get the table element
        table_element = self.table_fixed_header
        # Find all the rows in the table
        rows = self.table_fixed_header_row
        # Column for the position of each person
        table_position = self.table_fixed_header_position
        # Column for each person's name
        table_name = self.table_fixed_header_names
        row_amount = len(rows)
        #Go through the captured elements and compare against the expected position
        for r in range(0, row_amount):
            #The strip method is executed to trim extra blank characters
            if str(table_position[r].text.strip()) == str(position):
                engineers.append(table_name[r].text)
        return engineers



    def get_text_and_print(self, list_items, expected_value):
        for item in list_items:
            if item.text.strip() == expected_value.strip():
                print(item.text)
        return

    def get_list_items(self, tag_name):
        list_items = self.find_elements_by_tag_name(tag_name)
        return list_items