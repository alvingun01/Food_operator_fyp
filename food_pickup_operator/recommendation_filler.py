import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def setMinPrice(driver, price: int, place):
    #place = "recommendation-min-price", "min-price"
    minPriceInput = driver.find_element(By.ID, place)
    minPriceInput.clear()
    minPriceInput.send_keys(str(price))

def setMaxPrice(driver, price: int, place):
    #place = "recommendation-max-price", "max-price"
    maxPriceInput = driver.find_element(By.ID, place)
    maxPriceInput.clear()
    maxPriceInput.send_keys(str(price))

def setCategory(driver, cate: str,place):
    #cate = "All","Japanese","Chinese","Western","Arabian","Indian"
    #place = "recommendation-category", "category"
    categoryInput = Select(driver.find_element(By.ID,place))
    categoryInput.select_by_value(cate)

def setSpicy(driver, spicy: str, place):
    #spicy = "All", "Non-Spicy", "Spicy"
    #place = "recommendation-hot", "hot"
    spicyInput = Select(driver.find_element(By.ID,place))
    spicyInput.select_by_value(spicy)

def setVegetarian(driver, vegetarian: str, place):
    #vegetarian = "All", "Non-Vegetarian", "Vegetarian"
    #place = "recommendation-vegetarian", "vegetarian"
    vegetarianInput = Select(driver.find_element(By.ID,place))
    vegetarianInput.select_by_value(vegetarian)

def setHalal(driver, halal: str, place):
    #halal = "All", "Non-Halal", "Halal"
    #place = "recommendation-halal", "halal"
    halalInput = Select(driver.find_element(By.ID,place))
    halalInput.select_by_value(halal)

def setPeanut(driver, peanut: str, place):
    #peanut = "All", "Contains Peanut", "No Peanut"
    #place = "recommendation-peanut", "peanut"
    peanutInput = Select(driver.find_element(By.ID,place))
    peanutInput.select_by_value(peanut)

def setShrimp(driver, Shrimp: str, place):
    #Shrimp = "All", "Contains Shrimp", "No Shrimp"
    #place = "recommendation-shrimp", "shrimp"
    ShrimpInput = Select(driver.find_element(By.ID,place))
    ShrimpInput.select_by_value(Shrimp)
    
def setLactose(driver, Lactose: str, place):
    #Lactose = "All", "Contains Lactose", "No Lactose"
    #place = "recommendation-lactose", "lactose"
    LactoseInput = Select(driver.find_element(By.ID,place))
    LactoseInput.select_by_value(Lactose)