import pytest
from pypom import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Home(Page):
    _search_locator = (By.ID, 'query')
    _search_button = (By.CLASS_NAME, 'search__btn')

    def wait_for_page_to_load(self):
        self.wait.until(expected_conditions.visibility_of_element_located(
            self._search_locator))
        return self

    def search(self, search_term, error=False):
        self.find_element(*self._search_locator).send_keys(search_term)
        self.find_element(*self._search_button).click()
        if error:
            return self.wait.until(lambda _: self.error)
        return Search(self.driver, self.base_url).wait_for_page_to_load()


class Search(Page):
    URL_TEMPLATE = '/search'
    _search_list_locator = (By.CSS_SELECTOR, 'a.gs-title b')
    _search_header = (By.XPATH, '//h1')
    _search_no_result_msg = (By.CSS_SELECTOR, 'div.gs-no-results-result')

    @property
    def heading(self):
        return self.find_element(*self._search_header).text

    def wait_for_page_to_load(self):
        self.wait.until(expected_conditions.visibility_of_element_located(
            self._search_header))
        return self

    def look_at_search_result(self, search_term):
        list_result = self.find_elements(*self._search_list_locator)
        count = 0
        for i in list_result:
            while count <= 10:
                assert search_term.lower() in i.text.lower()
                count += 1


@pytest.mark.nondestructive
def test_valid_search(driver, base_url):
    page = Home(driver, base_url).open()
    page.search("business cards")
    page = Search(driver)
    page.look_at_search_result("Business Cards")
    assert page.heading == 'Results for "business cards"'


@pytest.mark.nondestructive
def test_invalid_search(driver, base_url):
    page = Home(driver, base_url).open()
    page.search("asdsadasdasd")
    page = Search(driver)
    page.find_element(*page._search_no_result_msg).is_displayed()
    assert page.heading == 'Results for "asdsadasdasd"'
