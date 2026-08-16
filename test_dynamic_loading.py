import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture()
def driver():
    d = webdriver.Edge()
    d.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    time.sleep(2)
    yield d
    d.quit()


def test_dynamic_loading(driver):
    """测试点：点击Start，等待元素加载出现"""
    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
    )
    start_button.click()

    finish_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )
    assert finish_element.text == "Hello World!"