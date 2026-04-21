from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):

    inventory_container = (By.ID, "inventory_container")

    def is_inventory_loaded(self):
        return self.wait_for_element(self.inventory_container)