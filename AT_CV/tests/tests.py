import time

from pages.base_page import BasePage
from pages.elements_page import TestsOfPage


class TestElements:
    class TestMainElements:
        def test_url(self, driver):
            page = TestsOfPage(driver, 'https://sergeycd.github.io/New_CV/index.html')
            page.open()
            get_url = driver.current_url
            str_url = str(get_url)
            print(str_url)
            assert str_url == "https://sergeycd.github.io/New_CV/index.html"
            time.sleep(3)

        def test_name_author(self, driver):
            page = TestsOfPage(driver, 'https://sergeycd.github.io/New_CV/index.html')
            page.open()
            page.test_name_of_author()
            get_name = page.test_name_of_author()
            assert get_name == "Голованов Сергей"
