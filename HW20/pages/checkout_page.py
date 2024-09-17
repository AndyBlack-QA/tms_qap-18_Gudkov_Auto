from selenium.webdriver.common.by import By


class CheckoutPage:
    checkout_emptiness_text_locator = ("//*[@class='i-textual__plain i-textual__plain_limited']")
    checkout_first_book_title_locator = ("//*[@class='goods-table-cell__line goods-table-cell__line_title']")
    checkout_first_book_checkbox_locator = ("//*[@class='i-checkbox__real']")
    checkout_delete_item_button_locator = ("//*[@class='i-button i-button_danger i-button_small remove']")
    checkout_yes_delete_button_click_locator = ("//*[@class='i-button i-button_danger i-button_small remove-yes']")
    checkout_cancel_delete_button_click_locator = ("//*[@class='i-button i-button_link i-button_small remove-no']")
    checkout_quantity_list_of_first_item_locator = ("//*[@class='i-amount-select__items i-amount-select__items_open']")
    checkout_quantity_choose_list_locator = ("//*[@class='i-amount-select']")


    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://oz.by/checkout/")

    def get_checkout_emptiness_text(self):
        return self.driver.find_element(By.XPATH, self.checkout_emptiness_text_locator).text

    def get_first_book_title(self):
        return self.driver.find_element(By.XPATH, self.checkout_first_book_title_locator).text

    def check_first_book_checkbox(self):
        return self.driver.find_element(By.XPATH, self.checkout_first_book_checkbox_locator).click()

    def delete_item_button_click(self):
        return self.driver.find_element(By.XPATH, self.checkout_delete_item_button_locator).click()

    def delete_confirmation_yes_click(self):
        return self.driver.find_element(By.XPATH, self.checkout_yes_delete_button_click_locator).click()

    def delete_confirmation_cancel_click(self):
        return self.driver.find_element(By.XPATH, self.checkout_cancel_delete_button_click_locator).click()

    def list_of_quantity_first_item(self):
        return self.driver.find_element(By.XPATH, self.checkout_quantity_list_of_first_item_locator)

    def click_quantity_of_the_first_item(self):
        return self.driver.find_element(By.XPATH, self.checkout_quantity_choose_list_locator).click()
