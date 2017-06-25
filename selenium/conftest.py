import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope='session')
def driver():
    _driver = Chrome()
    yield _driver
    _driver.quit()


@pytest.fixture(scope='session')
def base_url():
    return 'https://www.moo.com/uk/'
