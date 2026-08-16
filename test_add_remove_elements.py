import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture()
def driver():
    d = webdriver.Edge()
    d.get("https://the-internet.herokuapp.com/add_remove_elements/")
    time.sleep(2)
    yield d
    d.quit()


def test_add_remove_elements(driver):
    """完整流程：连续添加3个元素 → 验证数量 → 删除1个 → 验证数量变化"""
    print("当前页面标题:", driver.title)
    print("当前网址:", driver.current_url)

    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add Element']"))
    )
    add_button.click()
    add_button.click()
    add_button.click()

    delete_buttons = driver.find_elements(By.CSS_SELECTOR, ".added-manually")
    assert len(delete_buttons) == 3, f"预期3个元素，实际{len(delete_buttons)}个"

    delete_buttons[0].click()

    remaining = driver.find_elements(By.CSS_SELECTOR, ".added-manually")
    assert len(remaining) == 2, f"预期剩余2个元素，实际{len(remaining)}个"


def test_add_zero_then_nothing_to_delete(driver):
    """反向用例：一个元素都没加，页面上应该没有可删除的按钮"""
    delete_button = driver.find_elements(By.CSS_SELECTOR, ".added-manually")
    assert len(delete_button) == 0