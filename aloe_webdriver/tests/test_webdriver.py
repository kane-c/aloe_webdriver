"""
Test Webdriver steps.
"""

from aloe.testing import FeatureTest

from aloe_webdriver.tests.base import feature

# pylint:disable=line-too-long


class TestSteps(FeatureTest):
    """Test steps."""

    @feature()
    def test_I_should_see(self):
        """
        When I visit test page "basic_page"
        Then I should see "Hello there!"
        And I should see 'Welcome "User"'
        And I should see a link to "Google" with the url "http://google.com/"
        And I should see a link with the url "http://google.com/"
        And I should not see "Bogeyman"
        """

    @feature()
    def test_I_see_a_link(self):
        """
        When I visit test page "basic_page"
        Then  I should see a link to "Google" with the url "http://google.com/"
        And I see "Hello there!"
        """

    @feature()
    def test_see_a_link_containing(self):
        """
        When I visit test page "basic_page"
        Then The browser's URL should contain "http://"
        And I should see a link that contains the text "Goo" and the url "http://google.com/"
        """

    @feature()
    def test_basic_page_linking(self):
        """
        Given I visit test page "link_page"
        And I see "Page o link"
        When I click "Next Page"
        Then I should be at "http://0.0.0.0:7755/link_dest.html"
        And The browser's URL should be "http://0.0.0.0:7755/link_dest.html"
        And The browser's URL should not contain "irrelevant things"
        And I should see "Link destination page"
        """

    @feature()
    def test_ajax_action(self):
        """
        Given I visit test page "link_page"
        When I click "Load content with AJAX"
        Then I should see "Loaded with AJAX"
        """

    @feature()
    def test_I_see_a_form(self):
        """
        When I visit test page "basic_page"
        Then I should see a form that goes to "basic_page.html"
        And the element with id of "somediv" contains "Hello"
        And the element with id of "somediv" does not contain "bye"
        """

    @feature()
    def test_I_fill_in_a_form(self):
        """
        Given I visit test page "basic_page"
        And I fill in "bio" with "everything awesome"
        And I fill in "Password: " with "neat"
        When I press "Submit!"
        Then The browser's URL should contain "bio=everything"
        """

    @feature()
    def test_checkboxes_checked(self):
        """
        Given I visit test page "basic_page"
        When I check "I have a bike"
        Then The "I have a bike" checkbox should be checked
        And The "I have a car" checkbox should not be checked
        """

    @feature()
    def test_checkboxes_unchecked(self):
        """
        Given I visit test page "basic_page"
        And I check "I have a bike"
        And The "I have a bike" checkbox should be checked
        When I uncheck "I have a bike"
        Then The "I have a bike" checkbox should not be checked
        """

    @feature()
    def test_combo_boxes(self):
        """
        Given I visit test page "basic_page"
        Then I should see option "Mercedes" in selector "car_choice"
        And I should see option "Volvo" in selector "car_choice"
        And I should not see option "Skoda" in selector "car_choice"
        When I select "Mercedes" from "car_choice"
        Then The "Mercedes" option from "car_choice" should be selected
        """

    @feature(fails=True)
    def test_combo_boxes_fail(self):
        """
        Given I visit test page "basic_page"
        Then I should not see option "Mercedes" in selector "car_choice"
        """

    @feature()
    def test_multi_combo_boxes(self):
        '''
        Given I visit test page "basic_page"
        When I select the following from "Favorite Colors:":
            """
            Blue
            Green
            """
        Then The following options from "Favorite Colors:" should be selected:
            """
            Blue
            Green
            """
        '''

    @feature()
    def test_radio_buttons(self):
        """
        When I visit test page "basic_page"
        And I choose "Male"
        Then The "Male" option should be chosen
        And The "Female" option should not be chosen
        """

    @feature(fails=True)
    def test_hidden_text(self):
        """
        When I visit test page "basic_page"
        Then I should see an element with id of "bio_field"
        And I should see an element with id of "somediv"
        And I should not see an element with id of "hidden_text"
        And I should see "Weeeee"
        """

    @feature(fails=True)
    def test_hidden_text_2(self):
        """
        When I visit test page "basic_page"
        Then I should see "Hello there"
        And I should see an element with id of "oops_field"
        And I should not see an element with id of "hidden_text"
        """

    @feature()
    def test_alert_accept(self):
        """
        When I visit test page "alert_page"
        Then I should see an alert with text "This is an alerting alert"
        When I accept the alert
        Then I should not see an alert
        And I should see "true"
        """

    @feature()
    def test_alert_dismiss(self):
        """
        When I visit test page "alert_page"
        Then I should see an alert with text "This is an alerting alert"
        When I dismiss the alert
        Then I should not see an alert
        And I should see "false"
        """

    @feature()
    def test_tooltips(self):
        """
        When I visit test page "tooltips"
        Then I should see an element with tooltip "A tooltip"
        And I should not see an element with tooltip "Does not exist"
        And I should not see an element with tooltip "Hidden"
        When I click the element with tooltip "A tooltip"
        Then the browser's URL should contain "#anchor"
        """

    @feature()
    def test_labels(self):
        """
        When I visit test page "basic_page"
        And I click on label "Favorite Colors:"
        Then element with id "fav_colors" should be focused
        And element with id "bio_field" should not be focused
        """

    @feature(fails=True)
    def test_labels_fail(self):
        """
        When I visit test page "basic_page"
        And I click on label "Favorite Colors:"
        Then element with id "fav_colors" should not be focused
        """

    @feature()
    def test_input_values(self):
        """
        When I visit test page "basic_page"
        And I fill in "username" with "Danni"
        Then input "username" has value "Danni"
        """

    @feature(fails=True)
    def test_input_values_fail(self):
        """
        When I visit test page "basic_page"
        And I fill in "username" with "Danni"
        Then input "username" has value "Ricky"
        """

    @feature()
    def test_date_input(self):
        """
        When I visit test page "basic_page"
        And I fill in "dob" with "1900/01/01"
        Then input "dob" has value "1900/01/01"
        """

    @feature()
    def test_page_title(self):
        """
        When I visit test page "basic_page"
        Then the page title should be "A Basic Page"
        """

    @feature()
    def test_submit_only(self):
        """
        When I visit test page "basic_page"
        And I submit the only form
        Then the browser's URL should contain "bio="
        And the browser's URL should contain "user="
        """

    @feature()
    def test_submit_action(self):
        """
        When I visit test page "basic_page"
        And I submit the form with action "basic_page.html"
        Then the browser's URL should contain "bio="
        And the browser's URL should contain "user="
        """

    @feature()
    def test_submit_id(self):
        """
        When I visit test page "basic_page"
        And I submit the form with id "the-form"
        Then the browser's URL should contain "bio="
        And the browser's URL should contain "user="
        """
