def test_open_browser(driver):
    driver.get("https://www.saucedemo.com/")

    assert "Swag Labs" in driver.title