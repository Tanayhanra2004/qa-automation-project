from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.config_reader import load_config

def get_driver():
    config = load_config()
    browser = config["browser"]

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    else:
        raise Exception("Browser not supported")

    return driver