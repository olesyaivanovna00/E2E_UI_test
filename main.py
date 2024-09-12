import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'


class TestSauceDemo:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        yield self.driver
        self.driver.quit()

    def test_purchase(self, setup):
        driver = setup

        #авторизация
        driver.find_element(By.ID, "user-name").send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "login-button").click()

        #выбор товара
        driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']").click()
        driver.find_element(By.CLASS_NAME, "btn_primary").click()

        #в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        assert "Sauce Labs Backpack" in driver.page_source

        #оформление
        driver.find_element(By.XPATH, "//button[text()='Checkout']").click()
        driver.find_element(By.ID, "first-name").send_keys("John")
        driver.find_element(By.ID, "last-name").send_keys("Doe")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.XPATH, "//input[@value='Continue']").click()

        #завершение
        driver.find_element(By.XPATH, "//button[text()='Finish']").click()

        #проверка завершения
        assert "Thank you for your order!" in driver.page_source
