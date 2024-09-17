from selenium.webdriver.common.by import By


class BookPage:
    title_locator = "//h1[@itemprop='name']"
    put_to_the_shopping_cart_locator = "//form[@class='addtocartform']"
    in_shopping_cart_locator = "//a[@class='b-product-control__button i-button i-button_info second-button']"
    book_price_locator = ""

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://oz.by/books/more10647018.html")

    def get_title(self):
        return self.driver.find_element(By.XPATH, self.title_locator).text

    def put_to_the_shopping_cart(self):
        self.driver.find_element(By.XPATH, self.put_to_the_shopping_cart_locator).click()

    def in_shopping_cart(self):
        return self.driver.find_element(By.XPATH, self.in_shopping_cart_locator)
