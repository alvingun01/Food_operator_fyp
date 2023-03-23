from selenium.webdriver.common.by import By

def choose_menu(driver, menu_id: int):
    menu_card = driver.find_element(By.ID, f'menu-{menu_id}')
    menu_card.click()

def fill_quantity(driver, quantity: int):
    portion_input = driver.find_element(By.CLASS_NAME, 'portion-input')
    portion_input.clear()
    portion_input.send_keys(str(quantity))
def fill_quantity_non_recommendation(driver, quantity: int):
    portion_input = driver.find_element(By.ID, 'portion-input-non-recommendation')
    portion_input.clear()
    portion_input.send_keys(str(quantity))

def submit_order(driver):
    form = driver.find_element(By.ID, 'new-order-menu-form')
    form.submit()

def close_menu_card(driver):
    close_button = driver.find_element(By.CLASS_NAME, 'order-menu-modal-close-button')
    close_button.click()

def order_menu(driver, menu_id: int, quantity: int):
    choose_menu(driver, menu_id)
    fill_quantity_non_recommendation(driver, quantity)
    submit_order(driver)