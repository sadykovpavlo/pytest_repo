from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_button_present(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    expected_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(locator=(By.CSS_SELECTOR, '.btn-add-to-basket')))
    assert expected_button is not None, "Button not found"
    time.sleep(5)
