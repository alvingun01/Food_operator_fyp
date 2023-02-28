from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def init():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome("chromedriver", chrome_options=chrome_options)
    driver.get('http://127.0.0.1:8000/start/')
    return driver

from food_pickup_operator.general import *
from food_pickup_operator.start_page import *
from food_pickup_operator.home_page import *
from food_pickup_operator.stall_page import *
from food_pickup_operator.recommendation_filler import *
