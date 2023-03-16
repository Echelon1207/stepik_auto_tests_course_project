from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR,"#register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main > h1')
    PRODUCT_NAME_CHECK = (By.CSS_SELECTOR,'div.alertinner > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner')