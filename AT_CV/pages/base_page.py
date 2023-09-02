from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class BasePage:
    def __init__(self ,driver ,url):
        self.driver = driver
        self.url = url


    def open(self):
       self.driver.get(self.url)

    # ждем когда элемент станет видимым, если нам нужно взаимодействовать с элементом
    def element_is_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((locator)))

        # ждем когда элементы станут видимыми, если нам нужно взаимодействовать с ними

    def elements_are_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_all_elements_located((locator)))

    # если элемента не видно(не прогрузился находится за пределами страницы, а скролить мы не хотим), но нам достаточно что он есть
    def element_is_present(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((locator)))

    # (во множественном числе)если элемента не видно(не прогрузился находится за пределами страницы, а скролить мы не хотим), но нам достаточно что он есть
    def elements_are_present(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located((locator)))

    # если элемент не видимый
    def elements_is_not_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(ec.invisibility_of_element_located((locator)))

    # Элемент кликабельный
    def elements_is_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable((locator)))

    # скролл до элемента
    def scroll_to_element(self, element):
        return self.driver.execute_script("argument[0].scrollInToView();", element)
