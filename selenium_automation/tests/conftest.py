import pytest
from utils.driver_factory import get_driver


@pytest.fixture
def driver():
    driver = get_driver()
    driver.get("https://www.saucedemo.com/")

    yield driver

    driver.quit()