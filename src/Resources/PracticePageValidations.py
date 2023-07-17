class PracticePageValidations:

    def alert_confirm_text(self,alert_text, input):
        expected_text = "Hello " + input + ", Are you sure you want to confirm?"
        assert alert_text == expected_text, f"The alert text is incorrect. Expected: " + expected_text + " Actual: " + alert_text


    list_expected_text = "His mentorship program is most after in the software testing community with long waiting period."

