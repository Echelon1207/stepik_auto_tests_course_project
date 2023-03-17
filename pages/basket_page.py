from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_empty_cart(self):
        assert 'empty' in self.browser.find_element(*CartPageLocators.MESSAGE_EMPTY_CART).text, "Cart is not empty"