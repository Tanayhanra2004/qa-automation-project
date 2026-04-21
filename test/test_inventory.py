from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config_reader import load_config

def test_valid_login(driver):
    config = load_config()
    driver.get(config["base_url"])

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    assert inventory.is_inventory_loaded()