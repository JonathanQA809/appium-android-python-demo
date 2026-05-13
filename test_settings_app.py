
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


@pytest.fixture(scope="session")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "Pixel_5"
    options.app_package = "com.android.settings"
    options.app_activity = ".Settings"
    options.no_reset = True

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()


def test_settings_app_opens(driver):
    title = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Settings"]')
    assert title.is_displayed()


def test_apps_option_is_visible(driver):
    apps_option = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Apps"]')
    assert apps_option.is_displayed()