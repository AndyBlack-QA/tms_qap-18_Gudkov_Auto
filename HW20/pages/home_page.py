from selenium.webdriver.common.by import By


class HomePage:
    title_locator = "//*[@class='mpgs-title']"
    photo_locator = "//*[@class='ph']"
    search_button = "//*[@class='search-form__submit']"
    search_field = ("//*[@class='search-form__input ui-autocomplete-input position-relative digi-instant-search "
                    "jc-ignore']")
    cookie_field_locator = ("//*[@class='btn btn-lg btn-primary w-100 m-0']")


    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://oz.by/")

    def get_book_title(self, order):
        return self.driver.find_element(By.XPATH, f'({self.title_locator})[{order}]').text

    def open_book(self, order):
        self.driver.find_element(By.XPATH, f'({self.photo_locator})[{order}]').click()

    def cookie_accept(self):
        self.driver.find_element(By.XPATH, self.cookie_field_locator).click()






