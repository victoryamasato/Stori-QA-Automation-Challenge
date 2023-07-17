from src.Pages.PracticePage import PracticePage

import time

from src.Resources.PracticePageValidations import PracticePageValidations

class TestSuggestionClass:


    def test_suggestion_class_mexico(self, init_driver):
        element = PracticePage(init_driver)
        element.suggestion_class.click()
        # Input Me and select Mexico
        element.suggestion_class.send_keys("Me")
        element.mexico_country.click()
        element.screenshot_evidence("src/Evidence/test_suggestion_class.png")
        pass


    def test_dropdown(self, init_driver):
        element = PracticePage(init_driver)
        # Click the dropdown, sleeps are there to make changes visible to the user
        element.dropdown_class_id.click()
        time.sleep(1)
        # Select option 2
        element.dropdown_option2.click()
        element.dropdown_class_id.click()
        time.sleep(1)
        # Select option 3
        element.dropdown_class_id.click()
        element.dropdown_option3.click()
        element.dropdown_class_id.click()
        time.sleep(2)
        pass


    def test_alert(self, init_driver):
        element = PracticePage(init_driver)
        # Input Stori card into the field, then click the alert button
        element.enter_text_in_alert_field("Stori Card")
        element.switch_alert_btn.click()
        element.print_alert_text()
        # Switch focus to alert and accept
        element.switch_to_alert_accept()
        # Input Stori card again and click the confirm button
        element.enter_text_in_alert_field("Stori Card")
        element.confirm_alert_btn.click()
        time.sleep(2)
        # Get the text from the alert, print and assert
        element.switch_to_alert_get_text()
        alert_text = element.print_alert_text()
        PracticePageValidations.alert_confirm_text(self, alert_text, "Stori Card")
        element.switch_to_alert_accept()


    def test_web_table(self, init_driver):
        element = PracticePage(init_driver)
        courses_25 = element.get_courses_with_price("25")
        print(f"Number of courses that cost $25: {len(courses_25)}")
        # Print the names of courses that cost $25
        print("Courses that cost $25:")
        for course in courses_25:
            print(course)


    def test_table_fixed_header(self, init_driver):
        element = PracticePage(init_driver)
        # Get the people with the engineer role to print
        engineers = element.get_people_table("Engineer")
        for people in engineers:
            print ("The engineers from the list are: " + people)

    def test_iframe(self, init_driver):
        element = PracticePage(init_driver)
        # Switch to the iframe and get the list elements
        iframe = PracticePage.iframe_example
        element.switch_to_iframe()
        list_element = element.get_list_items("li")
        # Assert the text against the expected value
        element.get_text_and_print(list_element, PracticePageValidations.list_expected_text)
        element.switch_to_default()


