import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


@pytest.fixture()
def driver():
    d = webdriver.Edge()
    d.get("https://the-internet.herokuapp.com/dropdown")
    time.sleep(2)
    yield d
    d.quit()


def test_select_dropdown_option1(driver):
    """测试点：选择下拉框中的Option 1"""
    dropdown_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "dropdown"))
    )
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text("Option 1")

    select_option = dropdown.first_selected_option.text
    assert select_option == "Option 1"