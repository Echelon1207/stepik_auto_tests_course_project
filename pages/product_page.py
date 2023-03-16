from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_button_add_to_cart(self):
        button_cart = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        button_cart.click()

    def should_be_button_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CART), "Button add to cart is not presented"

    def should_match_product_names(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        print(f'Product name is {product_name}')
        product_name_check = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_CHECK).text
        print(f'Product name check is {product_name_check}')
        assert product_name == product_name_check, "Product names not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should be disappeared, but not disappeared"
