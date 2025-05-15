import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_open_homepage_and_focus_search(driver):
    driver.get("https://regem.store/")
    wait = WebDriverWait(driver, 10)
    #search_input = wait.until(EC.element_to_be_clickable((By.ID, "searchInput")))
    #search_input.click()
    # element = wait.until(
    #     EC.element_to_be_clickable((By.ID, "//a[text()='КОЛЬЦА']"))
    # )
    element = driver.find_element_by_link_text('КОЛЬЦА')
    element.click()

# def test_search_input_is_active(driver):
#     search_input = open_homepage_and_focus_search(driver)
#     search_input.send_keys("тест")
#     value = search_input.get_attribute("value")
#     assert "тест" in value, "Поле ввода не активно или не принимает текст"

# def test_search_button_appears(driver):
#     search_input = open_homepage_and_focus_search(driver)
#     search_input.send_keys("iphone")
#     WebDriverWait(driver, 5).until(
#         EC.visibility_of_element_located((By.ID, "applySearchBtn"))
#     )
#     assert driver.find_element(By.ID, "applySearchBtn").is_displayed(), "Кнопка 'Найти' не появилась после ввода"

# def test_search_on_enter_key(driver):
#     search_input = open_homepage_and_focus_search(driver)
#     search_input.send_keys("iphone")
#     search_input.send_keys(Keys.ENTER)
#     results = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.product-card"))
#     )
#     assert len(results) > 0, "Результаты не загрузились при нажатии Enter"
