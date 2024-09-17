from selenium.webdriver.common.by import By


class SearchResultsPage:
    book_title_bible_request = "//*[@class='digi-product__meta']"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://oz.by/?digiSearch=true&term=Andrei&params=%7Csort%3DDEFAULT")

    def book_title_bible_request_text(self):
        return self.driver.find_element(By.XPATH, self.book_title_bible_request).text
