from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_CART = (By.CSS_SELECTOR, "span.btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR,"#register_form")
    EMAIL_FOR_REGISTER =(By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_1_FOR_REGISTER = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_2_FOR_REGISTER = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_FOR_REGISTER = (By.CSS_SELECTOR, "button[name = 'registration_submit']")


class ProductPageLocators:
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main > h1')
    PRODUCT_NAME_CHECK = (By.CSS_SELECTOR,'div.alertinner > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner')


class CartPageLocators:
    MESSAGE_EMPTY_CART = (By.CSS_SELECTOR, "#content_inner > p")