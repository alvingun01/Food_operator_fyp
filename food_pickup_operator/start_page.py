from selenium.webdriver.common.by import By

def fill_table(driver, table_no: int):
    table_no_input = driver.find_element(By.NAME, 'table_no')
    table_no_input.clear()
    table_no_input.send_keys(str(table_no))

def start_order(driver):
    start_order_button = driver.find_element(By.ID, 'start-order')
    start_order_button.click()