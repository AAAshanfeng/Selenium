import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture()
def driver():
    d = webdriver.Edge()
    d.get("https://the-internet.herokuapp.com/login")
    time.sleep(2)
    yield d
    d.quit()


def test_login_success(driver):
    """TC01 正向用例：正确账号密码，登录成功"""
    username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username.send_keys("tomsmith")

    password = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password.send_keys("SuperSecretPassword!")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    ).click()

    success_message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area" in success_message


def test_login_wrong_password(driver):
    """TC02 反向用例：密码错误"""
    username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username.send_keys("tomsmith")

    password = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password.send_keys("wrong_password")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    ).click()

    success_message = driver.find_element(By.ID, "flash").text
    assert "Your password is invalid" in success_message


def test_login_wrong_username(driver):
    """TC03 反向用例：用户名不存在"""
    username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username.send_keys("wrong_username")

    password = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password.send_keys("SuperSecretPassword!")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    ).click()

    success_message = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid" in success_message