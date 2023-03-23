import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def setMinPrice(driver, price: int):
    #place = "recommendation-min-price", "min-price"
    try: minPriceInput = driver.find_element(By.ID, "min-price")
    except : minPriceInput = driver.find_element(By.ID, "recommendation-min-price")
    minPriceInput.clear()
    minPriceInput.send_keys(str(price))

def setMaxPrice(driver, price: int):
    #place = "recommendation-max-price", "max-price"
    try: maxPriceInput = driver.find_element(By.ID, "max-price")
    except : maxPriceInput = driver.find_element(By.ID, "recommendation-max-price")
    maxPriceInput.clear()
    maxPriceInput.send_keys(str(price))

def setCategory(driver, cate: str,):
    #cate = "All","Japanese","Chinese","Western","Arabian","Indian"
    #place = "recommendation-category", "category"
    try: categoryInput = Select(driver.find_element(By.ID, "category"))
    except : categoryInput = Select(driver.find_element(By.ID, "recommendation-category"))
    categoryInput.select_by_value(cate)

def setSpicy(driver, spicy: str):
    #spicy = "All", "Non-Spicy", "Spicy"
    #place = "recommendation-hot", "hot"
    try: spicyInput = Select(driver.find_element(By.ID, "hot"))
    except : spicyInput = Select(driver.find_element(By.ID, "recommendation-hot"))
    spicyInput.select_by_value(spicy)

def setVegetarian(driver, vegetarian: str):
    #vegetarian = "All", "Non-Vegetarian", "Vegetarian"
    #place = "recommendation-vegetarian", "vegetarian"
    try: vegetarianInput = Select(driver.find_element(By.ID, "vegetarian"))
    except : vegetarianInput = Select(driver.find_element(By.ID, "recommendation-vegetarian"))
    vegetarianInput.select_by_value(vegetarian)

def setHalal(driver, halal: str):
    #halal = "All", "Non-Halal", "Halal"
    #place = "recommendation-halal", "halal"
    try: halalInput = Select(driver.find_element(By.ID, "halal"))
    except : halalInput = Select(driver.find_element(By.ID, "recommendation-halal"))
    halalInput.select_by_value(halal)

def setPeanut(driver, peanut: str):
    #peanut = "All", "Contains Peanut", "No Peanut"
    #place = "recommendation-peanut", "peanut"
    try: peanutInput = Select(driver.find_element(By.ID, "peanut"))
    except : peanutInput = Select(driver.find_element(By.ID, "recommendation-peanut"))
    peanutInput.select_by_value(peanut)

def setShrimp(driver, shrimp: str):
    #shrimp = "All", "Contains shrimp", "No shrimp"
    #place = "recommendation-shrimp", "shrimp"
    try: shrimpInput = Select(driver.find_element(By.ID, "shrimp"))
    except : shrimpInput = Select(driver.find_element(By.ID, "recommendation-shrimp"))
    shrimpInput.select_by_value(shrimp)
    
def setLactose(driver, lactose: str, place):
    #lactose = "All", "Contains lactose", "No lactose"
    #place = "recommendation-lactose", "lactose"
    try: lactoseInput = Select(driver.find_element(By.ID, "lactose"))
    except : lactoseInput = Select(driver.find_element(By.ID, "recommendation-lactose"))
    lactoseInput.select_by_value(lactose)

def toggle_language(driver):
    toggle_language_button = driver.find_element(By.ID, "toggle-language")
    toggle_language_button.click()
    
def make_way(driver, open: bool):
    if (open): driver.get('http://127.0.0.1:8000/move-out/')
    else: driver.get('http://127.0.0.1:8000/start/')