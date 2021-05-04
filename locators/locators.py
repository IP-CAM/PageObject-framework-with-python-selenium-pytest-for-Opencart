from selenium.webdriver.common.by import By


class BasePageLocators:
    # HEADER
    # CURRENCY SETTINGS
    CURRENCY_BUTTON_DROPDOWN = (By.CSS_SELECTOR, '.btn.btn-link.dropdown-toggle')
    CURRENCY_BUTTON_EURO = (By.NAME, "EUR")
    CURRENCY_BUTTON_POUND_STERLING = (By.NAME, "GBR")
    CURRENCY_BUTTON_US_DOLLAR = (By.NAME, "USD")
    # CONTACT US
    CONTACT_US_BUTTON = (By.CSS_SELECTOR, '.fa.fa-phone')
    # MY ACCOUNT(LOGIN\REG)
    MY_ACCOUNT_BUTTON_DROPDOWN = (By.CSS_SELECTOR, '.fa.fa-user')
    MY_ACCOUNT_REGISTER_BUTTON = (By.XPATH, '//a[text() = "Register"]')
    MY_ACCOUNT_LOGIN_BUTTON = (By.XPATH, '//a[text() = "Login"]')
    # WISH LIST
    WISH_LIST_BUTTON = (By.ID, 'wishlist-total')
    # CART
    CART_ICON_BUTTON = (By.CSS_SELECTOR, "[title='Shopping Cart']")
    # CHECKOUT
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'strong .fa.fa-share')

    # SEARCH
    SEARCH_TEXT_HOLDER = (By.CSS_SELECTOR, '.form-control.input-lg')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.btn.btn-default.btn-lg .fa')
    # CART BIG BLACK BUTTON
    CART_BIG_BUTTON = (By.CSS_SELECTOR, '.btn.btn-inverse.btn-block.btn-lg.dropdown-toggle')
    CART_ITEMS_AND_TOTAL_COST = (By.CSS_SELECTOR, "#cart-total")
    CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#cart .text-center')

    NAVBAR_HOME_BUTTON = (By.CSS_SELECTOR, '.fa.fa-home')
    NAVBAR_DESKTOPS_BUTTON_DROPDOWN = '.dropdown-toggle[href="http://localhost/desktops"]'
    NAVBAR_DESKTOPS_PC_BUTTON = (By.CSS_SELECTOR, '#menu [href="http://localhost/desktops/pc"]')
    NAVBAR_DESKTOPS_MAC_BUTTON = (By.CSS_SELECTOR, '#menu [href="http://localhost/desktops/mac"]')
    NAVBAR_DESKTOPS_SHOW_ALL_BUTTON = (By.CSS_SELECTOR, '.see-all[href="http://localhost/desktops"]')
    pass
