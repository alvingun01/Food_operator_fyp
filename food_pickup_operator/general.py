from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def search(driver, keyword: str):
    search_input = driver.find_element(By.ID, 'search')
    search_input.clear()
    search_input.send_keys(keyword)
    search_input.send_keys(Keys.ENTER)

def open_filter(driver):
    open_filter = driver.find_element(By.ID, 'filter-modal-open-button')
    open_filter.click()

def apply_filter(driver):
    apply_filter = driver.find_element(By.ID, 'filter')
    apply_filter.click()

def close_filter(driver):
    close_filter = driver.find_element(By.CLASS_NAME, 'filter-modal-close-button')
    close_filter.click()

def open_cart(driver):
    open_cart_button = driver.find_element(By.ID, 'cart-modal-open-button')
    open_cart_button.click()

def close_cart(driver):
    close_cart = driver.find_element(By.CLASS_NAME, 'cart-modal-close-button')
    close_cart.click()

def open_recommendation(driver):
    open_recommendation = driver.find_element(By.ID, 'filter-recommendation-modal-open-button')
    open_recommendation.click()

def close_recommendation(driver):
    close_recommendation = driver.find_element(By.CLASS_NAME, 'filter-recommendation-modal-close-button')
    close_recommendation.click()

def checkout(driver):
    open_cart(driver)
    checkout_button = driver.find_element(By.ID, 'checkout-button')
    checkout_button.click()