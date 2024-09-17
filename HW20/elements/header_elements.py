from selenium.webdriver.common.by import By


class HeaderElement:
    oz_icon_locator = "//*[@class='link header__brand']"
    search_button = "//*[@class='search-form__submit']"
    search_field = ("//*[@class='search-form__input ui-autocomplete-input position-relative digi-instant-search "
                    "jc-ignore']")
    checkout_locator = ("//*[@class='link user-bar__item user-bar__cart']")

    def __init__(self, driver):
        self.driver = driver

    def checkout_click(self):
        return self.driver.find_element(By.XPATH, self.checkout_locator).click()

    def find_oz_icon(self):
        return self.driver.find_element(By.XPATH, self.oz_icon_locator)

    def search_button_click(self):
        return self.driver.find_element(By.XPATH, self.search_button).click()

    def search_field_click(self, text):
        return self.driver.find_element(By.XPATH, self.search_field).send_keys(text)

    def search_field_get_text(self):
        return self.driver.find_element(By.XPATH, self.search_field).text
