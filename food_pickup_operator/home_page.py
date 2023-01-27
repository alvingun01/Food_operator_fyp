from selenium.webdriver.common.by import By

def choose_stall(driver, stall_id: int):
    stall_card = driver.find_element(By.ID, f'stall-{stall_id}')
    stall_card.click()