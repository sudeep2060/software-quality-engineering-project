from utils.driver_factory import get_driver


def test_open_browser():
    driver = get_driver()

    driver.get("https://www.saucedemo.com")

    print("Page Title:", driver.title)

    assert "Swag Labs" in driver.title

    driver.quit()