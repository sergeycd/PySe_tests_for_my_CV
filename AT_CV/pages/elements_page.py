from locators.element_page_locators import PageLocators
from pages.base_page import BasePage


class TestsOfPage(BasePage):
    locators = PageLocators()

    def test_name_of_author(self):
        get_name=self.element_is_visible(self.locators.NAME_AUTHOR).text
        return get_name


