import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture()
def driver():
    d = webdriver.Edge()
    d.get("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(2)
    yield d
    d.quit()


def test_alert_accept(driver):
    """TC01：普通提示框，点击确认"""
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[onclick = "jsAlert()"]'))
    )
    button.click()
    alert = driver.switch_to.alert
    alert.accept()

    result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "result"))
    )
    assert "You successfully clicked an alert" in result.text


def test_confirm_accept(driver):
    """TC02：确认框，点击确认（Accept）"""
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[onclick = "jsConfirm()"]'))
    )
    button.click()
    alert = driver.switch_to.alert
    alert.accept()

    result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "result"))
    )
    assert "You clicked: Ok" in result.text


def test_confirm_dismiss(driver):
    """TC03：反向用例：确认框，点击取消"""
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[onclick = "jsConfirm()"]'))
    )
    button.click()
    alert = driver.switch_to.alert
    alert.dismiss()

    result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "result"))
    )
    assert "You clicked: Cancel" in result.text


def test_prompt_with_input(driver):
    """TC04：输入框弹窗，输入文字后确认"""
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[onclick = "jsPrompt()"]'))
    )
    button.click()
    alert = driver.switch_to.alert
    alert.send_keys("Selenium测试")
    alert.accept()

    result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "result"))
    )
    assert "You entered: Selenium测试" in result.text